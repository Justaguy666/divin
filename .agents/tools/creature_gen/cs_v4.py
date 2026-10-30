"""Clear spring v4 (October 2026): kept as a shortcut for `python3 v4/build_v4.py cs [names...]` (settings: v4/params/cs.json)."""
import os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.exit(subprocess.call([sys.executable, os.path.join(here, 'v4', 'build_v4.py'), 'cs'] + sys.argv[1:]))
