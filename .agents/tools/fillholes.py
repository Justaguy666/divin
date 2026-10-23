import sys, re, os
import numpy as np
from PIL import Image
from scipy import ndimage
def fill(path):
    m = re.search(r'_(\d+)x(\d+)_4f', path); fw, fh = int(m[1]), int(m[2])
    a = np.array(Image.open(path).convert('RGBA'))
    tot = 0
    for y0 in range(0, a.shape[0], fh):
        for x0 in range(0, a.shape[1], fw):
            f = a[y0:y0 + fh, x0:x0 + fw]
            for _ in range(20):
                op = f[:, :, 3] > 0
                h = ndimage.binary_fill_holes(op) & ~op
                if not h.any(): break
                src = f.copy()
                for y, x in zip(*np.nonzero(h)):
                    nb = [src[yy, xx] for yy, xx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1),(y-1,x-1),(y+1,x+1),(y-1,x+1),(y+1,x-1))
                          if 0 <= yy < fh and 0 <= xx < fw and src[yy, xx, 3] > 0]
                    if nb:
                        fins = [c for c in nb if c[3] < 255]
                        c = np.mean(fins if fins else nb, 0)
                        if not fins: c[3] = 200
                        f[y, x] = c.astype(np.uint8); tot += 1
    Image.fromarray(a, 'RGBA').save(path)
    return tot
for p in sys.argv[1:]:
    print(os.path.basename(p), fill(p))
