"""Clear Spring batch 2 - medium swimmers, each defined from its species name.
v3 (Oct 2026): one memorable set per species, coloured from the cs colour families (pal.FAM)."""
import numpy as np
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots, trail
from sp1 import bands, np_r
ALL = ['banded_cichlid', 'chanchito', 'pike_cichlid', 'lake_chubsucker', 'redbreast_sunfish', 'spotted_sunfish', 'suwannee_bass',
       'three_spot_piau', 'striped_mullet', 'banded_knifefish']
DEEP = [(0, .34, -.34), (.1, .52, -.5), (.26, .86, -.84), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.82), (.84, .74, -.6), (.92, .46, -.38), (.97, .22, -.24), (1, .04, -.14)]
def banded_cichlid():
    # set: tall sea-green disc / three broad soft bars fading out on the lower flank + one bold black bar on the peduncle /
    # red-brown worm marks on the cheek / long POINTED dorsal and anal lobes trailing past the tail / red eye
    F = Fish('banded_cichlid', 32, 20, DEEP, bands('A3', 'A3', 'A1', b1=(0.36, 0.4), b2=(0.92, 0.92)), tilt=15, eye=(0.8, 0.36, 2, '#c03a24'))
    B = F.B
    F.marks += [m_bar(B, u, 2.6, .06, .66, -1) for u in (.3, .45, .6)] + [m_bar(B, .08, 2.8, .02, .98, '#0c1a14')]
    F.marks += [m_stripe(B, .82, .9, [(.82, .62), (.9, .58)], 1.0, '#b6322b'), m_stripe(B, .84, .92, [(.84, .74), (.92, .7)], 1.0, '#b6322b')]
    dfin = dorsal(B, .16, .78, 4.6, 'long', col=fc('A3'), lean=-0.3, n=14, amp=0.6); afin = anal(B, .14, .42, 4.2, 'long', col=fc('A3'), lean=-0.3, n=8, amp=0.6)
    F.fins += [caudal(B, 'round', 7.4, col=fc('A3')), dfin, afin, trail(B, 1, .04, .2, 4.4, 4.6, FAM['A3'][3]), trail(B, -1, .04, .18, 4.0, 4.0, FAM['A3'][3]),
               pelvic(B, .6, 6.4, ang=-72, col=fc('A1')), pectoral(B, .72, .6, 4.4, col=fc('A1'))]
    return F
def chanchito():
    # set: chunky sand-bronze chameleon cichlid / five dark bars and one big black BLOTCH mid-side / turquoise cheek spots /
    # red eye / long soft dorsal and anal with dark-spotted rear lobes
    F = Fish('chanchito', 30, 17.5, DEEP, bands('C1', 'C1', 'N1', b1=(0.36, 0.4), b2=(0.9, 0.9)), tilt=15, eye=(0.8, 0.36, 2, '#c83a26'))
    B = F.B
    F.marks += [m_bar(B, u, 2.2, .06, .86, -2) for u in (.16, .32, .64, .78)] + [m_spot(B, .48, .5, 2.4, '#1a120a')]
    F.marks += [m_spot(B, u, t, 0.8, '#4fb0a8') for u, t in ((.84, .5), (.9, .62), (.8, .66))]
    dfin = dorsal(B, .04, .76, 5.6, 'long', col=fc('C1'), lean=-0.5, n=16, amp=0.6); afin = anal(B, .04, .4, 5.2, 'long', col=fc('C1'), lean=-0.5, n=12, amp=0.6)
    dfin['band'] = [fin_spots([(2.0, B.top(2.0) + 3.2), (4.6, B.top(4.6) + 3.6)], 0.75, '#3a2814')]; afin['band'] = [fin_spots([(2.4, B.bot(2.4) - 3.0)], 0.75, '#3a2814')]
    F.fins += [caudal(B, 'round', 7.4, col=fc('C1')), dfin, afin, pelvic(B, .6, 5.0, ang=-68, col=fc('C1')), pectoral(B, .72, .6, 4.0, col=fc('N1'))]
    return F
