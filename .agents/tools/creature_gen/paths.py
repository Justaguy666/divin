"""Where the sprite generator reads and writes. Everything is resolved from this folder, so the tools run from any clone of
the repo on any machine (no home-folder paths). Override with environment variables when needed:
  DIVIN_ROOT     repo root (default: three levels up from this file, i.e. the Godot project folder)
  DIVIN_GEN_OUT  build / pilot output folder (default: <repo>/_gen, gitignored)
  DIVIN_PREVIEW  preview images for review (default: <repo>/Claude outputs, gitignored)"""
import os
GEN = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.environ.get('DIVIN_ROOT') or os.path.join(GEN, '..', '..', '..'))
WORK = os.path.abspath(os.environ.get('DIVIN_GEN_OUT') or os.path.join(REPO, '_gen'))
PREVIEW = os.path.abspath(os.environ.get('DIVIN_PREVIEW') or os.path.join(REPO, 'Claude outputs'))
def out_dir(pre):
    """build.py / install.py hand-off folder of a biome: <WORK>/out (cs) or <WORK>/out_<pre>."""
    return os.path.join(WORK, 'out' + ('' if pre == 'cs' else '_' + pre))
def work(p):
    """a pilot folder name (relative = inside WORK, ~ and absolute paths kept)."""
    p = os.path.expanduser(p); return p if os.path.isabs(p) else os.path.join(WORK, p)
for _d in (WORK, PREVIEW):
    os.makedirs(_d, exist_ok=True)
    _g = os.path.join(_d, '.gdignore')   # keep Godot from importing build output and previews
    if not os.path.exists(_g): open(_g, 'w').close()
