"""pxview.py <dir> <names,...> <out> [bg r,g,b] - frame 0 of each sheet at 6x on the water colour.
<dir>: a pilot folder (relative = inside paths.WORK); <out>: a file name (relative = inside paths.PREVIEW)."""
import sys, glob, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); import paths
from PIL import Image
d, names, out = paths.work(sys.argv[1]), sys.argv[2].split(','), sys.argv[3]
out = out if os.path.isabs(os.path.expanduser(out)) else os.path.join(paths.PREVIEW, out)
bgc = tuple(int(v) for v in (sys.argv[4] if len(sys.argv) > 4 else '72,129,89').split(',')) + (255,)
ims = []
for n in names:
    f = glob.glob(f'{d}/*_{n}_*_4f.png')[0]
    im = Image.open(f).convert('RGBA'); w, h = im.size; fr = im.crop((0, 0, w // 4, h))
    bg = Image.new('RGBA', fr.size, bgc); bg.alpha_composite(fr); ims.append(bg.resize((fr.width * 6, fr.height * 6), Image.NEAREST))
o = Image.new('RGB', (1200, 1400), (40, 40, 40)); x = y = rh = 0
for i in ims:
    if x + i.width > 1200: x = 0; y += rh; rh = 0
    o.paste(i, (x, y)); x += i.width; rh = max(rh, i.height)
o.crop((0, 0, 1200, y + rh)).save(out); print(out)
