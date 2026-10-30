"""how creatures stand out from their background: biome bg (far+mid+near composite, water area) vs creature body / outline."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths, biomes   # generator folder: paths, pal, swim, species modules
import glob, os, re, sys, numpy as np
from PIL import Image
src = open(_os.path.join(STUDY, 'metrics.py')).read().split('def frames')[0]; g = {'__file__': _os.path.join(STUDY, 'metrics.py')}; exec(src, g); oklab = g['oklab']
E_ = _os.path.join(paths.REPO, 'assets/environments/'); C_ = _os.path.join(paths.REPO, 'assets/creatures/')
BIO = {p: biomes.rel(p) for p in biomes.ALL}
def bg(pre, d):
    lay = [Image.open(glob.glob(E_ + d + f'/background/{k}/*.png')[0]).convert('RGBA') for k in ('far', 'mid', 'near')]
    M = Image.new('RGBA', lay[0].size, (0, 0, 0, 255))
    for l in lay: M.alpha_composite(l)
    return np.array(M)[:, :, :3]
def hue(lab): return np.degrees(np.arctan2(lab[..., 2], lab[..., 1]))
def stats(pre, d, cdir=None):
    B = bg(pre, d); bl = oklab(B[:250].reshape(-1, 3).astype(float)); bL = bl[:, 0]; bC = np.hypot(bl[:, 1], bl[:, 2]); bh = np.degrees(np.arctan2(bl[:, 2].mean(), bl[:, 1].mean()))
    rows = []
    for f in sorted(glob.glob((cdir or C_ + d) + f'/{pre}_*_' + os.environ.get('KIND', 'swim') + '_*_4f.png')):
        W, H = map(int, re.search(r'_(\d+)x(\d+)_4f', f).groups()); a = np.array(Image.open(f).convert('RGBA'))[:H, :W].astype(float)
        op = a[..., 3] >= 250
        if op.sum() < 20: continue
        pad = np.pad(op, 1); edge = op & ~(pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:])
        L = oklab(a[op][:, :3]); E = oklab(a[edge][:, :3])
        rows.append(dict(bodyL=np.median(L[:, 0]), lightL=np.percentile(L[:, 0], 85), edgeL=np.median(E[:, 0]), C=np.median(np.hypot(L[:, 1], L[:, 2])),
                         h=np.degrees(np.arctan2(np.median(L[:, 2]), np.median(L[:, 1])))))
    m = lambda k: np.median([r[k] for r in rows])
    hd = abs(((m('h') - bh + 180) % 360) - 180)
    print(f"{pre}  bg L {np.median(bL):.2f} (p10 {np.percentile(bL,10):.2f} p90 {np.percentile(bL,90):.2f}) C {np.median(bC):.3f} hue {bh:5.0f} | fish body L {m('bodyL'):.2f} light {m('lightL'):.2f} edge {m('edgeL'):.2f} C {m('C'):.3f} hue {m('h'):5.0f} | "
          f"body-bg {m('bodyL') - np.median(bL):+.2f} light-bg {m('lightL') - np.median(bL):+.2f} edge-bg {m('edgeL') - np.median(bL):+.2f} C ratio {m('C') / max(1e-6, np.median(bC)):.2f} hue gap {hd:3.0f}")
for p in (sys.argv[1:] or BIO):
    if ':' in p: pre, cd = p.split(':'); stats(pre, BIO[pre], paths.work(cd))
    else: stats(p, BIO[p])
