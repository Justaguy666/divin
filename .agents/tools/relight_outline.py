"""Soften outlines that are too dark for the colour they wrap (pf_ rule: outline = shade of the adjacent body colour,
lower edge only slightly darker; no dark line where body meets a fin).
- body boundary next to a LIGHT body colour (belly white / beige / skin): ~72% of that colour's lightness, same hue
- body boundary that only touches fin pixels (tail base, fin roots): ~90% of the body colour
- fin rim pixels much darker than the fin next to them: ~85% of the fin colour, alpha kept
Eyes are untouched. One deterministic pass per pixel, so frames stay consistent.
Usage: relight_outline.py <out_dir> <sheets...>"""
import sys, os, re, colorsys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image
from soften_boundaries import eye_mask
N4 = ((-1, 0), (1, 0), (0, -1), (0, 1))
def shade(c, k, sat=1.0):
    h, l, s = colorsys.rgb_to_hls(*(np.array(c[:3]) / 255))
    r, g, b = colorsys.hls_to_rgb(h, max(0.0, min(1.0, l * k)), min(1.0, s * sat))
    return np.array([r * 255, g * 255, b * 255])
def light(c): return colorsys.rgb_to_hls(*(np.array(c[:3]) / 255))[1]
def frame(f):
    a = f.astype(float); al = a[:, :, 3]; H, W = al.shape
    body = al == 255; fin = (al > 0) & (al < 255); empty = al == 0
    def inside(y, x): return 0 <= y < H and 0 <= x < W
    bnd = np.zeros_like(body)
    for y, x in zip(*np.nonzero(body)):
        bnd[y, x] = any(not inside(y + dy, x + dx) or not body[y + dy, x + dx] for dy, dx in N4)
    keep = eye_mask(a, body)
    out = a.copy()
    for y, x in zip(*np.nonzero(bnd & ~keep)):
        nb_in = [(y + dy, x + dx) for dy, dx in N4 if inside(y + dy, x + dx) and body[y + dy, x + dx] and not bnd[y + dy, x + dx]]
        if not nb_in:
            nb_in = [(y + 2 * dy, x + 2 * dx) for dy, dx in N4 if inside(y + 2 * dy, x + 2 * dx) and body[y + 2 * dy, x + 2 * dx]]
        if not nb_in: continue
        ref = np.mean([a[p][:3] for p in nb_in], 0)
        touches_empty = any(not inside(y + dy, x + dx) or empty[y + dy, x + dx] for dy, dx in N4)
        if not touches_empty:                                   # body meets fin: no dark seam
            out[y, x, :3] = shade(ref, 0.9)
        elif light(ref) > 0.55 and light(a[y, x]) < light(ref) * 0.7:
            out[y, x, :3] = shade(ref, 0.72, 1.05)              # light belly: soft, same-hue edge
    # dark specks sitting inside a light belly band near the lower edge (left-over double outline)
    dist = np.full(body.shape, 9)
    for y, x in zip(*np.nonzero(body)):
        for d in (1, 2, 3, 4):
            if not inside(y + d, x) or not body[y + d, x]:
                dist[y, x] = d; break
    for y, x in zip(*np.nonzero(body & ~bnd & ~keep & (dist <= 4))):
        nb = [out[y + dy, x + dx] for dy, dx in N4 if inside(y + dy, x + dx) and body[y + dy, x + dx]]
        lights = [c for c in nb if light(c) > 0.55]
        if len(lights) >= 2 and light(a[y, x]) < 0.6 * np.mean([light(c) for c in lights]):
            out[y, x, :3] = shade(np.mean(lights, 0), 0.86)
    for y, x in zip(*np.nonzero(fin)):
        if not any(not inside(y + dy, x + dx) or empty[y + dy, x + dx] for dy, dx in N4): continue
        nb = [a[y + dy, x + dx] for dy, dx in N4 if inside(y + dy, x + dx) and fin[y + dy, x + dx]]
        if not nb: continue
        ref = np.mean(nb, 0)
        if light(a[y, x]) < light(ref) * 0.65:
            out[y, x, :3] = shade(ref, 0.85)
    return np.clip(out, 0, 255).astype(np.uint8)
if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for p in sys.argv[2:]:
        m = re.search(r'_(\d+)x(\d+)_4f', p); fw, fh = int(m[1]), int(m[2])
        a = np.array(Image.open(p).convert('RGBA'))
        for y0 in range(0, a.shape[0], fh):
            for x0 in range(0, a.shape[1], fw):
                a[y0:y0 + fh, x0:x0 + fw] = frame(a[y0:y0 + fh, x0:x0 + fw])
        Image.fromarray(a, 'RGBA').save(os.path.join(out, os.path.basename(p)))
    print('ok')
