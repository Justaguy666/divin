"""Shared paths and biome constants for the v4 tools. Everything is resolved from the generator folder (paths.py), so the tools
run from any clone; override with DIVIN_ROOT / DIVIN_GEN_OUT like the rest of the generator."""
import os, sys, math, re, glob
V4 = os.path.dirname(os.path.abspath(__file__)); GEN = os.path.dirname(V4); LIB = os.path.join(V4, 'lib')
for _p in (LIB, V4, GEN):
    if _p not in sys.path: sys.path.insert(0, _p)
import paths, biomes   # noqa: E402  (generator paths: REPO, WORK; biome registry)
REPO = paths.REPO
CREATURES = os.path.join(REPO, 'assets', 'creatures')
CACHE = os.path.join(paths.WORK, 'v4_cache'); os.makedirs(CACHE, exist_ok=True)
# all from the generator's biome registry (biomes.py) - add a biome there
BIOME = {p: biomes.rel(p) for p in biomes.ALL}
REFS = tuple(biomes.REFS)   # accepted reference dialects - never restyled
WATER = {p: b['water'] for p, b in biomes.ALL.items()}   # OKLab hue (deg), mean lightness where the fish swim
MODULES = {p: b['modules'] for p, b in biomes.GEN.items()}
PREVIEW_BG = {p: biomes.review_bg(p) for p in biomes.ALL}
def bright(pre): return WATER[pre][1] >= 0.6   # bright water: bodies below the water; dark water: bodies a little above it
def asset_dir(pre): return os.path.join(CREATURES, BIOME[pre])
def installed(pre, name, kind='swim'):
    g = glob.glob(os.path.join(asset_dir(pre), f'{pre}_{name}_{kind}_*_4f.png')); return g[0] if g else None
def ref_sheets(kind='swim'):
    return {p: sorted(glob.glob(os.path.join(asset_dir(p), f'{p}_*_{kind}_*_4f.png'))) for p in REFS}
def species(pre, kind='swim'):
    """[(module, name)] of a biome's generator species that are installed as <kind> sheets, in module order (review codes follow it)."""
    import importlib
    out = []
    for mod in MODULES[pre]:
        try: m = importlib.import_module(mod)
        except Exception: continue
        for n in getattr(m, 'ALL', []):
            if installed(pre, n, kind): out.append((mod, n))
    return out
def code(pre, i): return '%s%02d' % (pre.upper(), i + 1)
def eye_colours(pre):
    """pupil and catchlight tinted by the water, as in the refs (ac blue-black, bw brown-black, pf violet-black)."""
    import numpy as np, pal
    h = math.radians(WATER[pre][0]); f = lambda L, C: pal.hexl(np.array([L, C * math.cos(h), C * math.sin(h)]))
    return f(0.15, 0.012), f(0.94, 0.012)
def frame_size(f): return tuple(map(int, re.search(r'_(\d+)x(\d+)_4f', f).groups()))
