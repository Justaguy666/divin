"""Cold Water batch 2 - cod family, mackerel, john dory, big wrasses, dogfish, wolffish, lumpfish, cuttlefish; species names only."""
import numpy as np
from swim import Fish, tooth, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
from tidy import tidy
from cw1 import WRASSE, GAD, wfins, gfins
import pal; pal.use('cw')
from pal import ramp
ALL = ['atlantic_cod', 'haddock', 'pollock', 'ling', 'atlantic_mackerel', 'john_dory', 'ballan_wrasse', 'tautog', 'lumpfish', 'spiny_dogfish',
       'atlantic_wolffish', 'common_cuttlefish']
def atlantic_cod():
    # Gadus morhua: heavy cod, olive-brown to greenish back and sides densely leopard-spotted, a pale lateral line arching over the
    # pectoral, white belly, three dorsals and two anals, a long chin barbel, square tail
    F = Fish('atlantic_cod', 60, 15.4, GAD, bands('#4a5232', '#9a9a62', '#e4e2d0'), tilt=11, eye=(0.86, 0.36, 2, '#c8b880'))
    B = F.B; rng = np.random.RandomState(11)
    F.marks += [m_spot(B, u, t, .6, '#3a3a20') for u, t in zip(rng.uniform(.06, .86, 46), rng.uniform(.1, .7, 46))]
    F.marks += [m_stripe(B, .04, .8, [(0, .5), (.4, .46), (.7, .3), (.8, .3)], .6, '#e8e6d0')]
    F.fins += gfins(B, '#848656', s=1.4); F.gill = (.8, .2, .85, 1.6); F.mouth = (.6, 2.4); return F
def haddock():
    # Melanogrammus aeglefinus: dark purple-grey back, silver sides, a black lateral line, a dark blotch above the pectoral (the devil's
    # thumbprint), a tall pointed first dorsal, slightly forked tail, small chin barbel
    F = Fish('haddock', 54, 14, GAD, bands('#3e4250', '#a8acb4', '#e6e8ea'), tilt=11, eye=(0.86, 0.36, 2, '#c8c8c0'))
    B = F.B
    F.marks += [m_stripe(B, .04, .82, [(0, .5), (.4, .44), (.7, .3), (.82, .3)], .7, '#141418'), m_spot(B, .7, .44, 1.6, '#16161c')]
    fins = gfins(B, '#7a7e8a', s=1.3, cau=('emarg', 6.0)); fins[1] = dorsal(B, .58, .7, 7.0, 'tri', col='#7a7e8a', lean=0.6, n=6)
    F.fins += fins; F.gill = (.8, .2, .85, 1.6); F.mouth = (.6, 2.0); return F
def pollock():
    # Pollachius pollachius (pollack): streamlined cod with a projecting lower jaw and no barbel, golden-olive to bronze back, silvery
    # sides, a dark lateral line curving up over the pectoral, three dorsals and two anals, slightly forked tail
    P = [(0, .3, -.3), (.1, .42, -.4), (.28, .8, -.76), (.46, .98, -.94), (.62, 1, -.98), (.76, .92, -.92), (.88, .7, -.74), (.95, .42, -.52), (1, .1, -.36)]
    F = Fish('pollock', 56, 13.4, P, bands('#5a5430', '#b8ae78', '#e4e0cc'), tilt=11, eye=(0.86, 0.38, 2, '#c8b880'))
    B = F.B
    F.marks += [m_stripe(B, .04, .84, [(0, .5), (.5, .46), (.72, .26), (.84, .26)], .7, '#2a2814')]
    fins = gfins(B, '#9a9064', s=1.3, cau=('emarg', 6.4)); fins = fins[:-1]
    F.fins += fins; F.gill = (.8, .2, .85, 1.6); F.mouth = (.6, 2.6); return F
