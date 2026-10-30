"""Marsh Swamp batch 3 - bottom fish, newts, axolotl, turtles, snail and crayfish, defined from species names only.
v3 (Oct 2026): the three bottom fish are one memorable set each, coloured from the ms colour families (pal.FAM_MS); the kept
drawings (axolotl, newts, turtles) are re-mapped onto a family, the snail and crayfish take family colours."""
import math, numpy as np
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_dash
from sp1 import bands, np_r
from parts import Crawler, part, line, ell, cap
from sp4 import _crawlfish, _turtle
from fs3 import _sal, _crayfish
from recol import Recolor
import pal; pal.use('ms')
from pal import ramp, FAM, fc
from v3h import scatter, fin_spots
from ms1 import low
ALL = ['stone_loach', 'european_weatherfish', 'european_bullhead', 'axolotl', 'chinese_fire_bellied_newt', 'great_crested_newt',
       'chinese_softshell_turtle', 'european_pond_turtle', 'great_pond_snail', 'noble_crayfish']
def stone_loach():
    # set: slender round-bodied LOACH / brass-olive with big soft brown BLOTCHES along the side / SIX short barbels round the mouth /
    # small eyes high on the head / a dark bar at the tail base
    P = [(0, .44, -.44), (.1, .58, -.58), (.3, .86, -.88), (.55, 1, -1), (.75, .96, -.98), (.88, .8, -.84), (.96, .52, -.6), (1, .22, -.38)]
    F = Fish('stone_loach', 28, 6.6, P, bands('O1', 'O1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.86, 0.28, 1, '#a89860'))
    B = F.B; k = FAM['O1'][1]
    F.marks += [m_spot(B, u, t, 1.1, k, aspect=1.4) for u, t in scatter(7, .08, .8, .3, .62, seed=0.33, gap=0.1)] + [m_bar(B, .02, 1.4, .1, .9, FAM['O1'][0])]
    bc = FAM['O1'][4]
    F.fins += [caudal(B, 'truncate', 4.6, col=fc('O1')), dorsal(B, .44, .58, 3.2, 'round', col=fc('O1'), n=7), anal(B, .16, .28, 2.4, 'round', col=fc('O1'), n=6),
               pelvic(B, .46, 2.4, col=fc('N1')), pectoral(B, .84, .76, 3.2, ang=-8, col=fc('N1')),
               barbel(B, .99, .55, 2.2, 0, bc), barbel(B, .98, .68, 2.0, -35, bc), barbel(B, .97, .78, 1.8, -65, bc)]
    return _crawlfish(F)
def european_weatherfish():
    # set: long EEL-LIKE loach / peat-brown with a pale GOLD STRIPE along the upper side over a broad dark midline stripe / TEN barbels
    # round the small mouth / rounded tail
    P = [(0, .5, -.5), (.08, .64, -.64), (.3, .9, -.9), (.6, 1, -1), (.82, .96, -.96), (.92, .8, -.8), (.97, .52, -.56), (1, .2, -.3)]
    F = Fish('european_weatherfish', 40, 6.4, P, bands('N2', 'N2', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.9, 0.32, 1, '#a89060'))
    B = F.B
    F.marks += [m_stripe(B, .02, .94, .24, 1.2, FAM['Y1'][4]), m_stripe(B, .02, .96, .5, 1.6, FAM['N2'][0])]
    bc = FAM['Y1'][4]; fin = FAM['N2'][3]
    F.fins += [caudal(B, 'round', 5.0, col=fin), dorsal(B, .38, .52, 2.8, 'round', col=fin, n=7), anal(B, .14, .26, 2.2, 'round', col=fin, n=6),
               pelvic(B, .4, 2.0, col=fc('N2')), pectoral(B, .88, .78, 2.8, ang=-8, col=fc('N2')),
               barbel(B, .995, .5, 2.6, 0, bc), barbel(B, .99, .64, 2.4, -30, bc), barbel(B, .98, .76, 2.0, -60, bc), barbel(B, .985, .3, 2.0, 25, bc)]
    return _crawlfish(F)
def european_bullhead():
    # set: FLAT broad head with eyes on top, body tapering to the tail / mahogany-brown with three dark BANDS and soft mottling / huge
    # FAN pectorals crossed by dark bars / two dorsal fins
    P = [(0, .36, -.36), (.1, .46, -.46), (.3, .7, -.76), (.5, .86, -.9), (.66, .98, -.98), (.8, 1, -.98), (.9, .84, -.86), (.96, .56, -.6), (1, .22, -.3)]
    M = FAM['M1']; MD = ['#1e0e0e', M[0], M[1], M[2], M[3], M[4]]   # mahogany one step darker: brown, not mauve
    F = Fish('european_bullhead', 28, 9.6, P, [(0.4, 0.44, MD), (0.86, 0.86, MD), (1.01, 1.01, list(FAM['N1']))], eye=(0.84, 0.2, 2, '#c8a050'))
    B = F.B; F.tone0 = 1.2; k = '#140a08'
    F.marks += [m_bar(B, u, 2.6, 0, .78, k, lean=0.4) for u in (.12, .34, .56)] + [m_spot(B, u, t, .9, FAM['M1'][1]) for u, t in scatter(4, .2, .82, .46, .7, seed=0.43, gap=0.12)]
    x0, y0 = .78 * B.L, B.yat(.78, .56)
    pec = pectoral(B, .78, .56, 6.0, ang=-18, width=0.75, col=FAM['M1'][3], sig=True)
    pec['band'] = [(lambda X, Y: ((np.hypot(X - x0, Y - y0) % 2.2) < 0.9) & (np.hypot(X - x0, Y - y0) > 1.6), FAM['M1'][0])]
    fin = FAM['M1'][3]
    F.fins += [caudal(B, 'round', 5.0, col=fin), dorsal(B, .6, .74, 2.8, 'round', col=fin, n=7), dorsal(B, .22, .58, 3.4, 'round', col=fin, n=12),
               anal(B, .2, .5, 2.8, 'round', col=fin, n=10), pelvic(B, .7, 2.6, col=fc('N1')), pec]
    return _crawlfish(F)
def axolotl():
    # Ambystoma mexicanum (wild type): broad flat head with a wide smiling mouth, three pairs of feathery external gill stalks,
    # dark olive-grey body speckled with darker spots, small lidless eyes, tail fin that starts right behind the head
    L = 40; base = 19.4
    top = lambda x: base - ((0.8 + 5.0 * math.sin(min(1, (x - 2) / (L - 8)) * math.pi * 0.55) ** 0.8) if x < L - 8 else 3.4 + 0.3 * (L - x))
    bot = lambda x: base + 0.6 + 0.7 * math.sin(min(1, (x - 2) / (L - 2)) * math.pi) ** 2
    rng = np.random.RandomState(31)
    sp = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.6, '#20241a') for p in zip(rng.uniform(6, 36, 16), rng.uniform(14.6, 19.0, 16))]
    mouth = [(lambda X, Y: (X > 36.4) & (np.abs(Y - (base - 1.2) - (X - 36.4) * 0.12) < 0.5), '#20241a')]
    legs = [((31.0, 18.8), (33.0, 20.2), (33.8, 21.6), True), ((14.0, 18.8), (12.6, 20.2), (11.8, 21.6), True),
            ((29.4, 18.4), (30.8, 20.0), (31.6, 21.6), False), ((15.6, 18.4), (14.8, 20.0), (14.2, 21.6), False)]
    fin = [(2.0, base - 0.2), (8.0, base - 5.2), (30.0, base - 6.2), (30.0, base - 4.6), (2.0, base + 0.8)]
    gr = ramp('#9a5a6a', sig=True)
    def gills(f, idle):
        s = 0.5 * [0, 1, 0, -1][f]; out = []
        for k in range(3):
            a = (33.2, base - 3.4 + k * 1.3); b = (30.0 - k * 0.6, base - 7.0 + k * 1.6 + s)
            out.append(part(cap([a, b], [0.7, 0.6]), gr, z=3.5, name='gill'))
            for q in np.linspace(0.3, 0.9, 3): out.append(line([(a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q), (a[0] + (b[0] - a[0]) * q - 0.6, a[1] + (b[1] - a[1]) * q - 1.0)], gr[4], z=3.6))
        return out
    return _sal('axolotl', L, base, top, bot, '#5a6050', [], sp + mouth, legs, gills=gills, CW=46, CH=24, eye=[(37.6, base - 3.0, '#0c0e0c')], tailfin=fin)
