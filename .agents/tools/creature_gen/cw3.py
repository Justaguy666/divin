"""Cold Water batch 3 - bottom fishes: gurnard, monkfish, halibut, thornback ray, sculpins, snailfish, goby, shanny; species names only."""
import math, numpy as np
import swim
from swim import Fish, tooth, dorsal, anal, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_dash
from sp1 import bands, np_r
from sp4 import _crawlfish
from parts import Crawler, part, line, ell, cap
from tidy import tidy
import pal; pal.use('cw')
from pal import ramp
ALL = ['red_gurnard', 'monkfish', 'atlantic_halibut', 'thornback_ray', 'sea_raven', 'shorthorn_sculpin', 'montagus_sea_snail', 'black_goby', 'radiated_shanny']
PH = [0, 1, 0, -1]; EYE = '#0c0e0c'; HI = '#fff0c4'
SCUL = [(0, .3, -.3), (.1, .4, -.4), (.3, .66, -.68), (.5, .88, -.9), (.66, 1, -1), (.8, 1, -1), (.9, .86, -.9), (.96, .6, -.74), (1, .26, -.5)]
def red_gurnard():
    # Chelidonichthys cuculus: bright red gurnard with a steep armoured head, a row of tall plates along the lateral line, two dorsals,
    # big wing-like pectorals, and three free pectoral rays it uses like legs to walk over the bottom
    P = [(0, .3, -.3), (.1, .42, -.4), (.3, .74, -.74), (.5, .94, -.92), (.66, 1, -.98), (.8, 1, -1), (.9, .9, -1), (.96, .64, -.9), (1, .3, -.66)]
    F = Fish('red_gurnard', 36, 11, P, bands('#9a3424', '#d06a48', '#ecc8b0', sig=('back', 'flank')), eye=(0.84, 0.28, 2, '#d8a050'))
    B = F.B
    F.marks += [m_dash(B, .06, .76, .4, 1.2, '#f0d8c8', 1.6, .8)] + [m_stripe(B, .78, .98, [(.78, .2), (.98, .5)], .6, -1)]
    F.fins += [caudal(B, 'emarg', 5.6, col='#c06048', sig=True), dorsal(B, .56, .74, 4.0, 'spiny', col='#c05a40', lean=0.3, n=8, sig=True),
               dorsal(B, .14, .52, 3.4, 'round', col='#c86a50', n=12, sig=True), anal(B, .12, .5, 2.8, 'round', col='#d08a70', n=12),
               pectoral(B, .74, .6, 6.4, ang=10, width=0.5, col='#8a6a7a'), pelvic(B, .7, 3.0, col='#d8a088')]
    for k, (u, a) in enumerate(((.84, -84), (.77, -96), (.7, -108))):
        b = barbel(B, u, 1.0, 3.8, a, '#e8b098', thick=0.45); b['amp'] = 1.2; b['dir'] = np.array((1.0, 0.0)); F.fins.append(b)
    F.mouth = (.7, 1.2); return tidy(_crawlfish(F), 10)
