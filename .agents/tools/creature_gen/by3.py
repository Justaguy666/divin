"""Bayou batch 3 - floor crawlers: alligator, turtles, crab, crawfish, grass shrimp, sirens, snake, madtom and hogchoker; defined from species names only."""
import math, numpy as np
from parts import Crawler, part, line, ell, cap
import swim
from swim import Fish, dorsal, anal, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_dash
from sp1 import bands, np_r
from sp4 import _crawlfish, _turtle
from fs3 import _sal, _crayfish, cat_fins
from recol import Recolor
import pal; pal.use('by')
from pal import ramp
ALL = ['american_alligator', 'alligator_snapping_turtle', 'common_musk_turtle', 'blue_crab', 'red_swamp_crawfish', 'mississippi_grass_shrimp',
       'lesser_siren', 'three_toed_amphiuma', 'rainbow_snake', 'tadpole_madtom', 'hogchoker']
EYE = '#0c0e0c'; HI = '#fff0c4'; PH = [0, 1, 0, -1]
def american_alligator():
    # Alligator mississippiensis: long armoured reptile walking on the bottom, olive-black back with rows of raised bony scutes and a
    # double crest along the thick tail, pale cream belly and jaw, broad rounded snout with a row of pale teeth showing, raised eyes
    # and nostrils, short sprawling legs
    body = ramp('#3e4030'); legr = ramp('#3a3c2c'); far = ramp(pal.mix('#3e4030', '#000000', .25))
    xs = np.linspace(2.0, 98.0, 97)
    def top(x):
        if x < 34: y = 17.2 - 4.6 * ((x - 2) / 32) ** 0.85
        elif x < 70: y = 12.6 - 2.2 * math.sin((x - 34) / 36 * math.pi)
        elif x < 80: y = 12.6 - 0.7 * math.sin((x - 70) / 10 * math.pi)
        else: y = 12.6 + 2.2 * ((x - 80) / 18) ** 1.2
        return y - (0.7 if (int(x) % 3 == 0 and 8 < x < 72) else 0.0)
    def bot(x):
        if x < 34: return 18.4 + 1.0 * (x - 2) / 32
        if x < 70: return 19.4 + 0.6 * math.sin((x - 34) / 36 * math.pi)
        return 19.4 - 1.6 * ((x - 70) / 28) ** 1.3
    def frame(f, idle):
        ph = PH[f] * (0.4 if idle else 1.0)
        sw = lambda x: 0.8 * ph * max(0.0, (30 - x) / 28) ** 1.5
        poly = [(x, top(x) + sw(x)) for x in xs] + [(x, bot(x) + sw(x)) for x in xs[::-1]]
        marks = [(lambda X, Y: (Y > 18.6) & (X > 34) & (X < 72), '#b8b092'), (lambda X, Y: (X > 76) & (Y > 17.2), '#b0a888'),
                 (lambda X, Y: (X > 76) & (np.abs(Y - 16.7) < 0.45), '#1a1a12'), (lambda X, Y: (X > 78) & (X < 95) & (np.abs(Y - 17.3) < 0.4) & (np.round(X) % 2 == 0), '#e8e0c8'),
                 (lambda X, Y: (np.round(X) % 3 == 0) & (X > 8) & (X < 70) & (Y < 14.4), -1), (lambda X, Y: (np.round(X) % 4 == 0) & (X > 34) & (X < 70) & (np.abs(Y - 16.2) < 0.5), -1), (lambda X, Y: (X < 32) & ((np.round(X) // 3) % 2 == 0) & (Y < 17.6), 1)]
        P = [part(poly, body, z=3, name='body', marks=marks, lightc=(0.3, 0.4, 1.5, 1.3))]
        P.append(part(ell(80.6, 11.6, 2.0, 1.3), body, z=3.2, name='eyebump', tone=4))
        P.append(part(ell(96.2, 14.6, 1.4, 1.0), body, z=3.2, name='nose', tone=4))
        for k, (hx, near) in enumerate(((64.0, True), (40.0, True), (62.0, False), (42.0, False))):
            lift = 1.0 if (not idle and PH[f] != 0 and (k % 2 == 0) == (PH[f] > 0)) else 0.0; fw = 0.9 * PH[f] * (1 if k % 2 == 0 else -1) * (0 if idle else 1)
            hip = (hx, 18.8); knee = (hx + 1.8 + fw * .5, 20.2 - lift * .6); foot = (hx + 2.8 + fw, 21.6 - lift)
            P.append(part(cap([hip, knee, foot], [2.0, 1.5, 1.2]), legr if near else far, z=4 if near else 1, tone=3 if near else 2, name='leg%d' % k))
            for dx in (-0.8, 0.4, 1.6): P.append(line([foot, (foot[0] + dx + 0.6, foot[1] + 0.4)], (legr if near else far)[1], z=4.1 if near else 1.1))
        return P, [(81.0, 11.2, '#c8a040'), (81.6, 11.2, EYE)]
    return Crawler('american_alligator', frame, 104, 26)
def _legs4(xf, xr, base=15.4):
    return [((xf, base), (xf + 1.8, 18.4), (xf + 2.6, 21.6), True), ((xr, base), (xr - 1.0, 18.4), (xr - 1.4, 21.6), True),
            ((xf - 1.4, base - 0.2), (xf - 0.4, 18.2), (xf + 0.2, 21.6), False), ((xr + 1.4, base - 0.2), (xr + 0.8, 18.2), (xr + 0.6, 21.6), False)]
def alligator_snapping_turtle():
    # Macrochelys temminckii: massive turtle whose carapace carries three rows of tall spiky keels (a jagged, dinosaur-like back),
    # dark brown-grey often greened with algae, a huge head with a sharply hooked beak, small eyes ringed with a star pattern, thick
    # legs and a long tail edged with spiky scales
    top = [(7.0, 15.0)]
    for x in np.linspace(7.4, 34.6, 34):
        h = 8.0 * max(0, 1 - ((x - 21.0) / 14.0) ** 2) ** 0.5; spike = 1.2 if (int(x * 0.9) % 2 == 0 and 9 < x < 33) else 0.0
        top.append((x, 15.0 - h - spike))
    top.append((35.0, 15.0))
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0 - (Y - 10) * 0.15) < 0.5) & (Y > 8.6), -1) for x0 in (14.4, 20.6, 26.8)] + [(lambda X, Y: np.abs(Y - 13.6) < 0.5, -1)]
    algae = [(lambda X, Y, p=p: ((X - p[0]) / 1.8) ** 2 + ((Y - p[1]) / 0.9) ** 2 < 1, '#4e5a2e') for p in ((16.0, 9.0), (25.0, 9.4), (20.0, 11.4))]
    hm = [(lambda X, Y: (Y > 14.6) & (X > 39.0), '#8a8064'), (lambda X, Y: (np.abs(Y - 13.6) < 0.45) & (X > 40.6), '#1c1a12')]
    skin = ramp('#5a5444')
    def extra(f, idle):
        sw = 0.4 * PH[f] * (0.4 if idle else 1); dy = 2.6
        tail = [(8.0, 15.0 + dy), (4.0, 16.4 + dy + sw * .5), (0.6, 17.6 + dy + sw)]
        out = [part(cap(tail, [1.6, 1.1, 0.5]), skin, z=2.1, tone=2, name='tail2')]
        out += [line([(x, 15.6 + dy - 1.4 + (8.0 - x) * 0.3 + sw * (8 - x) / 8 * .5), (x - 0.4, 15.6 + dy - 2.4 + (8.0 - x) * 0.3 + sw * (8 - x) / 8 * .5)], skin[1], z=2.2) for x in (6.6, 4.6, 2.8)]
        out.append(part([(44.4, 13.0 + dy), (46.0, 14.6 + dy), (44.0, 15.6 + dy), (43.4, 14.0 + dy)], ramp('#3a3628'), z=2.8, shade='flat', tone=3, name='beak'))
        return out
    mk = _turtle('alligator_snapping_turtle', 52, 28, top, '#4a4434', '#b0a47c', '#5a5444', (40.6, 13.6, 4.6, 3.2, -4), [(33.6, 14.6), (37.0, 14.0)],
                 _legs4(30.6, 11.8), [(8.0, 15.0), (6.0, 15.6)], seams, algae, hm, (1.8, -1.2), extra)
    return mk([(7.0, 14.8), (35.0, 14.8), (34.0, 16.6), (8.0, 16.6)])
