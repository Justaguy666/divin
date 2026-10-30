import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths   # generator folder: paths, pal, swim, species modules
import glob, os, re, sys, numpy as np
from PIL import Image, ImageDraw
src = open(_os.path.join(STUDY, 'metrics.py')).read().split('def frames')[0]; g = {'__file__': _os.path.join(STUDY, 'metrics.py')}; exec(src, g); oklab = g['oklab']
pre, bio, newdir, bg, names, dst = sys.argv[1], sys.argv[2], sys.argv[3], tuple(int(x) for x in sys.argv[4].split(',')), sys.argv[5].split(','), sys.argv[6]
A = _os.path.join(paths.REPO, f'assets/creatures/{bio}/'); N = paths.work(newdir) + '/'
def load(p):
    W, H = map(int, re.search(r'_(\d+)x(\d+)_4f', p).groups()); a = np.array(Image.open(p).convert('RGBA'))[:H, :W]
    ys, xs = np.where(a[..., 3] > 0); return a[ys.min() - 1:ys.max() + 2, xs.min() - 1:xs.max() + 2]
def val(a):
    out = np.zeros_like(a); op = a[..., 3] > 0; L = np.zeros(a.shape[:2]); L[op] = oklab(a[op][:, :3].astype(float))[:, 0]
    v = (np.clip(L, 0, 1) * 255).astype(np.uint8); out[..., 0] = v; out[..., 1] = v; out[..., 2] = v; out[..., 3] = a[..., 3]; return out
rows = []
for n in names:
    o = load(glob.glob(A + f'{pre}_{n}_*_4f.png')[0]); w = load(glob.glob(N + f'{pre}_{n}_*_4f.png')[0]); rows.append([o, w, val(o), val(w)])
cw = max(c.shape[1] for r in rows for c in r) + 4; S = 5
M = Image.new('RGBA', (4 * cw, sum(max(c.shape[0] for c in r) + 4 for r in rows) + 12), (60, 60, 60, 255)); y = 12
for r in rows:
    for j, c in enumerate(r):
        im = Image.new('RGBA', (c.shape[1], c.shape[0]), (bg if j < 2 else (60, 60, 60)) + (255,)); im.alpha_composite(Image.fromarray(c)); M.alpha_composite(im, (j * cw + 2, y))
    y += max(c.shape[0] for c in r) + 4
M = M.resize((M.width * S, M.height * S), Image.NEAREST); d = ImageDraw.Draw(M)
for j, t in enumerate(['current', 'v3 pilot', 'current (value)', 'v3 (value)']): d.text((j * cw * S + 6, 14), t, fill=(255, 255, 255, 255))
M.save(os.path.join(paths.PREVIEW, dst)); print(M.size)
