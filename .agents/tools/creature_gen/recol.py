"""Keep an existing sprite's drawing but re-map its colours onto the biome lighting ramp and the BW outline rule."""
import os, numpy as np, re, glob
import paths
from PIL import Image
import pal
from swim import rgba
class Recolor:
    crawl = True
    def __init__(s, src, base, sig=(), tags=('walk_R', 'walk_L', 'idle_R', 'idle_L'), cuts=(6, 16, 32, 52, 74, 92)):
        s.src, s.base, s.sig, s.tags, s.cuts = src, base, sig, list(tags), cuts
    def sheet(s):
        f = glob.glob(s.src if os.path.isabs(s.src) else os.path.join(paths.GEN, s.src))[0]; W, H = map(int, re.search(r'_(\d+)x(\d+)_4f', f).groups())
        a = np.array(Image.open(f).convert('RGBA')).astype(float); op = a[..., 3] > 0
        L = np.zeros(a.shape[:2]); C = np.zeros(a.shape[:2]); Hh = np.zeros(a.shape[:2])
        for j, i in zip(*np.where(op)):
            l = pal.lab(a[j, i, :3] / 255); L[j, i] = l[0]; C[j, i] = np.hypot(l[1], l[2]); Hh[j, i] = np.degrees(np.arctan2(l[2], l[1])) % 360
        body = ramp_ = list(s.base) if isinstance(s.base, (list, tuple)) else (list(pal.FAM[s.base]) if s.base in pal.FAM else pal.ramp(s.base))   # hex base or a v3 colour family
        q = np.percentile(L[op], s.cuts); out = a.copy()
        sigm = np.zeros(op.shape, bool); sramp = None
        smax = 5
        for sg in s.sig:
            h0, h1, cmin, hexc = sg[:4]; smax = sg[4] if len(sg) > 4 else 5
            m = op & (C > cmin) & (((Hh - h0) % 360) < ((h1 - h0) % 360)); sigm |= m; sramp = (m, pal.ramp(hexc, sig=True))
        for j, i in zip(*np.where(op)):
            l = L[j, i]
            if l > 0.93: out[j, i, :3] = rgba('#fff0c4')[:3]; continue
            if l < 0.14: out[j, i, :3] = rgba('#0c0e0c')[:3]; continue
            t = int(np.clip(np.searchsorted(q, l) - 1, 0, 5))
            rp = body
            if sramp is not None and sigm[j, i]: rp = sramp[1]; t = min(smax, t + 1)
            out[j, i, :3] = rgba(rp[t])[:3]
        # BW outline: shade of the colour just inside, lit on top, darkest under the belly
        pad = np.pad(op, 1, constant_values=False); up = ~pad[:-2, 1:-1]; dn = ~pad[2:, 1:-1]; lf = ~pad[1:-1, :-2]; rt = ~pad[1:-1, 2:]
        res = out.copy(); A = out.shape
        for j, i in zip(*np.where(op & (up | dn | lf | rt) & (out[..., 3] == 255))):
            jj = j + 1 if (up[j, i] and not dn[j, i] and j + 1 < A[0] and op[j + 1, i]) else (j - 1 if (dn[j, i] and not up[j, i] and j > 0 and op[j - 1, i]) else j)
            side = lf[j, i] or rt[j, i]
            k = (0.58 if side else 0.64) if (up[j, i] and not dn[j, i]) else ((0.36 if side else 0.32) if (dn[j, i] and not up[j, i]) else 0.48)
            if sigm[j, i]: k = max(k, 0.8); jj = j   # thin signature parts (gills) keep their colour
            res[j, i, :3] = rgba(pal.shade(pal.r2h(out[jj, i, :3] / 255), k=k))[:3]
        return np.clip(np.round(res), 0, 255).astype(np.uint8), W, H, s.tags
def add_eye(sheet, W, H, facings, back=4, down=2, ring='#c8a050', size=2):
    """BW eye on a kept drawing: find the snout (outermost opaque column of the frame on the facing side), step `back` px toward the
    tail, take the head's top edge there and place highlight-over-pupil, iris behind, dark socket below."""
    out = sheet.copy()
    for r, fac in enumerate(facings):
        for c in range(4):
            fr = out[r * H:(r + 1) * H, c * W:(c + 1) * W]; op = fr[..., 3] == 255
            cols = np.where(op.any(0))[0]
            if not len(cols): continue
            xs = cols.max() - back if fac > 0 else cols.min() + back
            ys = np.where(op[:, xs])[0]
            if not len(ys): continue
            y0 = ys.min() + down; x0 = xs; bk = -fac
            def put(y, x, col):
                if 0 <= y < H and 0 <= x < W and fr[y, x, 3] == 255: fr[y, x, :3] = rgba(col)[:3]
            if size == 1: put(y0, x0, ring); continue
            sock = pal.shade(pal.r2h(fr[min(H - 1, y0 + 1), x0, :3] / 255), k=0.45)
            put(y0, x0, '#0c1416'); put(y0 - 1, x0, '#fff0c4'); put(y0, x0 + bk, ring)
            if size >= 2: put(y0 - 1, x0 + bk, pal.mix(ring, '#000000', 0.15))
            put(y0 + 1, x0, sock)
    return out
def shorten_legs(sheet, W, H, rows, k=0.55, frac=0.45):
    """compress everything hanging below the body's main mass (flippers / legs) vertically by factor k."""
    out = np.zeros_like(sheet)
    for r in range(rows):
        for c in range(4):
            fr = sheet[r * H:(r + 1) * H, c * W:(c + 1) * W]; op = fr[..., 3] > 0
            def run(row):
                best = cur = 0
                for v in row:
                    cur = cur + 1 if v else 0; best = max(best, cur)
                return best
            runs = np.array([run(op[y]) for y in range(H)]); main = np.where(runs >= frac * runs.max())[0]; ys = main.max()
            nf = np.zeros_like(fr); nf[:ys + 1] = fr[:ys + 1]
            for y in range(ys + 1, H):
                ny = ys + int(np.ceil((y - ys) * k)); m = fr[y, :, 3] > nf[ny, :, 3]
                nf[ny, m] = fr[y, m]
            out[r * H:(r + 1) * H, c * W:(c + 1) * W] = nf
    return out
_sheet = Recolor.sheet
def _sheet_post(s):
    sh, W, H, tags = _sheet(s)
    if getattr(s, 'legs', None): sh = shorten_legs(sh, W, H, len(tags), k=s.legs)
    if getattr(s, 'eye', None):
        fac = [1, 1, -1, -1, -1, 1] if len(tags) == 6 else [1, -1, 1, -1]
        sh = add_eye(sh, W, H, fac, **s.eye)
    R = len(tags); px, py = getattr(s, 'pad', (0, 0))
    if px or py or getattr(s, 'ac', False):   # 1 px safety margin around kept drawings and an exact A-B-A-C cycle for swimmers
        W2, H2 = W + 2 * px, H + 2 * py; new = np.zeros((H2 * R, W2 * 4, 4), np.uint8)
        for r in range(R):
            frs = [sh[r * H:(r + 1) * H, c * W:(c + 1) * W] for c in range(4)]
            if getattr(s, 'ac', False): frs[2] = frs[0]
            for c in range(4):
                oy = 2 * py if s.crawl else py
                new[r * H2 + oy:r * H2 + oy + H, c * W2 + px:c * W2 + px + W] = frs[c]
        sh, W, H = new, W2, H2
    return sh, W, H, tags
Recolor.sheet = _sheet_post
