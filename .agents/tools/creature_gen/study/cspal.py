"""CS background analysis + proposed creature colour families, drawn as one sheet."""
import os as _os, sys as _sys
STUDY = _os.path.dirname(_os.path.abspath(__file__)); _sys.path.insert(0, _os.path.dirname(STUDY)); import paths   # generator folder: paths, pal, swim, species modules
import os, math, numpy as np
from PIL import Image, ImageDraw
exec(open(_os.path.join(STUDY, 'bgfit.py')).read().split('def hue')[0])
M1i = np.linalg.inv(np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]]))
M2i = np.linalg.inv(np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]]))
def lch(L, C, h):
    lab = np.array([L, C * math.cos(math.radians(h)), C * math.sin(math.radians(h))]); lms = (M2i @ lab) ** 3; lin = M1i @ lms
    s = np.where(lin <= 0.0031308, lin * 12.92, 1.055 * np.clip(lin, 0, None) ** (1 / 2.4) - 0.055); return tuple(int(round(v * 255)) for v in np.clip(s, 0, 1))
def hexc(c): return '#%02x%02x%02x' % c
Ls = [0.28, 0.40, 0.52, 0.63, 0.86, 0.95]          # tones: skip the water band 0.70-0.82 the fish swim in
FAM = [  # name, hue, chroma per tone (shadows lean to teal, lights lose chroma), role
    ('A1 aqua silver', 195, [0.035, 0.035, 0.03, 0.025, 0.02, 0.012], 'analogous: silver tetras, shiners, mullet, silverside'),
    ('A2 slate teal', 210, [0.045, 0.045, 0.04, 0.035, 0.025, 0.015], 'analogous: dark backs, steel-blue fish'),
    ('A3 sea green', 165, [0.05, 0.055, 0.055, 0.05, 0.035, 0.02], 'analogous: replaces yellow-olive (cichlids, sunfish, bass)'),
    ('A4 azure steel', 235, [0.045, 0.05, 0.045, 0.04, 0.03, 0.015], 'analogous edge: molly, killifish, sturgeon'),
    ('N1 pearl / charcoal', 80, [0.012, 0.012, 0.012, 0.012, 0.01, 0.008], 'neutral: catfish, gar body, any silver'),
    ('C1 sand bronze', 65, [0.04, 0.05, 0.055, 0.055, 0.04, 0.02], 'complement, muted: browns, darters, suckers, gar'),
    ('C2 amber gold', 72, [0.07, 0.10, 0.12, 0.13, 0.10, 0.05], 'complement accent: dorado, gold fins'),
    ('C3 coral tangerine', 45, [0.09, 0.12, 0.14, 0.15, 0.10, 0.05], 'complement accent: orange breasts, fins'),
    ('C4 signal red', 28, [0.10, 0.14, 0.17, 0.17, 0.11, 0.05], 'complement accent: red fins, eyes'),
]
B = Image.fromarray(bg('cs', BIO['cs'])).convert('RGBA'); Bn = np.array(B)[:, :, :3]
W = 1100; H = 900; S = Image.new('RGB', (W, H), (24, 26, 28)); d = ImageDraw.Draw(S)
# 1) water gradient strip with lightness
d.text((16, 10), 'CLEAR SPRING BACKGROUND (far+mid+near) - water lightness by depth', fill=(235, 235, 235))
strip = B.crop((300, 0, 940, 360)).resize((320, 180), Image.NEAREST); S.paste(strip.convert('RGB'), (16, 28))
for y0 in range(0, 360, 30):
    band = Bn[y0:y0 + 30].reshape(-1, 3).astype(float); L = np.median(oklab(band)[:, 0]); med = tuple(int(v) for v in np.median(band, 0))
    yy = 28 + y0 // 2; d.rectangle((344, yy, 364, yy + 14), fill=med); d.text((370, yy + 1), f'y {y0:3d}-{y0 + 30:3d}  {hexc(med)}  L {L:.2f}', fill=(220, 220, 220))
