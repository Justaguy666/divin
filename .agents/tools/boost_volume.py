"""Raise a flat sprite's value range toward the pf_ reference (L* 95-5 percentile ~70) without changing hues.
One transform per sheet (measured on frame 0), so all frames stay consistent. Eyes are left untouched.
Usage: boost_volume.py <out_dir> <sheets...> [--target 70] [--sat 1.12] [--kmax 1.45]"""
import sys, os, re, colorsys, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image
from creature_audit import lab
ap = argparse.ArgumentParser(); ap.add_argument('out'); ap.add_argument('sheets', nargs='+')
ap.add_argument('--target', type=float, default=70); ap.add_argument('--sat', type=float, default=1.12); ap.add_argument('--kmax', type=float, default=1.45)
A = ap.parse_args(); os.makedirs(A.out, exist_ok=True)
for p in A.sheets:
    m = re.search(r'_(\d+)x(\d+)_4f', p); fw, fh = int(m[1]), int(m[2])
    a = np.array(Image.open(p).convert('RGBA')).astype(float)
    f0 = a[:fh, :fw]; op = f0[:, :, 3] == 255
    L = lab(f0[:, :, :3][op])[:, 0]
    rng = np.percentile(L, 95) - np.percentile(L, 5)
    k = float(np.clip(A.target / max(rng, 1), 1.0, A.kmax))
    hls = np.array([colorsys.rgb_to_hls(*(c / 255)) for c in f0[:, :, :3][op]])
    mid = float(np.median(hls[:, 1]))
    H, W = a.shape[:2]; out = a.copy()
    op_all = a[:, :, 3] > 0
    pad = np.pad(op_all, 1)
    edge = op_all & ~(pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:])
    ke = 1.0                                                  # outline and fins: gentler
    for y in range(H):
        for x in range(W):
            if a[y, x, 3] == 0: continue
            r, g, b = a[y, x, :3] / 255
            hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
            spread = a[y, x, :3].max() - a[y, x, :3].min()
            if (ll > 0.8 and spread < 70) or ll < 0.07: continue          # eye highlight / pupil
            kk = ke if (edge[y, x] or a[y, x, 3] < 255) else k
            nl = float(np.clip(mid + (ll - mid) * kk, 0.05, 0.9))
            ns = min(1.0, ss * A.sat)
            rr, gg, bb = colorsys.hls_to_rgb(hh, nl, ns)
            out[y, x, :3] = (rr * 255, gg * 255, bb * 255)
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), 'RGBA').save(os.path.join(A.out, os.path.basename(p)))
    print(os.path.basename(p), f'range {rng:.0f} -> k {k:.2f}')
