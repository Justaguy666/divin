"""Marsh Swamp batch 1 - small swimmers (bitterlings, sticklebacks, killifish, pygmy sunfish...), defined from species names only.
v3 (Oct 2026): one memorable set per species, coloured from the ms colour families (pal.FAM_MS: brass / reed green / gold analogous
to the olive swamp water, pearl and peat neutrals, slate and mahogany muted complements, crimson / rose / indigo accents)."""
import numpy as np
import pal; pal.use('ms')
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots
from sp1 import bands, np_r
ALL = ['european_bitterling', 'rosy_bitterling', 'sunbleak', 'medaka', 'topmouth_gudgeon', 'three_spined_stickleback', 'ninespine_stickleback',
       'okefenokee_pygmy_sunfish', 'blackbanded_sunfish', 'bluespotted_sunfish', 'banded_killifish', 'northern_redbelly_dace', 'golden_shiner',
       'paradise_fish', 'frog_tadpole']
MIN = [(0, .32, -.32), (.1, .42, -.42), (.28, .74, -.72), (.45, .94, -.92), (.6, 1, -.98), (.74, .92, -.9), (.86, .7, -.66), (.94, .42, -.38), (1, .08, -.1)]
DEEPS = [(0, .32, -.32), (.1, .5, -.48), (.26, .86, -.84), (.44, 1, -.98), (.6, 1, -.96), (.74, .9, -.84), (.86, .68, -.6), (.94, .4, -.34), (1, .08, -.1)]
SUNF = [(0, .34, -.34), (.1, .52, -.5), (.26, .86, -.84), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.82), (.84, .74, -.6), (.92, .46, -.38), (.97, .22, -.24), (1, .04, -.14)]
def sfins(B, col, d=(.38, .58, 4.0), a=(.2, .34, 2.8), cau=('fork', 6.4), pcol=None):
    return [caudal(B, cau[0], cau[1], col=col), dorsal(B, d[0], d[1], d[2], 'tri', col=col, lean=0.6), anal(B, a[0], a[1], a[2], 'tri', col=col),
            pelvic(B, .5, 2.4, col=pcol or col), pectoral(B, .76, .66, 3.0, col=pcol or col)]
def low(F, k=0.3): F.tone0 += k; return F   # fish of the dark low water lean on the light tones
def european_bitterling():
    # set: small DEEP pearl-silver bitterling / a short indigo-blue SHEEN STRIPE on the rear half only /
    # a ROSE THROAT and belly (breeding) / red upper iris / clear fins
    F = Fish('european_bitterling', 22, 10.4, DEEPS, bands('N1', 'N1', 'N1', b1=(0.34, 0.38), b2=(0.84, 0.84)), tilt=20, eye=(0.82, 0.38, 2, '#c8402a'))
    B = F.B
    F.marks += [m_stripe(B, .04, .48, [(.04, .5), (.48, .48)], 1.6, FAM['B1'][3])]
    F.patches.append((lambda X, Y, U, T: (T > .62) & (U > .5), FAM['R2']))
    F.fins += sfins(B, fc('N1'), d=(.36, .6, 4.2), pcol=FAM['R2'][4]); return F
def rosy_bitterling():
    # set: deep bitterling whose breeding male glows ROSE-VIOLET all over / a pale indigo sheen stripe toward the tail / CRIMSON
    # dorsal and anal fins with a dark edge / crimson eye
    F = Fish('rosy_bitterling', 22, 10.8, DEEPS, bands('R2', 'R2', 'N1', sig=('flank',), b1=(0.34, 0.38), b2=(0.82, 0.82)), tilt=20, eye=(0.82, 0.38, 2, '#d04030'))
    B = F.B
    F.marks += [m_stripe(B, .04, .44, [(.04, .5), (.44, .48)], 1.4, FAM['B1'][4])]
    red = FAM['R1'][3]; edge = FAM['R1'][0]
    d = dorsal(B, .36, .6, 4.4, 'tri', col=red, lean=0.6, sig=True); d['band'] = [(lambda X, Y, B=B: Y > B.top(X) + 3.2, edge)]
    a = anal(B, .2, .34, 3.0, 'tri', col=red, sig=True); a['band'] = [(lambda X, Y, B=B: Y < B.bot(X) - 2.2, edge)]
    F.fins += [caudal(B, 'fork', 6.4, col=FAM['R2'][4]), d, a, pelvic(B, .5, 2.4, col=red, sig=True), pectoral(B, .76, .66, 3.0, col=fc('N1'))]
    return F
