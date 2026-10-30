"""colour harmony with the water: for all swimmers' opaque pixels, share that are neutral (C < 0.025), share whose hue is
within 45 deg of the background hue, share far from it (> 90 deg), and the mean chroma relative to the background."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths   # generator folder: paths, pal, swim, species modules
import glob, os, re, sys, numpy as np
from PIL import Image
exec(open(_os.path.join(STUDY, 'bgfit.py')).read().split('def hue')[0])
def harm(pre, d, cdir=None):
    B = bg(pre, d); bl = oklab(B[:250].reshape(-1, 3).astype(float)); bh = np.degrees(np.arctan2(np.median(bl[:, 2]), np.median(bl[:, 1]))); bC = np.median(np.hypot(bl[:, 1], bl[:, 2]))
    px = []
    for f in sorted(glob.glob((cdir or C_ + d) + f'/{pre}_*_' + os.environ.get('KIND', 'swim') + '_*_4f.png')):
        W, H = map(int, re.search(r'_(\d+)x(\d+)_4f', f).groups()); a = np.array(Image.open(f).convert('RGBA'))[:H, :W].astype(float); op = a[..., 3] >= 250
        px.append(oklab(a[op][:, :3]))
    L = np.concatenate(px); C = np.hypot(L[:, 1], L[:, 2]); h = np.degrees(np.arctan2(L[:, 2], L[:, 1])); dh = np.abs(((h - bh + 180) % 360) - 180)
    col = C >= 0.025
    return dict(neutral=(~col).mean(), near=(col & (dh <= 45)).mean(), mid=(col & (dh > 45) & (dh <= 90)).mean(), far=(col & (dh > 90)).mean(), Cr=C.mean() / bC, bh=bh)
for p in sys.argv[1:]:
    if ':' in p: pre, cd = p.split(':'); r = harm(pre, BIO[pre], paths.work(cd)); tag = p
    else: r = harm(p, BIO[p]); tag = p
    print('%-22s bg hue %5.0f | neutral %3.0f%%  near-bg-hue %3.0f%%  45-90 %3.0f%%  opposite %3.0f%% | chroma vs bg %.2f' % (tag[:22], r['bh'], 100 * r['neutral'], 100 * r['near'], 100 * r['mid'], 100 * r['far'], r['Cr']))