def ling():
    # Molva molva: long, eel-like cod, mottled brown and olive, a long second dorsal and anal both edged white, a dark spot at the rear
    # of the first dorsal, a chin barbel, rounded tail
    P = [(0, .3, -.3), (.06, .5, -.5), (.2, .84, -.84), (.4, 1, -1), (.6, 1, -1), (.78, .94, -.94), (.9, .74, -.78), (.96, .46, -.54), (1, .18, -.32)]
    F = Fish('ling', 80, 11, P, bands('#4a4430', '#8a7e5a', '#d4ccb0'), tilt=8, eye=(0.88, 0.36, 2, '#c8b080'))
    B = F.B; rng = np.random.RandomState(12)
    F.marks += [m_spot(B, u, t, 1.4 + .8 * rng.rand(), -1) for u, t in zip(rng.uniform(.04, .86, 22), rng.uniform(.12, .7, 22))]
    white = [(lambda X, Y, B=B: (Y > B.top(np.clip(X, 0, B.L)) + 2.2) | (Y < B.bot(np.clip(X, 0, B.L)) - 2.0), '#e8e8e0')]
    d1 = dorsal(B, .66, .76, 3.6, 'round', col='#706448', n=6); d1['band'] = [(lambda X, Y, B=B: X < .69 * B.L, '#1a1810')]
    d2 = dorsal(B, .04, .64, 2.8, 'flat', col='#706448', n=26, lean=0.1); d2['band'] = white
    a = anal(B, .04, .56, 2.6, 'flat', col='#7a6e50', n=22, lean=0.1); a['band'] = white
    F.fins += [caudal(B, 'round', 6.0, col='#706448'), d1, d2, a, pelvic(B, .8, 3.0, col='#8a7e5e'), pectoral(B, .78, .5, 4.4, col='#9a8e6c'), barbel(B, .95, .96, 2.6, -80, '#8a7e5e')]
    F.gill = (.82, .2, .85, 1.6); F.mouth = (.6, 3.0); return F
def atlantic_mackerel():
    # Scomber scombrus: torpedo-shaped, iridescent blue-green back with bold dark wavy tiger bars, silver-white belly, two small dorsals set
    # far apart, a row of little finlets before the deeply forked tail
    P = [(0, .2, -.2), (.08, .36, -.34), (.24, .74, -.72), (.44, .98, -.96), (.6, 1, -.98), (.74, .9, -.88), (.86, .66, -.62), (.94, .4, -.34), (1, .12, -.1)]
    F = Fish('atlantic_mackerel', 46, 9.4, P, bands('#2a7a86', '#c0d8d4', '#f0f2ee', sig=('back',)), tilt=12, eye=(0.86, 0.42, 2, '#d0d8d0'))
    B = F.B
    F.marks += [m_stripe(B, u, u + .12, [(u, .02), (u + .04, .3), (u + .08, .1), (u + .12, .42)], 1.3, '#0e1e24') for u in np_r(.08, .68, 7)]
    F.fins += [caudal(B, 'deepfork', 7.4, col='#5a7a80'), dorsal(B, .54, .66, 3.6, 'tri', col='#4a6a70', lean=0.4, n=6), dorsal(B, .3, .38, 2.6, 'tri', col='#5a7a80', n=4),
               anal(B, .28, .36, 2.4, 'tri', col='#9ab0b0', n=4)]
    F.fins += [tooth(B, u, 0, ln=0.3, gap=0.3, col='#4a6a70') for u in np_r(.08, .24, 4)] + [tooth(B, u, 1, ln=0.3, gap=0.3, col='#8aa0a0') for u in np_r(.08, .24, 4)]
    F.fins += [pelvic(B, .66, 2.4, col='#c8d4d0'), pectoral(B, .8, .5, 3.0, col='#7a989a')]
    F.gill = (.82, .2, .85, 1.3); F.mouth = (.56, 1.6); return tidy(F, 4)
