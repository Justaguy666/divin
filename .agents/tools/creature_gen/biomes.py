"""The one list of creature biomes known to the generator, its study scripts and the v4 tools.
Adding a biome (.agents/rules/creature_workflow.md, path A) = one entry in GEN here; its colour data goes in pal.py (BIOMES, and
the v3 BIOMES_V3 / FIT_V3 / FAM_<PRE>) and its gait table in gait.py.
  cat, folder   assets/creatures/<cat>/<folder> and scenes/creatures/<cat>/<folder> (also the environment folder)
  modules       species modules in build order (review codes CS01.. follow it)
  water         OKLab hue (deg) and mean lightness of the water where the fish swim (study/bgfit.py); pal.BG_L is the lightness
  preview       RGB behind build.py preview images
  review        RGB behind v4 review pages (default: preview)
REFS are the hand-drawn reference biomes: measured by the study / v4 tools, never built or restyled."""
REFS = {
    'ac': dict(cat='freshwater', folder='ancient_cold_lake', water=(-121, 0.49), review=(52, 72, 92)),
    'bw': dict(cat='freshwater', folder='blackwater', water=(59, 0.46), review=(70, 52, 30)),
    'pf': dict(cat='freshwater', folder='planted_freshwater', water=(168, 0.60), review=(40, 92, 80)),
}
GEN = {
    'cs': dict(cat='freshwater', folder='clear_spring', modules=['sp1', 'sp2', 'sp3', 'sp4'], water=(-174, 0.73),
               preview=(79, 157, 150), review=(70, 150, 145)),
    'fs': dict(cat='freshwater', folder='forest_stream', modules=['fs1', 'fs2', 'fs3'], water=(152, 0.68), preview=(72, 129, 89)),
    'ms': dict(cat='freshwater', folder='marsh_swamp', modules=['ms1', 'ms2', 'ms3'], water=(132, 0.42), preview=(63, 81, 49)),
    'bb': dict(cat='freshwater', folder='billabong', modules=['bb1', 'bb2', 'bb3'], water=(173, 0.39), preview=(46, 76, 67)),
    'by': dict(cat='freshwater', folder='bayou', modules=['by1', 'by2', 'by3'], water=(121, 0.36), preview=(48, 60, 34)),
    'cw': dict(cat='marine', folder='cold_water', modules=['cw1', 'cw2', 'cw3', 'cw4'], water=(-123, 0.36), preview=(20, 62, 88)),
    'uc': dict(cat='special', folder='underwater_cave', modules=['uc1', 'uc2', 'uc3'], water=(-109, 0.21), preview=(20, 26, 32)),
}
ALL = {**REFS, **GEN}   # report order: references first, then the generator biomes
def rel(pre): return ALL[pre]['cat'] + '/' + ALL[pre]['folder']        # e.g. 'freshwater/clear_spring'
def review_bg(pre): return ALL[pre].get('review', ALL[pre].get('preview'))
