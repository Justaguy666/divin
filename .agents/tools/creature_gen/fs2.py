"""Forest Stream batch 2 - minnows, suckers, sunfish, bass, percids, pike, shad, lamprey; defined from species names only.
v3 (Oct 2026): one memorable set per species, coloured from the fs colour families (pal.FAM_FS)."""
import numpy as np
import pal; pal.use('fs')
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots
from fs1 import low
from sp1 import bands, np_r
ALL = ['central_stoneroller', 'bluehead_chub', 'creek_chub', 'fallfish', 'northern_hog_sucker', 'white_sucker', 'river_redhorse', 'longear_sunfish',
       'rock_bass', 'smallmouth_bass', 'logperch', 'walleye', 'sauger', 'muskellunge', 'american_shad', 'american_brook_lamprey']
CHUB = [(0, .34, -.34), (.1, .46, -.44), (.3, .82, -.8), (.48, 1, -.96), (.64, 1, -.96), (.78, .9, -.86), (.9, .66, -.6), (.97, .36, -.32), (1, .12, -.14)]
SUCK = [(0, .34, -.34), (.1, .46, -.44), (.3, .84, -.8), (.48, 1, -.94), (.64, .98, -.94), (.78, .86, -.86), (.9, .62, -.66), (.97, .34, -.42), (1, .14, -.28)]
DEEP = [(0, .34, -.34), (.1, .52, -.5), (.26, .86, -.84), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.82), (.84, .74, -.6), (.92, .46, -.38), (.97, .22, -.24), (1, .04, -.14)]
PERC = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.8), (.5, .98, -.96), (.66, 1, -.96), (.8, .86, -.86), (.9, .62, -.64), (.97, .32, -.36), (1, .1, -.16)]
def mfins(B, col, d=(.4, .58, 5.0), a=(.18, .32, 3.6), cau=('fork', 8.0), pec=(.78, .66, 4.0), pcol=None):
    return [caudal(B, cau[0], cau[1], col=col), dorsal(B, d[0], d[1], d[2], 'tri', col=col, lean=0.5), anal(B, a[0], a[1], a[2], 'tri', col=col),
            pelvic(B, .5, 3.4, col=pcol or col), pectoral(B, pec[0], pec[1], pec[2], col=pcol or col)]
