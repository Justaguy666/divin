import glob, re, sys, numpy as np
from PIL import Image
from scipy import ndimage
bad = 0; files = sorted(glob.glob(sys.argv[1]))
for f in files:
    kind, W, H = re.search(r'_(swim|crawl)_(\d+)x(\d+)_4f', f).groups(); W, H = int(W), int(H); rows = 6 if kind == 'swim' else 4
    a = np.array(Image.open(f).convert('RGBA')); iss = []
    if a.shape[:2] != (rows * H, 4 * W): iss.append('dims %s' % (a.shape[:2],))
    else:
        for r in range(rows):
            fr = [a[r * H:(r + 1) * H, c * W:(c + 1) * W] for c in range(4)]
            if not np.array_equal(fr[0], fr[2]): iss.append(f'r{r} A!=A')
            for c, F in enumerate(fr):
                al = F[..., 3] > 0
                if al[0].any() or al[:, 0].any() or al[:, -1].any() or (kind == 'swim' and al[-1].any()): iss.append(f'r{r}c{c} edge')
                if kind == 'crawl' and not al[-1].any(): iss.append(f'r{r}c{c} floor')
                lab, n = ndimage.label(al, structure=np.ones((3, 3)))
                if n > 1:
                    sz = ndimage.sum(al, lab, range(1, n + 1))
                    if (sz < 3).any(): iss.append(f'r{r}c{c} speck')
    if iss: bad += 1; print(f.split('/')[-1], iss[:4])
print(len(files), 'sheets,', bad, 'with issues')
