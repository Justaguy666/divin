"""Clear Spring batch 3 - large swimmers, each defined from its species name.
v3 (Oct 2026): one memorable set per species, coloured from the cs colour families (pal.FAM)."""
import numpy as np
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots, trail
from sp1 import bands, np_r
ALL = ['curimbata', 'piraputanga', 'piracanjuba', 'golden_dorado', 'common_snook', 'florida_gar', 'pacu', 'pintado', 'gulf_sturgeon']
CHAR = [(0, .34, -.34), (.1, .46, -.44), (.3, .84, -.8), (.48, 1, -.96), (.64, 1, -.96), (.78, .88, -.84), (.9, .6, -.56), (.97, .3, -.28), (1, .08, -.1)]
def curimbata():
    # set: high-backed silver migratory fish / slate back over a bright aqua-silver flank / two faint scale lines / pale fleshy
    # sucker LIPS on the snout / tall dorsal with a dark edge / forked tail crossed by bold dark ZIGZAG bands / sandy lower fins
    P = [(0, .34, -.34), (.1, .5, -.46), (.28, .9, -.8), (.46, 1, -.96), (.62, .98, -.96), (.76, .84, -.84), (.88, .58, -.58), (.96, .3, -.32), (1, .1, -.16)]
    F = Fish('curimbata', 40, 17, P, bands('A2', 'A1', 'A1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=12, eye=(0.86, 0.4, 3, '#c8c8a0'))
    B = F.B
    F.marks += [m_hline(B, .1, .8, y, 0.9, -1) for y in (2.4, -1.6)]
    F.marks += [m_spot(B, .995, .58, 1.1, '#e4ccb6', aspect=0.8)]     # fleshy lips
    tail = caudal(B, 'fork', 10.0, col=fc('A1'))
    tail['band'] = [(lambda X, Y: (X < -2.5) & (((-X + 0.6 * np.abs(Y - 0.0)) % 4.6) < 1.8), FAM['A2'][1])]
    dor = dorsal(B, .44, .6, 8.0, 'tri', col=fc('A1'), lean=0.5, n=10); dor['band'] = [(lambda X, Y, B=B: Y > B.top(X) + 5.4, FAM['A2'][1])]
    F.fins += [tail, dor, adipose(B, .14, 2.6, 2.0, col=FAM['A2'][3]), anal(B, .14, .28, 4.6, 'tri', col=fc('C1')), pelvic(B, .5, 4.4, col=fc('C1')), pectoral(B, .78, .64, 4.6, col=fc('A1'))]
    return F
def piraputanga():
    # set: sleek silver Brycon / slate-blue back / BRIGHT RED TAIL with a black streak through its middle that runs onto the
    # peduncle / red adipose / small dark humeral spot / amber-edged anal fin
    F = Fish('piraputanga', 40, 12.6, CHAR, bands('A2', 'A1', 'A1', b1=(0.32, 0.36), b2=(0.86, 0.86)), tilt=10, eye=(0.86, 0.4, 3, '#d8d0b0'))
    B = F.B; red = '#d43a2c'
    F.marks += [m_stripe(B, 0, .22, .5, 1.4, '#101418'), m_spot(B, .74, .36, 1.3, '#1c2a30', aspect=1.3)]
    tail = caudal(B, 'fork', 10.4, col=red, sig=True); tail['band'] = [(lambda X, Y, B=B: abs(Y - (B.top(0) + B.bot(0)) / 2) < 0.8, '#101418')]
    an = anal(B, .12, .3, 4.2, 'tri', col=fc('A1')); an['band'] = [(lambda X, Y, B=B: Y < B.bot(X) - 2.6, '#e8a632')]
    F.fins += [tail, dorsal(B, .44, .56, 5.8, 'tri', col=fc('A2'), lean=0.5), adipose(B, .14, 2.2, 2.0, col=red, sig=True), an,
               pelvic(B, .5, 3.6, col=fc('A1')), pectoral(B, .78, .66, 4.4, col=fc('A1'))]
    return F
def piracanjuba():
    # set: deeper, darker Brycon / sea-green back sprinkled with a few dark dots, silver flank / a big dark HUMERAL BLOTCH /
    # RED tail and RED anal fin / black streak through the middle of the tail
    P = [(0, .36, -.36), (.1, .5, -.46), (.28, .88, -.8), (.46, 1, -.96), (.62, 1, -.96), (.76, .88, -.84), (.88, .6, -.56), (.96, .3, -.28), (1, .08, -.1)]
    F = Fish('piracanjuba', 44, 16, P, bands('A3', 'A1', 'A1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=10, eye=(0.86, 0.4, 3, '#d0c890'))
    B = F.B; red = '#c8402c'
    F.marks += [m_spot(B, u, t, 0.8, '#14261c') for u, t in scatter(8, .2, .76, .14, .3, seed=0.43, gap=0.08)]
    F.marks += [m_spot(B, .76, .42, 2.0, '#14221a', aspect=1.2), m_stripe(B, 0, .14, .5, 1.4, '#101814')]
    tail = caudal(B, 'fork', 11.0, col=red, sig=True); tail['band'] = [(lambda X, Y, B=B: abs(Y - (B.top(0) + B.bot(0)) / 2) < 0.8, '#101814')]
    F.fins += [tail, dorsal(B, .44, .58, 6.4, 'tri', col=fc('A3'), lean=0.5), adipose(B, .14, 2.6, 2.2, col=FAM['A3'][3]), anal(B, .12, .32, 4.6, 'tri', col=red, sig=True),
               pelvic(B, .5, 4.0, col='#d86a50', sig=True), pectoral(B, .78, .66, 4.6, col=fc('A1'))]
    return F
def golden_dorado():
    # set: big muscular GOLD torpedo (the one all-gold fish of the spring) / amber back, gold flank / three rows of short dark
    # dashes (the scale lines), staggered / BLACK STREAK from the peduncle through the middle of a red-orange tail / orange adipose
    P = [(0, .36, -.36), (.1, .48, -.46), (.3, .86, -.82), (.48, 1, -.96), (.64, 1, -.96), (.78, .9, -.86), (.9, .64, -.62), (.97, .34, -.42), (1, .12, -.26)]
    F = Fish('golden_dorado', 46, 15, P, bands('C2', 'C2', 'C1', sig=('back', 'flank', 'belly'), b1=(0.34, 0.38), b2=(0.84, 0.84)), tilt=10, eye=(0.86, 0.4, 3, '#e8b040'))
    B = F.B; dk = '#5a3000'
    for k, y in enumerate((3.6, 1.2, -1.2)):
        def f(x, yy, uu, tt, y=y, k=k): return (uu > .12) & (uu < .84) & (np.abs(yy - y) <= 0.5) & (((x + 2.0 * k) % 4.2) < 2.0)
        F.marks.append((f, dk))
    F.marks += [m_stripe(B, 0, .1, .5, 1.6, '#1c1208')]
    tail = caudal(B, 'fork', 12.0, col='#e0603a', sig=True); tail['band'] = [(lambda X, Y, B=B: (abs(Y - (B.top(0) + B.bot(0)) / 2) < 1.0) & (X > -7), '#1c1208')]
    F.fins += [tail, dorsal(B, .44, .58, 6.4, 'tri', col='#e09a40', sig=True, lean=0.5), adipose(B, .14, 2.6, 2.2, col='#e07a38', sig=True),
               anal(B, .12, .32, 4.6, 'tri', col='#e08a48', sig=True), pelvic(B, .5, 4.0, col='#e09a52', sig=True), pectoral(B, .78, .64, 5.0, col='#f0c070', sig=True)]
    return F
def common_snook():
    # set: long predator with a CONCAVE forehead and a jutting lower jaw / bronze back over a silver flank / one bold BLACK LATERAL
    # LINE from the gill into the tail / spiny + soft dorsal / amber pelvic and tail fins
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.8), (.5, 1, -.96), (.66, .98, -.96), (.78, .84, -.88), (.88, .58, -.7), (.96, .3, -.5), (1, .1, -.36)]
    F = Fish('common_snook', 48, 13, P, bands('C1', 'A1', 'A1', b1=(0.36, 0.4), b2=(0.86, 0.86)), tilt=10, eye=(0.86, 0.36, 3, '#d8c890'))
    B = F.B
    F.marks += [m_stripe(B, 0, .8, [(0, .5), (.4, .46), (.8, .36)], 1.3, '#101210')]
    tail = caudal(B, 'fork', 10.4, col='#e8a632', sig=True); tail['band'] = [(lambda X, Y, B=B: abs(Y - (B.top(0) + B.bot(0)) / 2) < 0.6, '#2a2a20')]
    F.fins += [tail, dorsal(B, .48, .64, 6.6, 'spiny', col=FAM['C1'][3], lean=0.3, n=9), dorsal(B, .24, .38, 5.4, 'tri', col=fc('C1'), lean=0.4, n=8),
               anal(B, .2, .32, 4.8, 'tri', col=fc('A1')), pelvic(B, .56, 4.4, col='#ecb03c', sig=True), pectoral(B, .78, .56, 4.6, col=fc('A1'))]
    return F
def florida_gar():
    # set: long round tube with a short broad snout / sea-green back, sandy lower flank / big round dark SPOTS scattered over head,
    # body AND every fin / dorsal and anal set far back opposite each other / rounded spotted tail
    P = [(0, .5, -.5), (.08, .74, -.72), (.2, .92, -.9), (.4, 1, -1), (.56, 1, -.98), (.66, .94, -.9), (.73, .8, -.74), (.79, .62, -.56), (.88, .5, -.46), (1, .34, -.3)]
    F = Fish('florida_gar', 50, 9.4, P, bands('A3', 'A3', 'C1', b1=(0.38, 0.42), b2=(0.8, 0.8)), tilt=8, eye=(0.75, 0.36, 2, '#d8a83a'))
    B = F.B; sp = '#0e1a14'
    F.marks += [m_spot(B, u, t, 0.95, sp) for u, t in scatter(14, .04, .7, .16, .72, seed=0.31, gap=0.075)]
    F.marks += [m_spot(B, u, t, 0.9, sp) for u, t in ((.8, .32), (.88, .5), (.94, .36))]
    tail = caudal(B, 'round', 8.0, col=fc('A3'))
    tail['band'] = [fin_spots([(-2.4, .4), (-4.6, 2.2), (-4.8, -1.8), (-6.4, .4), (-2.8, -2.6), (-3.0, 3.0)], 0.75, FAM['A3'][1])]
    df = dorsal(B, .06, .16, 4.6, 'round', col=fc('A3'), n=7); af = anal(B, .04, .15, 4.4, 'round', col=fc('C1'), n=7)
    df['band'] = [fin_spots([(4.5, B.top(4.5) + 2.0), (6.8, B.top(6.8) + 1.6)], 0.7, FAM['A3'][1])]; af['band'] = [fin_spots([(4.0, B.bot(4.0) - 2.0)], 0.7, FAM['C1'][1])]
    F.fins += [tail, df, af, pelvic(B, .4, 3.6, col=fc('C1')), pectoral(B, .7, .78, 3.6, col=fc('C1'))]
    return F
def pacu():
    # set: the big DARK DISC / slate back and sides / warm ORANGE throat and belly / dark fins with an orange pelvic /
    # small blunt-toothed mouth, small adipose
    P = [(0, .3, -.3), (.08, .44, -.42), (.22, .8, -.8), (.4, 1, -.98), (.56, 1, -1), (.7, .92, -.92), (.82, .74, -.72), (.92, .46, -.42), (.98, .2, -.22), (1, .04, -.12)]
    F = Fish('pacu', 40, 26, P, bands('A2', 'A2', 'A2', b1=(0.4, 0.44), b2=(0.9, 0.9)), tilt=12, eye=(0.82, 0.4, 3, '#c8b88a'))
    B = F.B; F.tone0 = 0.0   # a dark fish
    F.patches.append((lambda X, Y, U, T: (T > .7) & (U > .24), FAM['C3']))
    F.fins += [caudal(B, 'emarg', 10.0, col=FAM['A2'][2]), dorsal(B, .44, .58, 7.4, 'tri', col=FAM['A2'][2], lean=0.6, n=10), adipose(B, .12, 2.6, 2.2, col=FAM['A2'][2]),
               anal(B, .1, .4, 6.0, 'long', col=FAM['A2'][2], lean=0.4, n=14), pelvic(B, .5, 4.4, col='#d87a4a', sig=True), pectoral(B, .76, .6, 5.4, col=FAM['A2'][3])]
    return F
def pintado():
    # set: long SHOVEL-NOSED catfish / slate back, silver flank, pearl belly / short dark vertical BARS over the back and a few round
    # spots below them / very LONG barbels / forked tail with dark spots / adipose
    P = [(0, .34, -.34), (.1, .46, -.42), (.3, .84, -.8), (.5, 1, -.96), (.66, .98, -.96), (.8, .8, -.86), (.9, .52, -.66), (.97, .26, -.42), (1, .12, -.3)]
    F = Fish('pintado', 56, 13, P, bands('A2', 'A1', 'N1', b1=(0.36, 0.4), b2=(0.84, 0.84)), tilt=8, eye=(0.88, 0.3, 2, '#c8c0a0'))
    B = F.B; d = '#101416'
    F.marks += [m_bar(B, u, 2.0, .04, .46, d, lean=0.3) for u in np_r(.14, .74, 6)] + [m_spot(B, u, t, 0.9, d) for u, t in ((.2, .62), (.36, .6), (.52, .62), (.66, .58))]
    tail = caudal(B, 'fork', 10.0, col=fc('A1')); tail['band'] = [fin_spots([(-3.0, 2.0), (-5.6, 3.8), (-3.2, -2.2), (-6.0, -3.6), (-7.6, .6)], 0.8, FAM['A2'][1])]
    F.fins += [tail, dorsal(B, .52, .64, 6.0, 'tri', col=fc('A2'), lean=0.4), adipose(B, .2, 5.0, 2.0, col=fc('A2')), anal(B, .14, .3, 4.4, 'round', col=fc('A1')),
               pelvic(B, .48, 4.0, col=fc('N1')), pectoral(B, .82, .6, 5.0, col=fc('A1')),
               barbel(B, .99, .55, 14, -6, '#d4d0ca'), barbel(B, .97, .82, 6, -60, '#c4c0b8'), barbel(B, .95, .9, 5, -80, '#c4c0b8')]
    return F
def gulf_sturgeon():
    # set: huge shark-like sturgeon / charcoal back, sand flank, pearl belly / three rows of pale bony SCUTES (back, side, belly) /
    # shovel snout with four barbels / long upper tail lobe
    P = [(0, .26, -.24), (.08, .44, -.4), (.2, .76, -.7), (.4, 1, -.92), (.6, .98, -.9), (.72, .86, -.78), (.82, .62, -.56), (.9, .4, -.38), (.97, .2, -.22), (1, .08, -.14)]
    F = Fish('gulf_sturgeon', 60, 12, P, bands('N1', 'C1', 'N1', b1=(0.36, 0.4), b2=(0.82, 0.82)), tilt=8, eye=(0.82, 0.34, 2, '#b8a888'))
    B = F.B; sc = '#f1eee9'; F.tone0 = 0.0   # heavy, dark bottom fish
    F.marks += [m_dash(B, .06, .78, t, 1.2, sc, 4.0, 1.6, off=k * 2) for k, t in ((0, .05), (1, .42), (0, .8))]
    F.fins += [caudal(B, 'hetero', 12.0, col=FAM['N1'][3], upper=1.2, lower=0.7), dorsal(B, .1, .2, 4.4, 'tri', col=FAM['N1'][3], lean=0.5, n=7), anal(B, .08, .16, 3.4, 'tri', col=fc('C1'), n=6),
               pelvic(B, .28, 3.4, col=fc('C1')), pectoral(B, .74, .7, 5.6, ang=-28, width=0.4, col=fc('C1')),
               barbel(B, .93, .9, 3.0, -95, '#d4d0ca'), barbel(B, .95, .92, 3.0, -85, '#d4d0ca')]
    return F
SCENE = {
    'curimbata': dict(band=(130, 250), speed=18, fps=8, crowd=90),
    'piraputanga': dict(band=(10, 160), speed=30, fps=9, crowd=90),
    'piracanjuba': dict(band=(40, 200), speed=28, fps=9, crowd=95),
    'golden_dorado': dict(band=(30, 200), speed=32, fps=9, crowd=110, rest=(0.6, 2.0)),
    'common_snook': dict(band=(80, 230), speed=24, fps=8, crowd=110, rest=(1.0, 3.0)),
    'florida_gar': dict(band=(10, 140), speed=14, fps=7, crowd=110, rest=(2.0, 5.0)),
    'pacu': dict(band=(60, 220), speed=18, fps=8, crowd=110),
    'pintado': dict(band=(190, 256), speed=16, fps=7, crowd=130, rest=(1.5, 4.0)),
    'gulf_sturgeon': dict(band=(200, 256), speed=14, fps=7, crowd=140, rest=(1.0, 3.0)),
}