d.text((600, 30), 'One hue only: cyan-teal (OKLab hue -176), low chroma 0.055-0.09.', fill=(220, 220, 220))
d.text((600, 46), 'Very light where the fish swim: L 0.81 at the surface,', fill=(220, 220, 220))
d.text((600, 62), '0.71 at mid depth, 0.54-0.60 just above the floor.', fill=(220, 220, 220))
d.text((600, 78), 'Floor and rocks: dark grey-green (L 0.41, C 0.03).', fill=(220, 220, 220))
d.text((600, 94), 'No warm colour anywhere in the scene.', fill=(220, 220, 220))
d.text((600, 118), 'Fish must bracket the water: lit parts > water + 0.10,', fill=(255, 230, 160))
d.text((600, 134), 'body darks < water - 0.15, outline deep teal.', fill=(255, 230, 160))
# 2) hue wheel
cx, cy, R = 180, 360, 110; h0 = -176
d.text((16, 222), 'HUE WHEEL around the water hue', fill=(235, 235, 235))
for deg in range(0, 360, 2):
    dh = ((deg - h0 + 180) % 360) - 180; ad = abs(dh)
    zone = (60, 170, 160) if ad <= 45 else ((200, 70, 70) if ad <= 110 else (230, 170, 80))
    a0 = math.radians(-deg); x1, y1 = cx + R * math.cos(a0), cy + R * math.sin(a0); x2, y2 = cx + (R - 22) * math.cos(a0), cy + (R - 22) * math.sin(a0)
    d.line((x2, y2, x1, y1), fill=lch(0.7, 0.12, deg), width=3); x3, y3 = cx + (R + 10) * math.cos(a0), cy + (R + 10) * math.sin(a0); x4, y4 = cx + (R + 4) * math.cos(a0), cy + (R + 4) * math.sin(a0)
    d.line((x4, y4, x3, y3), fill=zone, width=3)
a0 = math.radians(-h0); d.line((cx, cy, cx + (R - 26) * math.cos(a0), cy + (R - 26) * math.sin(a0)), fill=(255, 255, 255), width=2); d.text((cx + 30, cy - 8), 'water', fill=(255, 255, 255))
d.text((320, 250), 'teal ring = ANALOGOUS (within 45 deg): teal, aqua, sea-green, azure.', fill=(120, 220, 205))
d.text((320, 266), '  Bodies here belong to the water (the bw way: 65% of bw fish pixels).', fill=(200, 200, 200))
d.text((320, 290), 'red ring = DISCORD (45-110 deg): yellow-olive, lime, violet.', fill=(235, 110, 110))
d.text((320, 306), '  Neither belongs nor contrasts - this is where most cs fish sit today', fill=(200, 200, 200))
d.text((320, 322), '  (31% of pixels now, 42% in the last v3 batch): they look pasted on.', fill=(200, 200, 200))
d.text((320, 346), 'amber ring = COMPLEMENT (over 110 deg): sand, bronze, amber, coral, red.', fill=(240, 190, 110))
d.text((320, 362), '  Muted for bodies, saturated only for accents (fins, spots, eyes) -', fill=(200, 200, 200))
d.text((320, 378), '  the ac way: 57% neutral silver + 31% warm accents.', fill=(200, 200, 200))
d.text((320, 402), 'Neutral (silver, pearl, slate, charcoal) fits anywhere.', fill=(220, 220, 220))
d.text((320, 418), 'Chroma: bodies at or below the water (0.02-0.06); accents 0.10-0.17.', fill=(220, 220, 220))
# 3) families as ramps over three water depths
y = 486; d.text((16, y - 18), 'PROPOSED FAMILIES - 6 tones dark to light (L 0.28 0.40 0.52 0.63 | 0.86 0.95: no tone inside the water band), shown over surface / mid / deep water', fill=(235, 235, 235))
depth = [(Bn[20:60, 600:640].reshape(-1, 3).mean(0)), (Bn[150:190, 600:640].reshape(-1, 3).mean(0)), (Bn[220:260, 600:640].reshape(-1, 3).mean(0))]
for name, hue, cs, role in FAM:
    d.text((16, y + 6), name, fill=(235, 235, 235)); x = 170
    for k, wc in enumerate(depth):
        d.rectangle((x - 4, y - 2, x + 6 * 22 + 2, y + 24), fill=tuple(int(v) for v in wc))
        for i, (L, C) in enumerate(zip(Ls, cs)): d.rectangle((x + i * 22, y + 2, x + i * 22 + 18, y + 20), fill=lch(L, C, hue))
        x += 6 * 22 + 14
    codes = ' '.join(hexc(lch(L, C, hue)) for L, C in zip(Ls, cs)); d.text((x + 6, y), codes, fill=(200, 200, 200)); d.text((x + 6, y + 13), role, fill=(150, 150, 150))
    y += 34
d.text((16, y + 6), 'outline / shadow tint: deep teal #0c2228 (as now)   highlight: cool white #eef8f2 (water light, not cream)', fill=(235, 235, 235))
S.save(os.path.join(paths.PREVIEW, 'cs_palette_proposal.png')); print(S.size)
for name, hue, cs, role in FAM: print(name, ' '.join(hexc(lch(L, C, hue)) for L, C in zip(Ls, cs)))
