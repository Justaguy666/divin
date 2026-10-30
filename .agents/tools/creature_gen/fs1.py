"""Forest Stream batch 1 - small minnows, topminnow and darters, each defined from its species name only.
v3 (Oct 2026): one memorable set per species, coloured from the fs colour families (pal.FAM_FS: greens / teal analogous to
the stream, neutral, copper-rust-rose complements, turquoise accents)."""
import numpy as np
import pal; pal.use("fs")
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots
from sp1 import bands, np_r
ALL = ['blacknose_dace', 'longnose_dace', 'southern_redbelly_dace', 'rosyside_dace', 'warpaint_shiner', 'saffron_shiner', 'rosyface_shiner',
       'northern_studfish', 'central_mudminnow', 'rainbow_darter', 'greenside_darter', 'redline_darter', 'tangerine_darter', 'fantail_darter', 'tessellated_darter']
MIN = [(0, .32, -.32), (.1, .42, -.42), (.28, .74, -.72), (.45, .94, -.92), (.6, 1, -.98), (.74, .92, -.9), (.86, .7, -.66), (.94, .42, -.38), (1, .08, -.1)]
DART = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.72), (.5, .98, -.86), (.66, 1, -.9), (.8, .84, -.82), (.9, .6, -.6), (.96, .34, -.36), (1, .1, -.14)]
def dfins(B, col, first='#999', sp=(.5, .68, 3.2), so=(.22, .46, 3.2), cau='round', pec=4.2, sig1=False, band1=None):
    d1 = dorsal(B, sp[0], sp[1], sp[2], 'spiny', col=first, lean=0.3, n=9, sig=sig1)
    if band1: d1['band'] = band1
    return [caudal(B, cau, 5.6, col=col), d1, dorsal(B, so[0], so[1], so[2], 'round', col=col, lean=0.4, n=9),
            anal(B, .22, .38, 2.6, 'round', col=col), pelvic(B, .62, 2.8, col=col), pectoral(B, .74, .52, pec, width=0.55, col=col)]
def low(F, k=0.3): F.tone0 += k; return F   # bottom fish over the darker low water lean on the light tones
def blacknose_dace():
    # set: slender riffle minnow / moss-olive back, pearl belly / bold BLACK BAND from the snout through the eye to the tail /
    # a rust-orange breeding stripe under the band / clear olive fins, forked tail
    F = Fish('blacknose_dace', 24, 8.4, MIN, bands('G1', 'G1', 'N1', b1=(0.4, 0.44), b2=(0.84, 0.84)), tilt=25, eye=(0.82, 0.42, 2, '#c8a860'))
    B = F.B
    F.marks += [m_stripe(B, 0, 1.0, [(0, .48), (.5, .5), (1, .48)], 1.8, '#141608')]
    F.patches.append((lambda X, Y, U, T: (T > .6) & (T < .76) & (U > .14) & (U < .8), FAM['R2']))
    F.fins += [caudal(B, 'fork', 6.4, col=fc('G1')), dorsal(B, .38, .58, 3.8, 'tri', col=fc('G1'), lean=0.6), anal(B, .2, .34, 2.8, 'tri', col=fc('N1')),
               pelvic(B, .5, 2.4, col=FAM['R2'][4]), pectoral(B, .76, .66, 3.0, col=fc('N1'))]
    return F
def longnose_dace():
    # set: cylindrical riffle dweller with a long FLESHY SNOUT over the mouth / olive back, copper flank with a few dark MOTTLES /
    # red lips and red-based pelvic fins / big paddle pectorals
    P = [(0, .34, -.34), (.1, .44, -.42), (.28, .78, -.72), (.45, .96, -.88), (.6, 1, -.9), (.76, .92, -.84), (.88, .72, -.6), (.95, .5, -.34), (1, .26, -.06)]
    F = Fish('longnose_dace', 26, 8.2, P, bands('G1', 'R1', 'N1', b1=(0.36, 0.4), b2=(0.84, 0.84)), tilt=22, eye=(0.8, 0.36, 2, '#c8a860'))
    B = F.B; low(F)
    F.marks += [m_spot(B, u, t, 0.95, '#2a1c10', aspect=1.2) for u, t in scatter(6, .1, .78, .2, .58, seed=0.29, gap=0.1)]
    F.marks += [m_spot(B, .97, .72, .8, '#c65b4c')]
    F.fins += [caudal(B, 'fork', 6.0, col=fc('G1')), dorsal(B, .36, .56, 3.6, 'tri', col=fc('G1'), lean=0.6), anal(B, .2, .34, 2.6, 'tri', col=fc('R1')),
               pelvic(B, .5, 2.6, col='#c65b4c', sig=True), pectoral(B, .76, .7, 3.8, width=0.6, col=fc('R1'))]
    return F