def sunbleak():
    # set: slender little SILVERFISH of the surface / slate back / one BRIGHT SILVER BAND along the whole side with a dark upper edge /
    # upturned mouth / clear fins
    F = Fish('sunbleak', 24, 7.4, MIN, bands('S1', 'N1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=25, eye=(0.82, 0.4, 2, '#d0d0c0'))
    B = F.B
    F.marks += [m_stripe(B, .04, .86, [(.04, .5), (.86, .48)], 1.6, FAM['N1'][5]), m_stripe(B, .06, .84, [(.06, .38), (.84, .36)], 1.0, FAM['S1'][1])]
    F.fins += sfins(B, fc('S1')); return F
def medaka():
    # set: TINY rice fish with a flat back, upturned mouth and a BIG EYE / translucent brass with one pale line along the side /
    # a LONG ANAL FIN under a small dorsal set far back / square tail
    P = [(0, .36, -.36), (.1, .46, -.46), (.3, .76, -.82), (.5, .9, -1.0), (.66, .94, -.96), (.8, .9, -.82), (.9, .78, -.6), (.96, .6, -.3), (1, .38, -.06)]
    F = Fish('medaka', 21, 7.0, P, bands('O1', 'O1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=25, eye=(0.8, 0.36, 3, '#d8d8c0'))
    B = F.B
    F.marks += [m_stripe(B, .08, .74, [(.08, .5), (.74, .48)], 1.0, FAM['O1'][5]), m_hline(B, .1, .7, 0.0, 1.0, FAM['O1'][1])]
    F.fins += [caudal(B, 'truncate', 5.0, col=fc('O1')), dorsal(B, .16, .26, 2.4, 'round', col=fc('O1'), n=6), anal(B, .1, .52, 2.6, 'flat', col=fc('O1'), n=14),
               pelvic(B, .54, 2.0, col=fc('N1')), pectoral(B, .78, .4, 2.8, col=fc('N1'))]
    return F
def topmouth_gudgeon():
    # set: small minnow with a tiny UPTURNED mouth / brass back, pearl flank with one bold dark STRIPE from the snout to the tail / a loose row of
    # dark scale CRESCENTS above it / clear grey fins
    F = Fish('topmouth_gudgeon', 23, 8.2, MIN, bands('O1', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=25, eye=(0.82, 0.38, 2, '#c8c098'))
    B = F.B; F.lightc = (0.32, 0.45, 0.9, 1.3); F.tone0 = 1.2   # silver: the belly stays light
    F.marks += [m_stripe(B, .02, .96, [(0, .5), (1, .46)], 1.4, FAM['N1'][0])]
    F.marks += [m_spot(B, u, .24, .6, FAM['O1'][1], aspect=1.5) for u in (.22, .38, .54)]
    F.fins += sfins(B, fc('O1'), pcol=fc('N1')); return F
def three_spined_stickleback():
    # set: breeding male stickleback / reed-green back over a slate-silver flank / a blazing CRIMSON THROAT and belly / pale BLUE eye /
    # THREE free spines in front of the dorsal and a strong pelvic spine / slender keeled tail stalk
    P = [(0, .2, -.2), (.1, .28, -.28), (.26, .64, -.64), (.44, .92, -.92), (.6, 1, -1), (.74, .94, -.92), (.86, .72, -.66), (.94, .42, -.36), (1, .1, -.1)]
    F = Fish('three_spined_stickleback', 22, 8.6, P, bands('G1', 'S1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=22, eye=(0.82, 0.4, 2, '#a5bfec'))
    B = F.B
    F.patches.append((lambda X, Y, U, T: (T > .56) & (U > .48), FAM['R1']))
    sp = [dorsal(B, u, u + .04, 3.6, 'tri', col=FAM['G1'][2], lean=-0.2, n=3, amp=0.2) for u in (.76, .64, .52)]
    F.fins += [caudal(B, 'truncate', 5.4, col=fc('G1')), dorsal(B, .18, .4, 3.0, 'round', col=fc('G1'), n=8), anal(B, .16, .36, 2.6, 'round', col=fc('N1'), n=8),
               pelvic(B, .58, 3.4, ang=-40, col=FAM['G1'][2]), pectoral(B, .76, .5, 3.2, col=fc('N1'))] + sp
    return F
def ninespine_stickleback():
    # set: slender stickleback with a row of NINE small spines along the back / brass-olive with five soft dark bars / the breeding
    # male's BLACK THROAT / narrow tail stalk
    P = [(0, .2, -.2), (.1, .3, -.3), (.26, .64, -.64), (.44, .9, -.9), (.6, 1, -.98), (.76, .94, -.9), (.88, .7, -.62), (.95, .4, -.34), (1, .1, -.1)]
    F = Fish('ninespine_stickleback', 23, 7.0, P, bands('O1', 'O1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=22, eye=(0.82, 0.4, 2, '#c8b070'))
    B = F.B
    F.marks += [m_bar(B, u, 1.8, .04, .7, FAM['O1'][1]) for u in (.14, .28, .42, .56, .7)]
    F.marks += [(lambda x, y, uu, tt: (uu > .7) & (tt > .6), '#16160e')]
    sp = [dorsal(B, u, u + .025, 2.0, 'tri', col=FAM['O1'][2], lean=-0.1, n=3, amp=0.2) for u in np_r(.42, .74, 9)]
    F.fins += [caudal(B, 'truncate', 5.0, col=fc('O1')), dorsal(B, .18, .36, 2.6, 'round', col=fc('O1'), n=8), anal(B, .16, .34, 2.4, 'round', col=fc('O1'), n=8),
               pelvic(B, .58, 2.4, ang=-40, col=FAM['O1'][2]), pectoral(B, .76, .5, 3.0, col=fc('N1'))] + sp
    return F
def okefenokee_pygmy_sunfish():
    # set: TINY near-black sunfish / charcoal body sprinkled with bright INDIGO-BLUE flecks / two faint bars / every fin edged in blue /
    # rounded tail
    F = Fish('okefenokee_pygmy_sunfish', 19, 8.6, SUNF, bands('N1', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=18, eye=(0.8, 0.38, 2, '#a5bfec'))
    B = F.B; F.tone0 = -0.2; blue = FAM['B1'][4]
    F.marks += [m_spot(B, u, t, .6, blue) for u, t in scatter(8, .2, .74, .2, .7, seed=0.17, gap=0.1)]
    F.marks += [m_bar(B, u, 1.6, .1, .9, FAM['N1'][0]) for u in (.32, .52)]
    dk = FAM['N1'][2]
    fins = [caudal(B, 'round', 5.2, col=dk), dorsal(B, .2, .62, 3.6, 'round', col=dk, n=12), anal(B, .16, .38, 3.0, 'round', col=dk, n=8),
            pelvic(B, .6, 2.6, col=dk), pectoral(B, .72, .56, 3.0, col=fc('N1', 3))]
    fins[0]['band'] = [(lambda X, Y: X < -4.0, FAM['B1'][3])]
    fins[1]['band'] = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 2.8, FAM['B1'][3])]
    fins[2]['band'] = [(lambda X, Y, B=B: Y < B.bot(np.clip(X, 0, B.L)) - 2.2, FAM['B1'][3])]
    for f in fins[:3]: f['sig'] = True
    F.fins += fins; return F
def blackbanded_sunfish():
    # set: deep pearl DISC with five bold BLACK BANDS (the first through the eye) / black front of the dorsal / a CRIMSON front edge on
    # the pelvic fins / rounded tail
    F = Fish('blackbanded_sunfish', 22, 13.2, SUNF, bands('N1', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=16, eye=(0.8, 0.38, 2, '#c8b080'))
    B = F.B; F.tone0 = 1.3; k = '#121410'
    F.marks += [m_bar(B, u, 2.2, 0, 1.0, k) for u in (.08, .3, .5, .66, .82)]
    d = dorsal(B, .18, .66, 4.6, 'round', col=fc('N1', 3), n=14); d['band'] = [(lambda X, Y, B=B: X > .5 * B.L, k)]
    F.fins += [caudal(B, 'round', 6.0, col=fc('N1')), d, anal(B, .14, .4, 4.0, 'round', col=fc('N1', 3), n=10),
               pelvic(B, .6, 3.4, col=FAM['R1'][3], sig=True), pectoral(B, .72, .58, 3.6, col=fc('N1'))]
    return F
def bluespotted_sunfish():
    # set: deep DARK reed-green sunfish sprinkled with shining BLUE SPOTS / a black EAR SPOT / red eye / dusky rounded fins with a few
    # blue spots
    F = Fish('bluespotted_sunfish', 22, 12.6, SUNF, bands('G1', 'G1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=16, eye=(0.8, 0.38, 2, '#c03a24'))
    B = F.B; F.tone0 = -0.2; blue = FAM['B1'][4]
    F.marks += [m_spot(B, u, t, .65, blue) for u, t in scatter(11, .14, .68, .2, .76, seed=0.41, gap=0.09)] + [m_spot(B, .74, .36, 1.2, '#10140c')]
    d = dorsal(B, .18, .66, 4.4, 'round', col=FAM['G1'][2], n=14); d['band'] = [fin_spots([(.3 * B.L, B.top(.3 * B.L) + 2.6), (.48 * B.L, B.top(.48 * B.L) + 2.0)], 0.6, blue)]
    F.fins += [caudal(B, 'round', 6.0, col=FAM['G1'][2]), d, anal(B, .14, .4, 3.8, 'round', col=FAM['G1'][2], n=10),
               pelvic(B, .6, 3.2, col=FAM['G1'][3]), pectoral(B, .72, .58, 3.4, col=fc('G1'))]
    return F
def banded_killifish():
    # set: slender flat-headed killifish of the surface / brass-olive with EIGHT thin dark vertical BARS on the rear two thirds / pearl
    # belly / dorsal set far back over the anal / square tail
    P = [(0, .34, -.34), (.1, .44, -.44), (.3, .76, -.8), (.5, .92, -1.0), (.66, .96, -.96), (.8, .86, -.8), (.9, .66, -.56), (.96, .44, -.3), (1, .22, -.06)]
    F = Fish('banded_killifish', 25, 8.0, P, bands('O1', 'O1', 'N1', b1=(0.36, 0.4), b2=(0.84, 0.84)), tilt=22, eye=(0.82, 0.36, 2, '#c8c090'))
    B = F.B
    F.marks += [m_bar(B, u, 1.0, .16, .84, FAM['O1'][0]) for u in np_r(.08, .66, 8)]
    F.fins += [caudal(B, 'truncate', 5.6, col=fc('O1')), dorsal(B, .24, .42, 3.4, 'round', col=fc('O1'), n=8), anal(B, .2, .4, 3.0, 'round', col=fc('O1'), n=8),
               pelvic(B, .5, 2.2, col=fc('N1')), pectoral(B, .76, .58, 3.0, col=fc('N1'))]
    return F
def northern_redbelly_dace():
    # set: small dace / brass back / TWO DARK STRIPES - the upper one breaking into dashes toward the head - over a CRIMSON belly /
    # pale gold fins
    F = Fish('northern_redbelly_dace', 22, 7.8, MIN, bands('O1', 'O1', 'R1', sig=('belly',), b1=(0.36, 0.4), b2=(0.7, 0.7)), tilt=25, eye=(0.82, 0.4, 2, '#c8a050'))
    B = F.B; k = '#16180a'
    F.marks += [m_stripe(B, .06, .52, .32, 1.2, k), m_spot(B, .62, .32, .8, k, aspect=1.5), m_spot(B, .74, .32, .8, k, aspect=1.5),
                m_stripe(B, 0, 1.0, [(0, .54), (1, .52)], 1.8, k)]
    F.fins += sfins(B, FAM['Y1'][4], pcol=FAM['Y1'][4]); return F
def golden_shiner():
    # set: deep compressed shiner / a GOLD flank under a brass-olive back / one thin lateral line that DIPS low under the belly curve /
    # small upturned mouth / crimson-tinted pelvic and anal fins
    P = [(0, .32, -.32), (.1, .46, -.46), (.28, .82, -.86), (.46, 1, -1.0), (.62, 1, -.98), (.76, .88, -.82), (.88, .62, -.52), (.95, .38, -.24), (1, .14, -.04)]
    F = Fish('golden_shiner', 30, 12.4, P, bands('O1', 'Y1', 'N1', sig=('flank',), b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=16, eye=(0.84, 0.4, 2, '#d8c070'))
    B = F.B
    F.marks += [m_stripe(B, .04, .82, [(0, .5), (.4, .64), (.82, .46)], 1.0, FAM['Y1'][1])]
    F.fins += [caudal(B, 'fork', 8.0, col=fc('O1')), dorsal(B, .38, .54, 5.2, 'tri', col=fc('O1'), lean=0.6), anal(B, .12, .36, 3.4, 'tri', col=FAM['R1'][4]),
               pelvic(B, .5, 2.8, col=FAM['R1'][4]), pectoral(B, .76, .66, 3.4, col=fc('N1'))]
    return F
def paradise_fish():
    # set: the BANDED labyrinth fish - alternating INDIGO and CRIMSON vertical bands over a charcoal body / a blue-black GILL SPOT
    # ringed crimson / long flowing indigo dorsal and anal / deeply forked crimson tail with trailing filaments / thread pelvics
    P = [(0, .36, -.36), (.1, .5, -.5), (.3, .82, -.84), (.5, .98, -1.0), (.66, 1, -.98), (.8, .88, -.84), (.9, .64, -.6), (.96, .36, -.32), (1, .1, -.1)]
    F = Fish('paradise_fish', 26, 10.4, P, bands('N1', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=18, eye=(0.82, 0.38, 2, '#d0503a'))
    B = F.B; F.tone0 = 0.8; red = FAM['R1'][3]; blue = FAM['B1'][3]
    F.marks += [m_bar(B, u, 1.8, .08, .94, red) for u in (.12, .3, .48)] + [m_bar(B, u, 1.8, .08, .94, blue) for u in (.21, .39, .57)]
    F.marks += [m_spot(B, .76, .4, 1.4, red), m_spot(B, .76, .4, .9, '#121c2c')]
    F.fins += [caudal(B, 'deepfork', 10.0, col=red, sig=True), dorsal(B, .06, .56, 6.0, 'trib', col=blue, sig=True, lean=0.6, n=14, ray_every=3),
               anal(B, .04, .6, 6.0, 'trib', col=blue, sig=True, lean=0.6, n=14, ray_every=3), pelvic(B, .62, 6.0, ang=-75, col=red, sig=True), pectoral(B, .76, .56, 3.2, col=fc('N1'))]
    return F
def frog_tadpole():
    # set: round BODY flowing into a long muscular TAIL with clear fin folds above and below / peat-brown with a few dark speckles and
    # pale gold flecks / eyes on the sides of the head / no paired fins
    P = [(0, .06, -.06), (.08, .18, -.18), (.3, .36, -.34), (.5, .56, -.56), (.6, .86, -.88), (.72, 1, -1), (.84, .98, -.98), (.93, .78, -.76), (.98, .44, -.42), (1, .1, -.14)]
    F = Fish('frog_tadpole', 24, 10.4, P, bands('N2', 'N2', 'N2', b1=(0.4, 0.4), b2=(0.75, 0.75)), tilt=18, eye=(0.88, 0.38, 2, '#c8b070'))
    B = F.B; low(F, 0.2)
    F.marks += [m_spot(B, u, t, .6, FAM['N2'][0]) for u, t in scatter(7, .36, .92, .16, .7, seed=0.29, gap=0.08)]
    F.marks += [m_spot(B, u, t, .5, FAM['Y1'][4]) for u, t in scatter(4, .62, .9, .2, .6, seed=0.71, gap=0.1)]
    fin = FAM['N2'][3]
    tf1 = dorsal(B, .0, .56, 3.0, 'round', col=fin, lean=0.2, n=16, amp=1.0); tf1['wave'] = 1.2
    tf2 = anal(B, .0, .5, 2.6, 'round', col=fin, lean=0.2, n=16, amp=1.0); tf2['wave'] = 1.2
    F.fins += [caudal(B, 'lance', 3.0, col=fin), tf1, tf2]
    return F
SCENE = {
    'european_bitterling': dict(band=(60, 220), speed=20, fps=10, crowd=45),
    'rosy_bitterling': dict(band=(60, 220), speed=20, fps=10, crowd=45),
    'sunbleak': dict(band=(0, 110), speed=30, fps=11, crowd=40),
    'medaka': dict(band=(0, 90), speed=22, fps=10, crowd=40),
    'topmouth_gudgeon': dict(band=(80, 230), speed=24, fps=10, crowd=45),
    'three_spined_stickleback': dict(band=(60, 230), speed=20, fps=10, crowd=45, rest=(0.8, 2.5)),
    'ninespine_stickleback': dict(band=(100, 240), speed=18, fps=10, crowd=40, rest=(0.8, 2.5)),
    'okefenokee_pygmy_sunfish': dict(band=(150, 250), speed=10, fps=8, crowd=35, rest=(1.5, 4.0)),
    'blackbanded_sunfish': dict(band=(100, 230), speed=14, fps=8, crowd=50, rest=(1.0, 3.0)),
    'bluespotted_sunfish': dict(band=(110, 240), speed=14, fps=8, crowd=50, rest=(1.0, 3.0)),
    'banded_killifish': dict(band=(4, 120), speed=22, fps=9, crowd=50),
    'northern_redbelly_dace': dict(band=(40, 200), speed=26, fps=10, crowd=45),
    'golden_shiner': dict(band=(30, 190), speed=26, fps=9, crowd=60),
    'paradise_fish': dict(band=(0, 150), speed=16, fps=8, crowd=55, rest=(1.0, 3.0)),
    'frog_tadpole': dict(band=(120, 256), speed=12, fps=10, crowd=40, rest=(1.0, 3.0)),
}
