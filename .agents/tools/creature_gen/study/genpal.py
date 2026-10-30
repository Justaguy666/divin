"""background analysis + proposed creature colour families for a biome (sheet), and the family hex tables."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths   # generator folder: paths, pal, swim, species modules
import os, sys, math, json, numpy as np
from PIL import Image, ImageDraw
exec(open(_os.path.join(STUDY, 'bgfit.py')).read().split('def hue')[0])
M1i = np.linalg.inv(np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]]))
M2i = np.linalg.inv(np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]]))
def lch(L, C, h):
    lab = np.array([L, C * math.cos(math.radians(h)), C * math.sin(math.radians(h))]); lin = M1i @ ((M2i @ lab) ** 3)
    s = np.where(lin <= 0.0031308, lin * 12.92, 1.055 * np.clip(lin, 0, None) ** (1 / 2.4) - 0.055); return tuple(int(round(v * 255)) for v in np.clip(s, 0, 1))
def hexc(c): return '#%02x%02x%02x' % c
spec = json.load(open(sys.argv[1])); pre = spec['pre']; Ls = spec['L']; FAM = spec['families']; h0 = spec['water_hue']
out = {}
for name, hue, cs, role in FAM: out[name.split()[0]] = ' '.join(hexc(lch(L, C, hue)) for L, C in zip(Ls, cs))
B = Image.fromarray(bg(pre, BIO[pre])).convert('RGBA'); Bn = np.array(B)[:, :, :3]
W = 1100; H = 560 + 34 * len(FAM); S = Image.new('RGB', (W, H), (24, 26, 28)); d = ImageDraw.Draw(S)
d.text((16, 10), spec['title'], fill=(235, 235, 235))
strip = B.crop((300, 0, 940, 360)).resize((320, 180), Image.NEAREST); S.paste(strip.convert('RGB'), (16, 28))
for y0 in range(0, 360, 30):
    band = Bn[y0:y0 + 30].reshape(-1, 3).astype(float); L = np.median(oklab(band)[:, 0]); med = tuple(int(v) for v in np.median(band, 0))
    yy = 28 + y0 // 2; d.rectangle((344, yy, 364, yy + 14), fill=med); d.text((370, yy + 1), f'y {y0:3d}-{y0 + 30:3d}  {hexc(med)}  L {L:.2f}', fill=(220, 220, 220))
for i, t in enumerate(spec['notes']): d.text((600, 30 + 16 * i), t, fill=(255, 230, 160) if t.startswith('!') else (220, 220, 220))
cx, cy, R = 180, 360, 110
d.text((16, 222), 'HUE WHEEL around the water hue', fill=(235, 235, 235))
for deg in range(0, 360, 2):
    dh = ((deg - h0 + 180) % 360) - 180; ad = abs(dh)
    zone = (60, 170, 160) if ad <= 45 else ((200, 70, 70) if ad <= 110 else (230, 170, 80))
    a0 = math.radians(-deg); d.line((cx + (R - 22) * math.cos(a0), cy + (R - 22) * math.sin(a0), cx + R * math.cos(a0), cy + R * math.sin(a0)), fill=lch(0.7, 0.12, deg), width=3)
    d.line((cx + (R + 4) * math.cos(a0), cy + (R + 4) * math.sin(a0), cx + (R + 10) * math.cos(a0), cy + (R + 10) * math.sin(a0)), fill=zone, width=3)
a0 = math.radians(-h0); d.line((cx, cy, cx + (R - 26) * math.cos(a0), cy + (R - 26) * math.sin(a0)), fill=(255, 255, 255), width=2); d.text((cx + 6, cy - 14), 'water', fill=(255, 255, 255))
for i, t in enumerate(spec['wheel']): d.text((320, 250 + 16 * i), t, fill=(120, 220, 205) if t.startswith('teal') else ((235, 110, 110) if t.startswith('red') else ((240, 190, 110) if t.startswith('amber') else (200, 200, 200))))
y = 486; d.text((16, y - 18), 'PROPOSED FAMILIES - 6 tones dark to light (L ' + ' '.join('%.2f' % v for v in Ls) + '), over surface / mid / low water', fill=(235, 235, 235))
depth = [Bn[20:60, 600:640].reshape(-1, 3).mean(0), Bn[120:160, 600:640].reshape(-1, 3).mean(0), Bn[220:260, 600:640].reshape(-1, 3).mean(0)]
for name, hue, cs, role in FAM:
    d.text((16, y + 6), name, fill=(235, 235, 235)); x = 170
    for wc in depth:
        d.rectangle((x - 4, y - 2, x + 6 * 22 + 2, y + 24), fill=tuple(int(v) for v in wc))
        for i, (L, C) in enumerate(zip(Ls, cs)): d.rectangle((x + i * 22, y + 2, x + i * 22 + 18, y + 20), fill=lch(L, C, hue))
        x += 6 * 22 + 14
    d.text((x + 6, y), out[name.split()[0]], fill=(200, 200, 200)); d.text((x + 6, y + 13), role, fill=(150, 150, 150)); y += 34
d.text((16, y + 6), spec['footer'], fill=(235, 235, 235))
S.save(os.path.join(paths.PREVIEW, spec['out'])); print(json.dumps(out, indent=0))
