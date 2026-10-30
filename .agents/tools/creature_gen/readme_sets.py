"""readme_sets.py <pre> - refresh the generated parts of a biome README after an install:
  * '## Roster ...' table: every 'name WxH' frame size from the installed sheets
  * '## Species notes and scene tuning' table: Sheet column from the installed sheets and the last column replaced by the
    species' '# set:' comment from its generator module (the defining set: shape / fins / barbels / pattern / colour)
The prose sections (intro, water and colour families, rendering, gaits) are written by hand - see the cs / fs / ms READMEs."""
import os, re, glob, sys
import paths, biomes
PRE = os.environ.get('PRE') or sys.argv[1]
os.environ['PRE'] = PRE
bio = biomes.GEN[PRE]['folder']
cat = biomes.GEN[PRE]['cat']
A = os.path.join(paths.REPO, 'assets', 'creatures', cat, bio); R = os.path.join(A, 'README_creatures.md')
mods = biomes.GEN[PRE]['modules']
sets = {}
for m in mods:
    lines = open(os.path.join(paths.GEN, m + '.py')).read().split('\n')
    for i, l in enumerate(lines):
        d = re.match(r'def ([a-z_0-9]+)\(\):', l)
        if d and i + 1 < len(lines) and lines[i + 1].strip().startswith('# set:'):
            txt = []; j = i + 1
            while j < len(lines) and lines[j].strip().startswith('#'): txt.append(lines[j].strip()[1:].strip()); j += 1
            sets[d.group(1)] = re.sub(r'\s+', ' ', ' '.join(txt)[4:].strip())   # later definitions win (kept-drawing overrides)
size = {}
for f in glob.glob(os.path.join(A, PRE + '_*_4f.png')):
    n, k, w, h = re.match(PRE + r'_(.+)_(swim|crawl)_(\d+)x(\d+)_4f\.png', os.path.basename(f)).groups(); size[n] = (k, w, h)
src = open(R).read()
def roster(m):
    sec = m.group(0)
    return re.sub(r'([a-z][a-z ]+?) \d+x\d+', lambda q: '%s %sx%s' % (q.group(1), *size[q.group(1).strip().replace(' ', '_')][1:]), sec)
src = re.sub(r'## Roster[^\n]*\n(?:.*\n)*?(?=\n## |\Z)', roster, src)
def notes(m):
    out, miss = [], []
    for l in m.group(0).split('\n'):
        if l.startswith('| ') and not l.startswith('| Species') and not l.startswith('|---'):
            c = [x.strip() for x in l.strip('|').split('|')]; n = c[0].replace(' ', '_'); k, w, h = size[n]
            if n not in sets: miss.append(n)
            l = '| %s | %s %sx%s | %s | %s |' % (c[0], k, w, h, c[2], sets.get(n, c[3]))
        elif l.startswith('| Species'): l = '| Species | Sheet | Band / speed | Defining set (v3: shape / fins / barbels / pattern / colour) |'
        out.append(l)
    if miss: print('no # set: comment for', ', '.join(miss), '- kept the old text')
    return '\n'.join(out)
src = re.sub(r'## Species notes and scene tuning\n(?:.*\n)*?(?=\n## |\Z)', notes, src)
open(R, 'w').write(src); print('updated', os.path.relpath(R, paths.REPO), '-', len(sets), 'sets,', len(size), 'sheets')
