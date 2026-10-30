"""build sheets + aseprite + previews for Clear Spring species."""
import os, sys, numpy as np, importlib
from PIL import Image
import swim, ase, gait, paths, biomes
if os.environ.get('STYLE') == 'v2': swim.use_v2()
if os.environ.get('STYLE') == 'v3': swim.use_v3(os.environ.get('PRE', 'cs'))   # study proposal (fins / motion / colour), applied biome by biome
PRE = os.environ.get('PRE', 'cs')
OUT = paths.out_dir(PRE)
BG = biomes.GEN[PRE]['preview']
def export(name, sheet, W, H, tags, kind):
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.startswith(name + '_') and f.endswith('_4f.png'): os.remove(os.path.join(OUT, f))
    p = f'{OUT}/{name}_{kind}_{W}x{H}_4f.png'; Image.fromarray(sheet, 'RGBA').save(p)
    ase.write(f'{OUT}/{name}.aseprite', sheet, W, H, tags)
    return p
def preview(items, path, scale=3, bg=BG, frames=False):
    """items: list of (sheet, W, H). frames=True shows every row's first frame."""
    cells = []
    for sh, W, H in items:
        if frames:
            rows = sh.shape[0] // H; cells.append([sh[r * H:(r + 1) * H, :W] for r in range(rows)] + [sh[:H, W:2 * W], sh[:H, 3 * W:4 * W]])
        else: cells.append([sh[:H, :W]])
    cw = max(c.shape[1] for r in cells for c in r) + 4; ch = max(c.shape[0] for r in cells for c in r) + 4
    cols = max(len(r) for r in cells) if frames else 6
    if frames: Mw, Mh = cols * cw, len(cells) * ch
    else: Mw, Mh = cols * cw, ((len(cells) + cols - 1) // cols) * ch
    M = Image.new('RGBA', (Mw, Mh), bg + (255,))
    for k, r in enumerate(cells):
        for j, c in enumerate(r):
            x, y = ((j * cw, k * ch) if frames else ((k % cols) * cw, (k // cols) * ch))
            M.alpha_composite(Image.fromarray(c, 'RGBA'), (x + 2, y + 2))
    M.resize((M.width * scale, M.height * scale), Image.NEAREST).save(path)
def run(mod, names=None, prev=None):
    m = importlib.import_module(mod); names = names or m.ALL; items = []
    for n in names:
        F = getattr(m, n)()
        if os.environ.get('STYLE') in ('v2', 'v3'):
            g = gait.lookup(PRE, n)
            if g: F.gait = g
        if hasattr(F, 'sheet'): sh, W, H, tags = F.sheet()
        else: sh, W, H, tags = swim.sheet(F)
        kind = 'crawl' if getattr(F, 'crawl', False) else 'swim'
        export(PRE + '_' + n, sh, W, H, tags, kind); items.append((sh, W, H)); print(n, W, H, len({tuple(p) for p in sh.reshape(-1, 4) if p[3]}))
    if prev: preview(items, prev); preview(items, prev.replace('.png', '_rows.png'), frames=True)
    return items
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[3:] or None, sys.argv[2])