def monkfish():
    # Lophius piscatorius: huge flat head with a jutting lower jaw (no mouth line drawn, by request), a fishing-rod lure with a
    # fleshy flap on top of the head, fringed skin flaps round the jaw, body tapering to a small tail, arm-like pectorals, mottled brown
    P = [(0, .26, -.26), (.12, .34, -.36), (.3, .54, -.6), (.5, .8, -.86), (.66, .96, -1), (.8, 1, -1), (.9, .86, -1), (.96, .6, -.98), (1, .3, -.9)]
    F = Fish('monkfish', 56, 18, P, bands('#5a4a32', '#8a7650', '#c8b490'), eye=(0.86, 0.12, 2, '#c8a860'))
    B = F.B; rng = np.random.RandomState(21)
    F.marks += [m_spot(B, u, t, 1.4 + .8 * rng.rand(), -1) for u, t in zip(rng.uniform(.1, .9, 16), rng.uniform(.1, .7, 16))]
    F.fins += [caudal(B, 'truncate', 5.4, col='#6a5a3e'), dorsal(B, .16, .32, 3.4, 'round', col='#6a5a3e', n=7), anal(B, .14, .28, 2.8, 'round', col='#7a6a4a', n=6),
               dorsal(B, .58, .66, 2.6, 'spiny', col='#6a5a3e', n=4), pectoral(B, .62, .86, 5.6, ang=14, width=0.5, col='#7a6a4a')]
    lure = barbel(B, .93, 0.0, 7.0, 75, '#8a7a58', thick=0.5); flap = barbel(B, .99, -.62, 1.4, 20, '#d8c8a0', thick=0.7)
    F.fins += [lure] + [tooth(B, u, 0.74, ln=0.0, gap=0.0, col='#ece4cc') for u in ()]
    fringe = [barbel(B, u, 1.0, l, a, '#9a8a64') for u, l, a in ((.86, 1.2, -110), (.91, .8, -80), (.95, 1.4, -100))]
    for b in fringe: b['amp'] = 0.0   # jaw flaps rest on the sand
    F.fins += fringe
    return tidy(_crawlfish(F), 10)
def atlantic_halibut():
    # Hippoglossus hippoglossus: the largest flatfish, lying eyed-side up: plain dark olive-brown with faint paler mottling, both eyes
    # on the upper side of the head, a large mouth, long dorsal and anal fringes rippling, a slightly concave tail
    P = [(0, .28, -.28), (.08, .5, -.5), (.24, .86, -.86), (.46, 1, -1), (.66, .96, -.96), (.82, .78, -.72), (.92, .52, -.42), (.97, .3, -.18), (1, .12, -.02)]
    F = Fish('atlantic_halibut', 60, 22, P, bands('#3e3e2c', '#5e5c42', '#64624a', b1=(0.3, 0.3), b2=(0.7, 0.7)), eye=(0.88, 0.18, 2, '#c8b070'))
    F.lightc = (0.45, 0.15, 0.5, 1.6); F.tspan = 2.4
    B = F.B; rng = np.random.RandomState(22)
    F.marks += [m_spot(B, u, t, 1.8 + .8 * rng.rand(), 1) for u, t in zip(rng.uniform(.1, .8, 10), rng.uniform(.2, .8, 10))]
    F.marks += [m_spot(B, .91, .14, .7, '#1e1e14'), m_spot(B, .92, .12, .45, '#f0e8c8'), m_stripe(B, .9, 1.0, [(.9, .62), (1.0, .56)], .6, '#1e1e14')]
    df = dorsal(B, .06, .9, 3.4, 'flat', col='#5a5a42', lean=0.0, n=34, amp=0.9); df['wave'] = 3.0
    af = anal(B, .06, .76, 3.4, 'flat', col='#5a5a42', lean=0.0, n=30, amp=0.9); af['wave'] = 2.5
    F.fins += [caudal(B, 'emarg', 6.4, col='#4e4e38'), df, af, pectoral(B, .8, .4, 3.4, col='#6a6a50')]
    F.mouth = (.56, 2.0); return tidy(_crawlfish(F), 10)
