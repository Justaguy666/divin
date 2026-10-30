"""Underwater Cave batch 3 - floor dwellers: scorpionfish, triplefin, cave gobies, octopus, lobsters, shrimps, spider crab, giant isopod,
trumpet triton; species names only."""
import math, numpy as np
import swim
from swim import Fish, tooth, dorsal, anal, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_dash
from sp1 import bands, np_r
from sp4 import _crawlfish
from parts import Crawler, part, line, ell, cap
from tidy import tidy
from cw4 import _scaled, _spiral_shell
import pal; pal.use('uc')
from pal import ramp
# kept as drawn before (by request, not rebuilt): uc_blue_devilfish and uc_common_octopus
ALL = ['madeira_rockfish', 'blackface_blenny', 'leopard_spotted_goby', 'steinitzs_cave_goby', 'bentuvias_goby', 'liechtensteins_goby',
       'caribbean_spiny_lobster', 'slipper_lobster', 'banded_coral_shrimp', 'hawaiian_red_shrimp', 'mediterranean_spider_crab', 'giant_isopod', 'trumpet_triton']
PH = [0, 1, 0, -1]; EYE = '#0c0e0c'; HI = '#fff0c4'
GOBY = [(0, .34, -.34), (.1, .44, -.42), (.3, .76, -.74), (.5, .94, -.92), (.66, 1, -.96), (.8, .92, -.88), (.9, .7, -.66), (.96, .44, -.4), (1, .16, -.18)]
def gobyfins(B, col, d1=3.0, d1col=None):
    return [caudal(B, 'round', 4.6, col=col), dorsal(B, .5, .64, d1, 'spiny', col=d1col or col, lean=0.3, n=6), dorsal(B, .2, .44, 2.8, 'round', col=col, n=8),
            anal(B, .2, .4, 2.4, 'round', col=col, n=7), pelvic(B, .66, 2.0, col=col), pectoral(B, .74, .52, 3.4, width=0.55, col=col)]
def madeira_rockfish():
    # Scorpaena maderensis: small scorpionfish, mottled red-brown with dark bands and pale blotches, fleshy tabs over the eyes and on the
    # head, a venomous spiny dorsal with a dark spot, big fan pectorals, big mouth
    P = [(0, .3, -.3), (.1, .42, -.42), (.3, .74, -.76), (.5, .94, -.96), (.66, 1, -1), (.8, .96, -1), (.9, .8, -.9), (.96, .54, -.7), (1, .24, -.5)]
    F = Fish('madeira_rockfish', 30, 11, P, bands('#7a3a28', '#b8704a', '#dcb08c'), eye=(0.84, 0.24, 2, '#d8a050'))
    B = F.B; rng = np.random.RandomState(41)
    F.marks += [m_bar(B, u, 2.4, 0, .8, -1, lean=0.4) for u in (.14, .36, .56)] + [m_spot(B, u, t, .6, '#ecd4b8') for u, t in zip(rng.uniform(.1, .8, 9), rng.uniform(.2, .8, 9))]
    d = dorsal(B, .42, .74, 4.6, 'spiny', col='#a8603e', lean=0.3, n=11); d['band'] = [(lambda X, Y, B=B: (X > .56 * B.L) & (X < .66 * B.L) & (Y > B.top(np.clip(X, 0, B.L)) + 1.4), '#1e1410')]
    pec = pectoral(B, .74, .62, 5.6, width=0.6, col='#b87850'); pec['band'] = [(lambda X, Y: (np.round(X * .8) % 2) == 0, '#5a2a18')]
    F.fins += [caudal(B, 'round', 5.0, col='#a8603e'), d, dorsal(B, .16, .42, 3.4, 'round', col='#a8603e', n=8), anal(B, .14, .32, 3.0, 'round', col='#b06a46', n=6), pec,
               pelvic(B, .7, 2.8, col='#c08058'), barbel(B, .84, 0.0, 1.6, 75, '#d8a080', thick=0.6), barbel(B, .92, 0.1, 1.2, 60, '#d8a080', thick=0.6)]
    F.mouth = (.6, 2.0); return tidy(_crawlfish(F), 8)
