"""v4 build: a biome's swimmers rendered with the approved v4 shading / fin settings (see .agents/rules/creature_workflow.md, stage 2).
Every species' settings are in params/<pre>.json (the PILOT_* switches read by swim.py / this script, written by export_params.py).

  python3 v4/build_v4.py <pre> [names...]   build into paths.out_dir(pre) (sheet + .aseprite), then install.py as usual

What the pass does (all switches default off in swim.py, so other biomes and plain build.py are unchanged):
  colour   tone hue drift toward yellow in the lights / away in the darks, chroma profile per tone, outline hue kept off the
           water's discord band, body darks desaturated (DKC)
  shading  light tones in even steps (TOPSTEP) instead of the 0.23 jump from tone 3 to 4, light centre in the upper third,
           tone cap per species (TMAX: 3 = matte body), neighbouring tones mixed in small clusters (DITH), no lone pixels
  outline  bottom outline floor relative to the body, outline kept where the body meets a translucent fin (FINJ), ref pupil
  fins     smooth base-to-edge alpha (no ray alpha), membrane bands + soft mottle, faint rays, rim thins out; motion per fin kind:
           tail swings as one piece, dorsal / anal trailing edges trace a loop, anal fin follows the tail; species gaits kept"""
import os, sys, json, subprocess, math, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import v4env
GEN = v4env.GEN
def params(pre): return json.load(open(os.path.join(HERE, 'params', pre + '.json')))
def _body(fr):
    import numpy as np
    from scipy import ndimage as ndi
    op = fr[..., 3] >= 250; core = ndi.binary_opening(op, structure=ndi.generate_binary_structure(2, 1), iterations=2)
    if core.sum() < 20: core = op
    lab_, n = ndi.label(core)
    if n > 1: sz = ndi.sum(core, lab_, range(1, n + 1)); core = lab_ == (1 + int(np.argmax(sz)))
    return core
def _L(rgb):
    import numpy as np
    c = rgb / 255.; c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    l = 0.4122214708 * c[..., 0] + 0.5363325363 * c[..., 1] + 0.0514459929 * c[..., 2]
    m = 0.2119034982 * c[..., 0] + 0.6806995451 * c[..., 1] + 0.1073969566 * c[..., 2]
    s = 0.0883024619 * c[..., 0] + 0.2817188376 * c[..., 1] + 0.6299787005 * c[..., 2]
    return 0.2104542553 * np.cbrt(l) + 0.793617785 * np.cbrt(m) - 0.0040720468 * np.cbrt(s)