def thornback_ray():
    # Raja clavata: rhomboid disc lying on the bottom, seen slightly from above: brown with cream spots and dark marbling, a row of big
    # hooked thorns down the middle of the back and along the thick tail, two small dorsal fins near the tail tip, eyes and spiracles
    # raised on the head; the wing tips ripple
    top = ramp('#7a6448'); tailc = ramp('#6a5640'); cx, cy, rx = 42.0, 17.4, 16.0
    rng = np.random.RandomState(23)
    spots = [(lambda X, Y, p=p: (X - p[0]) ** 2 + ((Y - p[1]) * 1.8) ** 2 < 0.5, '#e0d0a8') for p in zip(rng.uniform(30, 56, 12), rng.uniform(12.4, 17.0, 12))]
    marb = [(lambda X, Y, p=p: ((X - p[0]) / 2.0) ** 2 + ((Y - p[1]) / 0.8) ** 2 < 1, -1) for p in zip(rng.uniform(30, 56, 7), rng.uniform(12.6, 16.6, 7))]
    def frame(f, idle):
        ph = PH[f] * (0.5 if idle else 1.0); xs = np.linspace(cx - rx, cx + rx, 50); q = (xs - cx) / rx
        s = np.clip(1 - np.abs(q), 0, 1) ** 0.75; s[0] = s[-1] = 0.0
        rip = 0.7 * ph * np.sin(2 * np.pi * (xs - cx) / 18.0) * (0.3 + 0.7 * np.abs(q))
        up = [(x, cy - 0.8 - 5.6 * si - 0.3 * r) for x, si, r in zip(xs, s, rip)]; lo = [(x, cy + 0.8 + 1.6 * si + 0.6 * r) for x, si, r in zip(xs[::-1], s[::-1], rip[::-1])]
        rim = [(lambda X, Y: Y > cy + 0.9 + 0.0 * X, '#d8ccb0')]
        P = [part(up + lo, top, z=3, name='disc', marks=spots + marb + rim, lightc=(0.25, 0.35, 1.3, 1.2))]
        sw = 0.6 * ph
        tail = [(cx - rx + 2.0, cy + 0.2), (18.0, cy + 0.4), (8.0, cy + 0.6 + sw * 0.5), (1.6, cy + 0.4 + sw)]
        P.append(part(cap(tail, [1.6, 1.2, 0.9, 0.5]), tailc, z=2.5, tone=3, name='tail'))
        for x in (6.0, 10.0):
            yy = cy + 0.6 + sw * (0.5 if x > 8 else 0.9)
            P.append(part([(x - 1.2, yy - 0.6), (x + 0.4, yy - 2.6), (x + 1.4, yy - 0.6)], tailc, z=2.6, tone=2, name='df'))
        for x in np.arange(13.0, 26.0, 2.4): P.append(line([(x, cy - 0.8), (x + 0.4, cy - 1.8)], '#e8dcc0', z=2.7, w=0.45))
        for x in np.arange(30.0, 52.0, 2.6):
            yy = cy - 0.8 - 5.6 * (max(0, 1 - abs((x - cx) / rx)) ** 0.75)
            P.append(line([(x, yy + 0.3), (x + 0.3, yy - 0.7)], '#e8dcc0', z=3.4, w=0.45))
        return P, [(cx + 8.6, cy - 3.4, EYE), (cx + 8.6, cy - 4.4, HI), (cx + 6.4, cy - 3.6, '#3a2e20')]
    return Crawler('thornback_ray', frame, 62, 26)
def sea_raven():
    # Hemitripterus americanus: rough, prickly sculpin with ragged fleshy tabs on the head and chin, a tall ragged first dorsal, mottled
    # red-brown to yellowish, big fan pectorals barred dark, wide mouth
    F = Fish('sea_raven', 36, 13, SCUL, bands('#7a3a24', '#b8784a', '#e0c08c'), eye=(0.86, 0.22, 2, '#d8b050'))
    B = F.B; rng = np.random.RandomState(24)
    F.marks += [m_spot(B, u, t, 1.4 + .6 * rng.rand(), -1) for u, t in zip(rng.uniform(.08, .86, 12), rng.uniform(.1, .7, 12))] + [m_spot(B, u, t, .45, '#f0d8a8') for u, t in zip(rng.uniform(.1, .8, 10), rng.uniform(.2, .8, 10))]
    d1 = dorsal(B, .54, .76, 6.4, 'spiny', col='#9a4a2c', lean=0.3, n=9); d1['band'] = [(lambda X, Y: (np.round(X) + np.round(Y)) % 3 == 0, '#4a2010')]
    pec = pectoral(B, .78, .6, 6.0, width=0.6, col='#a8603a'); pec['band'] = [(lambda X, Y: (np.round(X * .8) % 2) == 0, '#5a2a18')]
    F.fins += [caudal(B, 'round', 5.6, col='#a8603a'), d1, dorsal(B, .16, .5, 3.8, 'round', col='#a8603a', n=12), anal(B, .12, .44, 3.2, 'round', col='#b8784a', n=10), pec, pelvic(B, .74, 2.8, col='#c8905a')]
    F.fins += [barbel(B, u, 0.0, 1.6, a, '#c87a4a', thick=0.6) for u, a in ((.88, 70), (.94, 60), (.82, 85))] + [barbel(B, .97, 1.0, 1.6, -70, '#c87a4a', thick=0.6)]
    F.mouth = (.62, 2.6); return tidy(_crawlfish(F), 10)
