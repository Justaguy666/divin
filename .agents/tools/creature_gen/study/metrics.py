"""Per-biome metrics of creature sheets: motion between frames, colour, fin (semi-transparent) texture."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths, biomes   # generator folder: paths, pal, swim, species modules
import glob, os, re, json, sys, numpy as np
from PIL import Image
R = _os.path.join(paths.REPO, 'assets/creatures/')
BIOMES = {p: biomes.rel(p) for p in biomes.ALL}
def srgb2lin(c): c = c / 255.0; return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
def oklab(rgb):
    l = srgb2lin(rgb); M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]])
    lms = np.cbrt(l @ M1.T); M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]])
    return lms @ M2.T
def frames(a, W, H, row):
    return [a[row * H:(row + 1) * H, c * W:(c + 1) * W].astype(float) for c in range(4)]
def analyse(f):
    kind, W, H = re.search(r'_(swim|crawl)_(\d+)x(\d+)_4f', f).groups(); W, H = int(W), int(H)
    a = np.array(Image.open(f).convert('RGBA')); A, B_, A2, C = frames(a, W, H, 0)
    al = A[..., 3] > 0; n = al.sum()
    if n < 10: return None
    d = {}
    # motion: share of opaque pixels that change between A and B, and where (rear third / front / fins)
    chg = (np.abs(A - B_).sum(-1) > 0) & ((A[..., 3] > 0) | (B_[..., 3] > 0)); d['motion'] = chg.sum() / n
    xs = np.where(al.any(0))[0]; x0, x1 = xs.min(), xs.max(); L = x1 - x0 + 1
    rear = np.zeros_like(al); rear[:, x0:x0 + int(L * 0.33)] = True   # E row faces right: tail on the left
    d['motion_rear_share'] = (chg & rear).sum() / max(1, chg.sum())
    semi = (A[..., 3] > 0) & (A[..., 3] < 250)
    d['motion_in_semi'] = (chg & (semi | ((B_[..., 3] > 0) & (B_[..., 3] < 250)))).sum() / max(1, chg.sum())
    opq = A[..., 3] >= 250
    d['body_changed'] = (chg & opq & (B_[..., 3] >= 250)).sum() / max(1, opq.sum())    # opaque pixels whose colour changes (body flex / markings moving)
    # silhouette displacement between A, B, C (tail-tip swing)
    def ext(F):
        m = F[..., 3] > 0; ys, xs = np.where(m); return xs.min(), xs.max(), ys.min(), ys.max()
    eA, eB, eC = ext(A), ext(B_), ext(C); d['bbox_swing'] = float(max(abs(eB[i] - eA[i]) + abs(eC[i] - eA[i]) for i in range(4)))
    # colour
    px = A[al]; rgb = px[:, :3]; lab = oklab(rgb)
    d['colors'] = len({tuple(p) for p in px.astype(int)}); d['L_range'] = float(np.percentile(lab[:, 0], 97) - np.percentile(lab[:, 0], 3))
    C_ = np.hypot(lab[:, 1], lab[:, 2]); d['chroma_mean'] = float(C_.mean()); d['chroma_p90'] = float(np.percentile(C_, 90))
    # hue shift dark->light on the most common hue family (opaque pixels): mean hue of darkest vs lightest quartile
    o = A[opq][:, :3]
    if len(o) > 20:
        lo = oklab(o); q1, q3 = np.percentile(lo[:, 0], 25), np.percentile(lo[:, 0], 75)
        dk, lt = lo[lo[:, 0] <= q1], lo[lo[:, 0] >= q3]
        hd = np.degrees(np.arctan2(dk[:, 2].mean(), dk[:, 1].mean())); hl = np.degrees(np.arctan2(lt[:, 2].mean(), lt[:, 1].mean()))
        d['hue_shift'] = float(((hl - hd + 180) % 360) - 180); d['dark_chroma'] = float(np.hypot(dk[:, 1].mean(), dk[:, 2].mean())); d['light_chroma'] = float(np.hypot(lt[:, 1].mean(), lt[:, 2].mean()))
        d['dark_L'] = float(dk[:, 0].mean()); d['light_L'] = float(lt[:, 0].mean())
    # fins = semi-transparent pixels
    s = A[semi]; d['fin_share'] = semi.sum() / n
    if len(s) > 5:
        d['fin_alpha_mean'] = float(s[:, 3].mean()); d['fin_alpha_levels'] = len(set(s[:, 3].astype(int))); d['fin_colors'] = len({tuple(p) for p in s.astype(int)})
        fl = oklab(s[:, :3]); d['fin_L_std'] = float(fl[:, 0].std()); d['fin_chroma'] = float(np.hypot(fl[:, 1], fl[:, 2]).mean())
        d['fin_L_minus_body'] = float(fl[:, 0].mean() - (oklab(o)[:, 0].mean() if len(o) else 0))
    else:
        for k in ('fin_alpha_mean', 'fin_alpha_levels', 'fin_colors', 'fin_L_std', 'fin_chroma', 'fin_L_minus_body'): d[k] = np.nan
    # edge (outline) darkness: opaque pixels touching transparency vs the pixel inside
    pad = np.pad(al, 1); edge = al & (~pad[:-2, 1:-1] | ~pad[2:, 1:-1] | ~pad[1:-1, :-2] | ~pad[1:-1, 2:])
    el = oklab(A[edge & opq][:, :3])[:, 0] if (edge & opq).any() else np.array([np.nan]); il = oklab(A[opq & ~edge][:, :3])[:, 0] if (opq & ~edge).any() else np.array([np.nan])
    d['edge_L'] = float(np.nanmean(el)); d['inner_L'] = float(np.nanmean(il))
    d['kind'] = kind; d['W'] = W; d['H'] = H
    return d
out = {}
for b, p in BIOMES.items():
    rows = []
    for f in sorted(glob.glob(R + p + '/*_4f.png')):
        r = analyse(f)
        if r: r['name'] = os.path.basename(f); rows.append(r)
    out[b] = rows
json.dump(out, open(_os.path.join(paths.WORK, 'metrics.json'), 'w'))
keys = ['motion', 'motion_rear_share', 'motion_in_semi', 'body_changed', 'bbox_swing', 'colors', 'L_range', 'chroma_mean', 'chroma_p90', 'hue_shift', 'dark_chroma', 'light_chroma', 'dark_L', 'light_L',
        'fin_share', 'fin_alpha_mean', 'fin_alpha_levels', 'fin_colors', 'fin_L_std', 'fin_chroma', 'fin_L_minus_body', 'edge_L', 'inner_L']
print('swimmers (median)'.ljust(18) + ''.join(b.rjust(7) for b in BIOMES))
for k in keys:
    vals = []
    for b in BIOMES:
        v = [r[k] for r in out[b] if r['kind'] == 'swim' and k in r and r[k] == r[k]]
        vals.append(np.median(v) if v else np.nan)
    print(k.ljust(18) + ''.join(('%7.2f' % v) for v in vals))