def common_musk_turtle():
    # Sternotherus odoratus (stinkpot): small, smooth, high-domed carapace olive-brown to black, two pale yellow stripes on the side of
    # the head above and below the eye, a pointed snout with fleshy chin barbels, tiny plastron
    top = [(9.0, 15.0)] + [(x, 15.0 - 7.0 * max(0, 1 - ((x - 18.6) / 9.6) ** 2) ** 0.62) for x in np.linspace(9.2, 28.0, 21)] + [(28.2, 15.0)]
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0) < 0.5) & (Y > 9.4), -1) for x0 in (14.6, 18.8, 23.0)] + [(lambda X, Y: np.abs(Y - 13.4) < 0.5, -1)]
    rng = np.random.RandomState(71); flecks = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.35, '#1a1810') for p in zip(rng.uniform(11, 26, 7), rng.uniform(9.6, 13.0, 7))]
    hm = [(lambda X, Y: np.abs(Y - 12.6) < 0.45, '#e0d070'), (lambda X, Y: (np.abs(Y - 14.4) < 0.45) & (X > 31.4), '#e0d070')]
    legs = [((25.6, 15.4), (27.0, 18.4), (27.8, 21.6), True), ((12.0, 15.4), (11.0, 18.4), (10.6, 21.6), True),
            ((24.2, 15.2), (25.2, 18.2), (25.8, 21.6), False), ((13.4, 15.2), (12.8, 18.2), (12.6, 21.6), False)]
    extra = lambda f, idle: [line([(34.2, 17.0), (34.4, 18.2)], '#c8c090', z=2.8), line([(33.2, 17.0), (33.3, 18.0)], '#c8c090', z=2.8)]
    mk = _turtle('common_musk_turtle', 40, 26, top, '#3a3020', '#bca86c', '#4e4a3a', (32.8, 13.6, 3.0, 2.1, -6), [(28.0, 14.6), (30.6, 14.0)],
                 legs, [(9.4, 15.4), (7.4, 16.4)], seams, flecks, hm, (1.2, -0.8), extra)
    return mk([(9.0, 14.8), (28.2, 14.8), (27.4, 16.4), (10.0, 16.4)])
