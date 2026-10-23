"""Creature style audit - compares a biome's sprites against the pf_/bw_ reference numbers.

Usage (from the project root):
    python .agents/tools/creature_audit.py <biome_dir> [--rev <git rev>] [--montage out.png]
    e.g. python .agents/tools/creature_audit.py marine/cold_water --montage _audit_cw.png

<biome_dir> is relative to assets/creatures/ and assets/environments/. Without --rev the working tree is read.
Prints one line per sprite (E frame 0 / walk_R frame 0) and FLAGS every value outside the style contract
in .agents/rules/pixel_art_guidelines.md section 0, then the biome averages next to the reference.
--montage writes the reference strip (pf_/bw_ originals) above the biome's sprites on its own background.
"""
import argparse, colorsys, glob, io, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REF = {'planted_freshwater': ('freshwater/planted_freshwater', '5547197'), 'blackwater': ('freshwater/blackwater', '72167f7')}
# style contract (pf_/bw_ originals: colours 62-68, aspect 1.8-2.2, fins 25-29 %, L range 73, 0 % of fish blend into the bg)
LIM = dict(fin=(0.18, 1.0), dE_bg=(20, 999), hard_step=(0.0, 0.08))      # per sprite (fin ignored for crawlers)
BIOME_LIM = dict(aspect_mean=(0.0, 2.25), deep_share=(0.40, 1.0), fin_mean=(0.25, 1.0), blend_share=(0.0, 0.50),
                 colors_median=(45, 110), lrange_mean=(68, 100))


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


def lab(rgb):
    c = np.array(rgb, float) / 255
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.9505, 1, 1.089])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


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


def measure(im, bgl):
    a = np.array(im).astype(float)
    al = a[:, :, 3]
    op, full = al > 0, al == 255
    if full.sum() < 10:
        return None
    lum = 0.3 * a[:, :, 0] + 0.59 * a[:, :, 1] + 0.11 * a[:, :, 2]
    pad = np.pad(op, 1)
    inner = op & pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:] & full
    hd = np.abs(np.diff(lum, axis=1))[inner[:, 1:] & inner[:, :-1]]
    vd = np.abs(np.diff(lum, axis=0))[inner[1:, :] & inner[:-1, :]]
    L = lab(a[:, :, :3][full])
    ys, xs = np.nonzero(op)
    r = dict(colors=len({tuple(c) for c in a[op].astype(int)}),
             fin=((al > 0) & (al < 255)).sum() / op.sum(),
             lrange=np.percentile(L[:, 0], 95) - np.percentile(L[:, 0], 5),
             noise=((hd > 28).sum() + (vd > 28).sum()) / max(1, len(hd) + len(vd)),
             aspect=(xs.max() - xs.min() + 1) / (ys.max() - ys.min() + 1),
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
        flags = [k for k, (lo, hi) in LIM.items() if not lo <= m[k] <= hi and not (crawl and k == 'fin')]
        rows.append((n, crawl, m, flags))
        if not quiet:
            print(f"{n[:46]:46} col {m['colors']:4d} fin {m['fin']*100:4.0f}% L {m['lrange']:5.1f} "
                  f"asp {m['aspect']:4.2f} dEbg {m['dE_bg']:5.1f} step {m['hard_step']*100:4.1f}%  {'FLAG ' + ','.join(flags) if flags else ''}")
    sw = [m for n, c, m, f in rows if not c]
    summ = dict(aspect_mean=np.mean([m['aspect'] for m in sw]), deep_share=np.mean([m['aspect'] < 2.0 for m in sw]),
                fin_mean=np.mean([m['fin'] for m in sw]), blend_share=np.mean([m['dE_bg'] < 20 for n, c, m, f in rows]),
                colors_median=float(np.median([m['colors'] for n, c, m, f in rows])), lrange_mean=np.mean([m['lrange'] for n, c, m, f in rows]))
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
    a = ap.parse_args()
    rows, summ = audit(a.biome, a.rev)
    _, ref = audit(REF['planted_freshwater'][0], REF['planted_freshwater'][1], quiet=True)
    print('\nbiome averages (reference = planted_freshwater original):')
    bad = 0
    for k, (lo, hi) in BIOME_LIM.items():
        ok = lo <= summ[k] <= hi
        bad += not ok
        print(f"  {k:12} {summ[k]:6.2f}   ref {ref[k]:6.2f}   {'OK' if ok else 'FAIL'}")
    nflag = sum(1 for r in rows if r[3])
    print(f'  sprites flagged: {nflag}/{len(rows)}')
    if a.montage:
        montage(a.biome, a.montage)
        print('montage ->', a.montage)
    sys.exit(1 if bad else 0)