def one(pre, name):
    """runs in its own process: the colour shift edits pal.FAM and the switches are process-wide."""
    P = params(pre)[name]; os.environ.update(P['env']); os.environ['PRE'] = pre
    os.environ['PILOT_WATER'] = str(v4env.WATER[pre][0]) if os.environ.get('PILOT_STEER') == '1' else os.environ.get('PILOT_WATER', '')
    if not os.environ['PILOT_WATER']: del os.environ['PILOT_WATER']
    import numpy as np, swim, gait, pal, build
    swim.use_v3(pre)
    ROT = [float(x) for x in os.environ.get('PILOT_ROT_' + name, os.environ.get('PILOT_ROT', '-5,-2.5,0,3,8,10')).split(',')]
    CS = [float(x) for x in os.environ.get('PILOT_CS_' + name, os.environ.get('PILOT_CS', '0.6,0.8,1,1,1,1')).split(',')]
    WATER = v4env.WATER[pre][0]
    def warmshift(F):
        for k, tones in F.items():
            out = []; cmid = float(np.mean([math.hypot(*pal.lab(t)[1:]) for t in tones[2:4]]))
            for i, h in enumerate(tones):
                L = pal.lab(h); a, b = L[1], L[2]; C = math.hypot(a, b)
                if C >= 0.012:
                    hd = math.degrees(math.atan2(b, a)); d = ((100 - hd + 180) % 360) - 180; r = ROT[i]
                    step = math.copysign(min(abs(r), abs(d)), d) if r > 0 else -math.copysign(abs(r), d)
                    if abs(d) <= 15: step = 0.0   # a yellow family stays put
                    dn = abs(((hd + step) - WATER + 180) % 360 - 180); do = abs((hd - WATER + 180) % 360 - 180)
                    if 45 < dn < 110 and not (45 < do < 110): step = 0.0   # never steer a tone into the discord band
                    if 45 < do < 110 and os.environ.get('PILOT_STEER') == '1':   # a tone already in the band: out to the nearer edge
                        sgn = 1 if ((hd - WATER + 180) % 360 - 180) > 0 else -1
                        step = (sgn * 42.0 + WATER - hd) if do < 77.5 else (sgn * 113.0 + WATER - hd); step = ((step + 180) % 360) - 180
                    hn = math.radians(hd + step); C2 = (cmid * CS[i]) if (os.environ.get('PILOT_CPROF') == '1' and cmid >= 0.012 and i < 2) else C * CS[i]
                    L = np.array([L[0], C2 * math.cos(hn), C2 * math.sin(hn)])
                out.append(pal.hexl(L))
            F[k] = out
    if os.environ.get('PILOT_HUE') == '1': warmshift(pal.FAM)
    if os.environ.get('PILOT_CRIMSON_' + name) == '1': pal.FAM['R1'][4] = pal.FAM['R1'][3]
    m = importlib.import_module(P['module'])
    def render(bodyL=None):
        F = getattr(m, name)(); g = gait.lookup(pre, name)
        if g and not getattr(F, 'crawl', False): F.gait = g
        if os.environ.get('PILOT_LIGHTC', '') != 'keep' and hasattr(F, 'lightc'):
            F.lightc = tuple(float(x) for x in os.environ.get('PILOT_LIGHTC_' + name, os.environ.get('PILOT_LIGHTC', '0.40,0.45,1.0,1.6')).split(','))
        if 'PILOT_TSPANK_' + name in os.environ and hasattr(F, 'tspan'): F.tspan *= float(os.environ['PILOT_TSPANK_' + name])
        if 'PILOT_TONE0' in os.environ and hasattr(F, 'tone0'): F.tone0 += float(os.environ['PILOT_TONE0'])
        if 'PILOT_TONE0_' + name in os.environ and hasattr(F, 'tone0'): F.tone0 += float(os.environ['PILOT_TONE0_' + name])
        for k in ('TAILK', 'HEAD', 'RAMP0', 'FINLOOP', 'LOOPK', 'FINBASEW', 'FINMOT', 'FINMOTL', 'RAYA', 'FAMID', 'FAK', 'FINGRAD', 'FINGS', 'RAYMIX', 'RIMDA',
                  'AMPV', 'AMPD', 'FINDL_CAUD', 'TOPSTEP', 'DITH', 'BANDW', 'BANDC', 'BANDU', 'MOT', 'MOTP', 'FINSTEP', 'RAYDL', 'FLOORREL', 'CATCH', 'FINJ',
                  'DKC', 'TMAX', 'CAP', 'FINK', 'VIVC', 'VIVL'):
            if f'PILOT_{k}_' + name in os.environ: os.environ['PILOT_' + k] = os.environ[f'PILOT_{k}_' + name]
        if 'PILOT_SHOULDER_' + name in os.environ: swim.PILOT['shoulder'] = float(os.environ['PILOT_SHOULDER_' + name])
        if 'PILOT_PUPIL_' + name in os.environ: swim.PILOT['pupil'] = os.environ['PILOT_PUPIL_' + name]
        if 'PILOT_OLC_' + name in os.environ: swim.PILOT['olc'] = float(os.environ['PILOT_OLC_' + name])
        if 'PILOT_FINDL_' + name in os.environ: swim.PILOT['fin_dl'] = float(os.environ['PILOT_FINDL_' + name])
        if 'PILOT_TEX_' + name in os.environ: swim.PILOT['tex'] = float(os.environ['PILOT_TEX_' + name])
        F.pilot_bodyL = bodyL
        return F.sheet() if hasattr(F, 'sheet') else swim.sheet(F)
    # PILOT dict is read at import: re-read the global switches now that the env is set
    swim.PILOT.update(pupil=os.environ.get('PILOT_PUPIL', swim.PILOT['pupil']), fin=os.environ.get('PILOT_FIN') == '1', shoulder=float(os.environ.get('PILOT_SHOULDER', '0')),
                      tex=float(os.environ.get('PILOT_TEX', '0')), floor=float(os.environ.get('PILOT_FLOOR', '0')), fin_dl=float(os.environ.get('PILOT_FINDL', '0.15')), olc=float(os.environ.get('PILOT_OLC', '1.0')))
    sh, W, H, tags = render()
    if swim.PILOT['fin']:   # second pass: fin membranes are set relative to the body's mean lightness
        fr = sh[:H, :W]; bl = float(_L(fr[..., :3].astype(float))[_body(fr)].mean()); sh, W, H, tags = render(bl)
    build.export(pre + '_' + name, sh, W, H, tags, 'swim'); print(name, W, H)
if __name__ == '__main__':
    if len(sys.argv) > 3 and sys.argv[1] == '--one': one(sys.argv[2], sys.argv[3]); sys.exit()
    pre = sys.argv[1]; names = sys.argv[2:] or sorted(params(pre))
    for n in names:   # the generator modules are imported from GEN (cwd); build.export writes to paths.out_dir(pre)
        subprocess.run([sys.executable, os.path.abspath(__file__), '--one', pre, n], check=True, cwd=GEN, env=dict(os.environ, PRE=pre, PYTHONPATH=GEN))
