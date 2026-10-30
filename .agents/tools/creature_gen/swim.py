"""Clear Spring swimmer renderer (side view, body space x: 0 = caudal peduncle .. L = snout, y up).
Each species supplies its own silhouette, colour bands, markings, fins and eye; this file only rasterises them
at 1:1 per direction row with light from above, per-pixel tinted outline and fin flutter (A-B-A-C)."""
import math, numpy as np
from scipy.interpolate import PchipInterpolator
from matplotlib.path import Path
import pal
ROWS = [('E', 1, 0), ('SE', 1, -1), ('SW', -1, -1), ('W', -1, 0), ('NW', -1, 1), ('NE', 1, 1)]
BACKWARD_ROWS = [('E', -1, 0), ('SE', -1, 1), ('SW', 1, 1), ('W', 1, 0), ('NW', 1, -1), ('NE', -1, -1)]
CRAWL_ROWS = [('walk_R', 1, 0), ('walk_L', -1, 0), ('idle_R', 1, 0), ('idle_L', -1, 0)]
class Body:
    def __init__(s, L, depth, prof):
        s.L, s.D = L, depth; u = np.array([p[0] for p in prof])
        s._t = PchipInterpolator(u, [p[1] * depth / 2 for p in prof]); s._b = PchipInterpolator(u, [p[2] * depth / 2 for p in prof])
    def top(s, x): return s._t(np.clip(np.asarray(x, float) / s.L, 0, 1))
    def bot(s, x): return s._b(np.clip(np.asarray(x, float) / s.L, 0, 1))
    def yat(s, u, t): x = u * s.L; tp, bt = s.top(x), s.bot(x); return float(tp - t * (tp - bt))
    def outline_pts(s, n=60):
        xs = np.linspace(0, s.L, n); return [(x, float(s.top(x))) for x in xs] + [(x, float(s.bot(x))) for x in xs[::-1]]
# ------------------------------------------------------------------ fins (body-space polygons + flutter weights)
def _fin(pts, w, rays, kind, col, alpha=(185, 110), dirv=(0, 1), amp=1.0, front=False, rim=None, sig=False, band=None):
    c = pal.fin(col, sig); 
    if rim: c['rim'] = rim
    return dict(pts=np.array(pts, float), w=np.array(w, float), rays=rays, kind=kind, col=c, alpha=alpha, dir=np.array(dirv, float), amp=amp, front=front, band=band, sig=sig)
def _hprof(shape, f):
    if shape == 'tri': return (f / 0.15) if f < 0.15 else (1 - f) ** 0.85 * 1.0 / (0.85 ** 0.85) if f > 0.15 else 1
    if shape == 'round': return math.sin(math.pi * min(1, max(0, f * 0.92 + 0.04))) ** 0.6
    if shape == 'sail': return (0.25 + 0.75 * f / 0.8) if f < 0.8 else (1 - f) / 0.2
    if shape == 'spiny': return (0.7 + 0.3 * math.sin(math.pi * f)) * (0.75 + 0.25 * ((int(f * 9)) % 2)) * min(1, f / 0.1 + 0.2)
    if shape == 'low': return 0.6 + 0.4 * math.sin(math.pi * f) if 0.04 < f < 0.96 else 0.35
    if shape == 'long': return min(1, f / 0.2) * (1 - 0.4 * f)
    if shape == 'trib': return (f / 0.85) ** 0.9 if f < 0.85 else (1 - f) / 0.15
    if shape == 'flat': return 1.0
    return 1.0
def dorsal(B, u0, u1, h, shape='round', col='#888', lean=0.5, n=10, side=1, alpha=(185, 110), rim=None, sig=False, inset=1.0, kind=None, amp=0.8, ray_every=2):
    xs = np.linspace(u0 * B.L, u1 * B.L, n); edge = B.top if side > 0 else B.bot
    base = [(x, float(edge(x)) - side * inset) for x in xs]; f = np.linspace(0, 1, n)
    hh = [h * _hprof(shape, fi) for fi in f]
    tips = [(x - lean * hv, float(edge(x)) + side * hv) for x, hv in zip(xs, hh)]
    pts = base + tips[::-1]; w = [0] * n + [min(1, hv / max(h, 1e-6)) for hv in hh[::-1]]
    ray_every = max(ray_every, int(round(STYLE['ray_min_every'] * n / 10.0)) if STYLE['ray_min_every'] > 1 else ray_every)
    idx = sorted(set(list(range(n - 1, -1, -ray_every)) + [n - 1]))
    rays = [(base[i], tips[i]) for i in idx if hh[i] > 1.2]
    F_ = _fin(pts, w, rays, kind or ('dorsal' if side > 0 else 'anal'), col, alpha, (-1, 0.25 * side), amp, rim=rim, sig=sig)
    F_['fpos'] = np.concatenate([f, f[::-1]]); return F_
def anal(B, u0, u1, h, shape='round', col='#888', lean=0.5, n=10, **k): return dorsal(B, u0, u1, h, shape, col, lean, n, side=-1, **k)
def adipose(B, u, ln, h, col='#888', **k):
    xs = np.linspace(u * B.L - ln / 2, u * B.L + ln / 2, 7); base = [(x, float(B.top(x)) - 0.8) for x in xs]
    tips = [(x - 0.4 * h, float(B.top(x)) + h * math.sin(math.pi * i / 6) ** 0.7) for i, x in enumerate(xs)]
    return _fin(base + tips[::-1], [0] * 7 + [0.6] * 7, [], 'adipose', col, (230, 200), (-1, 0.2), 0.4, **k)
def caudal(B, shape='fork', ln=7.0, spread=None, col='#888', alpha=(185, 110), rim=None, sig=False, upper=1.0, lower=1.0, amp=1.0, n=11):
    t0, b0 = float(B.top(0)), float(B.bot(0)); c = (t0 + b0) / 2; sp = spread or max((t0 - b0) * 2.2, B.D * 0.82)
    a = np.linspace(0, 1, n); out = []
    for f in a:
        yv = c + sp / 2 * (1 - 2 * f) * (upper if f < 0.5 else lower)
        if shape == 'fork': d = ln * (0.6 + 0.4 * abs(1 - 2 * f) ** 1.2)
        elif shape == 'deepfork': d = ln * (0.35 + 0.65 * abs(1 - 2 * f) ** 0.8)
        elif shape == 'emarg': d = ln * (0.82 + 0.18 * abs(1 - 2 * f))
        elif shape == 'round': d = ln * (1 - 0.32 * (2 * f - 1) ** 2)
        elif shape == 'truncate': d = ln
        elif shape == 'lance': d = ln * (1 - 0.75 * abs(2 * f - 1) ** 0.8)
        elif shape == 'hetero': d = ln * ((1.0 - 0.55 * f / 0.45) if f < 0.45 else 0.45 + 0.25 * (f - 0.45) / 0.55)
        else: d = ln
        out.append((-d, yv))
    base = [(0.8, b0 + 0.3), (0.8, t0 - 0.3)]
    def margin(tip, y0, rev=False):
        pts = [(0.8 + (tip[0] - 0.8) * s_, y0 + (tip[1] - y0) * s_ ** 0.5) for s_ in (0.25, 0.5, 0.75)]
        return pts[::-1] if rev else pts
    up = margin(out[0], t0 - 0.3); lo = margin(out[-1], b0 + 0.3, rev=True)
    pts = [base[1]] + up + out + lo + [base[0]]
    w = [0] + [0.3, 0.55, 0.8] + [1.0] * n + [0.8, 0.55, 0.3] + [0]
    rays = [((0.6, c + (t0 - b0) * 0.4 * (1 - 2 * f)), out[i]) for i, f in enumerate(a) if i % (2 if STYLE['ray_min_every'] <= 1 else 3) == 0]
    return _fin(pts, w, rays, 'caudal', col, alpha, (0, 1), amp, rim=rim, sig=sig)
