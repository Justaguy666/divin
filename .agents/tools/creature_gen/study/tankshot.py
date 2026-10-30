"""tankshot.py <pre> <dir1,dir2> <out>: (dir "-" = installed sheets) whole roster in one tank per dir (swimmers spread through their bands, crawlers on the floor)."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths   # generator folder: paths, pal, swim, species modules
import glob, os, re, sys, importlib, numpy as np
from PIL import Image
exec(open(_os.path.join(STUDY, 'bgfit.py')).read().split('def hue')[0])
pre, dst = sys.argv[1], sys.argv[3]
dirs = [(_os.path.join(paths.REPO, 'assets/creatures', BIO[pre]) if d == '-' else paths.work(d)) for d in sys.argv[2].split(',')]   # '-' = installed sheets
mods = ('sp1', 'sp2', 'sp3', 'sp4') if pre == 'cs' else sorted(_os.path.basename(f)[:-3] for f in glob.glob(_os.path.join(paths.GEN, pre + '[0-9].py'))); SC = {}; names = []   # species modules of the biome
for m in mods: M_ = importlib.import_module(m); SC.update(M_.SCENE); names += M_.ALL
Bf = Image.fromarray(bg(pre, BIO[pre])).convert('RGBA')
rng = np.random.RandomState(7); pos = {}
sw = [n for n in names if SC[n].get('band')]; cr = [n for n in names if not SC[n].get('band')]
for i, n in enumerate(sw):
    b = SC[n]['band']; pos[n] = (int(20 + (i * 197) % 560), int(b[0] + (b[1] - b[0]) * (0.3 + 0.4 * rng.rand())))
for i, n in enumerate(cr): pos[n] = (12 + i * 68, None)
panels = []
for d in dirs:
    P = Bf.crop((0, 0, 640, 300)).copy()
    for n in sw + cr:
        p = glob.glob(d + f'/{pre}_{n}_*_4f.png')[0]; W, H = map(int, re.search(r'_(\d+)x(\d+)_4f', p).groups()); a = np.array(Image.open(p).convert('RGBA'))[:H, :W]
        x, y = pos[n]; y = 266 - H if y is None else min(300 - H, max(0, y - H // 2))
        P.alpha_composite(Image.fromarray(a), (x, y))
    panels.append(P)
O = Image.new('RGBA', (640, len(panels) * 304), (0, 0, 0, 255))
for k, P in enumerate(panels): O.alpha_composite(P, (0, k * 304))
O.resize((O.width * 2, O.height * 2), Image.NEAREST).save(os.path.join(paths.PREVIEW, dst)); print(O.size)