def chinese_fire_bellied_newt():
    # Cynops orientalis: small slim newt, smooth near-black back, a bright orange-red belly showing along the lower edge, flattened
    # tail with a low fin, small dark eyes
    L = 28; base = 19.6
    top = lambda x: base - ((0.8 + 4.0 * math.sin(min(1, (x - 2) / (L - 6)) * math.pi * 0.55) ** 0.8) if x < L - 6 else 2.6 + 0.36 * (L - x))
    bot = lambda x: base + 0.6 + 0.6 * math.sin(min(1, (x - 2) / (L - 2)) * math.pi) ** 2
    belly = [(lambda X, Y: (Y > base - 0.2) & (X > 6), '#e0602c')]
    legs = [((21.6, 19.0), (23.0, 20.2), (23.6, 21.6), True), ((10.4, 19.0), (9.4, 20.2), (8.8, 21.6), True),
            ((20.4, 18.6), (21.4, 20.0), (22.0, 21.6), False), ((11.6, 18.6), (11.0, 20.0), (10.6, 21.6), False)]
    fin = [(2.0, base - 0.2), (10.0, base - 2.8), (12.0, base - 1.8), (2.0, base + 0.8)]
    return _sal('chinese_fire_bellied_newt', L, base, top, bot, '#2a2a22', [], belly, legs, CW=34, CH=24, eye=[(24.8, base - 3.0, '#c8a050')], tailfin=fin)