def blackface_blenny():
    # Tripterygion delaisi (male): triplefin blenny with three separate dorsal fins, a bright yellow body and a jet-black head, pointed
    # snout, big eyes set high, rounded tail
    P = [(0, .3, -.3), (.1, .4, -.4), (.3, .7, -.72), (.5, .9, -.92), (.66, 1, -.98), (.8, .96, -.94), (.9, .78, -.74), (.96, .5, -.46), (1, .18, -.2)]
    F = Fish('blackface_blenny', 24, 7.4, P, bands('#d8a820', '#ecc838', '#f0dc78', sig=('back', 'flank', 'belly')), eye=(0.86, 0.3, 2, '#e8c840'))
    B = F.B
    F.marks += [m_region(B, .76, 1.0, 0, 1, '#141414')]
    F.fins += [caudal(B, 'round', 4.0, col='#e0b830', sig=True), dorsal(B, .62, .7, 2.6, 'tri', col='#e0b830', lean=0.3, n=4, sig=True),
               dorsal(B, .38, .6, 2.4, 'round', col='#e0b830', n=6, sig=True), dorsal(B, .14, .36, 2.2, 'round', col='#e0b830', n=6, sig=True),
               anal(B, .14, .44, 2.0, 'round', col='#e0b830', n=8, sig=True), pelvic(B, .74, 1.8, col='#e8c860'), pectoral(B, .74, .6, 3.0, width=0.55, col='#e8c860')]
    F.mouth = (.5, 1.0); return tidy(_crawlfish(F), 8)
def leopard_spotted_goby():
    # Thorogobius ephippiatus: pale grey-cream goby covered in large orange-brown leopard spots edged darker, a dark-edged first dorsal,
    # big eyes on top of the head, rounded tail
    F = Fish('leopard_spotted_goby', 26, 8.0, GOBY, bands('#a89a8a', '#d8ccbc', '#ece4d8'), eye=(0.84, 0.24, 2, '#c8a070'))
    B = F.B; rng = np.random.RandomState(42)
    F.marks += [m_spot(B, u, t, 1.0, '#7a3a1c') for u, t in zip(rng.uniform(.06, .86, 14), rng.uniform(.12, .8, 14))] + [m_spot(B, u, t, .6, '#d8702c') for u, t in zip(rng.uniform(.06, .86, 14), rng.uniform(.12, .8, 14))]
    fins = gobyfins(B, '#c8b8a4'); fins[1]['band'] = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 2.0, '#2a1a10')]
    F.fins += fins; F.mouth = (.5, 1.0); return tidy(_crawlfish(F), 8)
def steinitzs_cave_goby():
    # Amblyeleotris steinitzi: slender goby that shares a burrow with a shrimp, white with five broad orange-brown bars and scattered
    # small yellow spots, a tall first dorsal, rounded tail
    P = [(0, .3, -.3), (.1, .4, -.4), (.3, .72, -.72), (.5, .92, -.92), (.66, 1, -.96), (.8, .92, -.88), (.9, .7, -.66), (.96, .44, -.4), (1, .16, -.18)]
    F = Fish('steinitzs_cave_goby', 28, 6.8, P, bands('#c8c0b4', '#ece8e0', '#f4f2ee'), eye=(0.86, 0.26, 2, '#c8a070'))
    B = F.B
    F.marks += [m_bar(B, u, 2.6, 0, 1, '#b8582c') for u in np_r(.1, .74, 5)] + [m_spot(B, u, t, .45, '#e8c840') for u, t in ((.2, .3), (.42, .7), (.6, .3), (.8, .6), (.32, .5))]
    F.fins += gobyfins(B, '#d8d0c4', d1=4.2); F.mouth = (.5, 1.0); return tidy(_crawlfish(F), 8)
def bentuvias_goby():
    # Didogobius bentuvii: small, pale cave goby, translucent pinkish-cream with faint orange-brown blotches along the side, small eyes,
    # two dorsals, rounded tail
    F = Fish('bentuvias_goby', 22, 6.8, GOBY, bands('#c09a8a', '#e0c4b4', '#f0e0d8'), eye=(0.84, 0.26, 1, '#c8a080'))
    B = F.B
    F.marks += [m_spot(B, u, .5, 1.0, '#c87a5a', aspect=1.4) for u in np_r(.12, .7, 5)] + [m_spot(B, u, .16, .6, '#c87a5a') for u in (.3, .5)]
    F.fins += gobyfins(B, '#dcc0b0'); F.mouth = (.5, 1.0); F = _crawlfish(F)
    for f in F.fins:
        if f['kind'] in ('pelvic', 'anal'): f['amp'] = 0.0   # the pelvic sucker disc and the anal fin rest on the floor
    return tidy(F, 8)
