"""Soften hard colour boundaries inside the body: markings keep their core and get a halo of intermediate tone on the
surrounding region; boundaries between two large regions (back / belly) get a 2-px intermediate band on both sides.
Eyes, outline pixels and fins are left untouched."""
import sys, os, re, glob, colorsys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.cluster.vq import kmeans2
from creature_audit import lab
def eye_mask(a, body):
    H, W = body.shape; keep = np.zeros_like(body)
    for y in range(H - 1):
        for x in range(W):
            if not body[y, x]: continue
            hh, ll, ss = colorsys.rgb_to_hls(*(a[y, x, :3] / 255))
            ys = np.nonzero(body[:, x])[0]
            upper = y + 1 <= ys.min() + (ys.max() - ys.min()) * 0.6           # eyes sit in the upper part of the head
            if upper and ll > 0.72 and (a[y, x, :3].max() - a[y, x, :3].min()) < 70 and colorsys.rgb_to_hls(*(a[y + 1, x, :3] / 255))[1] < 0.3:
                keep[max(0, y - 1):y + 3, max(0, x - 1):x + 2] = True
    return keep
def soften_frame(f, T=18, w_halo=0.38, w_band=0.28, w2=0.16):
    a = f.astype(float); body = a[:, :, 3] == 255
    pad = np.pad(body, 1)
    inner = body & pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:]
    work = inner & ~eye_mask(a, body)
    if work.sum() < 12: return f
    L = lab(a[:, :, :3])
    pts = L[work]
    np.random.seed(1)
    k = min(10, max(3, len(pts) // 30))
    _, lbl = kmeans2(pts, k, minit='++', seed=1)
    cl = -np.ones(body.shape, int); cl[work] = lbl
    comp = np.zeros(body.shape, int); size = {}
    nid = 0
    for c in range(k):
        lab_, n = ndimage.label(cl == c)
        for i in range(1, n + 1):
            m = lab_ == i; nid += 1; comp[m] = nid; size[nid] = m.sum()
    H, W = body.shape
    out = a.copy(); moved = np.zeros_like(body)
    for y, x in zip(*np.nonzero(work)):
        best = None
        for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if not (0 <= yy < H and 0 <= xx < W) or not inner[yy, xx] or comp[yy, xx] == comp[y, x]: continue
            d = np.linalg.norm(L[y, x] - L[yy, xx])
            if d > T and (best is None or d > best[0]): best = (d, yy, xx)
        if not best: continue
        _, yy, xx = best
        sp, sq = size.get(comp[y, x], 1), size.get(comp[yy, xx], 1)
        if sp >= 1.5 * sq: w = w_halo                       # p is the surrounding region -> halo around the marking
        elif sq >= 1.5 * sp: continue                       # p is the (smaller) marking -> keep its core
        else: w = w_band                                    # two large regions -> soft band on both sides
        out[y, x, :3] = a[y, x, :3] + w * (a[yy, xx, :3] - a[y, x, :3]); moved[y, x] = True
    # second, fainter ring so the transition takes two tones
    a2 = out.copy()
    for y, x in zip(*np.nonzero(work & ~moved)):
        for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= yy < H and 0 <= xx < W and moved[yy, xx] and comp[yy, xx] == comp[y, x]:
                out[y, x, :3] = a2[y, x, :3] + w2 * (a2[yy, xx, :3] - a2[y, x, :3]); break
    return np.clip(out, 0, 255).astype(np.uint8)
def soften_sheet(path, outp):
    m = re.search(r'_(\d+)x(\d+)_4f', path); fw, fh = int(m[1]), int(m[2])
    a = np.array(Image.open(path).convert('RGBA'))
    for y0 in range(0, a.shape[0], fh):
        for x0 in range(0, a.shape[1], fw):
            a[y0:y0 + fh, x0:x0 + fw] = soften_frame(a[y0:y0 + fh, x0:x0 + fw])
    Image.fromarray(a, 'RGBA').save(outp)
if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for p in sys.argv[2:]:
        soften_sheet(p, f'{out}/{os.path.basename(p)}')
    print('ok')