def great_crested_newt():
    # Triturus cristatus (breeding male): dark brown-black warty skin with darker spots, orange-yellow belly blotched black, a tall
    # jagged crest along the back, a silvery-white stripe along the tail
    L = 36; base = 19.6
    top = lambda x: base - ((0.8 + 4.6 * math.sin(min(1, (x - 2) / (L - 7)) * math.pi * 0.55) ** 0.8) if x < L - 7 else 3.0 + 0.36 * (L - x))
    bot = lambda x: base + 0.6 + 0.7 * math.sin(min(1, (x - 2) / (L - 2)) * math.pi) ** 2
    rng = np.random.RandomState(41)
    warts = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.5, '#141410') for p in zip(rng.uniform(6, 32, 14), rng.uniform(16.0, 19.2, 14))]
    belly = [(lambda X, Y: (Y > base - 0.2) & (X > 8) & (((np.round(X) // 2) % 3) != 0), '#e0a040')]
    stripe = [(lambda X, Y: (X < 12) & (np.abs(Y - (base - 0.8)) < 0.5), '#d8d8d0')]
    legs = [((28.4, 19.0), (30.0, 20.2), (30.8, 21.6), True), ((13.0, 19.0), (11.8, 20.2), (11.0, 21.6), True),
            ((27.0, 18.6), (28.2, 20.0), (29.0, 21.6), False), ((14.4, 18.6), (13.6, 20.0), (13.0, 21.6), False)]
    crest = [(2.0, base - 0.4)] + [(x, base - 3.0 - 2.4 * math.sin((x - 2) / 26 * math.pi) - (1.2 if int(x) % 2 == 0 else 0)) for x in np.arange(3, 29, 1.0)] + [(29.0, base - 3.6), (2.0, base + 0.8)]
    return _sal('great_crested_newt', L, base, top, bot, '#3a3226', [], warts + belly + stripe, legs, CW=42, CH=24, eye=[(32.0, base - 3.4, '#c8a050')], tailfin=crest)
def chinese_softshell_turtle():
    # Pelodiscus sinensis: flat, round, leathery shell without scutes, olive-grey with small dark spots and a soft pale rim,
    # long tubular snout on a long neck, webbed feet
    top = [(7.0, 16.4)] + [(x, 16.4 - 4.2 * math.sqrt(max(0, 1 - ((x - 19.0) / 12.0) ** 2))) for x in np.linspace(7.2, 30.8, 23)] + [(31.0, 16.4)]
    rng = np.random.RandomState(51)
    spots = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.45, '#2e3024') for p in zip(rng.uniform(10, 28, 12), rng.uniform(12.6, 15.6, 12))]
    rim = [(lambda X, Y: Y > 15.4, 1)]
    hm = [(lambda X, Y: X > 39.6, '#4a4c3a')]
    legs = [((27.0, 16.6), (29.0, 18.8), (30.4, 21.6), True), ((11.0, 16.6), (9.6, 18.8), (8.6, 21.6), True),
            ((25.4, 16.4), (26.6, 18.6), (27.4, 21.6), False), ((12.6, 16.4), (12.0, 18.6), (11.6, 21.6), False)]
    def extra(f, idle):
        return [line([(39.6 + 2.6, 15.6), (41.6 + 2.6, 15.2)], '#6a6c56', z=2.7, w=0.6)]
    mk = _turtle('chinese_softshell_turtle', 50, 24, top, '#6a6c54', '#c8c0a0', '#7a7c64', (38.6, 15.6, 3.4, 1.8), [(30.4, 16.0), (35.6, 15.4)],
                 legs, [(7.4, 16.4), (5.0, 17.2)], [], spots + rim, hm, (1.4, -0.6), extra, dy=1.8)
    return mk([(7.0, 16.2), (31.0, 16.2), (30.0, 17.4), (8.0, 17.4)])
def european_pond_turtle():
    # Emys orbicularis: low-domed dark brown-black carapace sprinkled with yellow dots and short radiating streaks, dark skin with
    # yellow speckles, yellowish plastron edge
    top = [(9.0, 15.0)] + [(x, 15.0 - 6.8 * math.sqrt(max(0, 1 - ((x - 20.0) / 11.0) ** 2))) for x in np.linspace(9.2, 30.8, 23)] + [(31.0, 15.0)]
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0) < 0.5) & (Y > 9.4), -1) for x0 in (15.0, 20.0, 25.0)] + [(lambda X, Y: np.abs(Y - 13.6) < 0.5, -1)]
    rng = np.random.RandomState(61)
    dots = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.35, '#d8c050') for p in zip(rng.uniform(11, 29, 16), rng.uniform(9.4, 13.4, 16))]
    hm = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.35, '#d8c050') for p in ((33.6, 12.6), (35.0, 13.6), (36.2, 12.4), (34.4, 14.4))]
    legs = [((27.0, 15.4), (28.8, 18.4), (29.6, 21.6), True), ((13.0, 15.4), (12.0, 18.4), (11.4, 21.6), True),
            ((25.6, 15.2), (26.6, 18.2), (27.2, 21.6), False), ((14.4, 15.2), (13.8, 18.2), (13.6, 21.6), False)]
    mk = _turtle('european_pond_turtle', 44, 26, top, '#2e2a1e', '#c8b060', '#3a3628', (34.6, 13.4, 3.2, 2.2), [(29.4, 14.6), (32.0, 14.0)],
                 legs, [(9.4, 15.4), (6.6, 16.6)], seams, dots, hm, (1.4, -0.8))
    return mk([(9.0, 14.8), (31.0, 14.8), (30.2, 16.4), (10.0, 16.4)])