def liechtensteins_goby():
    # Corcyrogobius liechtensteini: tiny cave goby, translucent pale with yellow-orange saddles across the back and a pale blue sheen
    # on the head, big dark eyes, two dorsals
    F = Fish('liechtensteins_goby', 16, 5.6, GOBY, bands('#b8b0a0', '#dcd4c8', '#ece8e0'), eye=(0.84, 0.28, 1, '#6a8ab0'))
    B = F.B
    F.marks += [m_bar(B, u, 1.4, 0, .6, '#e0a030') for u in (.14, .34, .54)] + [m_region(B, .8, 1.0, .1, .6, '#8aa8c8')]
    F.fins += gobyfins(B, '#d0c8b8'); F.mouth = (.5, .8); return tidy(_crawlfish(F), 6)
def common_octopus():
    # Octopus vulgaris: reddish-brown mottled octopus sitting on the floor, a bulbous mantle raised behind the head, golden eyes with a
    # bar pupil, eight curling arms spread over the bottom with pale sucker rows, skin papillae; the arms ripple as it creeps
    body = ramp('#9a4a30'); armr = ramp('#a85a3a'); suck = '#e8c8a8'
    rng = np.random.RandomState(43)
    mott = [(lambda X, Y, p=p: ((X - p[0]) / 1.4) ** 2 + ((Y - p[1]) / 1.0) ** 2 < 1, -1) for p in zip(rng.uniform(10, 26, 8), rng.uniform(6, 15, 8))]
    def frame(f, idle):
        ph = PH[f] * (0.4 if idle else 1.0); P = []
        P.append(part(ell(16.0, 10.4, 7.0, 5.6, -24), body, z=3, name='mantle', marks=mott, lightc=(0.3, 0.4, 1.5, 1.3)))
        P.append(part(ell(22.4, 15.0, 4.6, 3.4, 0), body, z=3.2, name='head', marks=mott))
        for k in range(8):
            side = 1 if k % 2 == 0 else -1; i = k // 2
            sx = 21.0 + side * (1.0 + i * 0.6); far = k in (1, 3, 5, 7)
            pts = []
            for j in range(7):
                t = j / 6.0; x = sx + side * (3.0 + 12.0 * t) * (0.6 + 0.25 * i); y = 18.0 + 3.0 * math.sin(t * 1.6) + 0.5 * ph * math.sin(t * 6 + k)
                y = min(y, 21.6 - 0.5 * (1 - t)); pts.append((x, y - 1.6 * (t ** 2) * (1 if (j == 6 and k % 3 == 0) else 0)))
            P.append(part(cap(pts, list(np.linspace(1.6, 0.4, 7))), armr if not far else ramp(pal.mix('#a85a3a', '#000000', .25)), z=1 if far else 4, tone=3 if not far else 2,
                          name='arm%d' % k, marks=[(lambda X, Y: ((np.round(X) + np.round(Y)) % 2 == 0) & (Y > 19.6), suck)] if not far else []))
        return P, [(24.6, 13.6, '#d8a840'), (25.4, 13.6, EYE)]
    return Crawler('common_octopus', frame, 48, 26)