def john_dory():
    # Zeus faber: very deep, thin, oval body, olive-grey to golden with wavy lines, a big black eyespot ringed pale yellow in the middle of
    # the flank, long spiny dorsal rays trailing filaments, a huge upturned protrusible mouth, spiny bony plates along the dorsal and
    # anal bases
    P = [(0, .2, -.2), (.08, .4, -.4), (.2, .76, -.76), (.36, .98, -.98), (.52, 1, -1), (.66, .92, -.92), (.78, .76, -.74), (.88, .54, -.5), (.95, .34, -.3), (1, .2, -.18)]
    F = Fish('john_dory', 36, 26, P, bands('#5a5a40', '#b8ac80', '#d8ccaa'), tilt=13, eye=(0.84, 0.36, 2, '#d8c070'))
    B = F.B
    F.marks += [m_spot(B, .52, .52, 3.0, '#e8d890'), m_spot(B, .52, .52, 2.2, '#121210')]
    F.marks += [m_stripe(B, .14, .78, [(.14, t), (.4, t + .05), (.6, t - .04), (.78, t)], .6, -1) for t in (.24, .76)]
    spines = dorsal(B, .48, .74, 9.0, 'spiny', col='#7a7456', lean=0.9, n=10)
    F.fins += [caudal(B, 'round', 6.4, col='#8a8460'), spines, dorsal(B, .14, .46, 4.0, 'round', col='#8a8460', lean=0.4, n=10), anal(B, .14, .44, 3.8, 'round', col='#8a8460', n=10),
               pelvic(B, .66, 6.0, col='#6a6448'), pectoral(B, .76, .52, 3.6, col='#a8a07c')]
    F.mouth = (.4, 3.0); return F
def ballan_wrasse():
    # Labrus bergylta: big, thick-lipped wrasse, green-brown to reddish-brown, every scale with a pale centre so the flank is covered in
    # pale spots, mottled darker, long spiny-soft dorsal, rounded tail
    F = Fish('ballan_wrasse', 46, 15, WRASSE, bands('#3e4a30', '#7a7a4c', '#c8b88a'), tilt=13, eye=(0.85, 0.36, 2, '#c8803a'))
    B = F.B; rng = np.random.RandomState(13)
    F.marks += [m_spot(B, u, t, 1.6 + .6 * rng.rand(), -1) for u, t in zip(rng.uniform(.1, .7, 8), rng.uniform(.15, .75, 8))]
    F.marks += [m_spot(B, u, t, .45, '#d8d0a8') for k, t in enumerate((.24, .36, .48, .6, .72)) for u in np_r(.08 + (k % 2) * .04, .76, 9)]
    F.fins += wfins(B, '#6e6c46', d=(.18, .76, 5.0), a=(.14, .38, 4.4), cau=('round', 8.0)); F.gill = (.76, .2, .85, 1.5); F.mouth = (.56, 1.6); return F
def tautog():
    # Tautoga onitis (blackfish): stout wrasse with a steep rounded forehead and thick lips, dark grey-black to olive with darker blotches,
    # a pale chin, long spiny-soft dorsal, rounded tail
    P = [(0, .36, -.36), (.1, .5, -.48), (.3, .86, -.82), (.5, 1, -.96), (.66, 1, -.96), (.8, .96, -.84), (.9, .8, -.6), (.96, .54, -.4), (1, .2, -.28)]
    F = Fish('tautog', 44, 15, P, bands('#2a2c28', '#4e5048', '#8a8a7c'), tilt=13, eye=(0.85, 0.34, 2, '#c8a050'))
    B = F.B; rng = np.random.RandomState(14)
    F.marks += [m_spot(B, u, t, 1.6 + .6 * rng.rand(), -1) for u, t in zip(rng.uniform(.1, .7, 9), rng.uniform(.15, .75, 9))] + [m_region(B, .9, 1.0, .7, 1.0, '#c8c4b4')]
    F.fins += wfins(B, '#4a4c44', d=(.18, .76, 4.8), a=(.14, .38, 4.2), cau=('round', 7.4)); F.gill = (.76, .2, .85, 1.5); F.mouth = (.6, 1.6); return F
