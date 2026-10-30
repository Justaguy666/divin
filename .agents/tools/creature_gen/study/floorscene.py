"""crawlers on the real floor: current set above, new set below, same positions."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths   # generator folder: paths, pal, swim, species modules
import glob, os, re, sys, numpy as np
from PIL import Image, ImageDraw
exec(open(_os.path.join(STUDY, 'bgfit.py')).read().split('def hue')[0])
pre = sys.argv[1]; srcs = sys.argv[2].split(','); names = sys.argv[3].split(','); dst = sys.argv[4]; floor = int(sys.argv[5]) if len(sys.argv) > 5 else 266
Bfull = Image.fromarray(bg(pre, BIO[pre])).convert('RGBA'); crop = (300, 190, 940, 300)
rows = []
for s in srcs:
    d = (C_ + BIO[pre]) if s == '-' else paths.work(s); M = Bfull.crop(crop).copy(); x = 6
    for n in names:
        p = glob.glob(d + f'/{pre}_{n}_*_4f.png')[0]; W, H = map(int, re.search(r'_(\d+)x(\d+)_4f', p).groups()); a = np.array(Image.open(p).convert('RGBA'))[:H, :W]
        M.alpha_composite(Image.fromarray(a), (x, floor - crop[1] - H)); x += W + 4
    rows.append(M)
out = Image.new('RGBA', (rows[0].width, sum(r.height + 4 for r in rows)), (0, 0, 0, 255)); y = 0
for r in rows: out.alpha_composite(r, (0, y)); y += r.height + 4
out.resize((out.width * 3, out.height * 3), Image.NEAREST).save(os.path.join(paths.PREVIEW, dst)); print(out.size)
