"""Make the static parts of every frame identical to frame 0 of its row: wherever the ORIGINAL (git HEAD) frames agree
pixel-for-pixel with their row's frame 0, the processed frame takes the processed frame 0 pixel."""
import sys, io, re, os, subprocess, glob
import numpy as np
from PIL import Image
R = os.path.expanduser('~/mnt/divin')
def head(path):
    rel = os.path.relpath(path, R).replace(os.sep, '/')
    b = subprocess.run(['git', '-C', R, 'show', f'HEAD:{rel}'], capture_output=True).stdout
    return np.array(Image.open(io.BytesIO(b)).convert('RGBA')) if b else None
for p in sys.argv[1:]:
    m = re.search(r'_(\d+)x(\d+)_4f', p); fw, fh = int(m[1]), int(m[2])
    o = head(p); n = np.array(Image.open(p).convert('RGBA'))
    if o is None or o.shape != n.shape: print('skip', p); continue
    ch = 0
    for y0 in range(0, n.shape[0], fh):
        o0 = o[y0:y0 + fh, 0:fw]; n0 = n[y0:y0 + fh, 0:fw]
        for x0 in range(fw, n.shape[1], fw):
            oc = o[y0:y0 + fh, x0:x0 + fw]; nc = n[y0:y0 + fh, x0:x0 + fw]
            best = None
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    os_ = np.roll(np.roll(o0, dy, 0), dx, 1)
                    same = (oc == os_).all(-1) & (os_[:, :, 3] > 0)
                    if best is None or same.sum() > best[0]: best = (same.sum(), dy, dx, same)
            _, dy, dx, same = best
            ns = np.roll(np.roll(n0, dy, 0), dx, 1)
            diff = same & ~(nc == ns).all(-1)
            ch += diff.sum(); nc[same] = ns[same]
    Image.fromarray(n, 'RGBA').save(p)
    print(os.path.basename(p), 'stabilized px', int(ch))