def lumpfish():
    # Cyclopterus lumpus: globular, almost round fish with three rows of bony knobs along each side, a skin-covered hump instead of a
    # first dorsal, a small soft second dorsal and anal near the tail, blue-grey to green, sucker disc underneath
    P = [(0, .36, -.36), (.08, .6, -.58), (.2, .9, -.86), (.4, 1.04, -1), (.58, 1.18, -1), (.72, 1.1, -.96), (.84, .88, -.8), (.93, .6, -.56), (1, .28, -.3)]
    F = Fish('lumpfish', 30, 20, P, bands('#3e5a5a', '#7a9490', '#b8c4b0'), tilt=12, eye=(0.84, 0.4, 2, '#c8b880'))
    B = F.B
    F.marks += [m_spot(B, u, t, .7, '#d0dcd4') for t in (.08, .44, .8) for u in np_r(.18, .78, 6)] + [m_spot(B, u, t, .4, '#2a3a3a') for t in (.09, .45, .81) for u in np_r(.18, .78, 6)]
    F.fins += [caudal(B, 'round', 6.0, col='#5e7a78'), dorsal(B, .14, .3, 3.6, 'round', col='#5e7a78', n=6), anal(B, .14, .28, 3.2, 'round', col='#6a8682', n=6),
               pectoral(B, .78, .6, 4.4, width=0.55, col='#7a948e')]
    F.mouth = (.5, 1.4); return F
def spiny_dogfish():
    # Squalus acanthias: slender little shark, slate grey with rows of small white spots along the flanks, pale belly, a sharp spine in
    # front of each of the two dorsal fins, no anal fin, pointed snout, big green eye, tail with a longer upper lobe
    P = [(0, .26, -.24), (.08, .42, -.38), (.22, .74, -.68), (.42, .98, -.92), (.6, 1, -.94), (.76, .9, -.86), (.88, .66, -.64), (.95, .4, -.44), (1, .14, -.28)]
    F = Fish('spiny_dogfish', 72, 10.6, P, bands('#4a5258', '#8c9498', '#d8dcdc'), tilt=9, eye=(0.86, 0.36, 2, '#8ab8a0'))
    B = F.B
    F.marks += [m_spot(B, u, t, .6, '#e8ecec') for t, us in ((.3, np_r(.14, .74, 9)), (.46, np_r(.2, .68, 7))) for u in us]
    F.fins += [caudal(B, 'hetero', 10.0, col='#6a7276', upper=1.3, lower=0.7), dorsal(B, .54, .64, 4.6, 'tri', col='#5e666a', lean=0.7, n=6),
               dorsal(B, .2, .29, 3.6, 'tri', col='#5e666a', lean=0.7, n=5), tooth(B, .645, 0, ln=1.2, gap=0.2, col='#e0e4e4'), tooth(B, .295, 0, ln=1.0, gap=0.2, col='#e0e4e4'),
               pelvic(B, .3, 3.0, col='#7a8286'), pectoral(B, .72, .76, 6.0, ang=-30, width=0.42, col='#6e767a')]
    F.gill = (.74, .2, .7, 1.0); F.mouth = (.84, 1.6); return F
def atlantic_wolffish():
    # Anarhichas lupus: long, heavy, eel-like fish with a big blunt head and strong protruding canine teeth, blue-grey to olive with ten or
    # more dark vertical bars, a long dorsal fin running the length of the back, a long anal, small rounded tail
    P = [(0, .26, -.26), (.06, .44, -.44), (.2, .8, -.8), (.4, .98, -.96), (.6, 1, -.98), (.78, 1, -.96), (.88, .9, -.86), (.95, .66, -.64), (1, .3, -.36)]
    F = Fish('atlantic_wolffish', 76, 13, P, bands('#3e4a54', '#7e8a92', '#b8bebe'), tilt=8, eye=(0.88, 0.34, 2, '#c8b890'))
    B = F.B
    F.marks += [m_bar(B, u, 2.2, .04, .74, '#2a323a', lean=0.4) for u in np_r(.08, .76, 11)] + [m_region(B, .97, 1.0, .6, .92, '#e8e4d4')]
    F.fins += [caudal(B, 'round', 6.0, col='#5e6a72'), dorsal(B, .06, .84, 3.6, 'flat', col='#5e6a72', lean=0.1, n=32), anal(B, .06, .5, 3.0, 'flat', col='#6a767c', n=20),
               pectoral(B, .82, .7, 5.4, width=0.55, col='#76828a')]
    F.fins += [tooth(B, .985, 1, ln=0.8, gap=0.0, col='#ece8d8'), tooth(B, .965, 1, ln=0.6, gap=0.0, col='#ece8d8')]
    F.mouth = (.66, 3.6); return tidy(F, 4)
