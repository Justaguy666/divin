"""v4 auto-tuner for one biome's swimmers, in two stages.

  python3 tune.py <pre> body [names...]   -> <WORK>/v4_<pre>/body/<pre>_<name>_final_*.png + <pre>_<name>_tune.json
  python3 tune.py <pre> fins [names...]   -> <WORK>/v4_<pre>/fins/...   (starts from the body stage; body knobs frozen)

Each stage renders a species (render.py), measures it against the AC / BW / PF reference bands (lib/rulecheck4.py for the body,
lib/fincheck3.py for fins) and runs a coordinate search on a continuous violation score: every failing check adds 1 + its distance
outside the band in units of SCALE; a small penalty keeps knobs near their start. Body: tone cap 4 or 5 is tried first, then 3
sweeps over STEP. Fins: 3 sweeps over FSTEP with body checks kept as a light guard.

Per-species overrides (for review feedback, e.g. "less glossy"): OV_<name>="tmx=3;dith=1.3;kt=0.7" fixes / seeds knobs before the
search (tmx given -> only that cap is tried). R4_TOPT_MAX=0.33 tightens 'light in the upper third' for one run.
Runs 2 species in parallel (-j N to change); about 3-7 min per species per stage on one core."""
import os, sys, json, glob, subprocess, re
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v4env
import numpy as np
HERE = v4env.V4; RENDER = os.path.join(HERE, 'render.py')
def work(pre, stage): d = os.path.join(v4env.paths.WORK, f'v4_{pre}', stage); os.makedirs(d, exist_ok=True); return d
# ---- body stage knobs (shading / colour / outline); see swim.py PILOT_* switches and render.py
START = dict(t0=0.0, spk=1.0, lc=0.34, kt=0.45, kb=1.0, tk=0.35, c0=0.75, c1=0.9, c4=1.3, c5=1.8, olc=1.0, findl=0.18, vivl=0.08, vivc=1.0, rl=10.0, rd=8.0,
             dkc=1.0, fk=0.85, mot=0.0, raydl=0.10, flr=0.42, bw=0.0, bc=0.36, dith=1.0, ts=0.11)
BOUNDS = dict(t0=(-0.9, 0.6), spk=(0.7, 1.6), lc=(0.26, 0.55), kt=(0.15, 1.3), kb=(0.5, 1.9), tk=(0.05, 0.6), c0=(0.3, 1.2), c1=(0.4, 1.2), c4=(0.6, 2.0), c5=(0.6, 2.4),
              olc=(0.5, 1.4), findl=(0.0, 0.35), vivl=(-0.05, 0.14), vivc=(0.7, 1.3), rl=(0, 20), rd=(0, 16), dkc=(0.35, 1.0), fk=(0.4, 1.3), mot=(0.0, 0.6),
              raydl=(0.02, 0.22), flr=(0.28, 0.65), bw=(0.0, 0.18), bc=(0.22, 0.55), dith=(0.0, 2.0), ts=(0.05, 0.13))
STEP = dict(ts=0.015, t0=0.12, spk=0.1, dith=0.25, lc=0.04, kt=0.15, kb=0.15, tk=0.08, c0=0.1, c1=0.08, c4=0.1, c5=0.2, olc=0.1, rl=3, rd=3, dkc=0.1, fk=0.1,
            raydl=0.03, findl=0.03, vivl=0.03, vivc=0.1, flr=0.05)
# ---- fin stage knobs (FIN2 membrane / motion)
FSTART = dict(findl=-0.01, fcd=0.06, fgr=0.12, fms=0.35, fml=0.06, raydl=0.04, rmx=0.6, ampv=1.3, ampd=1.1, fbw=0.5, famid=168.0)
FB = dict(findl=(-0.12, 0.15), fcd=(-0.05, 0.15), fgr=(0, 0.25), fms=(0, 0.6), fml=(0.02, 0.12), raydl=(0, 0.1), rmx=(0.2, 1), ampv=(0.8, 1.8), ampd=(0.7, 1.4),
          fbw=(0, 0.8), famid=(150, 200))
FSTEP = dict(fgr=0.03, fml=0.02, fms=0.1, findl=0.03, fcd=0.03, raydl=0.02, rmx=0.15, ampv=0.3, ampd=0.15, fbw=0.15, famid=6)
BODY_GUARD = ('hue_lt', 'hue_dk', 'marks', 'p_top3', 'x_comp_largest', 't_L95', 't_Lrange', 'plat_share', 'plat_h', 'hl_step_ring', 'hl_major_step', 'hl_top_t', 'hl_back',
              'eyedom', 'e_pupil_L', 'len_amp', 's_tail_minus_mid', 's_light_t', 's_vslope', 'cshade', 'darkthick', 'outl', 'bottom', 'above', 'ident_dL', 'ident_C',
              'body_bg_cs', 'o_top_Cratio', 'clt', 'cdk', 'discord')
