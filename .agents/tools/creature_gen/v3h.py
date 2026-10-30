"""v3 design helpers shared by the species modules (Oct 2026)."""
import numpy as np
from swim import _fin
def m_hline(B, u0, u1, y, w, col):
    """straight body-space line (reads as a clean row of pixels when swimming level), y in body units from the axis."""
    def f(x, yy, uu, tt): return (uu >= u0) & (uu <= u1) & (np.abs(yy - y) <= w / 2)
    return (f, col)
def scatter(n, u0, u1, t0, t1, seed=0.0, gap=0.11):
    """irregular but even spot positions (golden-ratio sequence, minimum spacing) - reads as a natural spotting, not a grid."""
    out = []; k = 0; phi = 0.6180339887
    while len(out) < n and k < 400:
        u = u0 + (u1 - u0) * ((seed + k * phi) % 1.0); t = t0 + (t1 - t0) * ((seed * 1.7 + k * 0.7548776662) % 1.0); k += 1
        if all(abs(u - a) > gap or abs(t - b) > gap * 1.6 for a, b in out): out.append((u, t))
    return out
def fin_spots(pts, r, col):
    P = np.array(pts, float)
    def f(X, Y): return np.min([np.hypot(X - px, Y - py) for px, py in P], 0) <= r
    return (f, col)
def trail(B, side, u0, u1, h, back, col, **k):
    """pointed soft-ray lobe trailing back past the tail base (dorsal side=1 / anal side=-1)."""
    edge = B.top if side > 0 else B.bot; xs = np.linspace(u0 * B.L, u1 * B.L, 6)
    base = [(x, float(edge(x)) - side * 0.8) for x in xs]; e0 = float(edge(u0 * B.L))
    tip = (-back, e0 + side * h * 0.55); mid = (u0 * B.L - back * 0.2, e0 + side * h * 0.95)
    pts = base + [(xs[-1] - 0.5, float(edge(xs[-1])) + side * h * 0.8), mid, tip]
    w = [0] * 6 + [0.6, 0.9, 1.0]
    F_ = _fin(pts, w, [(base[2], tip), (base[4], mid)], 'dorsal' if side > 0 else 'anal', col, (185, 120), (-1, 0.25 * side), 0.8, **k)
    F_['fpos'] = np.array([i / 5 for i in range(6)][::-1] + [0.4, 0.2, 0.0]); return F_
