import os, sys, numpy as np, glob, importlib
os.environ['PRE'] = os.environ.get('PRE', 'cs')
import swim, gait, paths
from PIL import Image
swim.use_v3(os.environ['PRE'])
mod = importlib.import_module(sys.argv[1]); out = paths.work(sys.argv[2]); names = sys.argv[3].split(',') if len(sys.argv) > 3 else mod.ALL
os.makedirs(out, exist_ok=True)
for n in names:
    for f in glob.glob(f'{out}/{os.environ["PRE"]}_{n}_*_4f.png'): os.remove(f)
    F = getattr(mod, n)(); g = gait.lookup(os.environ['PRE'], n)
    if g and not getattr(F, 'crawl', False): F.gait = g
    sh, W, H, tags = F.sheet() if hasattr(F, 'sheet') else swim.sheet(F)
    kind = 'crawl' if getattr(F, 'crawl', False) else 'swim'
    Image.fromarray(sh, 'RGBA').save(f'{out}/{os.environ["PRE"]}_{n}_{kind}_{W}x{H}_4f.png'); print(n, W, H, len({tuple(p) for p in sh[:H, :W].reshape(-1, 4) if p[3] == 255}))