def base_env(pre, out):
    pupil, catch = v4env.eye_colours(pre)
    e = dict(os.environ); e.update(PILOT_PUPIL=pupil, PILOT_CATCH=catch, PILOT_FIN='1', PILOT_HUE='1', PILOT_CPROF='1', PILOT_SHOULDER='0', PILOT_SHMODE='ramp',
                                  PILOT_RAMP0='0.15', PILOT_TEX='0', PILOT_FLOOR='0.21', PILOT_STEER='1', PILOT_HEAD='0', PILOT_FINJ='1', PILOT_FINSTEP='4', PILOT_MOTP='2',
                                  DIVIN_ROOT=v4env.REPO, DIVIN_GEN_OUT=v4env.paths.WORK, PILOT_OUT=out)
    return e
def env_for(pre, name, p, out, fins=False):
    """the full environment for one render; build.py stores exactly these PILOT_* values per species in params/<pre>.json"""
    e = base_env(pre, out); n = name
    e.update({f'PILOT_TONE0_{n}': f"{p['t0']:.3f}", f'PILOT_TSPANK_{n}': f"{p['spk']:.3f}", f'PILOT_LIGHTC_{n}': f"{p['lc']:.3f},{p['kt']:.3f},{p['kb']:.3f},1.6",
              f'PILOT_TAILK_{n}': f"{p['tk']:.3f}", f'PILOT_CS_{n}': f"{p['c0']:.3f},{p['c1']:.3f},1,1,{p['c4']:.3f},{p['c5']:.3f}", f'PILOT_OLC_{n}': f"{p['olc']:.3f}",
              f'PILOT_FINDL_{n}': f"{p['findl']:.3f}", f'PILOT_VIVL_{n}': f"{p['vivl']:.3f}", f'PILOT_VIVC_{n}': f"{p['vivc']:.3f}", f'PILOT_DKC_{n}': f"{p['dkc']:.3f}",
              f'PILOT_FINK_{n}': f"{p['fk']:.3f}", f'PILOT_MOT_{n}': f"{p['mot']:.3f}", f'PILOT_RAYDL_{n}': f"{p['raydl']:.3f}", f'PILOT_FLOORREL_{n}': f"{p['flr']:.3f}",
              f'PILOT_BANDW_{n}': f"{p['bw']:.3f}", f'PILOT_DITH_{n}': f"{p['dith']:.3f}", f'PILOT_TOPSTEP_{n}': f"{p['ts']:.3f}", f'PILOT_BANDC_{n}': f"{p['bc']:.3f}",
              f'PILOT_TMAX_{n}': str(int(p.get('tmx', 4))), f'PILOT_ROT_{n}': f"{-p['rd']:.2f},{-p['rd'] / 2:.2f},0,3,{p['rl'] * 0.8:.2f},{p['rl']:.2f}"})
    if fins:
        e['PILOT_FIN2'] = '1'
        e.update({f'PILOT_FINDL_{n}': f"{p['findl']:.3f}", f'PILOT_FINDL_CAUD_{n}': f"{p['fcd']:.3f}", f'PILOT_FINGRAD_{n}': f"{p['fgr']:.3f}", f'PILOT_FINGS_{n}': '4',
                  f'PILOT_FINMOT_{n}': f"{p['fms']:.3f}", f'PILOT_FINMOTL_{n}': f"{p['fml']:.3f}", f'PILOT_RAYDL_{n}': f"{p['raydl']:.3f}", f'PILOT_RAYMIX_{n}': f"{p['rmx']:.3f}",
                  f'PILOT_RAYA_{n}': '0', f'PILOT_FINSTEP_{n}': '4', f'PILOT_AMPV_{n}': f"{p['ampv']:.3f}", f'PILOT_AMPD_{n}': f"{p['ampd']:.3f}",
                  f'PILOT_FINBASEW_{n}': f"{p['fbw']:.3f}", f'PILOT_FAMID_{n}': f"{p['famid']:.1f}", f'PILOT_RIMDA_{n}': '-10'})
    return e
