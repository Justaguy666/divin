"""Creature style audit - report measurements and advisory comparisons for a biome.

Usage (from the project root):
    python .agents/tools/creature_audit.py <biome_dir> [--rev <git rev>] [--montage out.png]
    e.g. python .agents/tools/creature_audit.py marine/cold_water --montage _audit_cw.png

<biome_dir> is relative to assets/creatures/ and assets/environments/. Without --rev the working tree is read.
Prints per-sprite measurements for the first frame and aggregate swimmer/crawler summaries.
Thresholds are diagnostic hints by default; pass --strict to use them as a non-zero exit gate.
--montage writes accepted PF/BW/AC reference strips above the biome's sprites on their respective backgrounds.
"""
import argparse, glob, io, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REF = {
    'planted_freshwater': ('freshwater/planted_freshwater', '5547197'),
    'blackwater': ('freshwater/blackwater', '72167f7'),
    # AC is an explicitly accepted style reference; its current tree version is measured.
    'ancient_cold_lake': ('freshwater/ancient_cold_lake', 'f755afe3'),
}
# Broad diagnostic ranges that contain the accepted PF/BW/AC snapshots.
# They locate extremes; they are not universal quality targets.
SPRITE_HINTS = dict(dE_bg=(20, 999), hard_step=(0.0, 0.08))
BIOME_HINTS = dict(body_aspect_mean=(1.0, 2.6), deep_share=(0.20, 0.80),
                   colors_rgb_median=(30, 70), lrange_mean=(60, 80))


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True).stdout


def sprites(d, rev=None):
    out = []
    if rev:
        names = [p for p in git('ls-tree', '--name-only', rev, f'assets/creatures/{d}/').decode().split() if p.endswith('.png')]
        load = lambda p: Image.open(io.BytesIO(git('show', f'{rev}:{p}')))
    else:
        names = sorted(glob.glob(os.path.join(ROOT, 'assets', 'creatures', d, '*.png')))
        load = Image.open
    for p in names:
        m = re.search(r'_(\d+)x(\d+)_4f', p)
        if m:
            w, h = int(m[1]), int(m[2])
            out.append((os.path.basename(p), load(p).convert('RGBA').crop((0, 0, w, h)), 'crawl' in p))
    return out


def sheet_checks(d, rev=None):
    """Check expected sheet dimensions, A-B-A equality, and empty row margins."""
    if rev:
        names = [p for p in git('ls-tree', '--name-only', rev, f'assets/creatures/{d}/').decode().split() if p.endswith('.png')]
        load = lambda p: Image.open(io.BytesIO(git('show', f'{rev}:{p}')))
    else:
        names = sorted(glob.glob(os.path.join(ROOT, 'assets', 'creatures', d, '*.png')))
        load = Image.open
    checks = []
    for p in names:
        m = re.search(r'_(\d+)x(\d+)_4f', p)
        if not m:
            continue
        w, h = int(m[1]), int(m[2])
        crawl = 'crawl' in p
        row_count = 4 if crawl else 6
        sheet = load(p).convert('RGBA')
        dim_ok = sheet.size == (w * 4, h * row_count)
        ac_bad = edge_rows = 0
        if dim_ok:
            for row in range(row_count):
                cell_a = sheet.crop((0, row * h, w, (row + 1) * h))
                cell_b = sheet.crop((w, row * h, 2 * w, (row + 1) * h))
                cell_c = sheet.crop((2 * w, row * h, 3 * w, (row + 1) * h))
                if not crawl:
                    aa, cc = np.asarray(cell_a), np.asarray(cell_c)
                    visible = (aa[:, :, 3] > 0) | (cc[:, :, 3] > 0)
                    if np.any((aa != cc).any(axis=2) & visible):
                        ac_bad += 1
                touched = False
                for col in range(4):
                    a = np.asarray(sheet.crop((col * w, row * h, (col + 1) * w, (row + 1) * h)))[:, :, 3]
                    if np.any(a[0, :] > 0) or np.any(a[-1, :] > 0) or np.any(a[:, 0] > 0) or np.any(a[:, -1] > 0):
                        touched = True
                edge_rows += int(touched)
        checks.append((os.path.basename(p), crawl, dim_ok, ac_bad, edge_rows))
    return checks


