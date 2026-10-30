"""install built cs sheets into the Godot project and write their scenes from scratch (BW workflow step 4-5)."""
import glob, os, re, shutil, sys, importlib, time, gait, paths, biomes
_cp = shutil.copyfile
def _retry(a, b):
    for k in range(10):
        try: return _cp(a, b)
        except OSError:
            if k == 9: raise
            time.sleep(1.5)
shutil.copyfile = _retry
PRE = os.environ.get('PRE', 'cs'); BIO = biomes.GEN[PRE]['folder']
CAT = biomes.GEN[PRE]['cat']
P = paths.REPO + '/'; A = P + f'assets/creatures/{CAT}/{BIO}/'; S = P + f'scenes/creatures/{CAT}/{BIO}/'
OUT = paths.out_dir(PRE) + '/'
camel = lambda n: ''.join(w.capitalize() for w in n.split('_'))
def install(mod, names=None):
    m = importlib.import_module(mod); names = names or m.ALL
    for n in names:
        f = glob.glob(OUT + f'{PRE}_{n}_*_4f.png'); assert len(f) == 1, (n, f); f = f[0]; b = os.path.basename(f)
        kind, W, H = re.search(r'_(swim|crawl)_(\d+)x(\d+)_4f', b).groups()
        for o in glob.glob(A + f'{PRE}_{n}_swim_*_4f.png*') + glob.glob(A + f'{PRE}_{n}_crawl_*_4f.png*'):
            if os.path.basename(o) not in (b, b + '.import'): os.remove(o)
        shutil.copyfile(f, A + b); shutil.copyfile(OUT + f'{PRE}_{n}.aseprite', A + f'{PRE}_{n}.aseprite')
        c = dict(m.SCENE[n]); g = gait.lookup(PRE, n) if os.environ.get('STYLE') in ('v2', 'v3') else None
        if g and kind == 'swim': c['fps'] = g['fps']   # gait sets the beat
        base = 'swimmer_base' if kind == 'swim' else 'crawler_base'
        uid = 'uid://ua86u84h3ug2' if kind == 'swim' else 'uid://dlpfppvngbl4j'
        L = ['[gd_scene format=3]', '', f'[ext_resource type="PackedScene" uid="{uid}" path="res://scenes/creatures/_shared/{base}.tscn" id="1_base"]',
             f'[ext_resource type="Texture2D" path="res://assets/creatures/{CAT}/{BIO}/{b}" id="2_sheet"]', '',
             f'[node name="{PRE.capitalize()}{camel(n)}" instance=ExtResource("1_base")]']
        if kind == 'swim':
            if 'rest' in c: L.append('rest_time = Vector2(%s, %s)' % c['rest'])
            if 'crowd' in c: L.append('crowd_radius = %.1f' % c['crowd'])
        else:
            for k in ('move_prefix', 'bob_speed', 'bob_amount', 'move_time', 'idle_time', 'floor_height', 'crowd_radius'):
                if k in c:
                    v = c[k]; L.append(f'{k} = ' + (f'"{v}"' if isinstance(v, str) else ('Vector2(%s, %s)' % v if isinstance(v, tuple) else str(float(v)))))
        L += ['sheet = ExtResource("2_sheet")', f'frame_size = Vector2i({W}, {H})', 'animation_fps = %.1f' % c['fps'], 'speed = %.1f' % c['speed']]
        if kind == 'swim': y0, y1 = c['band']; L.append(f'area = Rect2(0, {y0}, 640, {y1 - y0})')
        for k in range(10):
            try: open(S + f'{PRE}_{n}.tscn', 'w').write('\n'.join(L) + '\n'); break
            except OSError: time.sleep(1.5)
        print('installed', n, W, H)
if __name__ == '__main__': install(sys.argv[1], sys.argv[2:] or None)