def pectoral(B, u, t, ln, ang=-25, width=0.45, col='#888', alpha=(165, 100), sig=False, amp=1.0, rim=None):
    x0 = u * B.L; y0 = B.yat(u, t); a = math.radians(180 + ang); pts = [(x0 + 0.5, y0 + 1.0)]
    for k in np.linspace(-1, 1, 7):
        aa = a + k * width; r = ln * (1 - 0.25 * k * k); pts.append((x0 + r * math.cos(aa), y0 + r * math.sin(aa)))
    pts.append((x0 + 0.5, y0 - 1.0)); w = [0] + [1.0] * 7 + [0]
    rays = [((x0, y0), pts[i]) for i in (2, 4, 6)]
    return _fin(pts, w, rays, 'pectoral', col, alpha, (0.3, 1), amp, front=True, rim=rim, sig=sig)
def pelvic(B, u, ln, ang=-60, col='#888', alpha=(180, 115), sig=False, front=True, rim=None, amp=0.7):
    x0 = u * B.L; y0 = float(B.bot(x0)) + 0.8; a = math.radians(180 - ang)   # hangs below the belly (was mirrored up into the body)
    tip = (x0 + ln * math.cos(a), y0 + ln * math.sin(a)); tip2 = (x0 + ln * 0.62 * math.cos(a - 0.5), y0 + ln * 0.62 * math.sin(a - 0.5))
    pts = [(x0 + 1.2, y0), tip, tip2, (x0 - 1.6, y0 + 0.2)]   # leading edge to the tip, trailing edge back to the base
    return _fin(pts, [0, 1, .8, 0], [((x0, y0), tip)], 'pelvic', col, alpha, (-0.6, 0.6), amp, front=front, rim=rim, sig=sig)
def tooth(B, u, side, ln=1.0, col='#ddd6bc', gap=0.9):
    """short peg standing just outside the body edge (side 0 = top, 1 = bottom), e.g. sawfish rostral teeth"""
    x0 = u * B.L; y0 = B.yat(u, side); d = 1.0 if side == 0 else -1.0
    pts = [(x0, y0 + d * gap), (x0, y0 + d * (gap + ln * 0.5)), (x0, y0 + d * (gap + ln))]
    return dict(kind='barbel', line=np.array(pts), w=np.array([0, .3, .6]), col=col, thick=0.5, dir=np.array((1.0, 0.0)), amp=0.2, front=True, outside=True)
def barbel(B, u, t, ln, ang, col, thick=0.5):
    x0 = u * B.L; y0 = B.yat(u, t); a = math.radians(ang)
    pts = [(x0, y0), (x0 + ln * 0.5 * math.cos(a), y0 + ln * 0.5 * math.sin(a)), (x0 + ln * math.cos(a - 0.15), y0 + ln * math.sin(a - 0.15))]
    return dict(kind='barbel', line=np.array(pts), w=np.array([0, .5, 1]), col=col, thick=thick, dir=np.array((0.3, -1.0)), amp=0.5, front=True)
# ------------------------------------------------------------------ markings (flat single colour, body space)
def m_stripe(B, u0, u1, t, w, col, wob=0.0):
    """t may be a float or list of (u, t) control points; w = vertical width in px."""
    if isinstance(t, (int, float)): t = [(0, t), (1, t)]
    tu = np.array(t, float)
    def f(x, y, u, tt):
        tc = np.interp(u, tu[:, 0], tu[:, 1]); yc = np.array([B.yat(1, 0)]) * 0
        tp, bt = B.top(x), B.bot(x); ycen = tp - tc * (tp - bt)
        return (u >= u0) & (u <= u1) & (np.abs(y - ycen) <= w / 2)
    return (f, col)
def m_bar(B, u, w, t0, t1, col, lean=0.0):
    def f(x, y, uu, tt): return (np.abs(x - (u * B.L + lean * (tt - 0.5) * B.D)) <= w / 2) & (tt >= t0) & (tt <= t1)
    return (f, col)
def m_spot(B, u, t, r, col, aspect=1.0):
    def f(x, y, uu, tt):
        yc = B.yat(u, t); return ((x - u * B.L) / (r * aspect)) ** 2 + ((y - yc) / r) ** 2 <= 1.0
    return (f, col)
def m_dash(B, u0, u1, t, w, col, period=2.0, on=1.2, off=0.0):
    f0, _ = m_stripe(B, u0, u1, t, w, col)
    def f(x, y, uu, tt): return f0(x, y, uu, tt) & (((x + off) % period) < on)
    return (f, col)
def m_region(B, u0, u1, t0, t1, col):
    def f(x, y, uu, tt): return (uu >= u0) & (uu <= u1) & (tt >= t0) & (tt <= t1)
    return (f, col)
def m_poly(B, pts_ut, col):
    """polygon given in (u, t) coordinates"""
    P = Path(np.array(pts_ut, float))
    def f(x, y, uu, tt): return P.contains_points(np.stack([uu.ravel(), tt.ravel()], 1)).reshape(uu.shape)
    return (f, col)
# ------------------------------------------------------------------ species container
class Fish:
    def __init__(s, name, L, depth, prof, bands, tilt=25, eye=None, crawl=False, backward=False):
        s.name = name; s.B = Body(L, depth, prof); s.bands = bands; s.marks = []; s.fins = []; s.tilt = tilt
        s.eye = eye; s.crawl = crawl; s.backward = backward; s.gill = None; s.mouth = None; s.hl = (0.42, 0.9); s.patches = []
        s.lightc = (0.3, 0.45, 1.7, 1.3); s.tone0 = 1.0; s.tspan = 3.4
    def band_tone(s, u, t):
        pass
def _inpoly(P, X, Y):
    return Path(P).contains_points(np.stack([X.ravel(), Y.ravel()], 1)).reshape(X.shape)
def _segdist(px, py, a, b):
    ax, ay = a; bx, by = b; dx, dy = bx - ax, by - ay; L2 = dx * dx + dy * dy + 1e-9
    t = np.clip(((px - ax) * dx + (py - ay) * dy) / L2, 0, 1); return np.hypot(px - ax - t * dx, py - ay - t * dy)
def _flut(fin, phase):
    if phase == 0: return fin['pts'] if 'pts' in fin else fin['line']
    base = fin['pts'] if 'pts' in fin else fin['line']; d = fin['dir'] / (np.linalg.norm(fin['dir']) + 1e-9)
    g = fin.get('gait')
    if g is not None and not fin.get('floor'):   # per-species gait (gait.py)
        k = fin.get('kind')
        if fin.get('wave'):
            kk = fin['wave']; f = fin['fpos']; off = fin['w'] * fin['amp'] * g.get('ribbon', 1.0) * phase * np.sin(2 * np.pi * kk * f)
            return base + np.outer(off, np.array([0.0, 1.0]))
        w = fin['w'] * g.get(k, 1.0)
        if k == 'caudal' and g.get('tip'): w = fin['w'] ** g['tip'] * g.get(k, 1.0)   # only the lobe tips flick, the fin root holds
        if k in ('dorsal', 'anal') and 'fpos' in fin:
            mode = g.get('median', 'tips'); rear = np.clip(1.4 * (1 - fin['fpos']) ** 1.2, 0, 1.4)
            if mode == 'tips': w = w * rear
            elif mode == 'ripple':   # margin ripple (standing wave along the fin), soft rear rays strongest, plus a light sway with the tail
                side = 1.0 if d[1] >= 0 else -1.0; r = np.clip(0.35 + 0.9 * (1 - fin['fpos']), 0, 1.25)
                off = w * fin['amp'] * phase * r * np.sin(2 * np.pi * g.get('ripple_k', 1.5) * fin['fpos'] + 0.7)
                return base + np.outer(off, np.array([0.0, side])) + np.outer(w * rear * 0.5 * fin['amp'] * phase, d)
        if k == 'pectoral' and g.get('pec') == 'row': d = np.array([0.96, 0.28])   # sculling fore-and-aft
        return base + np.outer(w * fin['amp'] * phase, d)
    amp = STYLE['amp'] or {}
    if fin.get('kind') in amp and not fin.get('floor') and not fin.get('wave'):
        w = fin['w'] * (1.0 if fin.get('crawl_tail') else amp[fin['kind']])
        if fin.get('crawl_tail'): d = np.array([1.0, 0.0])   # a bottom fish flicks its tail fore-aft so the floor row holds
        if STYLE['rear_weight'] and fin['kind'] in ('dorsal', 'anal') and 'fpos' in fin: w = w * np.clip(1.4 * (1 - fin['fpos']) ** 1.2, 0, 1.4)   # only the trailing tips flutter
        return base + np.outer(w * fin['amp'] * phase, d)
    if fin.get('wave'):   # ribbon fin: a ripple runs along the fin (standing wave, sign flips between B and C)
        k = fin['wave']; f = fin['fpos']; off = fin['w'] * fin['amp'] * phase * np.sin(2 * np.pi * k * f)
        return base + np.outer(off, np.array([0.0, 1.0]))
    return base + np.outer(fin['w'] * fin['amp'] * phase, d)