def lab(rgb):
    c = np.array(rgb, float) / 255
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.9505, 1, 1.089])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def oklab(rgb):
    c = np.array(rgb, float) / 255
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    lms = c @ np.array([[0.4122214708, 0.2119034982, 0.0883024619],
                        [0.5363325363, 0.6806995451, 0.2817188376],
                        [0.0514459929, 0.1073969566, 0.6299787005]])
    lms = np.cbrt(lms)
    return lms @ np.array([[0.2104542553, 1.9779984951, 0.0259040371],
                           [0.7936177850, -2.4285922050, 0.7827717662],
                           [-0.0040720468, 0.4505937099, -0.8086757660]])


def hue_family_share(hues):
    if len(hues) == 0:
        return 0.0
    bins = np.bincount(np.floor(hues).astype(int) % 360, minlength=360)
    wrapped = np.r_[bins[-15:], bins, bins[:15]]
    window = np.convolve(wrapped, np.ones(31, dtype=int), mode='valid')
    return float(window.max() / len(hues))


def bg_lab(d):
    fs = sorted(glob.glob(os.path.join(ROOT, 'assets', 'environments', d, 'background', 'far', '*.png')))
    if not fs:
        return None
    a = np.array(Image.open(fs[0]).convert('RGBA')).reshape(-1, 4)
    return lab(a[a[:, 3] > 200][:, :3]).mean(0)


def hard_steps(a, inner, T=28, flat=12):
    """Share of interior pixel pairs that jump by more than dE T between two flat runs (no intermediate tone)."""
    Lb = lab(a[:, :, :3]); n = 0
    for arr, msk in ((Lb, inner), (Lb.transpose(1, 0, 2), inner.T)):
        d = np.linalg.norm(arr[1:] - arr[:-1], axis=-1)
        ok = msk[1:] & msk[:-1]
        for i in range(1, arr.shape[0] - 2):
            n += (ok[i] & ok[i - 1] & ok[i + 1] & (d[i] > T) & (d[i - 1] < flat) & (d[i + 1] < flat)).sum()
    return n / max(1, inner.sum())


def binary_open(mask):
    """3x3 cross opening used as a rough body mask; fall back for small/translucent sprites."""
    h, w = mask.shape
    offsets = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
    padded = np.pad(mask, 1)
    eroded = np.ones_like(mask, dtype=bool)
    for dy, dx in offsets:
        eroded &= padded[1 + dy:1 + dy + h, 1 + dx:1 + dx + w]
    padded = np.pad(eroded, 1)
    opened = np.zeros_like(mask, dtype=bool)
    for dy, dx in offsets:
        opened |= padded[1 + dy:1 + dy + h, 1 + dx:1 + dx + w]
    if opened.sum() < max(8, int(mask.sum() * 0.25)):
        return mask, True
    return opened, False


def bbox_aspect(mask):
    ys, xs = np.nonzero(mask)
    if len(xs) == 0:
        return 0.0
    return (xs.max() - xs.min() + 1) / (ys.max() - ys.min() + 1)