def great_pond_snail():
    # set: thin HORN-coloured shell with a huge rounded body whorl and a tall SHARP SPIRE / faint spiral lines / big ear-shaped dark
    # aperture / grey foot and flat triangular tentacles; the shell stays fixed while the foot glides
    shell = ramp(FAM['O1'][2]); foot = ramp(FAM['N1'][2])
    def frame(f, idle):
        ext = 0 if idle else [0, 0.8, 1.6, 0.8][f]; sw = 0.5 * [0, 1, 0, -1][f]
        P = [part(cap([(7.0, 18.6), (21.0 + ext, 18.4), (24.6 + ext, 18.8)], [1.9, 1.9, 1.2]), foot, z=1, name='foot')]
        P.append(part(ell(14.6, 13.0, 5.8, 4.6, -20), shell, z=3, name='bodywhorl', lightc=(0.3, 0.4, 1.5, 1.3), marks=[(lambda X, Y: np.abs(((X * 0.8 - Y) % 2.6) - 1.3) < 0.35, -1)]))
        for i in range(5):
            t = (i + 1) / 5.0; cx = 12.4 - 7.2 * t; cy = 10.4 - 7.4 * t; r = 3.9 - 2.9 * t
            P.append(part(ell(cx, cy, r, r * 0.7, -40), shell, z=2.9 - i * 0.1, name='whorl%d' % i, lightc=(0.3, 0.4, 1.5, 1.3)))
        P.append(part(ell(19.0, 15.0, 2.2, 3.0, 15), ramp('#2a2216'), z=3.5, shade='flat', tone=3, outline=False, name='ap'))
        P.append(part([(23.0 + ext, 17.2), (26.6 + ext, 14.8 + sw), (24.0 + ext, 17.8)], foot, z=4, shade='flat', tone=2, outline=False, name='tent'))
        P.append(part([(23.4 + ext, 17.6), (27.4 + ext, 16.8 - sw), (24.2 + ext, 18.2)], foot, z=4, shade='flat', tone=1, outline=False, name='tent'))
        return P, [(23.6 + ext, 17.4, '#141210')]
    return Crawler('great_pond_snail', frame, 34, 24, prefix='crawl_')