def shorthorn_sculpin():
    # Myoxocephalus scorpius: big-headed sculpin with short spines on the gill cover, broad fan pectorals, mottled dark brown and olive
    # with pale saddles, a pale-spotted reddish belly in breeding males, two dorsals
    F = Fish('shorthorn_sculpin', 32, 10.4, SCUL, bands('#3e3a2a', '#7a6e4c', '#c8784a', sig=('belly',)), eye=(0.86, 0.22, 2, '#c8a050'))
    B = F.B
    F.marks += [m_bar(B, u, 2.6, .0, .5, '#1e1c14', lean=0.4) for u in (.14, .36, .58)] + [m_spot(B, u, .85, .5, '#f0e0c8') for u in np_r(.3, .7, 5)]
    pec = pectoral(B, .78, .6, 6.0, width=0.6, col='#6a6448'); pec['band'] = [(lambda X, Y: (np.round(X * .8) % 2) == 0, '#2a281c')]
    F.fins += [caudal(B, 'round', 5.0, col='#6a6448'), dorsal(B, .56, .74, 3.6, 'spiny', col='#5e5a40', lean=0.3, n=8), dorsal(B, .16, .52, 3.4, 'round', col='#6a6448', n=12),
               anal(B, .12, .44, 2.8, 'round', col='#7a7050', n=10), pec, pelvic(B, .74, 2.6, col='#8a7e5a'), tooth(B, .8, 0.0, ln=1.0, gap=0.0, col='#3e3a2a')]
    F.mouth = (.62, 2.4); return tidy(_crawlfish(F), 10)
def montagus_sea_snail():
    # Liparis montagui: small tadpole-shaped snailfish with soft loose skin, a round head and tapering body, reddish-brown to yellow
    # with fine dark speckles, a long dorsal and anal running to the rounded tail, a sucker disc under the throat
    P = [(0, .26, -.26), (.12, .36, -.38), (.32, .62, -.66), (.54, .86, -.88), (.72, 1, -1), (.86, 1, -.98), (.94, .8, -.8), (.98, .5, -.56), (1, .2, -.36)]
    F = Fish('montagus_sea_snail', 24, 8.4, P, bands('#8a5a30', '#c8945a', '#e8c89a'), eye=(0.88, 0.34, 1, '#a07848'))
    B = F.B; rng = np.random.RandomState(25)
    F.marks += [m_spot(B, u, t, .4, '#4a2a14') for u, t in zip(rng.uniform(.1, .9, 18), rng.uniform(.1, .8, 18))]
    F.fins += [caudal(B, 'round', 3.6, col='#b07a48'), dorsal(B, .06, .66, 2.2, 'flat', col='#b07a48', n=18, lean=0.1), anal(B, .06, .5, 2.0, 'flat', col='#b88452', n=14, lean=0.1),
               pectoral(B, .8, .7, 3.4, width=0.6, col='#c8945a')]
    F.mouth = (.56, 1.0); return tidy(_crawlfish(F), 10)
