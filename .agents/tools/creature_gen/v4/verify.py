"""Compare a biome's sprites (installed and/or a pilot folder) with the AC / BW / PF references - as distributions, never as one
average. Writes <dir>/verify/report.txt (+ json/csv) and prints it.
  python3 verify.py <pre> <pilot_dir> [--prev <dir>]      (dir = a tune stage folder or a build out folder)

Sections: 1) 110-feature battery: share of species inside the reference p10-p90 band, separation from the CLOSEST dialect
(Mann-Whitney AUC; >0.5 = clearly off), spread ratio (homogeneity), features outside the band per species vs the refs' own count,
and kNN distance in feature space next to how far each dialect sits from the other two (the calibration: every dialect is itself
~100% separable, so 'separable' alone is no failure). 2) light handling (BW rules). 3) body light profile top->bottom.
4) fin rules (only rules true in all three dialects) and 5) fin motion signature."""
import os, sys, json, glob, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v4env
import numpy as np
def sheets(d, pre):
    out = {}
    for f in glob.glob(os.path.join(d, f'{pre}_*_swim_*_4f.png')):
        n = re.search(rf'{pre}_(\w+?)(?:_final)?_swim_', os.path.basename(f)).group(1); out[n] = f
    return out
def installed(pre): return {n: v4env.installed(pre, n) for m, n in v4env.species(pre)}
def refs():
    return {p: {re.search(rf'{p}_(\w+?)_swim', os.path.basename(f)).group(1): f for f in fs} for p, fs in v4env.ref_sheets().items()}
def cached(tag, fn):
    p = os.path.join(v4env.CACHE, tag + '.json')
    if os.path.exists(p): return json.load(open(p))
    r = fn(); json.dump(r, open(p, 'w'), default=float); return r
def battery_set(S, pre):
    from battery import feats
    out = {}
    for n, f in S.items():
        try: out[n] = feats(f, pre)
        except Exception as e: pass
    return out
def profile(f, NB=6):
    from PIL import Image
    from m import body
    from f2 import lab
    W, H = v4env.frame_size(f); fr = np.array(Image.open(f).convert('RGBA'))[:H, :W]; core = body(fr); L = lab(fr[..., :3].astype(float))[0]
    ys, xs = np.nonzero(core); x0, x1 = xs.min(), xs.max(); acc = [[] for _ in range(NB)]
    for x in range(x0 + int(0.2 * (x1 - x0)), x0 + int(0.8 * (x1 - x0)) + 1):
        c = np.nonzero(core[:, x])[0]
        if len(c) < 5: continue
        t = (c - c.min()) / (c.max() - c.min()); b = np.minimum((t * NB).astype(int), NB - 1)
        for i in range(NB):
            if (b == i).any(): acc[i].append(L[c[b == i], x].mean())
    med = np.median(L[core]); return [float(np.mean(a) - med) if a else float('nan') for a in acc]