def noble_crayfish():
    # set: BIG dark peat-brown crayfish / rough heavy claws whose undersides and joints are CRIMSON / long rostrum
    N = FAM['N2']; body = ['#140e08', N[0], N[1], N[2], N[3], N[4]]   # peat family one step darker: dark brown
    mot = lambda: [(lambda X, Y: (Y > 18.6) & (X > 24), FAM['R1'][2])]
    return _crayfish('noble_crayfish', body, body, body, FAM['R1'][3], mot, claw_w=1.35, rostrum=4.2)

# ------------------------------------------------------------------ kept drawings (by request): salamanders and turtles re-mapped onto the marsh ramp
def axolotl():
    # set: the existing axolotl drawing (kept) - leucistic, re-mapped onto the pale mahogany-rose family / feathery GILLS kept as a
    # rose signature / broad smiling head, tail fin
    return Recolor('old_ms/ms_axolotl_crawl_*_4f.png', 'M1', sig=[(340, 30, 0.07, FAM['R2'][3])])
def chinese_fire_bellied_newt():
    # set: the existing drawing (kept) - charcoal-black warty back on the pearl / charcoal family, the CRIMSON belly kept as a signature
    N = FAM['N1']; r = Recolor('old_ms/ms_chinese_fire_bellied_newt_crawl_*_4f.png', ['#121210', N[0], N[1], N[2], N[3], N[4]], sig=[(25, 80, 0.06, FAM['R1'][3], 3)])
    r.eye = dict(back=4, down=2, ring='#b88434', size=1); r.pad = (1, 0); return r
def great_crested_newt():
    # set: the existing drawing (kept) - dark peat-brown warty skin, the GOLD belly kept as a signature
    N = FAM['N2']; r = Recolor('old_ms/ms_great_crested_newt_crawl_*_4f.png', ['#140e08', N[0], N[1], N[2], N[3], N[4]], sig=[(25, 100, 0.07, '#b9a03a', 3)])
    r.eye = dict(back=5, down=2, ring='#a87830', size=1); return r
def chinese_softshell_turtle():
    # set: the existing swimming softshell drawing (six direction rows, kept) - flat leathery shell, re-mapped onto the brass-olive family
    O = FAM['O1']; r = Recolor('old_ms/ms_chinese_softshell_turtle_swim_*_4f.png', ['#141206', O[0], O[1], O[2], O[3], O[4]], tags=('E', 'SE', 'SW', 'W', 'NW', 'NE')); r.crawl = False
    r.legs = 0.55; r.eye = dict(back=4, down=1, ring='#14120c', size=1); r.pad = (1, 1); r.ac = True; return r
def european_pond_turtle():
    # set: the existing drawing (kept) - near-black shell and skin on the charcoal family, the GOLD speckles kept as a signature
    N = FAM['N1']; return Recolor('old_ms/ms_european_pond_turtle_crawl_*_4f.png', ['#121210', N[0], N[1], N[2], N[3], N[4]], sig=[(70, 115, 0.05, '#c8b04a', 3)])
SCENE = {
    'stone_loach': dict(speed=8, fps=8, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 6), crowd_radius=(40, 8)),
    'european_weatherfish': dict(speed=8, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(2, 6), crowd_radius=(50, 8)),
    'european_bullhead': dict(speed=6, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(45, 8)),
    'axolotl': dict(speed=5, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(3, 8), crowd_radius=(60, 8)),
    'chinese_fire_bellied_newt': dict(speed=6, fps=7, bob_amount=0.5, move_time=(1, 4), idle_time=(2, 5), crowd_radius=(40, 8)),
    'great_crested_newt': dict(speed=6, fps=7, bob_amount=0.5, move_time=(1, 4), idle_time=(2, 5), crowd_radius=(50, 8)),
    'chinese_softshell_turtle': dict(band=(150, 256), speed=12, fps=7, crowd=90, rest=(1.5, 4.0)),
    'european_pond_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(55, 8)),
    'great_pond_snail': dict(speed=2, fps=5, move_prefix='crawl_', bob_amount=0.0, move_time=(6, 10), idle_time=(2, 6), crowd_radius=(30, 8)),
    'noble_crayfish': dict(speed=10, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(1, 3), crowd_radius=(55, 8)),
}