def measure(im, bgl):
    a = np.array(im).astype(float)
    al = a[:, :, 3]
    op, full = al > 0, al == 255
    if op.sum() < 10:
        return None
    lum = 0.3 * a[:, :, 0] + 0.59 * a[:, :, 1] + 0.11 * a[:, :, 2]
    pad = np.pad(op, 1)
    inner = op & pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:] & full
    hd = np.abs(np.diff(lum, axis=1))[inner[:, 1:] & inner[:, :-1]]
    vd = np.abs(np.diff(lum, axis=0))[inner[1:, :] & inner[:-1, :]]
    # Use opaque colors for value range when available; translucent sprites still contribute
    # through their visible pixels instead of being dropped from the audit.
    value_mask = full if full.sum() >= 10 else op
    L = lab(a[:, :, :3][value_mask])
    body, body_fallback = binary_open(op)
    rgb = a[op, :3].astype(int)
    rgba = a[op].astype(int)
    ok = oklab(rgb)
    chroma = np.hypot(ok[:, 1], ok[:, 2])
    hue = (np.degrees(np.arctan2(ok[:, 2], ok[:, 1])) + 360) % 360
    chromatic = chroma >= 0.02
    r = dict(colors_rgb=len({tuple(c) for c in rgb}),
             colors_rgba=len({tuple(c) for c in rgba}),
             partial_alpha=((al > 0) & (al < 255)).sum() / op.sum(),
             dark_share=float(np.mean(ok[:, 0] < 0.35)),
             hue_family=hue_family_share(hue[chromatic]),
             chroma90=float(np.percentile(chroma, 90)),
             lrange=np.percentile(L[:, 0], 95) - np.percentile(L[:, 0], 5),
             noise=((hd > 28).sum() + (vd > 28).sum()) / max(1, len(hd) + len(vd)),
             aspect=bbox_aspect(body), silhouette_aspect=bbox_aspect(op), body_fallback=body_fallback,
             dE_bg=float(np.linalg.norm(L.mean(0) - bgl)) if bgl is not None else 99.0,
             hard_step=hard_steps(a, inner))
    return r


def audit(d, rev=None, quiet=False):
    bgl = bg_lab(d)
    rows = []
    for n, im, crawl in sprites(d, rev):
        m = measure(im, bgl)
        if not m:
            continue
        flags = [k for k, (lo, hi) in SPRITE_HINTS.items() if not lo <= m[k] <= hi]
        rows.append((n, crawl, m, flags))
        if not quiet:
            label = ('ADVISORY ' + ','.join(flags)) if flags else ''
            print(f"{n[:46]:46} RGB {m['colors_rgb']:3d} RGBA {m['colors_rgba']:3d} "
                  f"alpha {m['partial_alpha']*100:4.0f}% dark {m['dark_share']*100:4.0f}% "
                  f"hue {m['hue_family']*100:3.0f}% C90 {m['chroma90']:.3f} L {m['lrange']:5.1f} "
                  f"body {m['aspect']:4.2f} silhouette {m['silhouette_aspect']:4.2f} "
                  f"dEbg {m['dE_bg']:5.1f} step {m['hard_step']*100:4.1f}%  {label}")

    def summary(group):
        if not group:
            return dict(count=0)
        return dict(count=len(group),
                    body_aspect_mean=float(np.mean([m['aspect'] for m in group])),
                    deep_share=float(np.mean([m['aspect'] < 2.0 for m in group])),
                    partial_alpha_mean=float(np.mean([m['partial_alpha'] for m in group])),
                    blend_share=float(np.mean([m['dE_bg'] < 20 for m in group])),
                    colors_rgb_median=float(np.median([m['colors_rgb'] for m in group])),
                    colors_rgba_median=float(np.median([m['colors_rgba'] for m in group])),
                    dark_share_median=float(np.median([m['dark_share'] for m in group])),
                    hue_family_median=float(np.median([m['hue_family'] for m in group])),
                    chroma90_median=float(np.median([m['chroma90'] for m in group])),
                    lrange_mean=float(np.mean([m['lrange'] for m in group])))

    sw = [m for n, c, m, f in rows if not c]
    cr = [m for n, c, m, f in rows if c]
    summ = {'swimmers': summary(sw), 'crawlers': summary(cr)}
    return rows, summ


