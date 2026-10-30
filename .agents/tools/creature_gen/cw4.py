"""Cold Water batch 4 - invertebrates on the floor: hermit crab, whelk, edible crab, lobster, northern shrimp, squat lobster, sea cucumber;
species names only."""
import math, numpy as np
from parts import Crawler, part, line, ell, cap
from fs3 import _crayfish
import pal; pal.use('cw')
from pal import ramp
ALL = ['common_hermit_crab', 'common_whelk', 'edible_crab', 'european_lobster', 'northern_shrimp', 'squat_lobster', 'orange_footed_sea_cucumber']
PH = [0, 1, 0, -1]; EYE = '#0c0e0c'; HI = '#fff0c4'
def _scaled(C, s):
    """enlarge a part-built crawler by s (every mask, mark and eye is sampled in the unscaled space)"""
    fr = C.frame
    def frame(f, idle):
        P, E = fr(f, idle)
        for p in P:
            p['fn'] = (lambda X, Y, fn=p['fn']: fn(X / s, Y / s)); p['marks'] = [(lambda X, Y, mf=mf: mf(X / s, Y / s), c) for mf, c in p['marks']]
        return P, [(x * s, y * s, c) for x, y, c in E]
    C.frame = frame; C.CW = int(C.CW * s) + 2; C.CH = int(C.CH * s) + 2; return C
def _spiral_shell(cx, cy, r0, n, dx, dy, shrink, rot, rp, marks, z=3.0, name='sh'):
    out = []
    for i in range(n):
        t = i / max(1, n - 1); r = r0 * (1 - shrink * t)
        out.append(part(ell(cx + dx * t, cy + dy * t, r, r * 0.74, rot), rp, z=z - i * 0.1, name='%s%d' % (name, i), lightc=(0.3, 0.4, 1.5, 1.3), marks=marks))
    return out
