"""Clear Spring part-based crawler renderer (crayfish, crab, turtles, snail). Side view facing right in screen space
(y down). Each part is shaded with the same BW-style light (bright upper middle, darker toward the lower edge and the ends),
gets a selective outline against empty space and a darker contour where it overlaps a part behind it."""
import math, numpy as np
from matplotlib.path import Path
import pal
from swim import rgba
def ell(cx, cy, rx, ry, rot=0.0):
    a = np.linspace(0, 2 * np.pi, 40, endpoint=False); c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    return [(cx + rx * math.cos(t) * c - ry * math.sin(t) * s, cy + rx * math.cos(t) * s + ry * math.sin(t) * c) for t in a]
def cap(pts, r):
    """thick polyline as polygon list of circles+quads -> returns a callable mask"""
    pts = np.array(pts, float); r = np.broadcast_to(np.array(r, float), (len(pts),))
    def m(X, Y):
        out = np.zeros(X.shape, bool)
        for i in range(len(pts) - 1):
            (ax, ay), (bx, by) = pts[i], pts[i + 1]; dx, dy = bx - ax, by - ay; L2 = dx * dx + dy * dy + 1e-9
            t = np.clip(((X - ax) * dx + (Y - ay) * dy) / L2, 0, 1); d = np.hypot(X - ax - t * dx, Y - ay - t * dy)
            out |= d <= r[i] + (r[i + 1] - r[i]) * t
        return out
    return m
def part(shape, ramp, z=0, shade='dome', tone=3, outline=True, marks=(), sep=True, lightc=(0.3, 0.45, 1.6, 1.3), name='', alpha=255):
    if isinstance(shape, list): P = Path(np.array(shape)); fn = lambda X, Y: P.contains_points(np.stack([X.ravel(), Y.ravel()], 1)).reshape(X.shape)
    else: fn = shape
    return dict(fn=fn, ramp=ramp, z=z, shade=shade, tone=tone, outline=outline, marks=list(marks), sep=sep, lightc=lightc, name=name, alpha=alpha)
def line(pts, col, z=5, w=0.5):
    return dict(fn=cap(pts, w), ramp=[col] * 6, z=z, shade='flat', tone=3, outline=False, marks=[], sep=False, lightc=None, name='line')