def caribbean_spiny_lobster():
    # Panulirus argus: clawless spiny lobster, orange-brown with cream spots on the tail (two big pale spots on the second segment),
    # very long, thick, spiny antennae swept forward, striped legs, a broad tail fan
    body = ramp('#a8582e'); legr = ramp('#c8805a'); X0 = 2.0
    shape = [(1.2, 15.4), (2.2, 14.6), (5.0, 14.8), (8.0, 14.4), (12.0, 13.8), (16.0, 13.4), (19.0, 13.0), (22.0, 12.4), (26.0, 12.2), (29.0, 12.8), (31.4, 14.0), (33.0, 15.4),
             (31.0, 17.4), (28.0, 19.0), (22.0, 19.4), (16.0, 19.0), (11.0, 18.6), (7.0, 18.4), (4.0, 18.6), (1.6, 19.4), (0.4, 17.4)]
    seg = [(lambda X, Y, x0=x0: (np.abs(X - x0 - X0 - (Y - 16) * 0.2) < 0.5), -1) for x0 in (4.6, 7.4, 10.0, 12.6, 15.2, 17.8)]
    spots = [(lambda X, Y, p=p: (X - p[0] - X0) ** 2 + (Y - p[1]) ** 2 < 0.6, '#f0dcb0') for p in ((13.8, 15.4), (16.4, 15.4), (6.0, 15.8), (9.0, 16.2), (24.0, 14.2), (27.0, 14.6))]
    spines = [(lambda X, Y: (Y < 13.4) & (X > 22 + X0) & (np.round(X) % 2 == 0), -2)]
    def frame(f, idle):
        ph = PH[f]; sw = (0.3 if idle else 0.6) * ph; S = lambda pts: [(x + X0, y) for x, y in pts]
        P = [part(S(shape), body, z=3, name='body', marks=seg + spots + spines, lightc=(0.3, 0.4, 1.5, 1.3))]
        for k, x in enumerate((29.0, 26.8, 24.6, 22.4, 20.2)):
            up = 0.8 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(part(cap(S([(x, 18.8), (x + 1.4, 20.2 - up), (x + 0.6 + 0.8 * up, 21.6 - up)]), [0.55, 0.5, 0.45]), legr, z=4, shade='flat', tone=3, outline=False, name='leg%d' % k,
                          marks=[(lambda X, Y: np.round(Y) % 2 == 0, '#f0dcb0')]))
            P.append(line(S([(x + 1.0, 18.6), (x + 2.0, 20.0), (x + 1.6, 21.6)]), legr[1], z=0.4))
        for dy, z, tn in ((0.0, 5, 3), (-1.0, 0.6, 2)):
            ant = S([(31.6, 13.2 + dy), (36.0, 10.8 + dy), (41.0, 10.0 + dy + sw), (46.0, 11.0 + dy + sw), (50.0, 12.8 + dy + sw)])
            P.append(part(cap(ant, [1.1, 0.9, 0.7, 0.5, 0.4]), body, z=z, tone=tn, name='ant%d' % z, marks=[(lambda X, Y: np.round(X) % 3 == 0, -1)]))
        P.append(line(S([(32.0, 14.4), (35.4, 13.4), (37.6, 14.0 - sw)]), '#c8805a', z=6))
        return P, [(31.0 + X0, 13.4, EYE), (31.0 + X0, 12.6, HI)]
    return _scaled(Crawler('caribbean_spiny_lobster', frame, 56, 26), 1.15)
def slipper_lobster():
    # Scyllarides aequinoctialis: flat, broad, armoured slipper lobster with no claws, the antennae turned into wide flat shovel plates in
    # front of the head, mottled orange-brown with darker spots, short legs, a broad tail fan
    body = ramp('#9a5a34'); rng = np.random.RandomState(44)
    mott = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.5, '#5a2e18') for p in zip(rng.uniform(4, 28, 14), rng.uniform(14.6, 18.6, 14))]
    shape = [(1.0, 18.0), (2.0, 15.8), (5.0, 15.0), (10.0, 14.2), (16.0, 13.6), (22.0, 13.4), (27.0, 13.8), (29.0, 15.4), (28.6, 18.6), (24.0, 19.4), (14.0, 19.6), (6.0, 19.4), (2.0, 19.6)]
    def frame(f, idle):
        ph = PH[f]; sw = (0.2 if idle else 0.5) * ph
        P = [part(shape, body, z=3, name='body', marks=mott + [(lambda X, Y, x0=x0: np.abs(X - x0) < 0.45, -1) for x0 in (5, 8, 11, 14)], lightc=(0.3, 0.4, 1.4, 1.2))]
        P.append(part([(28.6, 14.6), (33.6, 13.6 + sw), (35.6, 15.4 + sw), (34.0, 17.8 + sw), (28.8, 18.0)], body, z=3.2, tone=4, name='plate',
                      marks=[(lambda X, Y: (np.round(X) + np.round(Y)) % 3 == 0, -1)]))
        for k, x in enumerate((26.0, 23.4, 20.8, 18.2)):
            up = 0.6 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line([(x, 19.2), (x + 1.2, 20.4 - up), (x + 1.0 + 0.6 * up, 21.6 - up)], body[2], z=4))
        return P, [(28.0, 14.6, EYE), (28.0, 13.8, HI)]
    return _scaled(Crawler('slipper_lobster', frame, 40, 26), 1.3)
