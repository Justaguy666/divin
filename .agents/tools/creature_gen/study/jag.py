"""silhouette staircase regularity (frame A, E row): along the top and bottom body contour, count 'jaggies' -
places where the step pattern breaks a smooth curve (a run between two shorter runs on a slope, or 1-px bumps)."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths, biomes   # generator folder: paths, pal, swim, species modules
import glob, os, re, sys, numpy as np
from PIL import Image
R = _os.path.join(paths.REPO, 'assets/creatures/')
BIO = {p: biomes.rel(p) for p in biomes.ALL}
def contour(col):
    # runs of equal y along x
    runs = []; y0 = col[0]; n = 1
    for y in col[1:]:
        if y == y0: n += 1
        else: runs.append((y0, n)); y0 = y; n = 1
    runs.append((y0, n)); return runs
def jag(f):
    kind, W, H = re.search(r'_(swim|crawl)_(\d+)x(\d+)_4f', f).groups(); W, H = int(W), int(H)
    if kind != 'swim': return None
    a = np.array(Image.open(f).convert('RGBA'))[:H, :W]; op = a[..., 3] >= 250
    xs = np.where(op.sum(0) >= 3)[0]
    if len(xs) < 8: return None
    xs = np.arange(xs.min(), xs.max() + 1); xs = [x for x in xs if op[:, x].any()]
    J = 0; steps = 0
    for c in ([np.where(op[:, x])[0].min() for x in xs], [np.where(op[:, x])[0].max() for x in xs]):
        r = contour(c)
        for i in range(1, len(r) - 1):
            (ya, na), (yb, nb), (yc, nc) = r[i - 1], r[i], r[i + 1]
            dy1, dy2 = yb - ya, yc - yb; steps += 1
            if abs(dy1) > 1 or abs(dy2) > 1: continue          # steep part: not judged
            if np.sign(dy1) != np.sign(dy2) and nb <= 2: J += 1  # 1-2 px bump or notch
            elif np.sign(dy1) == np.sign(dy2) and nb < min(na, nc) and min(na, nc) >= 3: J += 1   # short run between two longer ones on a slope
    return J / max(1, steps)
for pre in (sys.argv[1:] or BIO):
    if ':' in pre:
        p_, d_ = pre.split(':'); v = [x for x in (jag(f) for f in glob.glob(paths.work(d_) + f'/{p_}_*_4f.png')) if x is not None]; print(pre, 'jaggies median %.3f mean %.3f' % (np.median(v), np.mean(v))); continue
    v = [x for x in (jag(f) for f in glob.glob(R + BIO[pre] + f'/{pre}_*_4f.png')) if x is not None]
    print(pre, 'jaggies per contour step: median %.3f  mean %.3f' % (np.median(v), np.mean(v)))