def common_hermit_crab():
    # Pagurus bernhardus: a red-orange hermit crab living in a borrowed pale whelk shell, the big right claw and the smaller left claw
    # rough and granular, red-and-white banded walking legs and eyes on long stalks poking out of the shell mouth
    shell = ramp('#b8aa90'); crab = ramp('#c8603a', sig=True); band = '#ecd8c0'
    sm = [(lambda X, Y: np.abs(((Y + 0.6 * X) % 2.2) - 1.1) < 0.35, -1)]
    def frame(f, idle):
        ph = PH[f] * (0 if idle else 1); P = _spiral_shell(13.0, 13.6, 6.4, 5, -9.0, -7.4, 0.8, -32, shell, sm)
        P.append(part(ell(18.8, 15.6, 2.4, 3.0, 20), ramp('#3a2a20'), z=3.4, shade='flat', tone=3, outline=False, name='ap'))
        for k, x in enumerate((20.0, 22.0)):
            up = 0.9 if (ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            pts = [(x, 16.2), (x + 2.4, 17.6 - up), (x + 3.0 + 0.6 * up, 21.6 - up)]
            P.append(part(cap(pts, [0.8, 0.7, 0.5]), crab, z=4, tone=3, name='leg%d' % k, marks=[(lambda X, Y: np.abs(Y - 19.0) < 0.5, band)]))
        P.append(part(cap([(19.6, 15.0), (23.4, 15.6)], 1.1), crab, z=4.2, name='arm', shade='flat', tone=3, outline=False))
        P.append(part(ell(26.0, 15.6, 3.0, 2.0, -8), crab, z=4.3, name='claw', marks=[(lambda X, Y: (np.round(X) + np.round(Y)) % 2 == 0, -1)]))
        o = 0.5 * ph
        P.append(part([(28.2, 15.0), (30.4, 15.2 - o), (28.4, 15.8)], crab, z=4.4, shade='flat', tone=2, outline=False, name='claw'))
        P.append(part(ell(24.6, 18.2, 1.8, 1.2, -8), crab, z=3.9, tone=2, name='claw2'))
        P.append(line([(20.4, 13.6), (21.6, 10.8)], crab[2], z=4.5)); P.append(line([(19.6, 13.8), (20.4, 11.2)], crab[1], z=3.5))
        P.append(line([(21.0, 13.8), (26.0, 9.6), (29.4, 9.4 + o)], '#c87a5a', z=4.5))
        return P, [(21.8, 10.4, EYE), (20.6, 10.8, EYE)]
    return Crawler('common_hermit_crab', frame, 34, 26)
def common_whelk():
    # Buccinum undatum: big spiral whelk shell with wavy axial ribs crossed by fine spiral ridges, creamy brown, a wide aperture and a
    # short siphonal canal; a pale grey foot speckled dark, a long siphon tube held up in front and two tentacles; the shell stays fixed
    # while the foot glides
    shell = ramp('#a8946c'); foot = ramp('#c8c4b4')
    rib = [(lambda X, Y: np.abs(((X + 0.4 * Y) % 2.4) - 1.2) < 0.4, -1), (lambda X, Y: (np.round(Y) % 2 == 0) & ((np.round(X) + np.round(Y)) % 3 == 0), 1)]
    def frame(f, idle):
        ext = 0.8 if idle else [0.8, 1.6, 0.8, 0][f]; sw = 0.5 * PH[f]
        P = [part(cap([(6.0, 18.6), (21.0 + ext, 18.4), (24.6 + ext, 18.8)], [1.9, 1.9, 1.2]), foot, z=1, name='foot',
                  marks=[(lambda X, Y: (np.round(X) * 3 + np.round(Y)) % 5 == 0, '#4a4640')])]
        P += _spiral_shell(13.6, 13.0, 6.2, 6, -9.4, -8.4, 0.82, -36, shell, rib)
        P.append(part(ell(18.4, 15.2, 2.0, 2.8, 20), ramp('#e8d8b8'), z=3.5, shade='flat', tone=3, name='ap'))
        P.append(part(cap([(19.6, 13.0), (22.4, 9.6 + sw), (24.2, 8.4 + sw)], [0.9, 0.8, 0.7]), foot, z=3.6, tone=2, name='siphon'))
        P.append(line([(22.8 + ext, 17.4), (25.6 + ext, 15.0 - sw)], '#a8a494', z=4)); P.append(line([(23.4 + ext, 17.8), (26.6 + ext, 17.0 + sw)], '#a8a494', z=4))
        return P, [(23.2 + ext, 17.2, '#141210')]
    return Crawler('common_whelk', frame, 32, 26, prefix='crawl_')
def edible_crab():
    # Cancer pagurus seen from the front, walking sideways: a broad oval reddish-brown carapace with a crimped pie-crust edge, heavy
    # claws with black fingertips, hairy reddish walking legs
    shell = ramp('#a8583a'); legr = ramp('#b0603e'); clawr = ramp('#b8644a'); tip = ramp('#141210'); cx = 22.0
    crust = [(lambda X, Y: (Y < 10.6) & ((np.round(X) % 2) == 0), -1), (lambda X, Y: (np.abs(X - cx) > 8.6) & ((np.round(Y) % 2) == 0), -1)]
    def frame(f, idle):
        P = []
        for side in (-1, 1):
            for k in range(4):
                up = 1.2 if (not idle and (k + f + (side > 0)) % 2 == 0 and f % 2 == 1) else 0.0
                hip = (cx + side * (7.4 - k * 0.3), 12.0 + k * 0.8); knee = (cx + side * (12.0 + k * 0.7), 10.4 + k * 1.3 - up * 0.5)
                foot = (cx + side * (13.6 + k * 1.0), 21.6 - up)
                P.append(part(cap([hip, knee], 0.7), legr, z=1 + k * 0.01, shade='flat', tone=2 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
                P.append(part(cap([knee, foot], 0.55), legr, z=1 + k * 0.01, shade='flat', tone=1 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
        P.append(part(ell(cx, 12.4, 11.0, 4.6), shell, z=3, name='shell', marks=crust, lightc=(0.3, 0.4, 1.4, 1.2)))
        for side in (-1, 1):
            P.append(part(cap([(cx + side * 6.0, 15.0), (cx + side * 7.0, 16.6)], 1.4), clawr, z=4, name='arm%d' % side))
            P.append(part(ell(cx + side * 5.0, 17.8, 4.0, 2.6, -side * 10), clawr, z=4.1, name='claw%d' % side))
            o = 0.6 * PH[f] if not idle else 0
            P.append(part([(cx + side * 1.8, 17.0), (cx + side * -0.4, 17.4 - o), (cx + side * 1.6, 18.0)], tip, z=4.2, shade='flat', tone=3, outline=False, name='tip'))
            P.append(part([(cx + side * 1.8, 18.6), (cx + side * 0.0, 19.2 + o), (cx + side * 2.0, 19.4)], tip, z=4.2, shade='flat', tone=3, outline=False, name='tip'))
        return P, [(cx - 1.6, 8.6, EYE), (cx + 1.6, 8.6, EYE), (cx - 1.6, 7.8, HI), (cx + 1.6, 7.8, HI)]
    return Crawler('edible_crab', frame, 44, 26)
def european_lobster():
    # Homarus gammarus: big blue-black lobster speckled with pale yellow-white flecks, a heavy crusher claw and a slimmer cutter claw,
    # long reddish antennae, a segmented tail ending in a broad fan
    rng = np.random.RandomState(41); sp = list(zip(rng.uniform(3, 30, 14), rng.uniform(13.6, 18.0, 14)))
    fleck = lambda: [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.3, '#d8cc90') for p in sp]
    C = _crayfish('european_lobster', '#283a58', '#34486a', '#2a3e60', '#3a2e3a', fleck, claw_w=1.7, rostrum=3.0,
                  claw_marks=[(lambda X, Y: (np.round(X) * 2 + np.round(Y)) % 5 == 0, '#d8cc90')])
    return _scaled(C, 1.35)
def northern_shrimp():
    # Pandalus borealis: slender pink-red shrimp, a long upcurved toothed rostrum, a humped abdomen, long red antennae, thin legs, a
    # tail fan; semi-transparent pink with deeper red bands
    body = ramp('#d0705a', sig=True); X0 = 2.0; Y0 = 3.6
    shape = [(1.0, 13.0), (2.8, 11.4), (5.6, 9.8), (9.0, 8.8), (12.6, 8.4), (16.4, 8.6), (19.6, 9.2), (22.6, 8.6), (25.6, 8.8), (27.4, 9.8), (34.0, 7.0), (28.2, 10.6),
             (27.6, 11.8), (24.6, 13.0), (20.4, 13.0), (16.0, 12.6), (12.0, 12.4), (8.4, 12.8), (5.4, 13.6), (3.0, 14.4)]
    fan = [(3.2, 12.4), (-0.6, 11.4), (-1.6, 13.4), (-0.4, 15.4), (3.0, 14.6)]
    bandm = [(lambda X, Y, x0=x0: (np.abs(X - x0 - X0 + (Y - 11) * 0.3) < 0.5), -1) for x0 in (6.4, 10.0, 13.6, 17.2)] + [(lambda X, Y: (Y > 9.6) & (Y < 10.4) & (X > 26) & (X < 31), '#e8a090')]
    teeth = [(lambda X, Y: (Y < 9.2) & (X > 29 + X0) & (np.round(X) % 2 == 0), -2)]
    def frame(f, idle):
        ph = PH[f]; sw = (0.3 if idle else 0.7) * ph; S = lambda pts: [(x + X0, y + Y0) for x, y in pts]
        P = [part(S(shape), body, z=3, name='body', marks=[(lambda X, Y, m=m: m(X, Y - Y0), c) for m, c in bandm + teeth], lightc=(0.3, 0.4, 1.5, 1.3)), part(S(fan), body, z=2.9, name='fan', tone=2)]
        for k, x in enumerate((25.4, 23.4, 21.4, 19.4, 17.4)):
            up = 0.7 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line(S([(x, 12.8), (x + 1.2, 15.4 - up), (x + 0.8 + 0.6 * up, 18.0 - up)]), body[2], z=4))
        for k, x in enumerate((7.0, 10.6, 14.2)): P.append(line(S([(x, 12.6), (x - 0.6 + 0.4 * sw * (1 if k % 2 else -1), 14.6)]), body[3], z=4))
        P.append(line(S([(27.6, 9.4), (31.0, 6.0 + sw), (38.0, 4.6 + sw), (44.0, 5.4 + sw)]), '#b84a3a', z=4))
        P.append(line(S([(27.8, 10.0), (31.4, 8.6), (34.0, 9.0 - sw)]), '#b84a3a', z=4))
        return P, [(27.0 + X0, 9.6 + Y0, EYE), (27.0 + X0, 8.8 + Y0, HI)]
    return Crawler('northern_shrimp', frame, 50, 24)
def squat_lobster():
    # Galathea strigosa: flattened squat lobster with the tail tucked under, a bright orange-red carapace crossed by electric-blue
    # stripes, long spiny arms held out in front ending in slender claws, short rostrum
    body = ramp('#c84a30', sig=True); blue = '#3a8ad8'
    stripes = [(lambda X, Y, x0=x0: (np.abs(X - x0) < 0.45), blue) for x0 in (10.0, 12.6, 15.2, 17.8, 20.4)]
    def frame(f, idle):
        ph = PH[f]; o = 0.4 * ph * (0 if idle else 1)
        P = [part([(6.0, 18.4), (7.4, 15.2), (10.0, 13.6), (16.0, 13.0), (21.0, 13.6), (23.4, 15.0), (25.6, 15.6), (23.6, 16.6), (22.0, 18.6), (14.0, 19.0)],
                  body, z=3, name='body', marks=stripes, lightc=(0.3, 0.4, 1.5, 1.3))]
        P.append(part(ell(7.4, 18.6, 2.4, 1.4), body, z=2.9, tone=2, name='tail'))
        for k, x in enumerate((20.4, 17.6, 14.8, 12.0)):
            up = 0.8 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line([(x, 18.4), (x + 1.4, 19.6 - up), (x + 2.0 + 0.6 * up, 21.6 - up)], body[2], z=4))
        for dz, dy, rp in ((0.6, -1.0, ramp(pal.mix('#c84a30', '#000000', .25))), (5, 0, body)):
            arm = [(22.4, 16.0 + dy), (27.0, 17.4 + dy), (32.0, 16.8 + dy), (36.0, 16.2 + dy)]
            P.append(part(cap(arm, 0.7), rp, z=dz, shade='flat', tone=3, outline=False, name='arm%d' % dz, marks=[(lambda X, Y: np.round(X) % 3 == 0, blue)]))
            P.append(part(cap([(36.0, 16.2 + dy), (39.4, 15.6 + dy - o)], 0.5), rp, z=dz + .1, shade='flat', tone=2, outline=False, name='arm%d' % dz))
            P.append(part(cap([(36.0, 16.6 + dy), (39.0, 16.8 + dy + o)], 0.45), rp, z=dz + .1, shade='flat', tone=1, outline=False, name='arm%d' % dz))
        P.append(line([(24.4, 14.6), (28.0, 11.6), (32.0, 11.0 + o)], '#a8402a', z=5.5))
        return P, [(23.0, 14.4, EYE), (23.0, 13.6, HI)]
    return Crawler('squat_lobster', frame, 42, 26)
def orange_footed_sea_cucumber():
    # Cucumaria frondosa: fat, warty, dark brown-purple sea cucumber with rows of orange tube feet underneath and a crown of bushy,
    # branched orange feeding tentacles spread at the front end; it creeps very slowly while the tentacles sway
    body = ramp('#5a3a32'); orange = ramp('#e07a3a', sig=True)
    warts = [(lambda X, Y: ((np.round(X) * 2 + np.round(Y) * 3) % 5 == 0), 1), (lambda X, Y: ((np.round(X) * 3 + np.round(Y)) % 7 == 0), -1)]
    def frame(f, idle):
        ext = 0.6 if idle else [0.6, 1.2, 0.6, 0][f]; sw = 0.6 * PH[f]
        P = [part(cap([(4.0, 18.4), (12.0, 17.2), (22.0 + ext, 17.0), (27.0 + ext, 17.8)], [2.4, 3.4, 3.2, 2.2]), body, z=3, name='body', marks=warts)]
        for x in np.arange(5.0, 26.0, 2.0): P.append(line([(x + ext * x / 26, 20.0), (x + ext * x / 26 + 0.2, 21.6)], orange[3], z=2.8))
        base = (28.4 + ext, 16.8)
        for k, a in enumerate((-70, -45, -20, 5, 30)):
            r = math.radians(a + 6 * sw); tip = (base[0] + 4.6 * math.cos(r), base[1] + 4.6 * math.sin(r) - 1.0)
            P.append(part(cap([base, tip], [0.6, 0.5]), orange, z=3.5, shade='flat', tone=3, outline=False, name='tent'))
            for q in (0.55, 0.9):
                m = (base[0] + (tip[0] - base[0]) * q, base[1] + (tip[1] - base[1]) * q)
                P.append(line([m, (m[0] + 0.9 * math.cos(r - 0.9), m[1] + 0.9 * math.sin(r - 0.9))], orange[4], z=3.6))
                P.append(line([m, (m[0] + 0.9 * math.cos(r + 0.9), m[1] + 0.9 * math.sin(r + 0.9))], orange[2], z=3.6))
        return P, []
    return Crawler('orange_footed_sea_cucumber', frame, 40, 26, prefix='crawl_')
SCENE = {
    'common_hermit_crab': dict(speed=6, fps=7, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 5), crowd_radius=(35, 8)),
    'common_whelk': dict(speed=2, fps=5, move_prefix='crawl_', bob_amount=0.0, move_time=(6, 10), idle_time=(2, 6), crowd_radius=(30, 8)),
    'edible_crab': dict(speed=10, fps=8, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 5), crowd_radius=(50, 8)),
    'european_lobster': dict(speed=8, fps=7, bob_amount=0.5, move_time=(1, 4), idle_time=(2, 5), crowd_radius=(75, 8)),
    'northern_shrimp': dict(speed=8, fps=9, bob_amount=0.5, move_time=(1, 3), idle_time=(1, 3), crowd_radius=(40, 8)),
    'squat_lobster': dict(speed=8, fps=8, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 5), crowd_radius=(40, 8)),
    'orange_footed_sea_cucumber': dict(speed=1.5, fps=4, move_prefix='crawl_', bob_amount=0.0, move_time=(6, 12), idle_time=(4, 10), crowd_radius=(40, 8)),
}