def blue_crab():
    # Callinectes sapidus seen from the front, walking sideways: wide olive-green carapace with a long sharp spine at each side and
    # small teeth along the front edge, eyes on short stalks, bright blue claws with red-orange fingertips, blue walking legs and a
    # rear pair of flat swimming paddles
    shell = ramp('#5e6c48'); legr = ramp('#4a72a8', sig=True); clawr = ramp('#3a68b4', sig=True); tip = ramp('#c8482a', sig=True); cx = 24.0
    carap = [(cx - 16.0, 11.0), (cx - 10.8, 9.4), (cx - 8.0, 8.6), (cx - 5.4, 8.0), (cx - 2.6, 7.8), (cx, 7.6), (cx + 2.6, 7.8), (cx + 5.4, 8.0), (cx + 8.0, 8.6), (cx + 10.8, 9.4),
             (cx + 16.0, 11.0), (cx + 10.4, 12.0), (cx + 7.0, 14.0), (cx + 3.0, 15.0), (cx - 3.0, 15.0), (cx - 7.0, 14.0), (cx - 10.4, 12.0)]
    teeth = [(lambda X, Y: (Y < 9.4) & ((np.round(X) % 2) == 0) & (np.abs(X - cx) > 5), -1)]
    def frame(f, idle):
        P = []
        for side in (-1, 1):
            for k in range(3):
                up = 1.2 if (not idle and (k + f + (side > 0)) % 2 == 0 and f % 2 == 1) else 0.0
                hip = (cx + side * (6.6 - k * 0.4), 12.6 + k * 0.7); knee = (cx + side * (11.0 + k * 0.8), 11.6 + k * 1.2 - up * 0.5)
                foot = (cx + side * (13.0 + k * 1.1), 21.6 - up)
                P.append(part(cap([hip, knee], 0.6), legr, z=1 + k * 0.01, shade='flat', tone=2 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
                P.append(part(cap([knee, foot], 0.5), legr, z=1 + k * 0.01, shade='flat', tone=1 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
            pa = 0.5 * PH[f] * (0.4 if idle else 1)
            P.append(part(cap([(cx + side * 5.0, 14.4), (cx + side * 9.4, 13.4 - pa)], 0.6), legr, z=0.9, shade='flat', tone=2, outline=False, name='pad%d' % side))
            P.append(part(ell(cx + side * 11.0, 12.8 - pa, 1.8, 1.0, side * 20), legr, z=0.95, tone=3, name='pad%d' % side))
        P.append(part(carap, shell, z=3, name='shell', marks=teeth + [(lambda X, Y: (np.abs(X - cx) < 3.0) & (Y > 12.2), -1)], lightc=(0.3, 0.4, 1.4, 1.2)))
        for side in (-1, 1):
            P.append(part(cap([(cx + side * 2.0, 8.2), (cx + side * 2.6, 6.6)], 0.6), shell, z=2.5, shade='flat', tone=3, name='stalk'))
            P.append(part(cap([(cx + side * 6.0, 13.6), (cx + side * 7.4, 15.8)], 1.2), clawr, z=4, name='arm%d' % side))
            P.append(part(ell(cx + side * 5.4, 17.0, 3.8, 2.2, -side * 12), clawr, z=4.1, name='claw%d' % side))
            o = 0.6 * PH[f] if not idle else 0
            P.append(part([(cx + side * 2.0, 16.2), (cx + side * -0.4, 16.6 - o), (cx + side * 1.8, 17.2)], tip, z=4.2, shade='flat', tone=3, outline=False, name='tip'))
            P.append(part([(cx + side * 2.0, 17.8), (cx + side * 0.0, 18.4 + o), (cx + side * 2.2, 18.6)], tip, z=4.2, shade='flat', tone=2, outline=False, name='tip'))
        return P, [(cx - 2.8, 6.0, EYE), (cx + 2.8, 6.0, EYE), (cx - 2.8, 5.0, HI), (cx + 2.8, 5.0, HI)]
    return Crawler('blue_crab', frame, 48, 26)
def red_swamp_crawfish():
    # Procambarus clarkii: dark blood-red crawfish with a black wedge stripe along the top of the abdomen, long narrow claws covered in
    # raised bright red bumps, a pointed rostrum
    wedge = lambda: [(lambda X, Y: (Y < 15.0) & (X < 22) & (X > 2), '#1e1410')]
    bumps = [(lambda X, Y: ((np.round(X) + np.round(Y)) % 2 == 0), '#e04a36')]
    return _crayfish('red_swamp_crawfish', '#86281c', '#94321e', '#8c2a1c', '#c03a28', wedge, claw_w=1.0, rostrum=4.0, claw_marks=bumps)
class _Glass(Crawler):
    """see-through body: every pixel but the eye gets partial alpha after rendering (outline pixels keep a little more cover)."""
    def sheet(s, safety=1):
        sh, W, H, tags = Crawler.sheet(s, safety); a = sh[..., 3] > 0
        L = (sh[..., :3].astype(float) / 255) @ np.array([.3, .59, .11]); eye = a & (L < 0.08)
        sh[a & ~eye, 3] = np.where(L[a & ~eye] < 0.45, 200, 140).astype(np.uint8)
        return sh, W, H, tags
def mississippi_grass_shrimp():
    # Palaemonetes kadiakensis: small clear shrimp, nearly invisible apart from faint brown speckles and stripes, a long upturned toothed
    # rostrum, black eyes on short stalks, long whip antennae, thin legs, small first claws, a tail fan
    body = ramp('#c4ccb4'); X0 = 2.0
    shape = [(1.0, 10.6), (2.6, 9.0), (5.4, 7.8), (8.6, 7.2), (12.0, 7.2), (15.4, 7.6), (18.6, 7.0), (21.6, 7.2), (23.6, 8.0), (28.8, 6.0), (24.2, 8.8), (23.8, 10.0),
             (21.0, 11.0), (17.0, 11.2), (13.0, 10.8), (9.4, 10.6), (6.4, 11.0), (4.0, 11.8), (2.2, 12.2)]
    fan = [(2.6, 10.0), (-0.4, 9.0), (-1.4, 10.8), (-0.2, 12.6), (2.4, 12.0)]
    mk = [(lambda X, Y: (np.abs(X - x0 - X0) < 0.45) & (Y < 10.8), '#a07858') for x0 in (6.0, 9.4, 12.8, 16.2)] + [(lambda X, Y: (np.abs(Y - 9.2) < 0.45) & (X > 6) & (X < 20), '#6a5848')]
    def frame(f, idle):
        ph = PH[f]; sw = (0.3 if idle else 0.7) * ph; S = lambda pts: [(x + X0, y) for x, y in pts]
        P = [part(S(shape), body, z=3, name='body', marks=mk), part(S(fan), body, z=2.9, name='fan', tone=2)]
        for k, x in enumerate((21.0, 19.4, 17.8, 16.2)):
            up = 0.6 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line(S([(x, 10.8), (x + 1.0, 12.6 - up), (x + 0.6 + 0.6 * up, 14.4 - up)]), body[1], z=4))
        P.append(line(S([(22.4, 10.4), (25.4, 11.6), (27.6, 10.8 - sw * .5)]), body[1], z=4))
        P.append(line(S([(23.6, 8.0), (27.0, 5.2 + sw), (31.0, 4.6 + sw), (34.0, 5.2 + sw)]), '#8a8c78', z=4))
        P.append(line(S([(23.6, 8.4), (26.6, 7.4), (28.6, 7.8 - sw)]), '#8a8c78', z=4))
        return P, [(23.0 + X0, 8.0, EYE)]
    return _Glass('mississippi_grass_shrimp', frame, 40, 18)
def lesser_siren():
    # Siren intermedia: the existing drawing is kept (by request) and re-mapped onto the bayou ramp with the BW outline rule; the
    # pink-red external gill tufts stay a signature colour
    r = Recolor('old_by/by_lesser_siren_crawl_*_4f.png', '#3e4034', sig=[(320, 40, 0.04, '#a8584a')]); r.pad = (1, 0); return r
def three_toed_amphiuma():
    # Amphiuma tridactylum: the existing drawing is kept (by request) and re-mapped onto the bayou ramp with the BW outline rule
    r = Recolor('old_by/by_three_toed_amphiuma_crawl_*_4f.png', '#4a4030'); r.pad = (1, 0); return r
def rainbow_snake():
    # Farancia erytrogramma: glossy iridescent blue-black snake with three narrow red stripes running along the back and sides, a red
    # and yellow belly with rows of black spots, small head with a pointed snout, short tail with a spine-like tip
    body = ramp('#1e2430'); red = '#c8382a'
    def frame(f, idle):
        ph = PH[f] * (0.4 if idle else 1.0); xs = np.linspace(2.0, 60.0, 39)
        ys = [12.0 - (1.6 * math.sin(2 * math.pi * (x - 6.0 * ph * 0.3) / 24.0) + 0.4) * (0.35 + 0.65 * x / 60.0) for x in xs]
        r = [0.5 + 2.1 * math.sin(math.pi * min(1.0, (x - 2.0) / 52.0)) ** 0.5 if x < 54 else 2.5 - 0.08 * (x - 54) for x in xs]
        sh = 14.4 - max(y + rr for y, rr in zip(ys, r)); ys = [y + sh for y in ys]
        yc = lambda X: np.interp(X, xs, ys)
        mk = [(lambda X, Y: np.abs(Y - yc(X) + 0.5) < 0.45, red), (lambda X, Y: (Y > yc(X) + 1.5) & (X < 56), '#c8502a'), (lambda X, Y: (Y > yc(X) + 1.5) & (np.round(X) % 3 == 0), '#141414')]
        P = [part(cap(list(zip(xs, ys)), r), body, z=3, name='body', marks=mk, lightc=(0.25, 0.5, 1.4, 1.2))]
        hy = ys[-1] - 0.2
        P.append(part(ell(62.4, hy, 3.0, 1.8, -4), body, z=3.2, name='head', marks=[(lambda X, Y: Y > hy + 0.9, '#d8a04a')]))
        return P, [(63.6, hy - 1.0, EYE), (63.6, hy - 1.8, '#8a9ab8')]
    return Crawler('rainbow_snake', frame, 70, 18)
def tadpole_madtom():
    # Noturus gyrinus: tiny tadpole-shaped catfish, a plump head tapering to a thin tail, plain yellow-brown to grey with a thin dark
    # line along the side, the adipose fin joined to the rounded tail in one long fold, short barbels
    P = [(0, .3, -.3), (.1, .44, -.44), (.3, .7, -.74), (.55, .92, -.96), (.75, 1, -1), (.88, .88, -.92), (.96, .58, -.68), (1, .24, -.44)]
    F = Fish('tadpole_madtom', 22, 8.4, P, bands('#5e5034', '#a4925e', '#ccbe94'), eye=(0.87, 0.32, 1, '#a08860'))
    B = F.B
    F.marks += [m_stripe(B, .06, .82, .5, .7, '#3a3020')]
    F.fins += cat_fins(B, '#8c7c52', barb='#c8b890'); F.mouth = (.62, 1.0); return _crawlfish(F)   # v1 barbel colour (cat_fins default became a v3 family tone)
def hogchoker():
    # Trinectes maculatus: small, almost round sole lying on the mud, eyed side brown crossed by seven or eight thin dark bars, small
    # eyes close together near the top of the head, no pectoral fins, dorsal and anal fringes running round the body and rippling
    P = [(0, .3, -.3), (.08, .56, -.56), (.25, .9, -.9), (.5, 1, -1), (.72, .94, -.94), (.86, .76, -.7), (.95, .48, -.38), (1, .18, -.06)]
    F = Fish('hogchoker', 24, 15, P, bands('#5a4a30', '#7e6c48', '#86744e', b1=(0.3, 0.3), b2=(0.7, 0.7)), eye=(0.86, 0.2, 1, '#c8b070'))
    F.lightc = (0.5, 0.1, 0.35, 1.6); F.tspan = 2.2
    B = F.B; rng = np.random.RandomState(91)
    F.marks += [m_bar(B, u, .7, .04, .96, '#3a2e1c') for u in np_r(.1, .82, 8)] + [m_spot(B, u, t, .9, -1) for u, t in zip(rng.uniform(.1, .8, 10), rng.uniform(.2, .8, 10))] + [m_spot(B, .9, .12, .6, '#2a2014'), m_spot(B, .91, .1, .4, '#f0e8c8')]
    spots = [(lambda X, Y: (np.round(X * .7) + np.round(Y * .7)) % 4 == 0, '#2a2014')]
    df = dorsal(B, .04, .92, 2.6, 'flat', col='#9a8660', lean=0.0, n=30, amp=0.9); df['wave'] = 3.0; df['band'] = spots
    af = anal(B, .04, .8, 2.6, 'flat', col='#9a8660', lean=0.0, n=26, amp=0.9); af['wave'] = 2.5; af['band'] = spots
    F.fins += [caudal(B, 'round', 4.4, col='#5e5034'), df, af]
    F.mouth = (.5, 1.0); F = _crawlfish(F)
    def sheet(F=F):
        from scipy import ndimage
        sh, W, H, tags = swim.sheet(F)
        for r in range(sh.shape[0] // H):
            for c in range(4):
                fr = sh[r * H:(r + 1) * H, c * W:(c + 1) * W]; lab, n = ndimage.label(fr[..., 3] > 0, structure=np.ones((3, 3)))
                for k in range(1, n + 1):
                    if (lab == k).sum() < 6: fr[lab == k] = 0   # fringe-crest crumbs the ripple leaves floating above the fin
        return sh, W, H, tags
    F.sheet = sheet; return F
SCENE = {
    'american_alligator': dict(speed=6, fps=5, bob_amount=0.0, move_time=(2, 5), idle_time=(4, 10), crowd_radius=(130, 8)),
    'alligator_snapping_turtle': dict(speed=4, fps=5, bob_amount=0.5, move_time=(2, 4), idle_time=(4, 10), crowd_radius=(70, 8)),
    'common_musk_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(45, 8)),
    'blue_crab': dict(speed=12, fps=9, bob_amount=0.5, move_time=(1, 3), idle_time=(1, 4), crowd_radius=(50, 8)),
    'red_swamp_crawfish': dict(speed=10, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(1, 3), crowd_radius=(50, 8)),
    'mississippi_grass_shrimp': dict(speed=8, fps=9, bob_amount=0.5, move_time=(1, 3), idle_time=(1, 3), crowd_radius=(30, 8)),
    'lesser_siren': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 6), crowd_radius=(70, 8)),
    'three_toed_amphiuma': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(3, 8), crowd_radius=(85, 8)),
    'rainbow_snake': dict(speed=7, fps=6, bob_amount=0.0, move_time=(3, 6), idle_time=(2, 6), crowd_radius=(80, 8)),
    'tadpole_madtom': dict(speed=8, fps=8, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 5), crowd_radius=(35, 8)),
    'hogchoker': dict(speed=6, fps=6, bob_amount=0.0, move_time=(1, 3), idle_time=(4, 10), crowd_radius=(45, 8)),
}