def pike_cichlid():
    # set: long pike-shaped predator with a PROJECTING lower jaw / pearl-grey / dark STRIPE from snout through the eye along the body
    # / amber-ringed black OCELLUS behind the pectoral / black spot on the tail base / long low dorsal along the whole back
    P = [(0, .36, -.36), (.1, .5, -.48), (.3, .86, -.82), (.5, 1, -.96), (.7, .98, -.96), (.84, .82, -.86), (.94, .5, -.62), (1, .16, -.36)]
    F = Fish('pike_cichlid', 38, 10.4, P, bands('N1', 'N1', 'A1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=10, eye=(0.85, 0.38, 2, '#c8402a'))
    B = F.B
    F.marks += [m_stripe(B, .12, 1.0, [(.12, .5), (.6, .48), (1, .4)], 1.8, '#26221c'), m_spot(B, .7, .44, 2.1, '#e8a632'), m_spot(B, .7, .44, 1.2, '#14100a'),
                m_spot(B, .04, .42, 1.4, '#14100a')]
    F.fins += [caudal(B, 'round', 7.0, col=fc('N1')), dorsal(B, .1, .8, 3.4, 'low', col=FAM['N1'][3], lean=0.2, n=20, amp=0.5),
               anal(B, .08, .3, 3.4, 'round', col=fc('N1'), n=8), pelvic(B, .66, 3.4, col=fc('N1')), pectoral(B, .76, .58, 4.0, col=fc('N1'))]
    return F
def lake_chubsucker():
    # set: stout oval sucker / sea-green back over a pearl flank / one broad dusky LATERAL BAND (the young fish's mark) / tiny mouth
    # under the snout / HIGH rounded dorsal / tangerine-tinted lower fins
    P = [(0, .38, -.36), (.1, .5, -.48), (.3, .86, -.8), (.48, 1, -.94), (.64, .98, -.94), (.78, .84, -.84), (.9, .56, -.6), (.97, .3, -.38), (1, .12, -.24)]
    F = Fish('lake_chubsucker', 30, 13.4, P, bands('A3', 'N1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), tilt=15, eye=(0.83, 0.38, 2, '#c8a848'))
    B = F.B
    F.marks += [m_stripe(B, .04, .9, [(0, .52), (.5, .54), (.9, .5)], 2.6, -2)]
    F.fins += [caudal(B, 'emarg', 7.6, col=fc('A3')), dorsal(B, .42, .62, 7.0, 'round', col=FAM['A3'][3], lean=0.3, n=10), anal(B, .16, .3, 3.8, 'round', col='#d89a78'),
               pelvic(B, .5, 3.6, col='#dca07c'), pectoral(B, .76, .66, 3.8, col=fc('N1'))]
    return F
def redbreast_sunfish():
    # set: deep round sunfish / slate-teal back over a coral-orange BREAST / the long narrow BLACK EAR FLAP running back off the
    # gill cover / two turquoise cheek streaks / a few big coral flank spots / spiny + soft dorsal, coral pelvics
    F = Fish('redbreast_sunfish', 30, 17, DEEP, bands('A2', 'A1', 'A1', b1=(0.4, 0.42), b2=(0.9, 0.9)), tilt=15, eye=(0.81, 0.36, 2, '#b84a2c'))
    B = F.B
    F.patches.append((lambda X, Y, U, T: (T > .58) & (U > .16) & (U < .92), FAM['C3']))
    F.marks += [m_stripe(B, .6, .79, [(.6, .38), (.79, .34)], 2.0, '#0e1214')]                     # ear flap
    F.marks += [m_stripe(B, .83, .96, [(.83, .56), (.96, .5)], 1.0, '#58b6c8'), m_stripe(B, .8, .92, [(.8, .68), (.92, .64)], 1.0, '#58b6c8')]
    F.marks += [m_spot(B, u, t, 1.0, '#d16631') for u, t in ((.3, .3), (.46, .28), (.38, .46), (.24, .44))]
    F.fins += [caudal(B, 'emarg', 7.4, col=fc('A2')), dorsal(B, .44, .72, 4.4, 'spiny', col=FAM['A2'][3], lean=0.3, n=10),
               dorsal(B, .14, .46, 6.0, 'round', col=fc('A2'), lean=0.4, n=10), anal(B, .12, .4, 5.0, 'round', col='#e08a5e'),
               pelvic(B, .62, 4.2, col='#d16631', sig=True), pectoral(B, .72, .58, 5.2, col=fc('A1'))]
    return F
def spotted_sunfish():
    # set: the DARK sunfish - deep slate-charcoal body peppered with black specks / short black ear flap with a PALE RIM /
    # faint rust breast / red eye / dusky rounded fins
    F = Fish('spotted_sunfish', 28, 16, DEEP, bands('A2', 'N1', 'N1', b1=(0.4, 0.44), b2=(0.9, 0.9)), tilt=15, eye=(0.81, 0.36, 2, '#c03a24'))
    B = F.B; F.tone0 = 0.5   # a darker fish than its neighbours
    F.patches.append((lambda X, Y, U, T: (T > .74) & (U > .5) & (U < .9), FAM['C3']))
    F.marks += [m_spot(B, u, t, 0.75, '#0e1012') for u, t in scatter(16, .12, .72, .16, .76, seed=0.17, gap=0.07)]
    F.marks += [m_spot(B, .73, .35, 1.6, '#e4f1f4'), m_spot(B, .74, .35, 1.1, '#0c0e10')]
    F.fins += [caudal(B, 'round', 7.0, col=FAM['A2'][3]), dorsal(B, .16, .72, 5.0, 'round', col=FAM['A2'][3], lean=0.2, n=16), anal(B, .12, .4, 4.4, 'round', col=FAM['A2'][3]),
               pelvic(B, .62, 3.8, col=FAM['N1'][3]), pectoral(B, .72, .58, 4.6, col=fc('N1'))]
    return F
def suwannee_bass():
    # set: chunky bronze bass with a big jaw / row of dark lateral BLOTCHES / red eye / bright TURQUOISE chin, cheek and breast /
    # spiny + soft dorsal, emarginate tail
    P = [(0, .36, -.36), (.1, .48, -.46), (.3, .84, -.8), (.48, .98, -.96), (.64, 1, -.98), (.78, .9, -.92), (.9, .66, -.74), (.97, .36, -.5), (1, .14, -.34)]
    F = Fish('suwannee_bass', 34, 13.4, P, bands('C1', 'C1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=12, eye=(0.84, 0.36, 2, '#c83224'))
    B = F.B
    F.patches.append((lambda X, Y, U, T: (T > .6) & (U > .74), ramp('#3a96b4', sig=True)))
    F.marks += [m_spot(B, u, .5, 1.5, '#2a1c0c', aspect=1.3) for u in (.16, .32, .48, .64)]
    F.fins += [caudal(B, 'emarg', 8.4, col=fc('C1')), dorsal(B, .44, .66, 4.6, 'spiny', col=FAM['C1'][3], lean=0.2, n=10), dorsal(B, .2, .44, 5.0, 'round', col=fc('C1'), lean=0.3, n=10),
               anal(B, .14, .32, 4.4, 'round', col=fc('C1')), pelvic(B, .6, 4.0, col=fc('N1')), pectoral(B, .76, .58, 4.6, col=fc('N1'))]
    return F
def three_spot_piau():
    # set: cylindrical headstander / slate back, aqua-silver flank / THREE round BLACK SPOTS along the midline / three faint
    # saddles over the back / small mouth / tangerine-amber fins and tail
    P = [(0, .36, -.36), (.1, .48, -.46), (.3, .84, -.8), (.5, 1, -.96), (.68, .98, -.96), (.82, .82, -.8), (.92, .56, -.54), (.98, .3, -.3), (1, .12, -.14)]
    F = Fish('three_spot_piau', 36, 11.4, P, bands('A2', 'A1', 'A1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=10, eye=(0.84, 0.38, 2, '#d8c070'))
    B = F.B
    F.marks += [m_spot(B, u, .48, 1.8, '#101418') for u in (.08, .38, .64)] + [m_bar(B, u, 2.0, .0, .3, -1) for u in (.22, .5, .76)]
    F.fins += [caudal(B, 'fork', 8.4, col='#e09048', sig=True), dorsal(B, .48, .64, 5.4, 'tri', col=fc('A1'), lean=0.4), adipose(B, .16, 2.4, 1.8, col=FAM['A2'][3]),
               anal(B, .14, .28, 3.6, 'tri', col='#e09048', sig=True), pelvic(B, .52, 3.6, col='#e49a52', sig=True), pectoral(B, .78, .66, 3.8, col='#e8b07a', sig=True)]
    return F
def striped_mullet():
    # set: torpedo with a broad BLUNT head / slate back, silver flank with two thin dark scale stripes / TWO widely spaced dorsals /
    # a dark spot at the pectoral base set high on the side / forked tail
    P = [(0, .36, -.36), (.1, .46, -.46), (.3, .8, -.82), (.5, .96, -.98), (.66, 1, -.98), (.8, .92, -.86), (.9, .72, -.62), (.97, .44, -.32), (1, .18, -.1)]
    F = Fish('striped_mullet', 36, 11.2, P, bands('A2', 'A1', 'A1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=10, eye=(0.86, 0.4, 2, '#d0d4c0'))
    B = F.B
    F.marks += [m_hline(B, .06, .8, y, 0.9, -1) for y in (2.2, -0.6)] + [m_spot(B, .74, .3, 1.1, '#1c2a2e')]
    F.fins += [caudal(B, 'fork', 8.0, col=FAM['A2'][3]), dorsal(B, .5, .58, 3.4, 'tri', col=FAM['A2'][3], lean=0.3, n=6), dorsal(B, .22, .32, 3.2, 'tri', col=FAM['A2'][3], lean=0.4, n=6),
               anal(B, .18, .32, 3.0, 'tri', col=fc('A1')), pelvic(B, .54, 3.0, col=fc('A1')), pectoral(B, .74, .3, 3.8, ang=-15, col=fc('A2'))]
    return F
def banded_knifefish():
    # set: eel-like knifefish with NO tail or dorsal fin / sand-bronze body with OBLIQUE dark bands slanting back / one long rippling
    # RIBBON fin under the body / small eye
    P = [(0, .05, -.05), (.06, .2, -.22), (.2, .6, -.62), (.4, .9, -.92), (.6, 1, -1), (.78, .96, -.98), (.9, .8, -.78), (.97, .5, -.46), (1, .2, -.14)]
    F = Fish('banded_knifefish', 46, 8.0, P, bands('C1', 'C1', 'N1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=8, eye=(0.88, 0.36, 1, '#8a6a40'))
    B = F.B
    F.marks += [m_bar(B, u, 2.2, .02, .98, -2, lean=0.9) for u in np_r(.14, .78, 7)]
    rib = anal(B, .04, .8, 2.8, 'flat', col=fc('C1'), lean=0.0, n=30, amp=0.9); rib['wave'] = 3.0
    F.fins += [rib, pectoral(B, .82, .5, 3.0, col=fc('N1'))]
    return F
SCENE = {
    'banded_cichlid': dict(band=(90, 230), speed=16, fps=8, crowd=70, rest=(0.8, 2.5)),
    'chanchito': dict(band=(110, 240), speed=16, fps=8, crowd=65, rest=(0.8, 2.5)),
    'pike_cichlid': dict(band=(150, 250), speed=22, fps=8, crowd=70, rest=(1.0, 3.0)),
    'lake_chubsucker': dict(band=(150, 250), speed=16, fps=8, crowd=65),
    'redbreast_sunfish': dict(band=(60, 220), speed=18, fps=8, crowd=65),
    'spotted_sunfish': dict(band=(80, 230), speed=16, fps=8, crowd=60),
    'suwannee_bass': dict(band=(100, 240), speed=20, fps=8, crowd=75),
    'three_spot_piau': dict(band=(120, 250), speed=22, fps=9, crowd=65),
    'striped_mullet': dict(band=(10, 150), speed=26, fps=9, crowd=70),
    'banded_knifefish': dict(band=(190, 256), speed=12, fps=8, crowd=70, rest=(1.5, 4.0)),
}