def main():
    from scipy.stats import mannwhitneyu
    args = sys.argv[1:]; pre, d = args[0], args[1]; prev = args[args.index('--prev') + 1] if '--prev' in args else None
    R = refs(); SETS = {'installed': installed(pre), 'pilot': sheets(d, pre)}
    if prev: SETS['prev'] = sheets(prev, pre)
    lines = []; P = lambda *a: lines.append(' '.join(str(x) for x in a))
    # ---- 1. battery
    B = {p: cached(f'battery_{p}', lambda p=p: battery_set(R[p], p)) for p in R}
    Bs = {s: battery_set(S, pre) for s, S in SETS.items()}
    F = [k for k in next(iter(B['ac'].values())) if not k.startswith('g_') and k != 'w_dL']
    ref = {k: np.array([r[k] for p in B for r in B[p].values() if r.get(k) == r.get(k)]) for k in F}
    def auc(x, y):
        x = np.asarray(x); y = np.asarray(y)
        if len(x) < 4 or len(y) < 4 or np.ptp(np.r_[x, y]) == 0: return 0.5
        return mannwhitneyu(x, y).statistic / (len(x) * len(y))
    rows = []
    for k in F:
        rv = ref[k]
        if len(rv) < 10: continue
        p10, p25, p75, p90 = np.percentile(rv, [10, 25, 75, 90]); row = dict(f=k, p10=p10, p90=p90)
        for s in Bs:
            v = np.array([r[k] for r in Bs[s].values() if r.get(k) == r.get(k)])
            if not len(v): continue
            row[s + '_in'] = float(((v >= p10) & (v <= p90)).mean()); row[s + '_p50'] = float(np.median(v))
            row[s + '_sep'] = min(abs(auc(v, [r[k] for r in B[p].values() if r.get(k) == r.get(k)]) - 0.5) * 2 for p in B)
            row[s + '_spread'] = float((np.percentile(v, 75) - np.percentile(v, 25)) / (p75 - p25)) if p75 > p25 else float('nan')
        rows.append(row)
    rows.sort(key=lambda r: -r.get('pilot_sep', 0))
    P('== 1. battery (%d style features; refs %s)' % (len(rows), ', '.join(f'{p} {len(B[p])}' for p in B)))
    for s in Bs:
        P('  %-9s median in-band %.2f | features off the closest dialect (sep>0.5): %d | median spread vs refs %.2f' % (s, np.median([r.get(s + '_in', np.nan) for r in rows]),
          sum(r.get(s + '_sep', 0) > 0.5 for r in rows), np.nanmedian([r.get(s + '_spread', np.nan) for r in rows])))
    P('  worst features for the pilot (sep, in-band, p50 vs ref p10..p90):')
    for r in rows[:15]: P('    %-20s sep %.2f in %3.0f%% p50 %.3f [%.3f..%.3f]' % (r['f'], r.get('pilot_sep', 0), 100 * r.get('pilot_in', 0), r.get('pilot_p50', np.nan), r['p10'], r['p90']))
    G = [k for k in F if np.isfinite(ref[k]).mean() > 0.9]
    allref = [r for p in B for r in B[p].values()]
    med = {k: np.nanmedian([r.get(k, np.nan) for r in allref]) for k in G}
    iqr = {k: (np.nanpercentile([r.get(k, np.nan) for r in allref], 75) - np.nanpercentile([r.get(k, np.nan) for r in allref], 25)) or 1.0 for k in G}
    Z = lambda rs: np.array([[np.clip(((r.get(k, med[k]) if r.get(k) == r.get(k) else med[k]) - med[k]) / iqr[k], -6, 6) for k in G] for r in rs])
    def kd(rs, refrs): X = Z(refrs); return np.array([np.sort(np.sqrt(((X - x) ** 2).mean(1)))[:3].mean() for x in Z(rs)])
    P('  kNN distance (3 nearest, IQR units) to two dialects - p25/p50/p75/p90:')
    for p in B: P('    %-9s %s' % (p + '->others', np.round(np.percentile(kd(list(B[p].values()), [r for q in B if q != p for r in B[q].values()]), [25, 50, 75, 90]), 2)))
    out_cnt = {}
    for s in Bs:
        v = np.mean([kd(list(Bs[s].values()), [r for q in B if q != p for r in B[q].values()]) for p in B], 0)
        P('    %-9s %s' % (s, np.round(np.percentile(v, [25, 50, 75, 90]), 2)))
        out_cnt[s] = {n: sum(1 for r in rows if r['f'] in Bs[s][n] and Bs[s][n][r['f']] == Bs[s][n][r['f']] and not (r['p10'] <= Bs[s][n][r['f']] <= r['p90'])) for n in Bs[s]}
    rc = [sum(1 for r in rows if x.get(r['f']) == x.get(r['f']) and not (r['p10'] <= x[r['f']] <= r['p90'])) for x in allref]
    P('  features outside ref p10-p90 per species: refs p50 %d p90 %d | ' % (np.median(rc), np.percentile(rc, 90)) + ' | '.join('%s p50 %d p90 %d' % (s, np.median(list(c.values())), np.percentile(list(c.values()), 90)) for s, c in out_cnt.items()))
    # ---- 2. light handling + 3. profile
    from hlstudy import hl
    P('== 2. light handling (BW / PF IQR: step 0.12-0.34 / 0.10-0.22, major step 0.09-0.12 / 0.07-0.09, top_t 0.32-0.36 / 0.33-0.39, back +0.01..+0.13)')
    for s, S in list({'bw': R['bw'], 'pf': R['pf']}.items()) + list(SETS.items()):
        H = [hl(f) for f in S.values()]
        P('  %-9s ' % s + ' '.join('%s %s' % (k, np.round(np.nanpercentile([h[k] for h in H], [25, 50, 75]), 3).tolist()) for k in ('step_ring', 'major_top_step', 'top_t', 'back')))
    P('== 3. light profile top->bottom (L - body median, median over species)')
    P('  %-9s %s' % ('refs', np.round(np.nanmedian(cached('profile_refs', lambda: [profile(f) for p in R for f in R[p].values()]), 0), 3)))
    for s, S in SETS.items(): P('  %-9s %s' % (s, np.round(np.nanmedian([profile(f) for f in S.values()], 0), 3)))
    # ---- 4. fins + 5. motion
    import fincheck3 as FC
    from phase import sig
    FR = {p: cached(f'fins_{p}', lambda p=p: {n: FC.measure(f) for n, f in R[p].items()}) for p in R}
    FS = {s: {n: FC.measure(f) for n, f in S.items()} for s, S in SETS.items()}
    P('== 4. fin rules (share of species inside; p50)')
    hdr = list(FR) + list(FS)
    for (g, k), b in list(FC.B.items()) + list(FC.MB.items()):
        cells = []
        for s in hdr:
            D = FR.get(s) or FS.get(s); v = np.array([x[g][k] for x in D.values() if g in x and x[g].get(k) == x[g].get(k)])
            cells.append('%3.0f%% %.2f' % (100 * ((v >= b[0]) & (v <= b[1])).mean(), np.median(v)) if len(v) else '   -     ')
        P('  %-22s %-12s ' % (g + '.' + k, '%.2f..%.2f' % b) + ' | '.join('%s %s' % (h, c) for h, c in zip(hdr, cells)))
    P('== 5. fin motion (A B C D, A=C): share swinging like a mirror of the tail, base/tip change, magnitude px')
    for s, S in list(R.items()) + list(SETS.items()):
        Sg = [sig(f) for f in S.values()]
        P('  %-9s ' % s + ' | '.join('%s swing %.0f%% base/tip %.2f/%.2f mag %.2f' % (g, 100 * np.mean([x[g]['sym'] < -0.5 for x in Sg if g in x]), np.nanmedian([x[g]['base_change'] for x in Sg if g in x]),
                                     np.nanmedian([x[g]['tip_change'] for x in Sg if g in x]), np.median([x[g]['mag'] for x in Sg if g in x])) for g in ('caudal', 'dorsal', 'ventral')))
    od = os.path.join(d, 'verify'); os.makedirs(od, exist_ok=True)
    open(os.path.join(od, 'report.txt'), 'w').write('\n'.join(lines) + '\n'); json.dump(dict(rows=rows, outside=out_cnt), open(os.path.join(od, 'battery.json'), 'w'), default=float)
    print('\n'.join(lines))
if __name__ == '__main__': main()
