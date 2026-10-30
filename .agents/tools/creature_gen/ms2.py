"""Marsh Swamp batch 2 - medium and large swimmers, defined from species names only.
v3 (Oct 2026): one memorable set per species, coloured from the ms colour families (pal.FAM_MS)."""
import numpy as np
import pal; pal.use('ms')
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots
from sp1 import bands, np_r
from ms1 import low
GOLD = ['#6f5c00', '#957f23', '#a99039', '#d0be79', '#e0d199', '#ede5c7']   # gold belly ramp lifted two steps: breasts and bellies stay bright gold under the belly shading
def gold_belly(bd): bd[-1] = (1.01, 1.01, list(GOLD)); return bd
ALL = ['crucian_carp', 'rudd', 'tench', 'european_perch', 'ruffe', 'pumpkinseed', 'amur_sleeper', 'mandarin_fish', 'black_bullhead',
       'grass_pickerel', 'asian_swamp_eel', 'european_eel', 'northern_snakehead', 'northern_pike', 'wels_catfish']
CARP = [(0, .34, -.34), (.1, .5, -.48), (.28, .88, -.82), (.46, 1, -.98), (.62, 1, -.98), (.76, .88, -.86), (.88, .62, -.6), (.95, .36, -.34), (1, .1, -.12)]
PERCH = [(0, .34, -.34), (.1, .46, -.44), (.28, .86, -.78), (.44, 1, -.94), (.6, 1, -.96), (.76, .88, -.88), (.88, .62, -.66), (.96, .34, -.38), (1, .1, -.18)]
SUNF = [(0, .34, -.34), (.1, .52, -.5), (.26, .86, -.84), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.82), (.84, .74, -.6), (.92, .46, -.38), (.97, .22, -.24), (1, .04, -.14)]
PIKE = [(0, .36, -.36), (.08, .5, -.48), (.24, .82, -.8), (.44, .98, -.96), (.62, 1, -.98), (.76, .94, -.92), (.86, .7, -.68), (.94, .46, -.46), (1, .24, -.3)]
EEL = [(0, .1, -.1), (.06, .5, -.5), (.2, .84, -.84), (.4, .98, -.98), (.6, 1, -1), (.8, .98, -.96), (.9, .86, -.8), (.96, .6, -.56), (1, .26, -.3)]
def crucian_carp():
    # set: deep carp with a HIGH-ARCHED back and no barbels / plain brass-bronze body / a long convex dorsal / a dark SPOT on the tail
    # base / rounded brass fins, slightly notched tail
    F = Fish('crucian_carp', 32, 17, CARP, bands('O1', 'O1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=15, eye=(0.84, 0.4, 2, '#d0b060'))
    B = F.B; F.tone0, F.tspan = -0.4, 4.4   # deeper bronze body that keeps its highlight
    F.marks += [m_spot(B, .05, .5, 1.6, FAM['O1'][0])]
    F.fins += [caudal(B, 'emarg', 8.0, col=fc('O1')), dorsal(B, .22, .64, 5.4, 'round', col=FAM['O1'][3], lean=0.2, n=14), anal(B, .14, .3, 4.2, 'round', col=fc('O1')),
               pelvic(B, .5, 3.8, col=fc('O1')), pectoral(B, .78, .66, 4.4, col=fc('N1'))]
    return F
def rudd():
    # set: deep compressed cyprinid with an upturned mouth / reed-green back over a brass flank / blazing CRIMSON pelvic, anal and tail
    # fins / red-orange eye / dorsal set behind the pelvics
    F = Fish('rudd', 32, 13.6, CARP, bands('G1', 'O1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=15, eye=(0.84, 0.42, 2, '#d8501c'))
    B = F.B; F.tone0, F.tspan = -0.1, 4.0; red = FAM['R1'][3]
    F.fins += [caudal(B, 'fork', 8.0, col=red, sig=True), dorsal(B, .32, .48, 5.0, 'tri', col=FAM['G1'][3], lean=0.5), anal(B, .14, .32, 4.0, 'tri', col=red, sig=True),
               pelvic(B, .56, 3.6, col=red, sig=True), pectoral(B, .78, .66, 4.0, col=fc('N1'))]
    return F
def tench():
    # set: THICK smooth-skinned fish with a thick tail stalk / dark reed-green with a brass sheen on the flank, no pattern / a tiny RED
    # EYE / big rounded dark fins / one short barbel at the mouth corner
    P = [(0, .48, -.48), (.1, .58, -.58), (.3, .86, -.86), (.5, 1, -1), (.66, 1, -.98), (.8, .88, -.86), (.9, .66, -.62), (.96, .4, -.36), (1, .14, -.14)]
    F = Fish('tench', 38, 14, P, bands('G1', 'O1', 'O1', b1=(0.4, 0.44), b2=(0.86, 0.86)), tilt=12, eye=(0.86, 0.4, 2, '#d0301c'))
    B = F.B; F.tone0 = 0.6; fin = FAM['G1'][2]
    F.fins += [caudal(B, 'truncate', 8.0, col=fin), dorsal(B, .38, .56, 5.2, 'round', col=fin, n=10), anal(B, .14, .3, 4.2, 'round', col=fin),
               pelvic(B, .5, 4.6, col=fin), pectoral(B, .78, .7, 4.6, col=FAM['G1'][3]), barbel(B, .98, .6, 1.6, -40, FAM['O1'][3])]
    return F
def european_perch():
    # set: HUMP-backed perch / reed-green with six dark vertical BARS / a black SPOT at the rear of the spiny dorsal / CRIMSON pelvic,
    # anal and lower tail lobe
    F = Fish('european_perch', 34, 13.4, PERCH, bands('G1', 'G1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=14, eye=(0.84, 0.4, 2, '#d0a040'))
    B = F.B; red = FAM['R1'][3]
    F.marks += [m_bar(B, u, 2.0, 0, .76, FAM['G1'][0], lean=0.2) for u in np_r(.14, .66, 6)]
    d1 = dorsal(B, .48, .7, 5.0, 'spiny', col=FAM['G1'][3], lean=0.2, n=11); d1['band'] = [(lambda X, Y, B=B: (X < .54 * B.L) & (Y < B.top(X) + 3.4), '#121608')]
    t = caudal(B, 'emarg', 8.0, col=fc('G1')); t['band'] = [(lambda X, Y, B=B: Y < (B.top(0) + B.bot(0)) / 2 - 0.6, red)]
    F.fins += [t, d1, dorsal(B, .24, .46, 4.4, 'round', col=fc('G1'), n=9), anal(B, .16, .3, 3.8, 'round', col=red, sig=True), pelvic(B, .6, 3.8, col=red, sig=True),
               pectoral(B, .76, .56, 4.0, col=fc('N1'))]
    return F
def ruffe():
    # set: small big-headed perch / peat-brown sprinkled with dark spots / one long joined dorsal crossed by ROWS of black spots /
    # violet eye
    F = Fish('ruffe', 26, 9.6, PERCH, bands('N2', 'N2', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=18, eye=(0.82, 0.4, 2, '#8d3d67'))
    B = F.B; F.tone0 = 0.4; k = FAM['N2'][0]
    F.marks += [m_spot(B, u, t, .7, k) for u, t in scatter(8, .12, .74, .14, .62, seed=0.23, gap=0.1)]
    d = dorsal(B, .2, .72, 4.0, 'spiny', col=fc('N2'), lean=0.2, n=18)
    pts = [((.26 + .08 * i) * B.L, B.top((.26 + .08 * i) * B.L) + h) for i in range(6) for h in (1.4, 3.0)]
    d['band'] = [fin_spots(pts, 0.6, '#1a140a')]
    F.fins += [caudal(B, 'emarg', 6.0, col=fc('N2')), d, anal(B, .16, .3, 3.0, 'round', col=fc('N2')), pelvic(B, .6, 3.0, col=fc('N1')),
               pectoral(B, .76, .56, 3.6, col=fc('N1'))]
    return F
def pumpkinseed():
    # set: deep sunfish / reed-green with crimson-coral SPOTS / wavy INDIGO lines on the cheek / black EAR FLAP tipped with a crimson
    # spot / GOLD breast and belly
    F = Fish('pumpkinseed', 28, 16, SUNF, gold_belly(bands('G1', 'G1', 'Y1', b1=(0.36, 0.4), b2=(0.7, 0.7))), tilt=15, eye=(0.81, 0.36, 2, '#c03a24'))
    B = F.B; F.tone0, F.tspan = -0.4, 4.4
    F.marks += [m_spot(B, u, t, .7, FAM['R1'][3]) for u, t in scatter(7, .22, .64, .2, .58, seed=0.37, gap=0.09)]
    F.marks += [m_stripe(B, .82, .96, [(.82, .54), (.96, .48)], 1.0, FAM['B1'][3]), m_stripe(B, .8, .94, [(.8, .66), (.94, .6)], 1.0, FAM['B1'][3]),
                m_spot(B, .73, .36, 1.4, '#10140a'), m_spot(B, .69, .37, .8, FAM['R1'][2])]
    F.fins += [caudal(B, 'emarg', 6.6, col=fc('G1')), dorsal(B, .16, .72, 4.8, 'round', col=FAM['G1'][3], lean=0.2, n=16), anal(B, .12, .4, 4.2, 'round', col=fc('G1')),
               pelvic(B, .62, 3.6, col=FAM['Y1'][3], sig=True), pectoral(B, .72, .58, 4.4, col=fc('N1'))]
    return F
def amur_sleeper():
    # set: chunky SLEEPER with a big head and a wide mouth / dark peat-brown with darker soft BLOTCHES / two rounded dorsals / rounded
    # fins with rows of dark dots and a PALE EDGE
    P = [(0, .44, -.44), (.1, .56, -.56), (.3, .86, -.88), (.5, 1, -1), (.68, .98, -.98), (.82, .88, -.86), (.92, .66, -.6), (.97, .42, -.36), (1, .16, -.18)]
    F = Fish('amur_sleeper', 30, 11.6, P, bands('N2', 'N2', 'N2', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=16, eye=(0.84, 0.36, 2, '#c8a050'))
    B = F.B; F.tone0 = 0.3
    F.marks += [m_spot(B, u, t, 1.4, -2) for u, t in ((.2, .4), (.36, .3), (.5, .5), (.64, .34), (.3, .62), (.76, .56))]
    fin = FAM['N2'][2]; dots = '#1e180e'; edge = FAM['N2'][4]
    c = caudal(B, 'round', 7.0, col=fin); c['band'] = [(lambda X, Y: X < -5.6, edge), fin_spots([(-2.4, 2.0), (-2.6, -1.6), (-4.2, 0.2), (-4.0, 3.2), (-4.0, -3.0)], 0.6, dots)]
    d1 = dorsal(B, .52, .66, 4.4, 'round', col=fin, n=8); d2 = dorsal(B, .22, .46, 4.6, 'round', col=fin, n=10)
    for d, (u0, u1) in ((d1, (.52, .66)), (d2, (.22, .46))):
        d['band'] = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 3.4, edge), fin_spots([((u0 + (u1 - u0) * f) * B.L, B.top((u0 + (u1 - u0) * f) * B.L) + 1.8) for f in (.2, .5, .8)], 0.6, dots)]
    F.fins += [c, d1, d2, anal(B, .2, .4, 4.0, 'round', col=fin, n=9), pelvic(B, .66, 3.4, col=FAM['N2'][3]), pectoral(B, .76, .56, 4.6, width=0.55, col=FAM['N2'][3])]
    return F
def mandarin_fish():
    # set: deep AMBUSH predator with a HUGE mouth / brass-gold LEOPARD body with big irregular dark blotches / a black STRIPE from the
    # snout through the eye to the dorsal base / long spiny dorsal
    P = [(0, .36, -.36), (.1, .52, -.5), (.28, .86, -.84), (.46, 1, -.98), (.62, 1, -.98), (.76, .9, -.9), (.86, .7, -.74), (.94, .42, -.52), (1, .14, -.36)]
    F = Fish('mandarin_fish', 42, 18, P, bands('O1', 'Y1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=13, eye=(0.86, 0.4, 3, '#c8a040'))
    B = F.B; k = FAM['O1'][0]
    F.marks += [m_spot(B, u, t, 1.6 + (i % 3) * 0.4, k, aspect=1.3) for i, (u, t) in enumerate(scatter(9, .1, .72, .2, .7, seed=0.53, gap=0.12))]
    F.marks += [m_stripe(B, .72, 1.0, [(.72, .1), (1, .42)], 1.4, '#14120a')]
    F.fins += [caudal(B, 'round', 9.0, col=fc('O1')), dorsal(B, .14, .72, 6.4, 'spiny', col=FAM['O1'][3], lean=0.2, n=20), anal(B, .12, .34, 5.0, 'round', col=fc('O1')),
               pelvic(B, .62, 4.4, col=fc('O1')), pectoral(B, .76, .56, 5.0, col=fc('N1'))]
    return F
def black_bullhead():
    # set: stout CATFISH / charcoal-black back over a pale gold belly / dark whisker barbels / square tail with a PALE BAR across its
    # base / adipose fin
    P = [(0, .44, -.44), (.1, .58, -.58), (.3, .88, -.9), (.55, 1, -1), (.75, .96, -.96), (.88, .8, -.84), (.96, .5, -.6), (1, .22, -.38)]
    F = Fish('black_bullhead', 34, 11.4, P, gold_belly(bands('N1', 'N1', 'Y1', b1=(0.4, 0.44), b2=(0.78, 0.78))), tilt=12, eye=(0.88, 0.32, 2, '#8a8460'))
    B = F.B; F.tone0 = 0.0; dk = FAM['N1'][1]
    t = caudal(B, 'truncate', 6.6, col=dk); t['band'] = [(lambda X, Y: (X > -1.8), FAM['Y1'][4])]
    F.fins += [t, dorsal(B, .52, .64, 4.6, 'tri', col=dk, n=6), adipose(B, .18, 3.4, 2.2, col=dk), anal(B, .1, .3, 3.4, 'round', col=dk, n=9),
               pelvic(B, .46, 3.0, col=dk), pectoral(B, .82, .72, 4.4, ang=-8, width=0.35, col=FAM['N1'][2]),
               barbel(B, .99, .5, 5.0, 0, '#22221a'), barbel(B, .97, .8, 3.4, -45, '#1a1a12'), barbel(B, .95, .9, 3.0, -75, '#1a1a12'), barbel(B, .97, .25, 2.4, 30, '#22221a')]
    return F
def grass_pickerel():
    # set: small DUCKBILL pike / brass-olive with NINE wavy dark vertical BARS / a dark TEARDROP bar under the eye / dorsal and anal set
    # far back / forked tail
    F = Fish('grass_pickerel', 40, 8.6, PIKE, bands('O1', 'O1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=10, eye=(0.86, 0.36, 2, '#d0b060'))
    B = F.B; k = FAM['O1'][0]
    F.marks += [m_bar(B, u, 1.4, .1, .84, k, lean=(0.5 if j % 2 else -0.5)) for j, u in enumerate(np_r(.1, .74, 9))] + [m_bar(B, .87, 1.2, .5, .98, '#14120a')]
    F.fins += [caudal(B, 'fork', 7.4, col=fc('O1')), dorsal(B, .06, .2, 4.2, 'round', col=fc('O1'), n=8), anal(B, .04, .18, 4.0, 'round', col=fc('O1'), n=8),
               pelvic(B, .4, 3.0, col=fc('N1')), pectoral(B, .82, .7, 3.6, col=fc('N1'))]
    return F
def asian_swamp_eel():
    # set: slick EEL with NO paired fins and only a low fold round the pointed tail / peat-olive with a few dark speckles / pale gold
    # belly / small eye, blunt snout
    F = Fish('asian_swamp_eel', 52, 6.4, EEL, gold_belly(bands('N2', 'N2', 'Y1', b1=(0.4, 0.44), b2=(0.76, 0.76))), tilt=8, eye=(0.92, 0.34, 1, '#a89060'))
    B = F.B; F.tone0 = 0.2
    F.marks += [m_spot(B, u, t, .6, FAM['N2'][0]) for u, t in scatter(10, .06, .9, .12, .5, seed=0.61, gap=0.07)]
    F.fins += [dorsal(B, .0, .2, 1.2, 'flat', col=fc('N2'), n=8), anal(B, .0, .16, 1.0, 'flat', col=fc('N2'), n=6)]
    return F
def european_eel():
    # set: long snake-like YELLOW EEL / dark reed-green back over a gold-cream belly / small PECTORAL fins / one continuous fin from
    # mid-back round the tail to the belly
    F = Fish('european_eel', 58, 6.8, EEL, gold_belly(bands('G1', 'G1', 'Y1', b1=(0.44, 0.48), b2=(0.72, 0.72))), tilt=8, eye=(0.92, 0.36, 1, '#a8a070'))
    B = F.B; F.tone0 = 0.3
    df = dorsal(B, .0, .62, 2.0, 'flat', col=FAM['G1'][3], n=26, amp=0.7); df['wave'] = 2.5
    af = anal(B, .0, .5, 1.8, 'flat', col=FAM['G1'][3], n=22, amp=0.7); af['wave'] = 2.5
    F.fins += [caudal(B, 'round', 2.4, col=FAM['G1'][3]), df, af, pectoral(B, .86, .5, 2.6, col=fc('Y1'))]
    return F
def northern_snakehead():
    # set: long cylinder with a SNAKE-LIKE head / mahogany-tan with big dark PYTHON BLOTCHES in two rows / long low dorsal and anal
    # fins along most of the body / a dark streak behind the eye / rounded tail
    P = [(0, .4, -.4), (.1, .56, -.54), (.3, .86, -.84), (.5, .98, -.96), (.7, 1, -.98), (.84, .9, -.86), (.94, .6, -.58), (1, .28, -.3)]
    F = Fish('northern_snakehead', 52, 10.6, P, bands('M1', 'N2', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=9, eye=(0.9, 0.36, 2, '#c8a050'))
    B = F.B; k = '#1e1410'
    F.marks += [m_spot(B, u, .3, 2.0, k, aspect=1.4) for u in np_r(.1, .8, 7)] + [m_spot(B, u, .64, 1.8, k, aspect=1.3) for u in np_r(.16, .76, 6)]
    F.marks += [m_stripe(B, .84, 1.0, [(.84, .5), (1, .46)], 1.2, k)]
    fin = FAM['M1'][3]
    F.fins += [caudal(B, 'round', 8.0, col=fin), dorsal(B, .06, .78, 3.4, 'flat', col=fin, n=26), anal(B, .06, .5, 3.0, 'flat', col=fin, n=18),
               pelvic(B, .72, 2.8, col=fc('N2')), pectoral(B, .84, .6, 4.2, col=fc('N2'))]
    return F
def northern_pike():
    # set: long reed-green PIKE / rows of pale BEAN-SHAPED SPOTS / duckbill snout / dorsal and anal set far back / fins blotched dark /
    # forked tail
    F = Fish('northern_pike', 64, 11.6, PIKE, bands('G1', 'G1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=8, eye=(0.86, 0.36, 3, '#d0b058'))
    B = F.B; F.tone0 = 0.2; pale = FAM['O1'][4]
    F.marks += [m_spot(B, u, t, .9, pale, aspect=1.8) for u, t in scatter(16, .08, .78, .26, .66, seed=0.19, gap=0.06)]
    fin = FAM['G1'][3]; blot = FAM['G1'][1]
    c = caudal(B, 'fork', 11.0, col=fin); c['band'] = [fin_spots([(-3.0, 2.0), (-5.6, -2.4), (-7.6, 4.0), (-7.8, -4.4), (-4.4, 5.2)], 0.9, blot)]
    d = dorsal(B, .06, .2, 6.0, 'round', col=fin, n=9); d['band'] = [fin_spots([(.1 * B.L, B.top(.1 * B.L) + 2.4), (.16 * B.L, B.top(.16 * B.L) + 4.0)], 0.9, blot)]
    a = anal(B, .04, .18, 5.6, 'round', col=fin, n=9); a['band'] = [fin_spots([(.1 * B.L, B.bot(.1 * B.L) - 2.6)], 0.9, blot)]
    F.fins += [c, d, a, pelvic(B, .4, 4.4, col=fc('G1')), pectoral(B, .82, .7, 5.0, col=fc('N1'))]
    return F
def wels_catfish():
    # set: HUGE scaleless catfish with a broad flat head / slate-grey back marbled darker over a pale belly / TWO VERY LONG WHISKERS and
    # four short chin barbels / tiny dorsal, long anal fin reaching the tail
    P = [(0, .3, -.3), (.08, .46, -.46), (.24, .8, -.8), (.44, .96, -.96), (.62, 1, -1), (.78, .96, -.96), (.88, .8, -.84), (.95, .52, -.6), (1, .24, -.36)]
    F = Fish('wels_catfish', 70, 13.6, P, bands('S1', 'S1', 'N1', b1=(0.44, 0.48), b2=(0.8, 0.8)), tilt=8, eye=(0.92, 0.32, 2, '#a89a6a'))
    B = F.B; F.tone0, F.tspan = -0.8, 4.4; k = FAM['S1'][0]
    F.marks += [m_spot(B, u, t, 1.6 + (i % 3) * 0.5, k, aspect=1.6) for i, (u, t) in enumerate(scatter(10, .06, .88, .12, .52, seed=0.47, gap=0.08))]
    fin = FAM['S1'][2]
    F.fins += [caudal(B, 'round', 8.0, col=fin), dorsal(B, .62, .68, 3.4, 'tri', col=fin, n=5), anal(B, .02, .6, 3.6, 'flat', col=FAM['S1'][3], n=28),
               pelvic(B, .58, 3.0, col=FAM['S1'][3]), pectoral(B, .86, .74, 4.6, ang=-10, col=FAM['S1'][3]),
               barbel(B, .98, .38, 16, 4, FAM['S1'][1], thick=0.6), barbel(B, .96, .9, 3.0, -70, FAM['S1'][3]), barbel(B, .93, .94, 2.6, -80, FAM['S1'][3])]
    return F
SCENE = {
    'crucian_carp': dict(band=(120, 250), speed=14, fps=8, crowd=70, rest=(1.0, 3.0)),
    'rudd': dict(band=(20, 180), speed=22, fps=9, crowd=65),
    'tench': dict(band=(170, 256), speed=12, fps=7, crowd=85, rest=(1.5, 4.0)),
    'european_perch': dict(band=(60, 220), speed=20, fps=8, crowd=70),
    'ruffe': dict(band=(190, 256), speed=14, fps=9, crowd=50, rest=(1.0, 3.0)),
    'pumpkinseed': dict(band=(70, 220), speed=16, fps=8, crowd=60),
    'amur_sleeper': dict(band=(170, 256), speed=12, fps=8, crowd=55, rest=(2.0, 5.0)),
    'mandarin_fish': dict(band=(140, 250), speed=14, fps=7, crowd=95, rest=(2.0, 5.0)),
    'black_bullhead': dict(band=(196, 258), speed=14, fps=8, crowd=70, rest=(1.0, 3.0)),
    'grass_pickerel': dict(band=(20, 180), speed=14, fps=8, crowd=80, rest=(2.0, 5.0)),
    'asian_swamp_eel': dict(band=(210, 258), speed=10, fps=7, crowd=70, rest=(1.5, 4.0)),
    'european_eel': dict(band=(190, 258), speed=12, fps=7, crowd=90, rest=(1.0, 3.0)),
    'northern_snakehead': dict(band=(40, 220), speed=14, fps=7, crowd=100, rest=(2.0, 5.0)),
    'northern_pike': dict(band=(20, 200), speed=16, fps=7, crowd=130, rest=(2.0, 5.0)),
    'wels_catfish': dict(band=(200, 256), speed=12, fps=6, crowd=150, rest=(1.5, 4.0)),
}