def banded_coral_shrimp():
    # Stenopus hispidus: boxer shrimp banded red and white along the body and claws, a pair of very long banded claws held forward,
    # long white antennae, translucent white legs
    red = '#c8302a'
    body = ramp('#ece4dc'); X0 = 1.0
    shape = [(1.0, 16.6), (2.6, 15.0), (5.4, 13.8), (9.0, 13.2), (13.0, 13.0), (17.0, 13.2), (20.0, 13.8), (22.0, 14.6), (25.4, 13.6), (22.6, 15.6), (22.0, 16.8),
             (19.0, 17.6), (14.0, 17.8), (9.0, 17.6), (5.4, 17.8), (2.8, 18.2)]
    bandm = [(lambda X, Y: ((np.round(X - X0) // 3) % 2 == 0) & (X > 3), red)]
    def frame(f, idle):
        ph = PH[f]; sw = (0.3 if idle else 0.6) * ph; o = 0.4 * ph * (0 if idle else 1); S = lambda pts: [(x + X0, y) for x, y in pts]
        P = [part(S(shape), body, z=3, name='body', marks=bandm, lightc=(0.3, 0.4, 1.5, 1.3)), part(S([(2.6, 15.8), (-0.4, 14.6), (-0.8, 16.8), (2.6, 17.8)]), body, z=2.9, name='fan', tone=2)]
        for k, x in enumerate((20.0, 18.0, 16.0, 14.0)):
            up = 0.6 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line(S([(x, 17.6), (x + 1.0, 19.6 - up), (x + 0.6 + 0.6 * up, 21.6 - up)]), '#d8d0c8', z=4))
        for dz, dy in ((0.6, -1.0), (5, 0)):
            arm = S([(21.0, 16.6 + dy), (25.0, 18.8 + dy), (30.0, 18.0 + dy), (33.0, 17.4 + dy)])
            P.append(part(cap(arm, 0.6), body, z=dz, shade='flat', tone=3 if dz > 1 else 2, outline=False, name='arm%d' % dz, marks=[(lambda X, Y: (np.round(X) // 2) % 2 == 0, red)]))
            P.append(part(ell(35.0 + X0, 17.2 + dy, 2.2, 0.9, -4), body, z=dz + .05, name='claw%d' % dz, marks=[(lambda X, Y: X > 35.6 + X0, red)]))
            P.append(part(cap(S([(36.6, 16.8 + dy), (38.8, 16.6 + dy - o)]), 0.45), body, z=dz + .06, shade='flat', tone=3, outline=False, name='claw%d' % dz))
        P.append(line(S([(23.0, 14.2), (28.0, 9.6 + sw), (36.0, 7.8 + sw), (42.0, 8.6 + sw)]), '#f0ece8', z=6))
        P.append(line(S([(23.2, 14.6), (27.0, 12.4), (33.0, 11.6 - sw)]), '#f0ece8', z=6))
        return P, [(22.6 + X0, 14.4, EYE)]
    return Crawler('banded_coral_shrimp', frame, 46, 26)
def hawaiian_red_shrimp():
    # Halocaridina rubra: tiny bright red cave shrimp (opae ula), a short rostrum, black eyes, a curved abdomen and tail fan, fine legs
    body = ramp('#e2503a', sig=True); D = 1.4
    shape = [(1.4, 18.8), (2.8, 17.4), (5.0, 16.6), (7.8, 16.4), (10.4, 16.6), (12.0, 17.0), (14.6, 16.6), (12.6, 17.8), (11.0, 18.4), (8.0, 18.6), (5.0, 18.6), (3.0, 19.2)]
    shape = [(x, y + D) for x, y in shape]
    def frame(f, idle):
        ph = PH[f]; sw = (0.2 if idle else 0.5) * ph
        P = [part(shape, body, z=3, name='body', lightc=(0.3, 0.4, 1.5, 1.3)), part([(2.4, 17.8 + D), (0.4, 17.0 + D), (0.0, 18.4 + D), (2.2, 19.0 + D)], body, z=2.9, name='fan', tone=2)]
        for k, x in enumerate((10.6, 9.0, 7.4)):
            up = 0.4 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line([(x, 18.4 + D), (x + 0.6, 20.6 - up), (x + 0.4 + 0.4 * up, 21.6 - up)], body[3], z=4, w=0.3))
        P.append(line([(12.2, 16.8 + D), (15.0, 15.2 + D + sw), (17.6, 15.0 + D + sw)], '#d85a44', z=4, w=0.3))
        return P, [(11.8, 17.0 + D, EYE)]
    return _scaled(Crawler('hawaiian_red_shrimp', frame, 20, 24), 1.3)
def mediterranean_spider_crab():
    # Maja squinado seen from the front: a pear-shaped, knobbly orange-red carapace covered in spines with two forward horns, long
    # spindly hairy legs, slender claws, often bits of algae caught on the spines
    shell = ramp('#b8583a'); legr = ramp('#c06a48'); cx = 24.0
    carap = [(cx - 9.0, 13.4), (cx - 8.0, 10.4), (cx - 5.0, 8.4), (cx - 2.0, 7.6), (cx - 1.6, 5.6), (cx - 0.4, 7.4), (cx + 0.4, 7.4), (cx + 1.6, 5.6), (cx + 2.0, 7.6),
             (cx + 5.0, 8.4), (cx + 8.0, 10.4), (cx + 9.0, 13.4), (cx + 6.0, 15.4), (cx, 16.0), (cx - 6.0, 15.4)]
    knobs = [(lambda X, Y: ((np.round(X) * 2 + np.round(Y)) % 4 == 0), 1), (lambda X, Y: ((np.round(X) + np.round(Y) * 3) % 7 == 0), '#6a7a3a')]
    def frame(f, idle):
        P = []
        for side in (-1, 1):
            for k in range(4):
                up = 1.2 if (not idle and (k + f + (side > 0)) % 2 == 0 and f % 2 == 1) else 0.0
                hip = (cx + side * (6.4 - k * 0.6), 12.4 + k * 0.7); knee = (cx + side * (14.0 + k * 1.2), 9.4 + k * 1.4 - up * 0.5)
                foot = (cx + side * (17.0 + k * 1.4), 21.6 - up)
                P.append(part(cap([hip, knee], 0.6), legr, z=1 + k * 0.01, shade='flat', tone=2 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
                P.append(part(cap([knee, foot], 0.5), legr, z=1 + k * 0.01, shade='flat', tone=1 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
        P.append(part(carap, shell, z=3, name='shell', marks=knobs, lightc=(0.3, 0.4, 1.4, 1.2)))
        for side in (-1, 1):
            P.append(part(cap([(cx + side * 4.0, 14.8), (cx + side * 4.6, 17.0), (cx + side * 3.4, 18.6)], 0.7), shell, z=4, shade='flat', tone=3, outline=False, name='arm%d' % side))
            o = 0.5 * PH[f] if not idle else 0
            P.append(part(cap([(cx + side * 3.4, 18.6), (cx + side * (1.8 + o), 19.2)], 0.5), ramp('#e8d0b8'), z=4.1, shade='flat', tone=3, outline=False, name='tip'))
        return P, [(cx - 2.6, 9.0, EYE), (cx + 2.6, 9.0, EYE)]
    return Crawler('mediterranean_spider_crab', frame, 48, 26)
def giant_isopod():
    # Bathynomus giganteus: huge pill-bug of the deep, lilac-grey segmented armour plates, a broad head shield with big compound eyes,
    # short antennae, seven pairs of walking legs beneath, a fan-like tail plate
    shell = ramp('#a8a0b4'); legr = ramp('#c8c0c8')
    seg = [(lambda X, Y, x0=x0: np.abs(X - x0) < 0.5, -1) for x0 in np.arange(8.0, 32.0, 3.0)]
    top = [(2.0, 18.6), (3.0, 16.4)] + [(x, 18.6 - 6.4 * math.sin((x - 2.0) / 36.0 * math.pi) ** 0.7) for x in np.linspace(4.0, 36.0, 17)] + [(38.0, 17.6), (38.4, 19.0)]
    shape = top + [(36.0, 19.2), (4.0, 19.2)]
    def frame(f, idle):
        ph = PH[f]; P = [part(shape, shell, z=3, name='shell', marks=seg + [(lambda X, Y: Y > 18.2, 1)], lightc=(0.25, 0.35, 1.4, 1.2))]
        for k, x in enumerate(np.linspace(30.0, 8.0, 7)):
            up = 0.7 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line([(x, 19.0), (x + 0.8, 20.2 - up), (x + 0.4 + 0.6 * up, 21.6 - up)], legr[2], z=4))
        P.append(part(ell(35.0, 14.8, 1.6, 1.3), ramp('#2a2430'), z=3.5, shade='flat', tone=3, outline=False, name='eye'))
        sw = 0.4 * ph * (0 if idle else 1)
        P.append(line([(37.6, 16.6), (40.4, 15.4 + sw), (42.4, 16.4 + sw)], legr[1], z=4)); P.append(line([(37.4, 17.4), (40.0, 17.6 - sw)], legr[1], z=4))
        P.append(part([(2.4, 18.4), (0.2, 17.2), (0.0, 19.0), (2.2, 19.4)], shell, z=2.9, name='tailfan', tone=2))
        return P, [(35.4, 14.4, '#5a5068')]
    return Crawler('giant_isopod', frame, 46, 24)
def trumpet_triton():
    # Charonia: big, tall, trumpet-shaped spiral shell patterned with cream and brown crescents, a flared orange aperture with white
    # ridges, a pale orange foot spotted dark and two tentacles; the shell stays fixed while the foot glides
    shell = ramp('#c8a070'); foot = ramp('#d8a070')
    pat = [(lambda X, Y: np.abs(((X * 0.6 - Y) % 2.6) - 1.3) < 0.5, '#6a3e22'), (lambda X, Y: ((np.round(X) + np.round(Y)) % 4 == 0), 1)]
    def frame(f, idle):
        ext = 0.8 if idle else [0.8, 1.6, 0.8, 0][f]; sw = 0.5 * PH[f]
        P = [part(cap([(5.0, 18.6), (24.0 + ext, 18.4), (28.0 + ext, 18.8)], [1.9, 1.9, 1.2]), foot, z=1, name='foot',
                  marks=[(lambda X, Y: (np.round(X) * 3 + np.round(Y)) % 5 == 0, '#6a3a22')])]
        P += _spiral_shell(16.0, 13.2, 6.8, 7, -13.0, -9.6, 0.86, -34, shell, pat)
        P.append(part(ell(21.4, 15.4, 2.4, 3.2, 20), ramp('#e8904a', sig=True), z=3.5, shade='flat', tone=3, name='ap', marks=[(lambda X, Y: np.round(Y) % 2 == 0, '#f0e0c8')]))
        P.append(line([(25.6 + ext, 17.4), (28.4 + ext, 15.0 - sw)], '#b88050', z=4)); P.append(line([(26.2 + ext, 17.8), (29.4 + ext, 17.0 + sw)], '#b88050', z=4))
        return P, [(26.0 + ext, 17.2, '#141210')]
    return Crawler('trumpet_triton', frame, 34, 26, prefix='crawl_')
SCENE = {
    'madeira_rockfish': dict(speed=4, fps=6, bob_amount=0.0, move_time=(0.5, 2), idle_time=(4, 10), crowd_radius=(50, 8)),
    'blackface_blenny': dict(speed=7, fps=8, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(35, 8)),
    'leopard_spotted_goby': dict(speed=7, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(40, 8)),
    'steinitzs_cave_goby': dict(speed=7, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(40, 8)),
    'bentuvias_goby': dict(speed=7, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(35, 8)),
    'liechtensteins_goby': dict(speed=6, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(30, 8)),
    'common_octopus': dict(speed=5, fps=6, bob_amount=0.0, move_time=(1, 3), idle_time=(3, 8), crowd_radius=(60, 8)),
    'caribbean_spiny_lobster': dict(speed=8, fps=7, bob_amount=0.5, move_time=(1, 4), idle_time=(2, 5), crowd_radius=(75, 8)),
    'slipper_lobster': dict(speed=6, fps=7, bob_amount=0.0, move_time=(1, 3), idle_time=(3, 6), crowd_radius=(50, 8)),
    'banded_coral_shrimp': dict(speed=7, fps=8, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 5), crowd_radius=(45, 8)),
    'hawaiian_red_shrimp': dict(speed=6, fps=9, bob_amount=0.5, move_time=(1, 3), idle_time=(1, 3), crowd_radius=(20, 8)),
    'mediterranean_spider_crab': dict(speed=8, fps=7, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 5), crowd_radius=(55, 8)),
    'giant_isopod': dict(speed=5, fps=7, bob_amount=0.0, move_time=(2, 5), idle_time=(3, 8), crowd_radius=(55, 8)),
    'trumpet_triton': dict(speed=2, fps=5, move_prefix='crawl_', bob_amount=0.0, move_time=(6, 10), idle_time=(2, 6), crowd_radius=(35, 8)),
}
