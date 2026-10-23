import numpy as np
from scipy import ndimage
def scale_fins(sheet, fw, fh, k=1.3):
    a = np.array(sheet).copy()
    H, W = a.shape[:2]
    for y0 in range(0, H, fh):
        for x0 in range(0, W, fw):
            f = a[y0:y0 + fh, x0:x0 + fw]
            al = f[:, :, 3]
            body = al == 255
            fin = (al > 0) & (al < 255)
            near = ndimage.binary_dilation(body)
            lab, n = ndimage.label(fin)
            src = f.copy()
            for i in range(1, n + 1):
                comp = lab == i
                base = comp & near
                if comp.sum() < 4 or not base.any():
                    continue
                by, bx = np.nonzero(base); cy, cx = by.mean(), bx.mean()
                ys, xs = np.nonzero(comp)
                Y0, Y1 = max(1, int(cy + (ys.min() - cy) * k) - 1), min(fh - 2, int(cy + (ys.max() - cy) * k) + 1)
                X0, X1 = max(1, int(cx + (xs.min() - cx) * k) - 1), min(fw - 2, int(cx + (xs.max() - cx) * k) + 1)
                for ty in range(Y0, Y1 + 1):
                    for tx in range(X0, X1 + 1):
                        if f[ty, tx, 3] != 0:
                            continue
                        sy, sx = int(round(cy + (ty - cy) / k)), int(round(cx + (tx - cx) / k))
                        if 0 <= sy < fh and 0 <= sx < fw and comp[sy, sx]:
                            f[ty, tx] = src[sy, sx]
    return a