def common_cuttlefish():
    # Sepia officinalis: broad oval mantle fringed all round by a thin rippling fin, zebra-striped brown and cream on the back (male
    # display) with pale spots, a big eye with a W-shaped pupil, eight short arms held together in a point in front of the head
    P = [(0, .4, -.4), (.06, .7, -.7), (.2, .92, -.92), (.42, 1, -1), (.62, .96, -.96), (.7, .8, -.82), (.76, .86, -.86), (.82, .74, -.74), (.9, .46, -.48), (1, .14, -.18)]
    F = Fish('common_cuttlefish', 40, 15, P, bands('#5a4632', '#a88a68', '#d8c8b0'), tilt=10, eye=(0.78, 0.44, 3, '#d8c070'), backward=True)
    B = F.B
    F.marks += [m_bar(B, u, 1.0, .06, .44, '#3a2a1c', lean=-0.3) for u in np_r(.08, .62, 7)] + [m_dash(B, .06, .66, .5, .7, '#ece4d4', 2.0, 1.0)]
    F.marks += [m_spot(B, u, .7, .6, '#e0d4bc') for u in np_r(.12, .56, 5)]
    F.marks += [m_region(B, .83, 1.0, 0, 1, '#b8a084')] + [m_stripe(B, .84, 1.0, t, .5, '#6a5440') for t in (.3, .5, .7)]
    df = dorsal(B, .02, .68, 2.8, 'flat', col='#d8c8ac', lean=0.0, n=30, amp=0.9, alpha=(200, 150)); df['wave'] = 3.0
    af = anal(B, .02, .68, 2.8, 'flat', col='#d8c8ac', lean=0.0, n=30, amp=0.9, alpha=(200, 150)); af['wave'] = 3.0
    F.fins += [df, af] + [barbel(B, .98, t, 2.6, a, '#b8a084', thick=0.55) for t, a in ((.3, 12), (.5, 0), (.7, -12))]
    return F
SCENE = {
    'atlantic_cod': dict(band=(120, 250), speed=18, fps=8, crowd=110, rest=(1.0, 3.0)),
    'haddock': dict(band=(140, 250), speed=18, fps=8, crowd=100),
    'pollock': dict(band=(40, 200), speed=24, fps=8, crowd=100),
    'ling': dict(band=(190, 256), speed=12, fps=7, crowd=130, rest=(2.0, 5.0)),
    'atlantic_mackerel': dict(band=(0, 140), speed=34, fps=9, crowd=70),
    'john_dory': dict(band=(60, 220), speed=10, fps=7, crowd=80, rest=(2.0, 5.0)),
    'ballan_wrasse': dict(band=(120, 245), speed=14, fps=8, crowd=90, rest=(1.0, 3.0)),
    'tautog': dict(band=(140, 250), speed=14, fps=8, crowd=85, rest=(1.0, 3.0)),
    'lumpfish': dict(band=(100, 240), speed=8, fps=7, crowd=65, rest=(2.0, 5.0)),
    'spiny_dogfish': dict(band=(80, 240), speed=20, fps=7, crowd=120),
    'atlantic_wolffish': dict(band=(200, 258), speed=10, fps=6, crowd=130, rest=(2.0, 5.0)),
    'common_cuttlefish': dict(band=(80, 230), speed=10, fps=7, crowd=80, rest=(1.5, 4.0)),
}