def montage(d, out, S=3):
    strips = []
    for label, (rd, rev) in list(REF.items()) + [(d.split('/')[-1], (d, None))]:
        fr = sprites(rd, rev)
        sw = sorted([f for f in fr if not f[2]], key=lambda f: f[1].size[0] * f[1].size[1])
        cr = [f for f in fr if f[2]]
        pick = [sw[i] for i in np.linspace(0, len(sw) - 1, min(7, len(sw))).astype(int)] + cr[:2]
        W, Hh = 520, 64
        bg = Image.new('RGBA', (W, Hh), (0, 0, 0, 255))
        for lay in ('far', 'mid'):
            fs = sorted(glob.glob(os.path.join(ROOT, 'assets', 'environments', rd, 'background', lay, '*.png')))
            if fs:
                im = Image.open(fs[0]).convert('RGBA')
                y0 = int(im.height * 0.45)
                bg.alpha_composite(im.crop((200, y0, 200 + W, y0 + Hh)))
        x = 4
        for n, im, c in pick:
            if x + im.width > W - 2:
                break
            bg.alpha_composite(im, (x, max(0, Hh - im.height - 2 if c else (Hh - im.height) // 2)))
            x += im.width + 5
        strips.append((label + (' (reference)' if rev else ''), bg.resize((W * S, Hh * S), Image.NEAREST)))
    res = Image.new('RGBA', (strips[0][1].width, sum(s.height + 22 for _, s in strips)), (16, 16, 20, 255))
    dr = ImageDraw.Draw(res)
    y = 0
    for lab_, s in strips:
        dr.text((6, y + 5), lab_, fill=(240, 240, 240, 255))
        res.paste(s, (0, y + 22))
        y += s.height + 22
    res.save(out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('biome')
    ap.add_argument('--rev')
    ap.add_argument('--montage')
    ap.add_argument('--strict', action='store_true', help='return exit code 1 when any advisory range or per-sprite hint is triggered')
    a = ap.parse_args()
    rows, summ = audit(a.biome, a.rev)
    print('\nSwimmer summary (diagnostic hints; swimmers only):')
    sw = summ['swimmers']
    for k, (lo, hi) in BIOME_HINTS.items():
        v = sw.get(k, float('nan'))
        within = lo <= v <= hi
        state = 'within hint' if within else 'outside hint'
        print(f'  {k:22} {v:7.2f}   hint {lo:.2f}..{hi:.2f}   {state}')

    print('\nAccepted reference snapshots:')
    refs = {}
    for label, (rd, rev) in REF.items():
        _, refs[label] = audit(rd, rev, quiet=True)
    for label, ref in refs.items():
        s = ref['swimmers']
        print(f"  {label:24} body {s.get('body_aspect_mean', float('nan')):.2f}  "
              f"deep {s.get('deep_share', float('nan'))*100:.0f}%  "
              f"RGB {s.get('colors_rgb_median', float('nan')):.1f}  "
              f"alpha {s.get('partial_alpha_mean', float('nan'))*100:.0f}%  "
              f"dark {s.get('dark_share_median', float('nan'))*100:.0f}%  "
              f"hue {s.get('hue_family_median', float('nan'))*100:.0f}%  "
              f"C90 {s.get('chroma90_median', float('nan')):.3f}  "
              f"L {s.get('lrange_mean', float('nan')):.1f}")

    print('\nCrawler summary (separate sample; no swimmer targets):')
    cr = summ['crawlers']
    if cr.get('count', 0):
        print(f"  measured {cr['count']}; RGB median {cr['colors_rgb_median']:.1f}; "
              f"RGBA median {cr['colors_rgba_median']:.1f}; "
              f"partial alpha mean {cr['partial_alpha_mean']*100:.1f}%; L range mean {cr['lrange_mean']:.1f}")
    else:
        print('  no crawler sprites')

    checks = sheet_checks(a.biome, a.rev)
    swims = [c for c in checks if not c[1]]
    bad_dims = sum(not c[2] for c in checks)
    bad_ac = sum(c[3] for c in swims)
    edge_rows = sum(c[4] for c in swims)
    swim_rows = 6 * len(swims)
    print('\nSheet/animation checks:')
    print(f'  dimension mismatches: {bad_dims}/{len(checks)} sheets')
    print(f'  A=C mismatched rows: {bad_ac}/{swim_rows} swimmer rows')
    print(f'  boundary-touch rows: {edge_rows}/{swim_rows} swimmer rows (any frame in row touches edge)')

    nflag = sum(1 for r in rows if r[3])
    print(f'\nPer-sprite advisory flags: {nflag}/{len(rows)}; use them to locate sprites for visual review.')
    hint_out = any(not (lo <= sw.get(k, float('nan')) <= hi) for k, (lo, hi) in BIOME_HINTS.items())
    if a.montage:
        montage(a.biome, a.montage)
        print('montage ->', a.montage)
    sys.exit(1 if a.strict and (hint_out or nflag or bad_dims or bad_ac) else 0)