def render(parts, W, H, eyes=(), ox=0.0, oy=0.0):
    I, J = np.meshgrid(np.arange(W) + 0.5 + ox, np.arange(H) + 0.5 + oy)
    img = np.zeros((H, W, 4)); pid = np.full((H, W), -1); zz = np.full((H, W), -1e9)
    order = sorted(range(len(parts)), key=lambda k: parts[k]['z'])
    for k in order:
        p = parts[k]; m = p['fn'](I, J)
        if not m.any(): continue
        if p['shade'] == 'flat': tone = np.full((H, W), p['tone'])
        else:
            cols = m.any(0); T = np.zeros((H, W)); U = np.zeros((H, W))
            xs = np.where(cols)[0]; x0, x1 = xs.min(), xs.max()
            for x in xs:
                ys = np.where(m[:, x])[0]; t0, t1 = ys.min(), ys.max()
                T[:, x] = (np.arange(H) - t0 + 0.5) / max(1.0, t1 - t0 + 1)
            U[:] = (np.arange(W) - x0 + 0.5) / max(1.0, x1 - x0 + 1)
            lc, kt, kb, pb = p['lightc']
            v = np.where(T < lc, 1 - kt * (np.clip(lc - T, 0, 1) / lc) ** 2, 1 - kb * (np.clip(T - lc, 0, 1) / (1 - lc)) ** pb)
            v = v - 0.35 * np.clip((0.12 - U) / 0.12, 0, 1) - 0.35 * np.clip((U - 0.88) / 0.12, 0, 1)
            tone = np.clip(np.round(1.0 + v * 3.4), 0, 5).astype(int) + (p['tone'] - 3)
            tone = np.clip(tone, 0, 5)
        col = np.zeros((H, W, 4))
        for t in range(6): col[m & (tone == t)] = rgba(p['ramp'][t])
        for (mf, mc) in p['marks']:
            mm = m & mf(I, J)
            if isinstance(mc, (int, float)):
                tt = np.clip(tone + int(mc), 0, 5)
                for t in range(6): col[mm & (tt == t)] = rgba(p['ramp'][t])
            else: col[mm] = rgba(mc)
        if p.get('alpha', 255) < 255: col[m, 3] = p['alpha']
        img[m] = col[m]; pid[m] = k; zz[m] = p['z']
    op = img[..., 3] > 0; pad = np.pad(op, 1, constant_values=False)
    up = ~pad[:-2, 1:-1]; dn = ~pad[2:, 1:-1]; lf = ~pad[1:-1, :-2]; rt = ~pad[1:-1, 2:]
    out = img.copy(); pp = np.pad(pid, 1, constant_values=-1); pz = np.pad(zz, 1, constant_values=-1e9)
    for j, i in zip(*np.where(op)):
        p = parts[pid[j, i]]
        if not p['outline']: continue
        if up[j, i] or dn[j, i] or lf[j, i] or rt[j, i]:
            jj, ii = j, i
            if up[j, i] and not dn[j, i] and j + 1 < H and op[j + 1, i]: jj = j + 1
            elif dn[j, i] and not up[j, i] and j - 1 >= 0 and op[j - 1, i]: jj = j - 1
            side = lf[j, i] or rt[j, i]
            if up[j, i] and not dn[j, i]: k = 0.58 if side else 0.64
            elif dn[j, i] and not up[j, i]: k = 0.36 if side else 0.32
            else: k = 0.48
            out[j, i] = rgba(pal.shade(pal.r2h(img[jj, ii, :3] / 255), k=k))
        elif p['sep']:
            nb = [(pp[j, i + 1], pz[j, i + 1]), (pp[j + 2, i + 1], pz[j + 2, i + 1]), (pp[j + 1, i], pz[j + 1, i]), (pp[j + 1, i + 2], pz[j + 1, i + 2])]
            if any(q >= 0 and q != pid[j, i] and qz < p['z'] and parts[q]['name'] != p['name'] for q, qz in nb):
                out[j, i] = rgba(pal.shade(pal.r2h(img[j, i, :3] / 255), k=0.62))
    for (x, y, c) in eyes:
        xi, yi = int(math.floor(x - ox)), int(math.floor(y - oy))
        if 0 <= yi < H and 0 <= xi < W: out[yi, xi] = rgba(c)
    return np.clip(np.round(out), 0, 255).astype(np.uint8)
class Crawler:
    """species supplies frame(f, idle) -> (parts, eyes) for a right-facing animal in a generous canvas (CW x CH)."""
    crawl = True
    def __init__(s, name, frame, CW, CH, prefix='walk_'):
        s.name, s.frame, s.CW, s.CH, s.prefix = name, frame, CW, CH, prefix
    def sheet(s, safety=1):
        raw = []
        for idle in (False, True):
            raw.append([(lambda r: render(r[0], s.CW, s.CH, eyes=r[1]))(s.frame(f, idle)) for f in range(4)])
        allm = np.zeros((s.CH, s.CW), bool)
        for r in raw:
            for f in r: allm |= f[..., 3] > 0
        ys, xs = np.where(allm); x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        W = x1 - x0 + 1 + 2 * safety; W += W % 2; H = y1 - y0 + 1 + safety; H += H % 2
        def crop(f):
            c = np.zeros((H, W, 4), np.uint8); sub = f[y0:y1 + 1, x0:x1 + 1]
            c[H - sub.shape[0]:, safety:safety + sub.shape[1]] = sub; return c
        R = [[crop(f) for f in raw[0]], [crop(f)[:, ::-1] for f in raw[0]], [crop(f) for f in raw[1]], [crop(f)[:, ::-1] for f in raw[1]]]
        sheet = np.concatenate([np.concatenate(r, 1) for r in R], 0)
        tags = [s.prefix + 'R', s.prefix + 'L', 'idle_R', 'idle_L']
        return sheet, W, H, tags