def southern_redbelly_dace():
    # set: small minnow / moss back / TWO BLACK STRIPES (thin upper, broad lower) split by a pale cream stripe / SCARLET belly /
    # cream fins with red-tinted pelvics
    F = Fish('southern_redbelly_dace', 23, 8.0, MIN, bands('G1', 'G1', 'R2', sig=('belly',), b1=(0.36, 0.4), b2=(0.72, 0.72)), tilt=25, eye=(0.82, 0.4, 2, '#c8a050'))
    B = F.B
    F.marks += [m_stripe(B, .06, .9, [(.06, .32), (.9, .3)], 1.0, '#141608'), m_stripe(B, 0, 1.0, [(0, .56), (1, .54)], 1.8, '#141608'),
                m_stripe(B, .06, .9, [(.06, .43), (.9, .42)], 1.0, '#e6eadc')]
    F.fins += [caudal(B, 'fork', 6.0, col=fc('G1')), dorsal(B, .38, .58, 3.6, 'tri', col=fc('G1'), lean=0.6), anal(B, .2, .34, 2.6, 'tri', col=FAM['R2'][4]),
               pelvic(B, .5, 2.4, col='#c65b4c', sig=True), pectoral(B, .76, .66, 3.0, col=fc('N1'))]
    return F
def rosyside_dace():
    # set: deeper big-mouthed dace / river-green back, pool-teal silver flank / a ROSE PATCH on the lower flank / one faint dark
    # lateral stripe / clear teal fins
    P = [(0, .34, -.34), (.1, .46, -.44), (.28, .8, -.76), (.45, .98, -.94), (.6, 1, -.98), (.74, .92, -.9), (.86, .72, -.7), (.94, .46, -.46), (1, .14, -.2)]
    F = Fish('rosyside_dace', 25, 9.8, P, bands('G2', 'G3', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=25, eye=(0.82, 0.38, 2, '#c8b070'))
    B = F.B
    F.patches.append((lambda X, Y, U, T: (T > .56) & (T < .86) & (U > .28) & (U < .76), FAM['R3']))
    F.marks += [m_stripe(B, .04, .86, .48, 1.6, -1)]
    F.fins += [caudal(B, 'fork', 6.6, col=fc('G3')), dorsal(B, .38, .58, 4.0, 'tri', col=fc('G3'), lean=0.6), anal(B, .2, .34, 3.0, 'tri', col=fc('G3')),
               pelvic(B, .5, 2.6, col=FAM['R3'][4]), pectoral(B, .76, .66, 3.2, col=fc('N1'))]
    return F
def warpaint_shiner():
    # set: deep silvery shiner / river-green back, pool-teal flank / the WAR PAINT - red snout and a red bar on the upper gill cover
    # / black shoulder bar / dorsal crossed by a black band / dark tail margin
    P = [(0, .34, -.34), (.1, .46, -.44), (.28, .82, -.78), (.45, 1, -.96), (.6, 1, -.98), (.74, .9, -.88), (.86, .68, -.66), (.94, .4, -.4), (1, .1, -.12)]
    F = Fish('warpaint_shiner', 25, 10.4, P, bands('G2', 'G3', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=25, eye=(0.82, 0.38, 2, '#c8c0a0'))
    B = F.B; red = '#c8402e'
    F.marks += [m_stripe(B, .8, .9, [(.8, .28), (.9, .3)], 1.4, red), m_spot(B, .99, .4, .9, red), m_bar(B, .72, 1.6, .1, .9, '#101410', lean=0.2)]
    d = dorsal(B, .38, .58, 4.6, 'tri', col=fc('G3'), lean=0.6); d['band'] = [(lambda X, Y, B=B: (Y > B.top(X) + 2.2) & (Y < B.top(X) + 3.6), '#101410')]
    t = caudal(B, 'fork', 6.6, col=fc('G3')); t['band'] = [(lambda X, Y: X < -5.4, FAM['G2'][1])]
    F.fins += [t, d, anal(B, .2, .34, 3.0, 'tri', col=fc('G3')), pelvic(B, .5, 2.6, col=fc('N1')), pectoral(B, .76, .66, 3.2, col=fc('N1'))]
    return F
def saffron_shiner():
    # set: the RED-HOT minnow - breeding male glowing rust-red over flank and every fin / dark moss back / dusky lateral stripe ending
    # in a dark tail spot
    F = Fish('saffron_shiner', 23, 8.2, MIN, bands('G1', 'R2', 'R2', sig=('flank', 'belly'), b1=(0.36, 0.4), b2=(0.84, 0.84)), tilt=25, eye=(0.82, 0.4, 2, '#d8b060'))
    B = F.B
    F.marks += [m_stripe(B, .04, .88, .46, 1.2, '#5a1c10'), m_spot(B, .03, .48, 1.1, '#2a0e06')]
    F.fins += [caudal(B, 'fork', 6.2, col='#c65b4c', sig=True), dorsal(B, .38, .58, 3.8, 'tri', col='#c65b4c', sig=True, lean=0.6), anal(B, .2, .34, 2.8, 'tri', col='#c65b4c', sig=True),
               pelvic(B, .5, 2.4, col='#d8705e', sig=True), pectoral(B, .76, .66, 3.0, col='#e8907e', sig=True)]
    return F
def rosyface_shiner():
    # set: slender pointed shiner / pool-teal silver / a ROSE HEAD (breeding) / one thin dark lateral line / dark stripe along the top
    # of the back / clear teal fins
    F = Fish('rosyface_shiner', 25, 7.8, MIN, bands('G3', 'G3', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=25, eye=(0.82, 0.4, 2, '#d0c8a8'))
    B = F.B
    F.patches.append((lambda X, Y, U, T: (U > .78) & (T > .12) & (T < .8), FAM['R3']))
    F.marks += [m_stripe(B, .04, .76, .48, 1.0, FAM['G3'][1]), m_stripe(B, .1, .74, .04, 1.2, FAM['G3'][0])]
    F.fins += [caudal(B, 'fork', 6.4, col=fc('G3')), dorsal(B, .38, .58, 3.8, 'tri', col=fc('G3'), lean=0.6), anal(B, .2, .34, 2.8, 'tri', col=fc('G3')),
               pelvic(B, .5, 2.4, col=fc('N1')), pectoral(B, .76, .66, 3.0, col=fc('N1'))]
    return F
def northern_studfish():
    # set: big flat-headed topminnow / pool-teal back and flank / CHAINS of rust-red spots in two rows / rust-orange fins with a dark
    # edge / dorsal set far back
    P = [(0, .36, -.36), (.1, .46, -.46), (.3, .78, -.8), (.5, .94, -1.0), (.66, .96, -.96), (.8, .86, -.8), (.9, .66, -.56), (.96, .44, -.3), (1, .22, -.06)]
    F = Fish('northern_studfish', 27, 9.6, P, bands('G3', 'G3', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=22, eye=(0.82, 0.34, 2, '#c8c090'))
    B = F.B
    F.marks += [m_spot(B, u, t, 0.85, FAM['R2'][2]) for t, us in ((.42, np_r(.12, .66, 6)), (.62, np_r(.16, .62, 5))) for u in us]
    t = caudal(B, 'truncate', 6.0, col='#c8704e', sig=True); t['band'] = [(lambda X, Y: X < -4.8, '#3a1a10')]
    d = dorsal(B, .22, .4, 3.8, 'round', col='#c8704e', sig=True, lean=0.4); d['band'] = [(lambda X, Y, B=B: Y > B.top(X) + 2.6, '#3a1a10')]
    F.fins += [t, d, anal(B, .18, .38, 3.4, 'round', col='#cc7852', sig=True), pelvic(B, .5, 2.4, col=FAM['R2'][4]), pectoral(B, .76, .6, 3.2, col=fc('N1'))]
    return F
def central_mudminnow():
    # set: chunky cylindrical mudminnow / dark moss olive with three faint bars / a bold BLACK BAR across the tail base / rounded fins,
    # dorsal set far back over the anal
    P = [(0, .44, -.44), (.1, .56, -.56), (.3, .84, -.86), (.5, .98, -1.0), (.68, 1, -.98), (.82, .88, -.84), (.92, .64, -.6), (.97, .4, -.36), (1, .14, -.14)]
    F = Fish('central_mudminnow', 25, 9.0, P, bands('G1', 'G1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), tilt=22, eye=(0.82, 0.38, 2, '#c09a50'))
    B = F.B; low(F, 0.15)
    F.marks += [m_bar(B, .03, 2.4, .04, .96, '#121408')] + [m_bar(B, u, 2.0, .1, .76, -1) for u in (.26, .44, .62)]
    F.fins += [caudal(B, 'round', 5.6, col=FAM['G1'][3]), dorsal(B, .2, .4, 3.4, 'round', col=FAM['G1'][3], n=9), anal(B, .2, .34, 3.0, 'round', col=fc('G1')),
               pelvic(B, .5, 2.4, col=fc('G1')), pectoral(B, .78, .58, 3.2, col=fc('N1'))]
    return F
def rainbow_darter():
    # set: the RAINBOW - copper flank crossed by four TURQUOISE bars / dark saddles on a moss back / first dorsal banded red with a
    # turquoise edge / turquoise anal fin
    F = Fish('rainbow_darter', 22, 7.6, DART, bands('G1', 'R1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=22, eye=(0.8, 0.36, 2, '#c8a050'))
    B = F.B; low(F)
    F.marks += [m_bar(B, u, 2.0, .36, .96, '#0f9293') for u in np_r(.14, .64, 4)] + [m_bar(B, u, 2.0, 0, .26, '#2a2a14') for u in (.26, .5)]
    b1 = [(lambda X, Y, B=B: (Y > B.top(X) + 1.0) & (Y < B.top(X) + 2.4), '#c65b4c')]
    F.fins += dfins(B, fc('R1'), first='#0f9293', band1=b1)
    F.fins[3] = anal(B, .22, .38, 2.6, 'round', col='#0f9293', sig=True)
    return F
def greenside_darter():
    # set: big GREEN darter with a rounded overhanging snout / river-green body with five dark green V-BLOTCHES / small saddles /
    # bright green fins
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.72), (.5, .98, -.86), (.66, 1, -.9), (.8, .86, -.8), (.9, .66, -.6), (.96, .42, -.34), (1, .18, -.1)]
    F = Fish('greenside_darter', 26, 8.6, P, bands('G2', 'G2', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=22, eye=(0.8, 0.34, 2, '#c8a858'))
    B = F.B; low(F); g = FAM['G2'][0]
    F.marks += [m_poly(B, [(u - .045, .38), (u, .66), (u + .045, .38), (u + .02, .38), (u, .5), (u - .02, .38)], g) for u in np_r(.18, .66, 5)]
    F.marks += [m_bar(B, u, 1.8, 0, .22, FAM['G2'][1]) for u in (.3, .54)]
    F.fins += dfins(B, '#5f9a68', first='#4f8a5a', sp=(.5, .7, 3.4), so=(.22, .48, 3.4))
    for f in F.fins[1:3]: f['col'] = __import__('pal').fin('#4f8a5a', True); f['alpha'] = (170, 100)
    return F
def redline_darter():
    # set: pale copper darter with two continuous RED LINES along the side / four dark side blotches / two dark bars on the cheek /
    # rust-red fins with a dark band
    F = Fish('redline_darter', 23, 7.8, DART, bands('R1', 'N1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=22, eye=(0.8, 0.36, 2, '#c8a050'))
    B = F.B; low(F)
    F.marks += [m_hline(B, .1, .72, y, 1.0, '#b6322b') for y in (1.0, -1.4)]
    F.marks += [m_spot(B, u, .52, 1.0, '#24180c', aspect=1.2) for u in np_r(.18, .62, 4)] + [m_bar(B, .86, 1.0, .5, .95, '#1c140a', lean=.6), m_bar(B, .91, 1.0, .5, .9, '#1c140a', lean=.6)]
    F.fins += dfins(B, '#c65b4c', first='#b6503e')
    for f in F.fins: f['col'] = __import__('pal').fin('#c65b4c', True) if f['kind'] in ('caudal', 'dorsal', 'anal') else f['col']
    F.fins[0]['band'] = [(lambda X, Y: (X < -2.6) & (X > -3.8), '#3a1810')]
    return F
def tangerine_darter():
    # set: the BIG darter / moss back with dark saddles / bold BLACK STRIPE of joined blotches / glowing TANGERINE-RED lower body /
    # emarginate tail
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.76), (.5, .98, -.92), (.66, 1, -.94), (.8, .86, -.84), (.9, .6, -.62), (.96, .32, -.36), (1, .08, -.12)]
    F = Fish('tangerine_darter', 28, 8.6, P, bands('G1', 'G1', 'R2', sig=('belly',), b1=(0.36, 0.4), b2=(0.66, 0.66)), tilt=20, eye=(0.82, 0.38, 2, '#c8a050'))
    B = F.B; low(F, 0.2)
    F.marks += [m_stripe(B, .06, .8, [(0, .5), (.8, .48)], 2.0, '#121408')] + [m_bar(B, u, 2.0, 0, .2, '#2a2a14') for u in (.24, .44, .64)]
    F.fins += dfins(B, fc('G1'), first=FAM['G1'][3], sp=(.5, .7, 3.6), so=(.22, .48, 3.6), cau='emarg')
    return F
def fantail_darter():
    # set: pale pearl-tan darter with five soft bars / low first dorsal with PALE KNOBS on the spine tips / a big rounded FAN TAIL crossed
    # by dark bands
    F = Fish('fantail_darter', 22, 7.6, DART, bands('R1', 'N1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=22, eye=(0.8, 0.36, 2, '#c8a050'))
    B = F.B; low(F)
    F.marks += [m_bar(B, u, 2.0, .1, .9, -1) for u in np_r(.14, .7, 5)]
    b1 = [(lambda X, Y, B=B: (Y > B.top(X) + 1.8), '#ebe7e2')]
    fins = dfins(B, fc('N1'), first=FAM['R1'][3], sp=(.5, .68, 2.4), band1=b1)
    fan = caudal(B, 'round', 7.4, col=fc('N1'), spread=B.D * 1.25); fan['band'] = [(lambda X, Y: (X < -1.5) & ((np.floor(-X / 2.0) % 2) == 0), FAM['R1'][1])]
    fins[0] = fan; F.fins += fins
    return F
def tessellated_darter():
    # set: pale straw darter speckled with small dark TESSELLATION marks / three faint saddles / a dark TEARDROP bar under the eye /
    # clear pale fins
    F = Fish('tessellated_darter', 23, 7.4, DART, bands('N1', 'N1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=22, eye=(0.8, 0.36, 2, '#c8a858'))
    B = F.B; low(F); d = '#2e2416'
    F.marks += [m_spot(B, u, t, 0.75, d, aspect=1.5) for u, t in scatter(10, .12, .72, .3, .74, seed=0.61, gap=0.07)]
    F.marks += [m_bar(B, u, 1.8, 0, .2, FAM['N1'][2]) for u in (.26, .46, .66)] + [m_bar(B, .84, 1.0, .5, .95, '#1c160a')]
    F.fins += dfins(B, fc('N1'), first=FAM['N1'][3])
    return F
SCENE = {
    'blacknose_dace': dict(band=(60, 220), speed=26, fps=10, crowd=45),
    'longnose_dace': dict(band=(170, 256), speed=22, fps=10, crowd=45, rest=(0.8, 2.5)),
    'southern_redbelly_dace': dict(band=(40, 200), speed=26, fps=10, crowd=45),
    'rosyside_dace': dict(band=(40, 200), speed=28, fps=10, crowd=50),
    'warpaint_shiner': dict(band=(30, 190), speed=28, fps=10, crowd=50),
    'saffron_shiner': dict(band=(40, 200), speed=28, fps=10, crowd=45),
    'rosyface_shiner': dict(band=(20, 170), speed=30, fps=10, crowd=45),
    'northern_studfish': dict(band=(4, 110), speed=22, fps=9, crowd=55),
    'central_mudminnow': dict(band=(170, 250), speed=14, fps=8, crowd=45, rest=(1.0, 3.0)),
    'rainbow_darter': dict(band=(200, 258), speed=14, fps=9, crowd=40, rest=(1.5, 4.0)),
    'greenside_darter': dict(band=(198, 258), speed=14, fps=9, crowd=45, rest=(1.5, 4.0)),
    'redline_darter': dict(band=(200, 258), speed=14, fps=9, crowd=40, rest=(1.5, 4.0)),
    'tangerine_darter': dict(band=(190, 256), speed=16, fps=9, crowd=45, rest=(1.2, 3.5)),
    'fantail_darter': dict(band=(204, 258), speed=12, fps=9, crowd=40, rest=(2.0, 5.0)),
    'tessellated_darter': dict(band=(204, 258), speed=12, fps=9, crowd=40, rest=(2.0, 5.0)),
}