def black_goby():
    # Gobius niger: stocky dark goby, brown-black mottled darker, a dark spot at the front top of the first dorsal, a tall first dorsal
    # in males, pelvic fins fused into a sucker disc, big eyes set high on the head
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .76, -.74), (.5, .94, -.92), (.66, 1, -.96), (.8, .92, -.88), (.9, .7, -.66), (.96, .44, -.4), (1, .16, -.18)]
    F = Fish('black_goby', 26, 8.4, P, bands('#2a2620', '#55503e', '#8a8268'), eye=(0.84, 0.24, 2, '#b89a60'))
    B = F.B; rng = np.random.RandomState(26)
    F.marks += [m_spot(B, u, t, .9, -1) for u, t in zip(rng.uniform(.1, .8, 10), rng.uniform(.2, .7, 10))]
    d1 = dorsal(B, .5, .64, 4.4, 'spiny', col='#4a463a', lean=0.3, n=6); d1['band'] = [(lambda X, Y, B=B: (X > .6 * B.L) & (Y > B.top(np.clip(X, 0, B.L)) + 2.2), '#0e0e0c')]
    F.fins += [caudal(B, 'round', 5.0, col='#4a463a'), d1, dorsal(B, .2, .44, 3.2, 'round', col='#4a463a', n=8), anal(B, .2, .4, 2.6, 'round', col='#55503e', n=7),
               pelvic(B, .66, 2.0, col='#55503e'), pectoral(B, .74, .52, 3.6, width=0.55, col='#6a6450')]
    F.mouth = (.5, 1.2); return tidy(_crawlfish(F), 10)
def radiated_shanny():
    # Ulvaria subbifurcata: elongated blenny-like prickleback, brown mottled with darker blotches, a dark oval blotch at the front of the
    # long dorsal fin, a dark bar slanting down from the eye, rounded tail
    P = [(0, .34, -.34), (.06, .5, -.5), (.2, .84, -.84), (.42, 1, -1), (.62, 1, -1), (.8, .94, -.92), (.9, .76, -.7), (.96, .5, -.44), (1, .2, -.16)]
    F = Fish('radiated_shanny', 32, 6.8, P, bands('#5a4630', '#9a7e5a', '#cab494'), eye=(0.9, 0.34, 1, '#c8a060'))
    B = F.B; rng = np.random.RandomState(27)
    F.marks += [m_spot(B, u, t, 1.0 + .5 * rng.rand(), -1) for u, t in zip(rng.uniform(.06, .86, 12), rng.uniform(.15, .75, 12))]
    F.marks += [m_stripe(B, .88, .93, [(.88, .5), (.93, .95)], .8, '#1e1610')]
    d = dorsal(B, .06, .84, 2.6, 'flat', col='#7a6448', n=26, lean=0.1); d['band'] = [(lambda X, Y, B=B: (X > .7 * B.L) & (X < .8 * B.L), '#141010')]
    F.fins += [caudal(B, 'round', 3.8, col='#7a6448'), d, anal(B, .06, .52, 2.2, 'flat', col='#8a7454', n=16), pectoral(B, .84, .6, 2.6, col='#a8906c')]
    F.mouth = (.5, 1.0); return tidy(_crawlfish(F), 10)
SCENE = {
    'red_gurnard': dict(speed=8, fps=8, bob_amount=0.0, move_time=(1, 4), idle_time=(1, 4), crowd_radius=(50, 8)),
    'monkfish': dict(speed=3, fps=5, bob_amount=0.0, move_time=(1, 2), idle_time=(6, 14), crowd_radius=(80, 8)),
    'atlantic_halibut': dict(speed=6, fps=6, bob_amount=0.0, move_time=(1, 3), idle_time=(4, 10), crowd_radius=(90, 8)),
    'thornback_ray': dict(speed=6, fps=5, bob_amount=0.0, move_time=(2, 5), idle_time=(3, 8), crowd_radius=(75, 8)),
    'sea_raven': dict(speed=5, fps=6, bob_amount=0.0, move_time=(0.5, 2), idle_time=(3, 8), crowd_radius=(55, 8)),
    'shorthorn_sculpin': dict(speed=5, fps=6, bob_amount=0.0, move_time=(0.5, 2), idle_time=(3, 8), crowd_radius=(50, 8)),
    'montagus_sea_snail': dict(speed=5, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(35, 8)),
    'black_goby': dict(speed=7, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(40, 8)),
    'radiated_shanny': dict(speed=7, fps=7, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 6), crowd_radius=(45, 8)),
}