def rgba(h, a=255): c = pal.h2r(h); return np.array([*np.round(c * 255), a], float)
# style switches; the defaults reproduce the sheets shipped in October 2026. STYLE_V2 is the study proposal (softer fins,
# tail-led motion, lighter outline) - see Claude outputs/study_* for the comparison.
import os as _os
GLINTS = set()   # pilot: glint colours stay out of the near-duplicate merge
PILOT = dict(pupil=_os.environ.get('PILOT_PUPIL', '#0c1416'), fin=_os.environ.get('PILOT_FIN') == '1', shoulder=float(_os.environ.get('PILOT_SHOULDER', '0')),
             tex=float(_os.environ.get('PILOT_TEX', '0')), floor=float(_os.environ.get('PILOT_FLOOR', '0')), fin_dl=float(_os.environ.get('PILOT_FINDL', '0.15')), olc=float(_os.environ.get('PILOT_OLC', '1.0')))
STYLE = dict(fin_levels=3, fin_edge_L=0.0, ray_min_every=1, ray_dL=0.2, ray_alpha=45, ray_fade=False, rim='dark', amp=None, rear_weight=False,
             outline=(0.64, 0.58, 0.48, 0.36, 0.32, 0.68))
STYLE_V2 = dict(despeck=6, fin_levels=None, fin_step=12, fin_edge_L=0.03, ray_min_every=3, ray_dL=0.09, ray_alpha=18, ray_fade=True, rim='light',
                amp=dict(caudal=1.9, dorsal=0.4, anal=0.4, pectoral=0.0, pelvic=0.6, adipose=0.5), rear_weight=True,
                outline=(0.80, 0.74, 0.62, 0.48, 0.42, 0.80))
STYLE_V3 = dict(no_head_lines=True, nub=False, sil_smooth=True, body_v3=True, volume=True, zone_k=2, zone_min=5, rim_h=10, merge_dE=0.016)
def use_v3(biome=None):
    use_v2(); STYLE.update(STYLE_V3)
    if biome: STYLE['tone_shift'] = pal.use_v3(biome)   # colour fit to the biome's water (pal.BG_L / BIOMES_V3 / FIT_V3)
    if biome and 'outline' in pal.FIT_V3.get(biome, {}): STYLE['outline'] = pal.FIT_V3[biome]['outline']   # dark water: a deeper outline (bw edge -0.13)
def use_v2():
    """switch to the study proposal (Oct 2026): tail-led motion, soft graded fins with sparse fading rays and a light-catching
    margin, fins keeping the body hue, lighter outline, warmer and brighter highlights."""
    STYLE.update(STYLE_V2); pal.FINSTYLE.update(tint=0.15, lift=0.0, ray_dL=0.09, sig_dL=0.06); pal.RAMPSTYLE.update(hi_mix=0.28, hi_lift=0.02)

def _oklab_rgb(rgb):
    c = rgb / 255.0; l = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]])
    M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]])
    return np.cbrt(l @ M1.T) @ M2.T
def _runfill(Lb, inside, k=2, axis=1):
    """runs of <= k pixels whose two neighbours along the axis carry the same zone are filled with it (removes notches)."""
    A = Lb if axis == 1 else Lb.T; ins = inside if axis == 1 else inside.T; A = A.copy()
    for y in range(A.shape[0]):
        row = A[y]; x = 0; n = len(row)
        while x < n:
            if not ins[y, x]: x += 1; continue
            x2 = x
            while x2 + 1 < n and ins[y, x2 + 1] and row[x2 + 1] == row[x]: x2 += 1
            ln = x2 - x + 1
            if ln <= k and x - 1 >= 0 and x2 + 1 < n and ins[y, x - 1] and ins[y, x2 + 1] and row[x - 1] == row[x2 + 1] and row[x - 1] != row[x]:
                row[x:x2 + 1] = row[x - 1]
            x = x2 + 1
    return A if axis == 1 else A.T
def _clean_zones(Lb, inside, k=2, min_area=5):
    """BW-style tone zones: no notches, no islands - each tone reads as one broad, clean area."""
    from scipy import ndimage
    for _ in range(2):
        Lb = _runfill(Lb, inside, k, 1); Lb = _runfill(Lb, inside, k, 0)
    for v in np.unique(Lb[inside]):
        lab, n = ndimage.label((Lb == v) & inside)
        for i in range(1, n + 1):
            m = lab == i
            if m.sum() >= min_area: continue
            nb = ndimage.binary_dilation(m) & ~m & inside
            if nb.any():
                vals, cnt = np.unique(Lb[nb], return_counts=True); Lb[m] = vals[cnt.argmax()]
    return Lb
def _merge_colours(frames, thr):
    """merge near-duplicate opaque colours (OKLab distance < thr) into the more common one, the same way in every frame."""
    px = np.concatenate([f[f[..., 3] >= 250][:, :3] for r in frames for f in r]).astype(int)
    if not len(px): return
    cols, cnt = np.unique(px, axis=0, return_counts=True); order = np.argsort(-cnt); cols = cols[order]
    lab = _oklab_rgb(cols.astype(float)); keep = []; mp = {}
    for i in range(len(cols)):
        if tuple(int(v) for v in cols[i]) in GLINTS: keep.append(i); continue
        if keep:
            d = np.linalg.norm(lab[keep] - lab[i], axis=1); j = int(np.argmin(d))
            if d[j] < thr: mp[tuple(cols[i])] = cols[keep[j]]; continue
        keep.append(i)
    if not mp: return
    for r in frames:
        for f in r:
            o = f[..., 3] >= 250; key = f[..., :3].astype(int)
            for c, t in mp.items():
                m = o & (key[..., 0] == c[0]) & (key[..., 1] == c[1]) & (key[..., 2] == c[2]); f[m, :3] = t