def render(pre, mod, name, p, tag, out, fins=False):
    subprocess.run([sys.executable, RENDER, pre, mod, name, tag], cwd=v4env.GEN, env=env_for(pre, name, p, out, fins), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return glob.glob(f'{out}/{pre}_{name}_{tag}_swim_*_4f.png')[0]
def score(res, p, start, steps, guard=1.0):
    import rulecheck4 as R4, fincheck3 as FC
    s = 0.0; fails = []
    for k, (v, b, ok) in res.items():
        if ok is not False: continue
        fails.append(k)
        if k in ('jag', 'AC'): continue   # silhouette / frame rule: not something these knobs change
        if k.startswith('fin_'):
            kk = k[4:]; sc = FC.SCALE.get(kk.split('_', 1)[1] if '_' in kk else kk, 1); w = 1.0
        else: sc = R4.SCALE.get(k, 1); w = guard if k in BODY_GUARD else 1.0
        d = (b[0] - v) if v < b[0] else (v - b[1]); s += w * (1 + d / sc)
    return s + 0.002 * sum(abs(p[k] - start[k]) / steps[k] for k in steps), fails
def measure(pre, f, base, small, fins):
    import rulecheck4 as R4
    res = R4.check(R4.measure(f, base, pre), small)
    if fins:
        import fincheck3 as FC; res.update(FC.check(FC.measure(f, base)))
    return res
def search(job):
    pre, stage, mod, name, small = job; fins = stage == 'fins'; out = work(pre, stage); base = v4env.installed(pre, name)
    ov = dict(x.split('=') for x in os.environ.get('OV_' + name, '').split(';') if x)
    p = dict(START)
    if fins:
        j = json.load(open(os.path.join(work(pre, 'body'), f'{pre}_{name}_tune.json'))); p.update(j['params'])
        prev = os.path.join(out, f'{pre}_{name}_tune.json')
        p.update(FSTART)
        if os.path.exists(prev): p.update({k: v for k, v in json.load(open(prev))['params'].items() if k in FSTART})   # re-run: continue from the last fin result
        p['ampv'] = min(p['ampv'], 1.3); p['ampd'] = min(p['ampd'], 1.1)
        start, steps, bounds, guard = dict(p), FSTEP, FB, 0.3
    else:
        start, steps, bounds, guard = dict(START), STEP, BOUNDS, 1.0
    p.update({k: float(v) for k, v in ov.items() if k != 'tmx'})
    clamp = lambda q: {k: (float(min(bounds[k][1], max(bounds[k][0], v))) if k in bounds else v) for k, v in q.items()}
    p = clamp(p); n = 0; best = None
    caps = [int(ov['tmx'])] if 'tmx' in ov else ([int(p.get('tmx', 4))] if fins else [4, 5])
    for tmx in caps:
        q = dict(p, tmx=tmx); f = render(pre, mod, name, q, f's{n}', out, fins); s, fails = score(measure(pre, f, base, small, fins), q, start, steps, guard); n += 1
        if best is None or s < best[0]:
            if best and os.path.exists(best[3]): os.remove(best[3])
            best = (s, q, fails, f)
        else: os.remove(f)
    for sweep in range(3):
        if not [k for k in best[2] if k not in ('jag', 'AC')]: break
        improved = False
        for k in steps:
            for sgn in (1, -1):
                q = dict(best[1]); q[k] += sgn * steps[k] * [1.0, 0.5, 1.5][sweep]; q = clamp(q)
                if q == best[1]: continue
                f = render(pre, mod, name, q, f's{n}', out, fins); s, fails = score(measure(pre, f, base, small, fins), q, start, steps, guard); n += 1
                if s < best[0] - 1e-6:
                    if os.path.exists(best[3]): os.remove(best[3])
                    best = (s, q, fails, f); improved = True; break
                else: os.remove(f)
        if not improved: break
    s, bp, fails, f = best; final = os.path.join(out, f'{pre}_{name}_final_swim_' + f.split('_swim_')[1]); os.replace(f, final)
    for g in glob.glob(os.path.join(out, f'{pre}_{name}_s*_swim_*_4f.png')): os.remove(g)
    json.dump(dict(pre=pre, stage=stage, name=name, mod=mod, small=small, params=bp, fails=fails, evals=n, score=s, overrides=ov), open(os.path.join(out, f'{pre}_{name}_tune.json'), 'w'), indent=1)
    return name, fails, n
def small_of(pre, name):
    from PIL import Image
    from m import body
    f = v4env.installed(pre, name); W, H = v4env.frame_size(f); fr = np.array(Image.open(f).convert('RGBA'))[:H, :W]
    xs = np.nonzero(body(fr))[1]; return bool(xs.max() - xs.min() + 1 <= 24)
if __name__ == '__main__':
    args = sys.argv[1:]; nj = 2
    if '-j' in args: i = args.index('-j'); nj = int(args[i + 1]); del args[i:i + 2]
    pre, stage, names = args[0], args[1], args[2:]
    sp = [(m, n) for m, n in v4env.species(pre) if not names or n in names]
    J = [(pre, stage, m, n, small_of(pre, n)) for m, n in sp]
    print('jobs', len(J), flush=True)
    with Pool(nj) as pool:
        for name, fails, n in pool.imap_unordered(search, J): print(f'{name}: {n} evals, fails {fails}', flush=True)