def central_stoneroller():
    # set: cylindrical algae scraper with a blunt snout over a hard jaw / moss back, brown-copper flank with a few dark scales / the
    # breeding FINS - dorsal crossed by a rust-orange band and a black band, rust band on the anal
    P = [(0, .36, -.36), (.1, .48, -.46), (.3, .84, -.82), (.5, 1, -.96), (.66, .98, -.96), (.8, .86, -.84), (.9, .64, -.58), (.96, .4, -.3), (1, .2, -.08)]
    F = Fish('central_stoneroller', 30, 10.4, P, bands('G1', 'R1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=20, eye=(0.82, 0.38, 2, '#c8a050'))
    B = F.B; F.tone0 = 0.8
    F.marks += [m_spot(B, u, t, 0.8, '#2a1a10') for u, t in scatter(6, .12, .78, .2, .6, seed=0.13, gap=0.1)]
    fins = mfins(B, fc('R1'), d=(.42, .6, 5.4), pcol=fc('N1')); fins[1]['sig'] = fins[2]['sig'] = True
    for k in (1, 2): fins[k]['col'] = pal.fin(FAM['R1'][3], True); fins[k]['alpha'] = (210, 150)
    fins[1]['band'] = [(lambda X, Y, B=B: (Y > B.top(X) + 1.6) & (Y < B.top(X) + 3.0), '#c65b4c'), (lambda X, Y, B=B: (Y > B.top(X) + 3.0) & (Y < B.top(X) + 4.2), '#1a1008')]
    fins[2]['band'] = [(lambda X, Y, B=B: (Y < B.bot(X) - 1.4) & (Y > B.bot(X) - 2.8), '#c65b4c')]
    F.fins += fins; return F
def bluehead_chub():
    # set: stout chub / moss back, pearl flank / a TURQUOISE HEAD with a swollen crest (breeding) / ROSE lower sides / faint dark
    # spot on the tail base / moss fins
    F = Fish('bluehead_chub', 32, 11.8, CHUB, bands('G1', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=18, eye=(0.82, 0.38, 2, '#c8a050'))
    B = F.B
    F.patches += [(lambda X, Y, U, T: (U > .78) & (T < .62), FAM['T1']), (lambda X, Y, U, T: (T > .64) & (U > .28) & (U < .74), FAM['R3'])]
    F.marks += [m_spot(B, .03, .5, 1.2, '#22261a')]
    F.fins += mfins(B, fc('G1'), pcol=fc('N1')); return F
def creek_chub():
    # set: big-mouthed chub / river-green back, pearl flank / dusky LATERAL STRIPE ending in a black CAUDAL SPOT / a black SPOT
    # at the front base of the dorsal / teal fins
    F = Fish('creek_chub', 34, 11.6, CHUB, bands('G2', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=18, eye=(0.82, 0.4, 2, '#c8b070'))
    B = F.B
    F.marks += [m_stripe(B, .06, .9, [(0, .5), (.9, .46)], 1.8, '#1e2a20'), m_spot(B, .04, .5, 1.4, '#101410')]
    fins = mfins(B, fc('G3')); fins[1]['band'] = [(lambda X, Y, B=B: (X > .55 * B.L) & (Y < B.top(X) + 2.2), '#101410')]
    F.fins += fins; return F
def fallfish():
    # set: the BIG silver minnow / river-green back, pearl-teal flank / two loose rows of dark scale CRESCENTS on the upper side /
    # plain teal fins, big forked tail
    F = Fish('fallfish', 40, 13.6, CHUB, bands('G2', 'G3', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=14, eye=(0.84, 0.4, 3, '#c8c4a0'))
    B = F.B
    for k, y in enumerate((3.6, 1.2)):
        def f(x, yy, uu, tt, y=y, k=k): return (uu > .1) & (uu < .8) & (np.abs(yy - y) <= 0.5) & (((x + 2.4 * k) % 4.8) < 2.0)
        F.marks.append((f, FAM['G2'][1]))
    F.fins += mfins(B, fc('G3'), d=(.42, .58, 5.6), cau=('fork', 9.4)); return F
def northern_hog_sucker():
    # set: broad FLAT head with a concave crown, body tapering behind / olive-brown with four bold dark OBLIQUE SADDLES / huge FAN pectorals /
    # sucker lips under the snout
    P = [(0, .36, -.36), (.1, .48, -.44), (.3, .84, -.76), (.5, 1, -.86), (.66, .96, -.9), (.78, .78, -.9), (.88, .62, -.8), (.96, .4, -.6), (1, .14, -.44)]
    F = Fish('northern_hog_sucker', 34, 11.0, P, bands('G1', 'G1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=14, eye=(0.8, 0.28, 2, '#c8a050'))
    B = F.B; low(F, 0.15)
    F.marks += [m_bar(B, u, 2.6, 0, .72, '#1a1c0c', lean=0.8) for u in (.14, .34, .54, .72)]
    F.fins += mfins(B, fc('G1'), pec=(.74, .74, 6.4)); return F
def white_sucker():
    # set: long cylindrical sucker with thick lips / moss back, pearl flank / a dark LATERAL BAND riding over a ROSE STRIPE (breeding) /
    # pale fins
    F = Fish('white_sucker', 40, 11.6, SUCK, bands('G1', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=14, eye=(0.82, 0.36, 2, '#c8c090'))
    B = F.B; low(F)
    F.marks += [m_stripe(B, .04, .9, .46, 1.8, -2), m_stripe(B, .1, .86, .62, 1.2, '#c4576d')]
    F.fins += mfins(B, fc('N1'), d=(.44, .6, 5.4)); return F
def river_redhorse():
    # set: big heavy sucker / copper-bronze body with two loose rows of dark scale crescents / BRICK-RED tail, dorsal and anal /
    # big head, sucker lips
    F = Fish('river_redhorse', 44, 15.4, SUCK, bands('R1', 'R1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=12, eye=(0.82, 0.38, 3, '#d0a848'))
    B = F.B; F.tone0 = 0.75; red = '#b6322b'
    for k, y in enumerate((3.2, 0.4)):
        def f(x, yy, uu, tt, y=y, k=k): return (uu > .1) & (uu < .8) & (np.abs(yy - y) <= 0.5) & (((x + 2.2 * k) % 4.4) < 2.0)
        F.marks.append((f, FAM['R1'][1]))
    F.fins += [caudal(B, 'fork', 10.0, col=red, sig=True), dorsal(B, .42, .62, 6.6, 'tri', col=red, sig=True, lean=0.5, n=11), anal(B, .16, .3, 4.6, 'tri', col=red, sig=True),
               pelvic(B, .5, 4.0, col='#c65b4c', sig=True), pectoral(B, .78, .7, 5.0, col=fc('R1'))]
    return F
def longear_sunfish():
    # set: the COLOURFUL sunfish / river-green back over a rust-orange BREAST / TURQUOISE wavy cheek lines / long black EAR FLAP with a
    # pale rim / orange flecks along the side / orange anal and pelvics
    F = Fish('longear_sunfish', 26, 16, DEEP, bands('G2', 'G2', 'R2', sig=('belly',), b1=(0.36, 0.4), b2=(0.7, 0.7)), tilt=15, eye=(0.81, 0.36, 2, '#c03a24'))
    B = F.B; F.tone0 = 0.75
    F.marks += [m_spot(B, u, t, 0.85, '#d16631') for u, t in ((.3, .32), (.46, .3), (.38, .5), (.24, .46), (.54, .48))]
    F.marks += [m_stripe(B, .82, .96, [(.82, .54), (.96, .48)], 1.0, '#0f9293'), m_stripe(B, .8, .94, [(.8, .66), (.94, .6)], 1.0, '#0f9293'),
                m_stripe(B, .6, .78, [(.6, .38), (.78, .36)], 2.2, '#efe5e2'), m_stripe(B, .61, .78, [(.61, .38), (.78, .36)], 1.4, '#0e140c')]
    F.fins += [caudal(B, 'emarg', 6.6, col=fc('G2')), dorsal(B, .16, .72, 4.8, 'round', col=FAM['G2'][3], lean=0.2, n=16), anal(B, .12, .4, 4.2, 'round', col='#c65b4c', sig=True),
               pelvic(B, .62, 3.6, col='#c65b4c', sig=True), pectoral(B, .72, .58, 4.4, col=fc('G2'))]
    return F
def rock_bass():
    # set: deep big-mouthed panfish / dark moss-olive with two lines of dark spots / a blazing RED EYE / dark spot on the gill cover /
    # big rounded soft dorsal and anal
    P = [(0, .34, -.34), (.1, .5, -.48), (.26, .84, -.82), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.86), (.84, .76, -.7), (.92, .5, -.52), (.97, .26, -.38), (1, .08, -.28)]
    F = Fish('rock_bass', 30, 15, P, bands('G1', 'G1', 'N1', b1=(0.4, 0.44), b2=(0.88, 0.88)), tilt=15, eye=(0.82, 0.36, 2, '#e0201a'))
    B = F.B; F.tone0 = 0.6
    for k, y in enumerate((1.4, -2.4)):
        def f(x, yy, uu, tt, y=y, k=k): return (uu > .1) & (uu < .72) & (np.abs(yy - y) <= 0.5) & (((x + 2.0 * k) % 4.0) < 2.0)
        F.marks.append((f, FAM['G1'][0]))
    F.marks += [m_spot(B, .74, .4, 1.1, '#121408')]
    F.fins += [caudal(B, 'emarg', 7.4, col=FAM['G1'][3]), dorsal(B, .14, .72, 5.8, 'round', col=FAM['G1'][3], lean=0.2, n=16), anal(B, .12, .4, 5.2, 'round', col=FAM['G1'][3]),
               pelvic(B, .62, 4.0, col=fc('G1')), pectoral(B, .74, .58, 4.6, col=fc('G1'))]
    return F
def smallmouth_bass():
    # set: copper-bronze bass / six faint vertical bars / three dark BARS RADIATING back from the orange eye / notched spiny + soft
    # dorsal, emarginate tail
    P = [(0, .34, -.34), (.1, .46, -.44), (.3, .82, -.8), (.48, .98, -.96), (.64, 1, -.98), (.78, .9, -.92), (.9, .66, -.74), (.97, .36, -.5), (1, .14, -.34)]
    F = Fish('smallmouth_bass', 44, 14.6, P, bands('R1', 'R1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=12, eye=(0.85, 0.36, 3, '#e0601c'))
    B = F.B; F.tone0 = 0.55
    F.marks += [m_bar(B, u, 2.2, .06, .76, -1) for u in np_r(.12, .66, 6)] + [m_stripe(B, .86, .98, [(.86, t + .04), (.98, t)], 1.2, '#24140c') for t in (.42, .56, .7)]
    F.fins += [caudal(B, 'emarg', 9.4, col=fc('R1')), dorsal(B, .44, .66, 5.4, 'spiny', col=FAM['R1'][3], lean=0.2, n=10), dorsal(B, .2, .44, 5.8, 'round', col=fc('R1'), lean=0.3, n=10),
               anal(B, .14, .32, 5.0, 'round', col=fc('R1')), pelvic(B, .6, 4.4, col=fc('N1')), pectoral(B, .76, .58, 5.0, col=fc('N1'))]
    return F
def logperch():
    # set: long darter with a PIG-LIKE conical snout / pale moss body / TIGER BARS alternating long and short / a rust-orange band on
    # the first dorsal / big paddle pectorals
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.76), (.5, .98, -.92), (.66, 1, -.94), (.8, .86, -.84), (.9, .62, -.6), (.96, .36, -.34), (1, .16, -.1)]
    F = Fish('logperch', 34, 9.0, P, bands('G1', 'G1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=14, eye=(0.82, 0.36, 2, '#c8a050'))
    B = F.B; low(F)
    F.marks += [m_bar(B, u, 2.0, 0, (.86 if k % 2 == 0 else .5), FAM['G1'][0]) for k, u in enumerate(np_r(.08, .8, 9))]
    d1 = dorsal(B, .5, .7, 3.6, 'spiny', col=fc('G1'), lean=0.3, n=10); d1['band'] = [(lambda X, Y, B=B: Y > B.top(X) + 2.0, '#c65b4c')]
    F.fins += [caudal(B, 'emarg', 6.4, col=fc('G1')), d1, dorsal(B, .24, .46, 3.6, 'round', col=fc('G1'), n=9), anal(B, .2, .34, 3.0, 'round', col=fc('N1')),
               pelvic(B, .6, 3.0, col=fc('N1')), pectoral(B, .76, .5, 4.6, width=0.55, col=fc('N1'))]
    return F
def walleye():
    # set: long moss-olive percid / five dark SADDLES / big pale GLASSY EYE / a black blotch at the rear of the spiny dorsal / WHITE TIP
    # on the lower tail lobe
    F = Fish('walleye', 50, 12.6, PERC, bands('G1', 'G1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=10, eye=(0.86, 0.36, 3, '#eef0e0'))
    B = F.B
    F.marks += [m_bar(B, u, 3.0, 0, .54, -2, lean=0.4) for u in np_r(.1, .72, 5)]
    d1 = dorsal(B, .48, .68, 5.4, 'spiny', col=fc('G1'), lean=0.3, n=10); d1['band'] = [(lambda X, Y, B=B: (X < .52 * B.L) & (Y < B.top(X) + 2.6), '#121408')]
    t = caudal(B, 'fork', 10.0, col=FAM['G1'][2], sig=True); t['band'] = [(lambda X, Y, B=B: (X < -5.0) & (Y < (B.top(0) + B.bot(0)) / 2 - 2.8), '#f4f6ee')]
    F.fins += [t, d1, dorsal(B, .24, .44, 4.8, 'round', col=fc('G1'), n=9), anal(B, .16, .3, 4.0, 'tri', col=fc('N1')), pelvic(B, .6, 4.0, col=fc('N1')),
               pectoral(B, .78, .56, 4.6, col=fc('N1'))]
    return F
def sauger():
    # set: the walleye's sandy cousin / four BLOTCHY dark saddles / rows of black SPOTS on the spiny dorsal / no white tail tip /
    # glassy eye
    F = Fish('sauger', 46, 11.6, PERC, bands('N1', 'N1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=10, eye=(0.86, 0.36, 3, '#e8e6d0'))
    B = F.B; low(F, 0.15)
    F.marks += [m_bar(B, u, 3.6, 0, .62, '#1e1a12', lean=0.6) for u in (.14, .34, .54, .72)]
    d1 = dorsal(B, .48, .68, 5.0, 'spiny', col=fc('N1'), lean=0.3, n=10)
    d1['band'] = [fin_spots([(.52 * B.L, B.top(.52 * B.L) + 2.0), (.58 * B.L, B.top(.58 * B.L) + 3.2), (.63 * B.L, B.top(.63 * B.L) + 1.8), (.55 * B.L - 1.0, B.top(.55 * B.L) + 4.2)], 0.7, '#1e100a')]
    F.fins += [caudal(B, 'fork', 9.4, col=fc('N1')), d1, dorsal(B, .24, .44, 4.4, 'round', col=fc('N1'), n=9), anal(B, .16, .3, 3.8, 'tri', col=fc('N1')),
               pelvic(B, .6, 3.8, col=fc('N1')), pectoral(B, .78, .56, 4.4, col=fc('N1'))]
    return F
def muskellunge():
    # set: very long DUCKBILL pike, dorsal and anal set far back / river-green with seven dark vertical BARS / pale belly / rust-bronze
    # fins with dark SPOTS / forked tail
    P = [(0, .36, -.36), (.08, .5, -.48), (.24, .82, -.8), (.44, .98, -.96), (.62, 1, -.98), (.76, .94, -.92), (.86, .7, -.68), (.94, .46, -.46), (1, .24, -.3)]
    F = Fish('muskellunge', 64, 11.6, P, bands('G2', 'G2', 'N1', b1=(0.36, 0.4), b2=(0.84, 0.84)), tilt=8, eye=(0.86, 0.34, 3, '#d8c070'))
    B = F.B
    F.marks += [m_bar(B, u, 2.4, .04, .76, -2, lean=0.3) for u in np_r(.1, .74, 7)]
    fcol = '#b0705a'
    tail = caudal(B, 'fork', 11.0, col=fcol, sig=True); tail['band'] = [fin_spots([(-3.0, 1.8), (-5.4, -2.0), (-7.4, 3.6), (-7.6, -3.8), (-4.0, -4.6)], 0.8, '#3a1a10')]
    df = dorsal(B, .06, .2, 6.0, 'round', col=fcol, n=9, sig=True); df['band'] = [fin_spots([(.1 * B.L, B.top(.1 * B.L) + 2.6), (.15 * B.L, B.top(.15 * B.L) + 4.2)], 0.8, '#3a1a10')]
    af = anal(B, .04, .18, 5.6, 'round', col=fcol, n=9, sig=True); af['band'] = [fin_spots([(.1 * B.L, B.bot(.1 * B.L) - 2.8)], 0.8, '#3a1a10')]
    F.fins += [tail, df, af, pelvic(B, .4, 4.4, col=fcol, sig=True), pectoral(B, .82, .7, 5.0, col=fc('N1'))]
    return F
def american_shad():
    # set: deep silver HERRING / pool-teal back over a pearl flank / a black SHOULDER SPOT followed by a row of four smaller spots /
    # saw-edged belly / DEEPLY forked tail
    P = [(0, .3, -.3), (.1, .44, -.42), (.28, .82, -.82), (.46, 1, -1), (.62, 1, -.98), (.76, .9, -.86), (.88, .64, -.58), (.96, .34, -.28), (1, .1, -.08)]
    F = Fish('american_shad', 42, 16, P, bands('G3', 'N1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=12, eye=(0.86, 0.42, 3, '#d8d8c8'))
    B = F.B
    F.marks += [m_spot(B, .74, .32, 1.6, '#0e1a18')] + [m_spot(B, u, .34, 0.9, '#1a2826') for u in np_r(.42, .64, 4)]
    F.fins += [caudal(B, 'deepfork', 11.0, col=fc('G3')), dorsal(B, .44, .56, 4.6, 'tri', col=fc('G3'), lean=0.5), anal(B, .14, .34, 3.4, 'low', col=fc('N1'), n=10),
               pelvic(B, .5, 3.0, col=fc('N1')), pectoral(B, .8, .66, 4.4, col=fc('N1'))]
    return F
def american_brook_lamprey():
    # set: EEL-like lamprey with no paired fins / charcoal-grey back, pale belly / a short row of GILL PORES behind the eye / oval
    # sucking-disc mouth / two low dorsal fins running into the tail fin
    P = [(0, .1, -.1), (.06, .42, -.42), (.2, .8, -.8), (.4, .98, -.98), (.6, 1, -1), (.8, .96, -.96), (.92, .84, -.8), (.98, .6, -.5), (1, .3, -.2)]
    F = Fish('american_brook_lamprey', 40, 5.4, P, bands('N1', 'N1', 'N1', b1=(0.4, 0.44), b2=(0.84, 0.84)), tilt=8, eye=(0.9, 0.34, 1, '#a8a080'))
    B = F.B; F.tone0 = 0.85
    F.marks += [m_spot(B, u, .5, .5, '#1e1a14') for u in np_r(.72, .86, 6)]
    tail = dorsal(B, .0, .24, 2.0, 'round', col=FAM['N1'][3], n=10); tail2 = anal(B, .0, .16, 1.6, 'round', col=FAM['N1'][3], n=8)
    F.fins += [caudal(B, 'round', 3.0, col=FAM['N1'][3]), tail, tail2, dorsal(B, .3, .46, 1.8, 'round', col=FAM['N1'][3], n=8)]
    return F
SCENE = {
    'central_stoneroller': dict(band=(180, 256), speed=18, fps=9, crowd=55, rest=(0.8, 2.5)),
    'bluehead_chub': dict(band=(80, 230), speed=22, fps=9, crowd=60),
    'creek_chub': dict(band=(60, 220), speed=24, fps=9, crowd=65),
    'fallfish': dict(band=(30, 200), speed=26, fps=9, crowd=80),
    'northern_hog_sucker': dict(band=(200, 258), speed=14, fps=8, crowd=70, rest=(1.5, 4.0)),
    'white_sucker': dict(band=(180, 256), speed=16, fps=8, crowd=75, rest=(1.0, 3.0)),
    'river_redhorse': dict(band=(170, 256), speed=16, fps=8, crowd=95, rest=(1.0, 3.0)),
    'longear_sunfish': dict(band=(80, 220), speed=16, fps=8, crowd=60),
    'rock_bass': dict(band=(130, 240), speed=16, fps=8, crowd=65, rest=(1.0, 3.0)),
    'smallmouth_bass': dict(band=(60, 230), speed=24, fps=8, crowd=95),
    'logperch': dict(band=(196, 258), speed=16, fps=9, crowd=55, rest=(1.2, 3.5)),
    'walleye': dict(band=(120, 250), speed=20, fps=8, crowd=110, rest=(1.0, 3.0)),
    'sauger': dict(band=(140, 254), speed=18, fps=8, crowd=105, rest=(1.0, 3.0)),
    'muskellunge': dict(band=(20, 200), speed=16, fps=7, crowd=140, rest=(2.0, 5.0)),
    'american_shad': dict(band=(20, 180), speed=30, fps=9, crowd=90),
    'american_brook_lamprey': dict(band=(220, 258), speed=10, fps=8, crowd=45, rest=(2.0, 5.0)),
}