def _sil_edge(inside, top=True):
    """pixel-art clean-up of one body contour (top or bottom edge, one y per column). On a convex hump the stair runs
    should grow steadily toward the crest (1-1-2-3-5-8 ... 4-3-2-1); rasterising the curve gives jitter like 4-2-2-5-3.
    The runs in the convex, shallow part on each side of the crest are re-ordered by length (their y levels stay), and
    the crest run becomes the longest. Concave stretches (peduncle, forehead) and steep stretches are left alone."""
    from scipy.ndimage import gaussian_filter1d
    xs = np.where(inside.any(0))[0]
    if len(xs) < 8: return inside
    cols = np.arange(xs.min(), xs.max() + 1)
    if not all(inside[:, x].any() for x in cols): return inside
    c = np.array([np.where(inside[:, x])[0].min() if top else np.where(inside[:, x])[0].max() for x in cols])
    sm = gaussian_filter1d(c.astype(float), 2.0, mode='nearest'); d2 = np.gradient(np.gradient(sm))
    hump = (d2 >= -0.02) if top else (d2 <= 0.02)   # curving like the crest of the body
    R = []   # runs: [y, start, length]
    for i, y in enumerate(c):
        if R and R[-1][0] == y: R[-1][2] += 1
        else: R.append([y, i, 1])
    if len(R) < 4: return inside
    ext = min(r[0] for r in R) if top else max(r[0] for r in R)
    k = max((i for i, r in enumerate(R) if r[0] == ext), key=lambda i: R[i][2])
    def block(idx):   # contiguous shallow convex runs walking away from the crest
        out = []
        for i in idx:
            nb = i + 1 if i < k else i - 1
            if abs(R[i][0] - R[nb][0]) != 1 or not hump[R[i][1] + R[i][2] // 2]: break
            out.append(i)
        return out
    L = block(range(k - 1, 0, -1)); Rr = block(range(k + 1, len(R) - 1))   # the outermost runs stay (they meet fins / ends)
    lens = {i: R[i][2] for i in L + Rr + [k]}
    for blk in (L, Rr):
        v = sorted((lens[i] for i in blk), reverse=True)   # longest next to the crest
        for i, n in zip(blk, v): lens[i] = n
    near = [b[0] for b in (L, Rr) if b]
    if near:
        j = max(near, key=lambda i: lens[i])
        if lens[j] > lens[k]: lens[j], lens[k] = lens[k], lens[j]
        for blk in (L, Rr):
            v = sorted((lens[i] for i in blk), reverse=True)
            for i, n in zip(blk, v): lens[i] = n
    for i, n in lens.items(): R[i][2] = n
    new = np.concatenate([[r[0]] * r[2] for r in R])
    if len(new) != len(c): return inside
    out = inside.copy()
    for x, y0, y1 in zip(cols, c, new):
        if y1 == y0: continue
        if top:
            if y1 < y0: out[y1:y0, x] = True
            else: out[y0:y1, x] = False
        else:
            if y1 > y0: out[y0 + 1:y1 + 1, x] = True
            else: out[y1 + 1:y0 + 1, x] = False
    return out
def _smooth_silhouette(inside):
    m = _sil_edge(inside, True); m = _sil_edge(m, False)
    m = _sil_edge(m.T, True).T; m = _sil_edge(m.T, False).T   # snout and tail ends (contour as a function of y)
    return m
def render(F, facing, tdir, phase, cx, cy, W, H, idle=False):
    _FIN2 = PILOT['fin'] and _os.environ.get('PILOT_FIN2') == '1'
    """one frame. facing 1 right / -1 left; tdir -1 nose down, 0 level, 1 nose up; phase -1/0/1 fin flutter."""
    B = F.B; th = math.radians(F.tilt) * tdir
    I, J = np.meshgrid(np.arange(W) + 0.5, np.arange(H) + 0.5)
    xp = (I - cx) * facing; yp = cy - J
    X = xp * math.cos(th) + yp * math.sin(th) + F.piv[0]; Y = -xp * math.sin(th) + yp * math.cos(th) + F.piv[1]
    img = np.zeros((H, W, 4)); kind = np.zeros((H, W), int)   # 0 empty 1 back-fin 2 body 3 front-fin
    def eff(fin, ph):   # idle rows: subtler flutter, except fins whose sweep sets the lowest pixel (ribbon waves, barbels)
        return ph if (not idle or fin.get('wave') or fin.get('floor') or fin['kind'] == 'barbel') else ph * 0.5
    def put_fin(fin, ph):
        ph = eff(fin, ph)
        _mul = {'anal': float(_os.environ.get('PILOT_AMPV', '1')), 'pelvic': float(_os.environ.get('PILOT_AMPV', '1')), 'dorsal': float(_os.environ.get('PILOT_AMPD', '1'))}.get(fin.get('kind'), 1.0) if _FIN2 else 1.0
        _k = fin.get('kind'); _fx = fin
        if _FIN2:
            # each fin kind keeps its own motion (AC/BW/PF): the tail swings up-down as one piece; dorsal and anal fins move at the
            # trailing tips (species gait: tips / ripple / whole) and trace a loop - back in B, lifting away from the body in D -
            # instead of mirroring the tail; the anal fin follows the tail's vertical direction
            _bw = float(_os.environ.get('PILOT_FINBASEW', '0')) if _k == 'caudal' else 0.0
            _d = np.asarray(fin.get('dir', (0, 1)), float).copy()
            if _k == 'anal': _d[1] = abs(_d[1])
            if _k in ('dorsal', 'anal') and _os.environ.get('PILOT_FINLOOP', '1') == '1' and ph < 0:
                away = 1.0 if _k == 'dorsal' else -1.0; _d = np.array([0.3, away]); ph = ph * float(_os.environ.get('PILOT_LOOPK', '0.6'))
            _fx = dict(fin, amp=fin['amp'] * _mul, w=_bw + (1 - _bw) * np.asarray(fin['w'], float), dir=_d)
        P = _flut(_fx, ph); m = _inpoly(P, X, Y)
        _dP = P.mean(0) - np.asarray(fin['pts'], float).mean(0) if 'pts' in fin else np.zeros(2)   # membrane texture rides with the fin
        if not m.any(): return
        c = fin['col']; a0, a1 = fin['alpha']
        if PILOT['fin']:
            _fk = float(_os.environ.get('PILOT_FINK', '0.55')); a0, a1 = 187.5 + _fk * (a0 - 150), 187.5 + _fk * (a1 - 150)   # narrow, high alpha band like the references
            if _FIN2:   # AC/BW membranes: base ~180, free edge ~155, one smooth fall (no ray alpha)
                _am, _ak = float(_os.environ.get('PILOT_FAMID', '168')), float(_os.environ.get('PILOT_FAK', '0.35')); a0, a1 = _am + _ak * (fin['alpha'][0] - 147.5), _am + _ak * (fin['alpha'][1] - 147.5)
            c = dict(c); _m = pal.lab(c['mem'])
            _viv = fin.get('sig') or np.hypot(_m[1], _m[2]) > 0.08
            if getattr(F, 'pilot_bodyL', None) is not None:
                _m[0] = max(_m[0], F.pilot_bodyL + float(_os.environ.get('PILOT_VIVL', '0.12'))) if _viv else min(0.93, F.pilot_bodyL + PILOT['fin_dl'] + (float(_os.environ.get('PILOT_FINDL_CAUD', '0')) if fin['kind'] == 'caudal' else 0.0))   # signature fins keep their colour, only never darker than the body
                if _viv and _m[0] > pal.lab(fin['col']['mem'])[0] + 0.02: _m[1:] *= float(_os.environ.get('PILOT_VIVC', '1.0'))   # a lifted complement fin loses some chroma so it does not turn salmon
                _o = pal.lab(fin['col']['mem']); _oh = math.degrees(math.atan2(_o[2], _o[1]))
                if _viv and -35 <= _oh <= 75:   # red / orange / copper signature fins: a lift turns them salmon, so they keep their own depth (at most +0.04) and gain a little chroma
                    _m = _o.copy(); _m[0] = _o[0] + min(0.04, max(0.0, F.pilot_bodyL + float(_os.environ.get('PILOT_VIVL', '0.08')) - _o[0]) if getattr(F, 'pilot_bodyL', None) is not None else 0.0); _m[1:] = _o[1:] * 1.1
            else: _m[0] -= 0.07
            c['mem'] = pal.hexl(_m); _r = pal.lab(c['ray']); _r[0] = _m[0] - float(_os.environ.get('PILOT_RAYDL', '0.06')); c['ray'] = pal.hexl(_r)
        col = np.zeros((H, W, 4)); col[...] = rgba(c['mem'], a1)
        # alpha falls from the base (a0) to the free edge (a1): inverse-distance blend of vertex weights
        d = np.stack([np.hypot(X - px, Y - py) for px, py in P], 0) + 0.3; wv = (fin['w'][:, None, None] / d ** 2).sum(0) / (1 / d ** 2).sum(0)
        av = a0 + (a1 - a0) * np.clip(wv * 1.15, 0, 1)
        if STYLE['fin_levels']:
            lv = np.linspace(a1, a0, STYLE['fin_levels']); col[..., 3] = lv[np.argmin(np.abs(av[..., None] - lv), -1)]
        else: st = int(_os.environ.get('PILOT_FINSTEP', STYLE.get('fin_step', 6))); col[..., 3] = np.round(av / st) * st   # soft membrane: alpha in fine steps from base to edge
        Lm0 = pal.lab(c['mem']); vivid = fin.get('sig') or np.hypot(Lm0[1], Lm0[2]) > 0.08
        if vivid and STYLE['rim'] == 'light' and not PILOT['fin']: col[..., 3] = np.minimum(235, col[..., 3] + 24)   # coloured fins stay a little denser so the hue reads over water
        if STYLE['fin_edge_L'] and not vivid and not PILOT['fin']:   # clear membrane lightens toward the free edge (glassy, light-catching margin)
            ew = np.round(np.clip(wv * 1.15, 0, 1) * 2) / 2; Lm = pal.lab(c['mem']); Lm[0] = min(0.95, Lm[0] + STYLE['fin_edge_L']); hi = rgba(pal.hexl(Lm))[:3]   # same hue, lighter
            col[..., :3] = col[..., :3] + (hi - col[..., :3]) * ew[..., None]
        if _FIN2:
            _g = float(_os.environ.get('PILOT_FINGRAD', '0.08')) * (0.5 if vivid else 1.0); _ns = int(_os.environ.get('PILOT_FINGS', '4'))
            if _g > 0:
                ew2 = np.round(np.clip(wv * 1.15, 0, 1) * (_ns - 1)) / (_ns - 1); Lm = pal.lab(c['mem'])
                for _q in np.unique(ew2):
                    _c = Lm.copy(); _c[0] = min(0.95, Lm[0] + _g * (_q - 0.5)); mm_ = ew2 == _q; col[mm_, :3] = rgba(pal.hexl(_c))[:3]
        _fm = float(_os.environ.get('PILOT_FINMOT', '0')) if _FIN2 else 0.0
        if _fm > 0:   # ref fins: soft isotropic mottle inside the membrane instead of hard ray lines
            hx_ = np.round(X - _dP[0]); hy_ = np.round(Y - _dP[1]); h1_ = np.modf(np.abs(np.sin(hx_ * 17.31 + hy_ * 61.7) * 43758.5453))[0]; h2_ = np.modf(np.abs(np.sin(hx_ * 7.13 + hy_ * 29.9) * 24634.6345))[0]
            sel_ = m & (h1_ < _fm); dl_ = float(_os.environ.get('PILOT_FINMOTL', '0.05'))
            for sg_ in (1, -1):
                mm_ = sel_ & ((h2_ < 0.5) == (sg_ > 0))
                if not mm_.any(): continue
                for key_ in np.unique(col[mm_, :3].round().astype(int), axis=0):
                    k2_ = mm_ & (np.abs(col[..., :3] - key_).sum(-1) < 1)
                    _c = pal.lab(pal.r2h(key_ / 255)); _c[0] = min(0.95, max(0.05, _c[0] + sg_ * dl_)); col[k2_, :3] = rgba(pal.hexl(_c))[:3]
        bandm = np.zeros((H, W), bool)
        if fin.get('band'):
            for (bm, bc) in fin['band']:
                mm = bm(X, Y); col[mm, :3] = rgba(bc)[:3]; col[mm, 3] = np.maximum(col[mm, 3], a0 - 10); bandm |= mm
        for (a, b) in [(p, q) for (p, q) in fin['rays'] if np.hypot(q[0] - p[0], q[1] - p[1]) >= 2.5]:
            if ph:
                ia = int(np.argmin(np.hypot(*(fin['pts'] - np.array(b)).T))); b = P[ia]
            dd = _segdist(X, Y, a, b); rm = dd < 0.5
            if STYLE['ray_fade']:   # ray fades out toward the free edge
                tt = np.clip(np.hypot(X - a[0], Y - a[1]) / max(1e-6, np.hypot(b[0] - a[0], b[1] - a[1])), 0, 1); k_ = np.ceil((1 - tt ** 1.5)[rm] * 3) / 3
                if vivid: k_ = np.maximum(k_, 2 / 3)   # coloured fins keep their rays to the edge (the rays carry the hue)
                if _FIN2: k_ = k_ * float(_os.environ.get('PILOT_RAYMIX', '0.6'))
                col[rm, :3] = col[rm, :3] + (rgba(c['ray'])[:3] - col[rm, :3]) * k_[:, None]; col[rm, 3] = np.minimum(235, col[rm, 3] + (float(_os.environ.get('PILOT_RAYA', '0')) if _FIN2 else STYLE['ray_alpha']) * k_)
            else: col[rm, :3] = rgba(c['ray'])[:3]; col[rm, 3] = np.minimum(235, col[rm, 3] + STYLE['ray_alpha'])
        if STYLE['rim'] == 'light':   # fin margin: clear fins catch the light, coloured fins get a deeper rim of their own hue
            pm = np.pad(m, 1); inner = pm[:-2, 1:-1] & pm[2:, 1:-1] & pm[1:-1, :-2] & pm[1:-1, 2:]; e = m & ~inner & ~bandm   # fin markings run through the margin
            Lr = pal.lab(c['mem'])
            if vivid: Lr[0] -= 0.04; Lr[1:] *= 1.06; da = 0 if _FIN2 else 24
            else: Lr[0] = min(0.95, Lr[0] + 0.025); da = float(_os.environ.get('PILOT_RIMDA', '-10')) if _FIN2 else 10
            col[e, :3] = rgba(pal.hexl(Lr))[:3]; col[e, 3] = np.minimum(240 if PILOT['fin'] else 255, col[e, 3] + da)   # pilot: a fin rim never turns opaque (it would join the silhouette)
        return m, col
    def comp(m, col, k):
        a = col[..., 3:] / 255.0; under = img.copy()
        out = col.copy(); emp = under[..., 3] == 0
        mix = (~emp) & m
        out[mix, :3] = col[mix, :3] * a[mix] + under[mix, :3] * (1 - a[mix]); out[mix, 3] = 255
        img[m] = out[m]; kind[m] = np.where(emp[m], k, kind[m] if k == 3 else k)
    back = [f for f in F.fins if not f.get('front')]; front = [f for f in F.fins if f.get('front')]
    for f in back:
        if 'pts' in f:
            r = put_fin(f, phase)
            if r: comp(r[0], r[1], 1)
    # body
    tp, bt = B.top(X), B.bot(X); inside = (X >= 0) & (X <= B.L) & (Y <= tp) & (Y >= bt)
    U = np.clip(X / B.L, 0, 1); T = np.clip((tp - Y) / np.maximum(tp - bt, 1e-6), 0, 1)
    if STYLE.get('sil_smooth'): inside = _smooth_silhouette(inside)   # clean stair runs on the body contour
    body = np.zeros((H, W, 4))
    dtop = tp - Y; dbot = Y - bt
    # BW-style form shading: value falls off from a light centre in the upper middle of the body, gently toward the
    # back edge and the two ends, strongly toward the belly; quantised into contour-following tone bands.
    lc, kt, kb, pb = F.lightc
    v = np.where(T < lc, 1 - kt * (np.clip(lc - T, 0, 1) / lc) ** 2, 1 - kb * (np.clip(T - lc, 0, 1) / (1 - lc)) ** pb)
    v = v - float(_os.environ.get('PILOT_TAILK', '0.55')) * np.clip((0.16 - U) / 0.16, 0, 1) - 0.4 * np.clip((U - 0.88) / 0.12, 0, 1)
    if PILOT['shoulder']:
        if _os.environ.get('PILOT_SHMODE') == 'ramp':   # value rises gently from the tail to the shoulder, then the head darkens as before (no spot)
            _r0 = float(_os.environ.get('PILOT_RAMP0', '0.15')); v = v + PILOT['shoulder'] * (np.clip((U - _r0) / (0.70 - _r0), 0, 1) - 0.5)
            v = v - float(_os.environ.get('PILOT_HEAD', '0')) * np.clip((U - 0.84) / 0.16, 0, 1)   # head a little darker than the shoulder
        else: v = v + PILOT['shoulder'] * (np.exp(-((U - 0.66) / float(_os.environ.get('PILOT_SHW', '0.22'))) ** 2) - 0.45)   # light peaks at the shoulder behind the head
    tone = np.clip(np.round(F.tone0 + STYLE.get('tone_shift', 0.0) + v * F.tspan), 0, 5).astype(int)
    _qraw = F.tone0 + STYLE.get('tone_shift', 0.0) + v * F.tspan
    # bands: list of (t_end_at_tail, t_end_at_head, ramp); first matching band wins
    assigned = np.zeros((H, W), bool); ramps = []; ridx = np.full((H, W), -1)
    for (e0, e1, ramp) in F.bands:
        tend = e0 + (e1 - e0) * U; m = inside & ~assigned & (T <= tend); ramps.append(ramp); ridx[m] = len(ramps) - 1
        assigned |= m
    for (fn, ramp) in F.patches:
        m = inside & fn(X, Y, U, T); ramps.append(ramp); ridx[m] = len(ramps) - 1
    npatch0 = len(ramps) - len(F.patches)   # index of the first patch ramp (signature patches)
    if STYLE.get('body_v3'):   # clean tone zones, then a one-step darker inner rim on deep bodies (BW severum / hemiodus look)
        from scipy import ndimage
        Lb = np.where(inside, (ridx + 1) * 8 + tone, -1); Lb = _clean_zones(Lb, inside, STYLE.get('zone_k', 2), STYLE.get('zone_min', 5))
        ridx = np.where(inside, Lb // 8 - 1, ridx); tone = np.where(inside, Lb % 8, tone)
        if STYLE.get('volume'):   # one volume: below the brightest pixel of each column the value only falls, and above it too
            RL = [np.array([pal.lab(c)[0] for c in rp]) for rp in ramps]
            def Lof(j, i): return RL[ridx[j, i]][tone[j, i]] if ridx[j, i] >= 0 else None
            for i in np.where(inside.any(0))[0]:
                js = np.where(inside[:, i] & (ridx[:, i] >= 0))[0]
                if len(js) < 3: continue
                Ls = np.array([Lof(j, i) for j in js]); h = int(np.argmax(Ls))
                for step in (1, -1):
                    k = h + step
                    while 0 <= k < len(js):
                        j, jp = js[k], js[k - step]; lim = Lof(jp, i) + 0.02
                        while tone[j, i] > 0 and Lof(j, i) > lim: tone[j, i] -= 1
                        k += step
        if F.patches: tone = np.where(ridx >= npatch0, np.clip(tone, 2, 3), tone)   # signature patches keep their own colour depth (never washed out, never muddy)
        if STYLE.get('rim_h'):
            e1 = ndimage.binary_erosion(inside); e2 = ndimage.binary_erosion(e1); ring = e1 & ~e2
            deep = (inside.sum(0) >= STYLE['rim_h'])[None, :] & np.ones_like(inside)
            m = ring & deep & (T < 0.72); tone = np.where(m, np.maximum(tone - 1, 0), tone)
    _dith = float(_os.environ.get('PILOT_DITH', '0'))
    if _dith > 0:   # reference micro-texture: where the form value sits between two tones the pixels mix them in small clusters (2 px cells + per-pixel jitter, body coords -> stable across frames)
        hx = np.round(X); hy = np.round(Y)
        nc = np.modf(np.abs(np.sin(np.floor(hx / 2) * 12.9898 + np.floor(hy / 2) * 78.233 + 3.1) * 43758.5453))[0]
        npx = np.modf(np.abs(np.sin(hx * 39.3468 + hy * 11.135) * 24634.6345))[0]
        n_ = 0.55 * nc + 0.45 * npx
        d_ = _qraw - np.round(_qraw); off = np.floor(d_ + _dith * (n_ - 0.5) + 0.5).astype(int)
        ok = inside & (ridx >= 0)
        if F.patches: ok &= ridx < npatch0
        tone = np.where(ok, np.clip(tone + np.clip(off, -1, 1), 0, 5), tone)
        for _ in range(2):   # no lone pixel: a pixel whose four neighbours share one other tone joins them
            nb = [np.roll(tone, 1, 0), np.roll(tone, -1, 0), np.roll(tone, 1, 1), np.roll(tone, -1, 1)]
            nr = [np.roll(ridx, 1, 0), np.roll(ridx, -1, 0), np.roll(ridx, 1, 1), np.roll(ridx, -1, 1)]
            lone = ok & (nb[0] == nb[1]) & (nb[1] == nb[2]) & (nb[2] == nb[3]) & (nb[0] != tone) & (nr[0] == ridx) & (nr[1] == ridx) & (nr[2] == ridx) & (nr[3] == ridx)
            tone = np.where(lone, nb[0], tone)
    _cap = float(_os.environ.get('PILOT_CAP', '0'))
    if _cap > 0:   # reference-style lit cap: one step lighter along the whole back contour, from just under the top edge down to T=_cap
        _top = np.zeros_like(inside); _top[1:] = inside[1:] & ~inside[:-1]
        _in1 = inside & ~_top & (T <= _cap) & (U > 0.08) & (U < 0.9) & (ridx >= 0)
        if F.patches: _in1 &= ridx < npatch0
        _cm = int(_os.environ.get('PILOT_CAPMAX', '4')); tone = np.where(_in1, np.maximum(tone, np.minimum(tone + 1, _cm)), tone)
        _c4 = float(_os.environ.get('PILOT_CAP4', '0'))
        if _c4 > 0: tone = np.where(_in1 & (T <= _c4), np.maximum(tone, np.minimum(tone + 1, 4)), tone)   # a thinner top strip of the light tone along the same contour
    _tmax = int(_os.environ.get('PILOT_TMAX', '5')); _bw = float(_os.environ.get('PILOT_BANDW', '0'))
    if _bw > 0:   # reference lit streak: tone 3 cap everywhere, one step lighter (max 4) only in a thin streak along the flank, thickest mid-body, tapering to the ends
        _bc = float(_os.environ.get('PILOT_BANDC', str(F.lightc[0]))); _u0, _u1 = [float(x) for x in _os.environ.get('PILOT_BANDU', '0.18,0.82').split(',')]
        _um = (_u0 + _u1) / 2; _hs = (_u1 - _u0) / 2; _we = _bw * np.sqrt(np.clip(1 - ((U - _um) / _hs) ** 2, 0, 1))
        _band = inside & (ridx >= 0) & (np.abs(T - _bc) <= _we) & (_we > 0)
        if F.patches: _band &= ridx < npatch0
        _tc = np.where(inside & (ridx >= 0), np.minimum(tone, 3), tone)
        tone = np.where(_band & (tone >= 3), np.minimum(np.maximum(tone, _tc + 1), 4), _tc)
    elif _tmax < 5: tone = np.where(inside & (ridx >= 0), np.minimum(tone, _tmax), tone)   # no highlight plateau above this tone
    _mot = float(_os.environ.get('PILOT_MOT', '0'))
    if _mot > 0:
        hx = np.round(X); hy = np.round(Y)
        for _pass, _salt in ((0, 0.0), (1, 7.31))[:int(_os.environ.get('PILOT_MOTP', '2'))]:
            h1 = np.modf(np.abs(np.sin(hx * 12.9898 + hy * 78.233 + _salt) * 43758.5453))[0]; h2 = np.modf(np.abs(np.sin(hx * 39.3468 + hy * 11.135 + _salt) * 24634.6345))[0]
            ok = inside & (ridx >= 0)
            if F.patches: ok &= ridx < npatch0
            new_t = tone.copy(); pr = _mot * (1.0 if _pass == 0 else 0.6)
            for dj, di in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                tn_ = np.roll(np.roll(tone, dj, 0), di, 1); rn_ = np.roll(np.roll(ridx, dj, 0), di, 1); okn = np.roll(np.roll(ok, dj, 0), di, 1)
                cand = ok & okn & (rn_ == ridx) & (np.abs(tn_ - tone) == 1) & (new_t == tone) & (h1 < pr) & ((h2 < 0.5) == (dj + di < 0))
                new_t = np.where(cand, tn_, new_t)
            tone = new_t
    _ts = float(_os.environ.get('PILOT_TOPSTEP', '0'))
    def _remap(rp):   # reference tone ladder: the light tones climb in the same small steps as the rest (no 0.23 jump from tone 3 to tone 4)
        if _ts <= 0: return rp
        out = list(rp); L3 = pal.lab(rp[3])[0]
        for k_, tgt in ((4, L3 + _ts), (5, L3 + 2 * _ts)):
            c = pal.lab(rp[k_]); c[0] = min(c[0], tgt); out[k_] = pal.hexl(c)
        return out
    ramps_p = [_remap(rp) for rp in ramps]
    def paint(m, tn):
        for r, rp in enumerate(ramps_p):
            for k in range(6):
                mk = m & (ridx == r) & (tn == k); body[mk] = rgba(rp[k])
    paint(inside, tone)
    if F.gill and not STYLE.get('no_head_lines'):
        gu, gt0, gt1, bow = F.gill; gx = gu * B.L + bow * (2 * (T - 0.5)) ** 2 * -1
        m = inside & (np.abs(X - gx) < 0.55) & (T > gt0) & (T < gt1)
        body[m, :3] = body[m, :3] * 0.8
    for (fn, col) in F.marks:
        m = inside & fn(X, Y, U, T)
        if isinstance(col, (int, float)): paint(m, np.clip(tone + int(col), 0, 5))   # shaded mark: body tone shifted darker
        else: body[m] = rgba(col)
    if PILOT['tex']:   # scattered single-pixel half-tones in the lit zone; hash of body coordinates -> same pixels in every frame of a row
        hx = np.round(X); hy = np.round(Y); hsh = np.modf(np.abs(np.sin(hx * 12.9898 + hy * 78.233) * 43758.5453))[0]
        hs2 = np.modf(np.abs(np.sin(hx * 39.3468 + hy * 11.135) * 24634.6345))[0]
        sel = inside & (body[..., 3] > 0) & (T > 0.12) & (T < 0.62) & (U > 0.14) & (U < 0.84) & (hsh < PILOT['tex'])
        done = np.zeros((H, W), bool); idx_ = 0
        for j, i in zip(*np.where(sel)):
            r_ = ridx[j, i]; k_ = tone[j, i]
            if r_ < 0 or done[max(j - 1, 0):j + 2, max(i - 1, 0):i + 2].any(): continue
            done[j, i] = True; idx_ += 1
            s_ = 1 if (hs2[j, i] < 0.45 and k_ < 5) else -1
            if not (0 <= k_ + s_ <= 5): s_ = -s_
            c0 = pal.lab(ramps[r_][k_]); c1 = pal.lab(ramps[r_][k_ + s_]); c = c0 + (c1 - c0) * 0.55
            ang = math.radians((hs2[j, i] - 0.5) * 16); ca, sa = math.cos(ang), math.sin(ang); c = np.array([c[0], c[1] * ca - c[2] * sa, c[1] * sa + c[2] * ca])
            g1 = (idx_ * 0.6180339887) % 1.0; g2 = (idx_ * 0.4142135624 + 0.3) % 1.0
            c[0] += (g1 - 0.5) * 0.04; c[1:] *= 0.85 + 0.3 * g2   # each glint its own colour, as hand-placed pixels are
            body[j, i] = rgba(pal.hexl(c)); GLINTS.add(tuple(int(v) for v in body[j, i, :3]))
    if F.mouth and not STYLE.get('no_head_lines'):   # v3: no mouth line and no dark gill line (clean heads, as in bw)
        mt, ml = F.mouth; ym = np.array([B.yat(1, mt)])
        m = inside & (X > B.L - ml) & (np.abs(Y - (tp - mt * (tp - bt))) < 0.5)
        body[m, :3] = body[m, :3] * 0.72
    body[~inside] = 0
    m = body[..., 3] > 0; img[m] = body[m]; kind[m] = 2
    for f in front:
        if 'line' in f:
            P = _flut(f, eff(f, phase)); d = np.min([_segdist(X, Y, P[i], P[i + 1]) for i in range(len(P) - 1)], 0)
            m = (d < f['thick']) & ~(kind == 2) | ((d < f['thick']) & (kind == 2) & False)
            mm = (d < f['thick']) & ~(kind == 2) if f.get('outside') else (d < f['thick'])
            img[mm] = rgba(f['col']); kind[mm] = 3
        else:
            r = put_fin(f, phase)
            if r: comp(r[0], r[1], 3)
    # cleanup: drop isolated pixels, fill body pinholes
    op = img[..., 3] > 0; pad = np.pad(op, 1)
    nb = sum(np.roll(np.roll(pad, a, 0), b, 1) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0))[1:-1, 1:-1]
    img[op & (nb == 0)] = 0
    # silhouette cleanup: drop stair-corner nubs (body pixel with exactly two opaque 4-neighbours forming an L)
    for _ in range(1 if STYLE.get('nub', True) else 0):
        op = img[..., 3] > 0; pad = np.pad(op, 1, constant_values=False)
        u_, d_, l_, r_ = pad[:-2, 1:-1], pad[2:, 1:-1], pad[1:-1, :-2], pad[1:-1, 2:]
        cnt = u_.astype(int) + d_ + l_ + r_
        nub = op & (kind == 2) & (cnt == 2) & ((u_ & l_) | (u_ & r_) | (d_ & l_) | (d_ & r_))
        img[nub] = 0; kind[nub] = 0
    # BW-style selective outline: the edge pixel takes a darker shade of the colour just inside it; the top edge is
    # lit (only a little darker than the body), the sides darker, the belly edge darkest, and the row above the
    # belly edge is pulled down too so the shadow and the outline merge into one dark rim.
    op = img[..., 3] > 0; pad = np.pad(op, 1, constant_values=False)
    if _os.environ.get('PILOT_FINJ') == '1': pad = np.pad(img[..., 3] >= 250, 1, constant_values=False)   # a translucent fin next to the body edge does not hide the outline
    up = ~pad[:-2, 1:-1]; dn = ~pad[2:, 1:-1]; lf = ~pad[1:-1, :-2]; rt = ~pad[1:-1, 2:]
    edge = op & (kind == 2) & (up | dn | lf | rt)
    out = img.copy()
    for j, i in zip(*np.where(edge)):
        jj, ii = j, i
        if up[j, i] and not dn[j, i] and j + 1 < H: jj = j + 1
        elif dn[j, i] and not up[j, i] and j - 1 >= 0: jj = j - 1
        elif lf[j, i] and not rt[j, i] and i + 1 < W: ii = i + 1
        elif rt[j, i] and not lf[j, i] and i - 1 >= 0: ii = i - 1
        src = img[jj, ii] if img[jj, ii, 3] > 0 else img[j, i]
        side = lf[j, i] or rt[j, i]
        ot, ots, osd, obs, ob, orow = STYLE['outline']
        if up[j, i] and not dn[j, i]: k = ots if side else ot
        elif dn[j, i] and not up[j, i]: k = obs if side else ob
        else: k = osd
        out[j, i] = rgba(pal.shade(pal.r2h(src[:3] / 255), k=k))
        if PILOT['olc'] != 1.0 or _os.environ.get('PILOT_WATER'):
            _c = pal.lab(pal.r2h(out[j, i, :3] / 255)); _c[1:] *= PILOT['olc']
            if _os.environ.get('PILOT_WATER'):   # outline hue kept out of the discord band around the water hue (v3 steer rule)
                _w = float(_os.environ['PILOT_WATER']); _C = math.hypot(_c[1], _c[2]); _h = math.degrees(math.atan2(_c[2], _c[1])); _d = (_h - _w + 180) % 360 - 180
                if _C >= 0.02 and 45 < abs(_d) < 110:
                    _t = _w + math.copysign(42.0 if abs(_d) < 77.5 else 113.0, _d); _c[1], _c[2] = _C * math.cos(math.radians(_t)), _C * math.sin(math.radians(_t))
                for _k in range(8):   # 8-bit rounding / gamut clipping can push a dark tone back into the band: give up chroma until it stays out
                    _q = pal.lab(pal.hexl(_c)); _qC = math.hypot(_q[1], _q[2]); _qd = (math.degrees(math.atan2(_q[2], _q[1])) - _w + 180) % 360 - 180
                    if _qC < 0.025 or not (45 < abs(_qd) < 110): break
                    _c[1:] *= 0.85
            out[j, i, :3] = rgba(pal.hexl(_c))[:3]
        _fl = PILOT['floor']
        if _os.environ.get('PILOT_FLOORREL') and getattr(F, 'pilot_bodyL', None) is not None: _fl = max(0.15, float(_os.environ['PILOT_FLOORREL']) * F.pilot_bodyL)
        if _fl and dn[j, i] and not up[j, i]:
            _c = pal.lab(pal.r2h(out[j, i, :3] / 255))
            if _c[0] < _fl: _c[0] = _fl; out[j, i, :3] = rgba(pal.hexl(_c))[:3]
        if dn[j, i] and not up[j, i] and j - 1 >= 0 and kind[j - 1, i] == 2 and not edge[j - 1, i] and T[j - 1, i] > 0.55:
            out[j - 1, i] = rgba(pal.shade(pal.r2h(img[j - 1, i, :3] / 255), k=orow))
    # fin rims: fin pixels touching transparency
    _pp = np.pad(op, 1, constant_values=False); fe = op & ((kind == 1) | (kind == 3)) & (~_pp[:-2, 1:-1] | ~_pp[2:, 1:-1] | ~_pp[1:-1, :-2] | ~_pp[1:-1, 2:])
    for j, i in zip(*np.where(fe)):
        if STYLE['rim'] != 'light': out[j, i, :3] = out[j, i, :3] * 0.95   # (v2 draws the fin margin per fin, above)
    img = out
    _dkc = float(_os.environ.get('PILOT_DKC', '1'))
    if _dkc < 1.0:   # body darks (shadow tones, dark marks, outline) give up chroma toward the reference dark/mid ratio
        bm = img[..., 3] >= 250; cols = {}
        for j, i in zip(*np.where(bm)):
            key = tuple(int(v) for v in img[j, i, :3])
            if key in GLINTS: continue
            cols.setdefault(key, []).append((j, i))
        if cols:
            Ls = {k_: pal.lab(pal.r2h(np.array(k_) / 255)) for k_ in cols}
            _all = np.array([Ls[k_][0] for k_, v in cols.items() for _ in v]); q40, q10 = np.percentile(_all, 55), np.percentile(_all, 15)
            for k_, pts in cols.items():
                c = Ls[k_].copy(); w = min(1.0, max(0.0, (q40 - c[0]) / max(q40 - q10, 0.05)))
                if w <= 0: continue
                c[1:] *= 1 - (1 - _dkc) * w; nc = rgba(pal.hexl(c))[:3]
                for j, i in pts: img[j, i, :3] = nc
    # eye (screen space)
    if F.eye:
        eu, et, size, ring = F.eye; ex, ey = eu * B.L - F.piv[0], B.yat(eu, et) - F.piv[1]
        xr = ex * math.cos(th) - ey * math.sin(th); yr = ex * math.sin(th) + ey * math.cos(th)
        sx = cx + facing * xr; sy = cy - yr
        # BW eye: warm highlight pixel on top of a dark pupil, coloured iris pixels on the back side,
        # and a dark socket pixel under the pupil (a darker shade of the body colour there).
        x0 = int(math.floor(sx)); y0 = int(math.floor(sy + 0.5)); bk = -facing
        def put(yy, xx, c):
            if 0 <= yy < H and 0 <= xx < W and img[yy, xx, 3] > 0: img[yy, xx] = c
        sock = rgba(pal.shade(pal.r2h(img[min(H - 1, y0 + 1), x0, :3] / 255), k=0.45)) if 0 <= y0 + 1 < H and 0 <= x0 < W else None
        put(y0, x0, rgba(PILOT['pupil'])); put(y0 - 1, x0, rgba(_os.environ.get('PILOT_CATCH', '#fff0c4')))
        put(y0, x0 + bk, rgba(ring))
        if size >= 2: put(y0 - 1, x0 + bk, rgba(pal.mix(ring, '#000000', 0.15)))
        if sock is not None: put(y0 + 1, x0, sock)
        if size >= 3:
            put(y0 + 1, x0 + bk, rgba(pal.mix(ring, '#000000', 0.3))); put(y0, x0 + facing, rgba(PILOT['pupil']))
    return np.clip(np.round(img), 0, 255).astype(np.uint8)
def extents(F, rows, phases=(-1, 0, 1)):
    B = F.B; pts = list(B.outline_pts())
    for f in F.fins:
        for ph in phases:
            P = _flut(f, ph); pts += [tuple(p) for p in P]
    pts = np.array(pts); F.piv = ((pts[:, 0].min() + pts[:, 0].max()) / 2, (pts[:, 1].min() + pts[:, 1].max()) / 2); pts = pts - np.array(F.piv); out = []
    for (_, facing, td) in rows:
        th = math.radians(F.tilt) * td
        xr = pts[:, 0] * math.cos(th) - pts[:, 1] * math.sin(th); yr = pts[:, 0] * math.sin(th) + pts[:, 1] * math.cos(th)
        out.append(np.stack([facing * xr, -yr], 1))
    return np.concatenate(out)
def sheet(F, safety=1):
    rows = CRAWL_ROWS if F.crawl else (BACKWARD_ROWS if getattr(F, 'backward', False) else ROWS)
    if getattr(F, 'gait', None) and not F.crawl:
        for f in F.fins: f['gait'] = F.gait
    if F.crawl: F.tilt = 0
    E = extents(F, rows); x0, y0 = E.min(0); x1, y1 = E.max(0)
    W = int(math.ceil(x1 - x0)) + 2 * safety + 1; H = int(math.ceil(y1 - y0)) + 2 * safety + 1
    W += W % 2; H += H % 2
    cx = W / 2 - (x0 + x1) / 2; cy = H / 2 - (y0 + y1) / 2
    frames = []
    for (name, facing, td) in rows:
        idle = name.startswith('idle')
        seq = [0, 1, 0, -1]
        fr = []
        for ph in seq:
            fr.append(render(F, facing, td, ph, cx, cy, W, H, idle=idle))
        frames.append(fr)
    if STYLE.get('merge_dE') and not _os.environ.get('PILOT_NOMERGE'): _merge_colours(frames, STYLE['merge_dE'])
    if STYLE.get('despeck'):   # crumbs of fewer than n pixels cut loose from the animal by tilt or flutter
        from scipy import ndimage
        floor_row = max(np.where(r[0][..., 3].any(1))[0].max() for r in frames) if F.crawl else 10 ** 6
        for r in frames:
            for f in r:
                lab, k = ndimage.label(f[..., 3] > 0, structure=np.ones((3, 3)))
                for i in range(1, k + 1):
                    mi = lab == i
                    if mi.sum() < STYLE['despeck'] and np.where(mi.any(1))[0].max() < floor_row: f[mi] = 0   # a crawler's crumbs on the floor row stay
    if F.crawl:
        low = max(np.where(r[0][..., 3].any(1))[0].max() for r in frames)   # rest pose sits on the floor row; flutter below it is clipped
        sh = H - 1 - low
        def drop(f):
            g = np.roll(f, sh, 0)
            if sh < 0: g[sh:] = 0
            if sh > 0: g[:sh] = 0   # flutter that dipped below the floor row must not wrap round to the top
            return g
        frames = [[drop(f) for f in r] for r in frames]
        top = min(np.where(f[..., 3].any(1))[0].min() for r in frames for f in r)
        if top > safety + 1:
            cut = top - safety; H2 = H - cut; H2 += H2 % 2; cut = H - H2
            frames = [[f[cut:] for f in r] for r in frames]; H = H2
    sheet = np.concatenate([np.concatenate(r, 1) for r in frames], 0)
    return sheet, W, H, [r[0] for r in rows]
