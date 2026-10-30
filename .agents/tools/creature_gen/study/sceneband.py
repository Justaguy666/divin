"""current vs new, each species at the middle of its own swim band (real depth/water colour), two panels side by side."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths   # generator folder: paths, pal, swim, species modules
import glob, os, re, sys, importlib, numpy as np
from PIL import Image, ImageDraw
exec(open(_os.path.join(STUDY, 'bgfit.py')).read().split('def hue')[0])
pre, mod, newdir, names, dst = sys.argv[1], sys.argv[2], paths.work(sys.argv[3]), sys.argv[4].split(','), sys.argv[5]
SC = {}
for m in mod.split('+'): SC.update(importlib.import_module(m).SCENE)
Bfull = Image.fromarray(bg(pre, BIO[pre])).convert('RGBA'); pw = 400
M = Image.new('RGBA', (2 * pw + 6, 300), (0, 0, 0, 255))
for j, d in enumerate((C_ + BIO[pre], newdir)):
    P = Bfull.crop((260 + j * pw, 0, 260 + (j + 1) * pw, 300)).copy(); lanes = [0, 0, 0]
    for i, n in enumerate(names):
        p = glob.glob(d + f'/{pre}_{n}_*_4f.png')[0]; W, H = map(int, re.search(r'_(\d+)x(\d+)_4f', p).groups()); a = np.array(Image.open(p).convert('RGBA'))[:H, :W]
        b = SC[n].get('band'); yc = (b[0] + b[1]) // 2 if b else 262; lane = i % 3; x = 10 + lane * 130 + (i // 3 % 2) * 20
        y = min(300 - H, max(0, yc - H // 2)) if b else 266 - H
        P.alpha_composite(Image.fromarray(a), (x, y))
    M.alpha_composite(P, (j * (pw + 6), 0))
M = M.resize((M.width * 3, M.height * 3), Image.NEAREST); dr = ImageDraw.Draw(M)
dr.text((8, 6), 'current', fill=(0, 0, 0, 255)); dr.text(((pw + 6) * 3 + 8, 6), 'v3', fill=(0, 0, 0, 255))
M.save(os.path.join(paths.PREVIEW, dst)); print(M.size)
