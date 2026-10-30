"""Clear Spring batch 1 - small swimmers. Each species is defined from its name only (natural anatomy & colour).
v3 (Oct 2026): each species is one memorable set - body shape + fin set + barbels / filaments + pattern + colour - drawn with
few bold markings (nothing finer than 2 px except one defining line, repeats spaced at least their own width)."""
import swim as S
from swim import Fish, m_dash, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots, trail
ALL = ['buenos_aires_tetra', 'coastal_shiner', 'ironcolor_shiner', 'moenkhausia_bonita', 'yellowtail_lambari', 'spotted_pyrrhulina',
       'seminole_killifish', 'swamp_darter', 'tidewater_silverside', 'florida_flagfish', 'sailfin_molly']
def bands(back, flank, belly, b1=(0.34, 0.38), b2=(0.68, 0.7), sig=()):
    """back / flank / belly colours: a hex base (ramp built around it) or a colour-family key ('A1' ... 'C4', pal.FAM)."""
    from pal import lab, hexl, FAM
    if belly not in FAM: b = lab(belly); b[0] = min(b[0], 0.86); belly = hexl(b)
    R = lambda c, s: list(FAM[c]) if c in FAM else ramp(c, sig=s)
    return [(b1[0], b1[1], R(back, 'back' in sig)), (b2[0], b2[1], R(flank, 'flank' in sig)), (1.01, 1.01, R(belly, 'belly' in sig))]
TETRA = [(0, .30, -.30), (.1, .40, -.40), (.28, .74, -.72), (.45, .96, -.92), (.58, 1, -.96), (.7, .94, -.9), (.82, .74, -.7), (.92, .44, -.42), (.97, .24, -.22), (1, .06, -.06)]
MINNOW = [(0, .32, -.32), (.1, .42, -.42), (.28, .74, -.72), (.45, .94, -.92), (.6, 1, -.98), (.74, .92, -.9), (.86, .7, -.66), (.94, .42, -.38), (1, .08, -.1)]
def buenos_aires_tetra():
    # set: compact aqua-silver tetra / slate back / black CROSS on the peduncle (wedge + upright bar) that runs on as a black
    # streak through the red tail / red anal, pelvic and adipose / one faint silver-blue lateral line / small humeral spot
    F = Fish('buenos_aires_tetra', 24, 11.4, TETRA, bands('A2', 'A1', 'A1', b1=(0.3, 0.34), b2=(0.8, 0.8)), eye=(0.82, 0.36, 2, '#d8b860'))
    B = F.B; red = '#d0452e'; blk = '#151b20'
    F.marks += [m_poly(B, [(0, .32), (.17, .44), (.17, .56), (0, .68)], blk), m_bar(B, .07, 1.6, .14, .86, blk),
                m_stripe(B, .18, .58, .44, 1.0, '#bfd6da'), m_spot(B, .76, .34, 1.0, '#284e55')]
    tail = caudal(B, 'fork', 7.4, col=red, sig=True); tail['band'] = [(lambda X, Y, B=B: (X < 0) & (abs(Y - (B.top(0) + B.bot(0)) / 2) < 0.9), blk)]
    F.fins += [tail, dorsal(B, .42, .6, 4.6, 'tri', col='#d8b4ac', lean=0.6), adipose(B, .14, 2.0, 1.6, col='#c85848', sig=True),
               anal(B, .1, .36, 3.4, 'tri', col=red, sig=True, lean=0.6), pelvic(B, .5, 2.8, col=red, sig=True), pectoral(B, .76, .64, 3.0, col=fc('A1'))]
    return F
def coastal_shiner():
    # set: slim pointed minnow / sand-bronze back over a pearl belly / ONE dusky lateral band from the gill that ends in a round
    # black CAUDAL SPOT / clear sandy fins with a forked tail
    F = Fish('coastal_shiner', 25, 9.0, MINNOW, bands('C1', 'C1', 'N1', b1=(0.4, 0.42), b2=(0.82, 0.82)), eye=(0.83, 0.4, 2, '#d4c890'))
    B = F.B
    F.marks += [m_stripe(B, .08, .78, [(0, .5), (.6, .5), (.8, .48)], 1.6, '#4a3622'), m_spot(B, .04, .5, 1.5, '#1e1810')]
    F.fins += [caudal(B, 'fork', 6.8, col=fc('C1')), dorsal(B, .4, .6, 4.0, 'tri', col=fc('C1'), lean=0.6), anal(B, .2, .34, 2.8, 'tri', col=fc('N1')),
               pelvic(B, .5, 2.4, col=fc('N1')), pectoral(B, .78, .64, 3.0, col=fc('N1'))]
    return F
def ironcolor_shiner():
    # set: small minnow / slate back, aqua-silver flank / bold BLACK BAND from the lips through the eye to the tail base, a pale
    # sand stripe riding on top / tangerine blush on the lower flank and the fins (breeding colours)
    F = Fish('ironcolor_shiner', 24, 9.4, MINNOW, bands('A2', 'A1', 'N1', b1=(0.34, 0.36), b2=(0.84, 0.84)), eye=(0.83, 0.42, 2, '#e0c070'))
    B = F.B
    F.marks += [m_stripe(B, 0, 1.0, [(0, .52), (.5, .55), (1, .5)], 2.4, '#141618'), m_stripe(B, .1, .86, [(0, .29), (1, .28)], 1.4, '#e4ccb6')]
    F.patches.append((lambda X, Y, U, T: (T > .72) & (U > .24) & (U < .82), FAM['C3']))
    F.fins += [caudal(B, 'fork', 6.4, col='#e08a5a', sig=True), dorsal(B, .4, .6, 3.8, 'tri', col='#dca088', lean=0.6), anal(B, .2, .34, 2.8, 'tri', col='#e08a5a', sig=True),
               pelvic(B, .5, 2.4, col='#e4925e', sig=True), pectoral(B, .78, .66, 3.0, col=fc('N1'))]
    return F
def moenkhausia_bonita():
    # set: small high-backed tetra / sea-green silver with a pale shine line / RED EYE / black WEDGE on the peduncle that runs
    # into the tail base / white-tipped dorsal and anal fins / dark humeral comma
    F = Fish('moenkhausia_bonita', 23, 11.6, TETRA, bands('A3', 'A3', 'A1', b1=(0.3, 0.34), b2=(0.82, 0.82)), eye=(0.82, 0.36, 2, '#d03a26'))
    B = F.B
    F.marks += [m_poly(B, [(0, .28), (.14, .32), (.18, .5), (.14, .68), (0, .72)], '#0e1814'), m_spot(B, .72, .38, 1.1, '#285140', aspect=0.7),
                m_stripe(B, .2, .66, .46, 1.0, '#e3f3eb')]
    dor = dorsal(B, .38, .58, 5.0, 'tri', col=fc('A3'), lean=0.6); dor['band'] = [(lambda X, Y, B=B: Y > B.top(X) + 3.4, '#f4f8f4')]
    an = anal(B, .1, .38, 3.4, 'tri', col=fc('A3'), lean=0.6); an['band'] = [(lambda X, Y, B=B: Y < B.bot(X) - 2.4, '#f4f8f4')]
    tail = caudal(B, 'fork', 6.6, col=fc('A3')); tail['band'] = [(lambda X, Y, B=B: (X < 0) & (X > -2.6) & (abs(Y - (B.top(0) + B.bot(0)) / 2) < 1.2), '#0e1814')]
    F.fins += [tail, dor, adipose(B, .14, 1.8, 1.4, col=FAM['A3'][3]), an, pelvic(B, .5, 2.4, col=fc('A1')), pectoral(B, .76, .64, 2.8, col=fc('A1'))]
    return F
def yellowtail_lambari():
    # set: lively silver characin / slate back, aqua-silver flank / TWO BLACK SPOTS - a long oval humeral blotch and a diamond on
    # the tail base / bright AMBER tail, amber adipose and anal / faint dusky midline joining the two spots
    F = Fish('yellowtail_lambari', 25, 11.6, TETRA, bands('A2', 'A1', 'A1', b1=(0.3, 0.34), b2=(0.82, 0.82)), eye=(0.82, 0.37, 2, '#d8c070'))
    B = F.B; amb = '#e8a632'
    F.marks += [m_spot(B, .7, .38, 1.3, '#121618', aspect=1.8), m_poly(B, [(0, .5), (.06, .36), (.12, .5), (.06, .64)], '#121618'),
                m_stripe(B, .1, .62, [(0, .5), (.6, .48)], 1.2, -1)]
    F.fins += [caudal(B, 'fork', 7.4, col=amb, sig=True), dorsal(B, .4, .6, 4.4, 'tri', col=fc('A1'), lean=0.6), adipose(B, .14, 1.8, 1.5, col='#e4a238', sig=True),
               anal(B, .12, .36, 3.0, 'tri', col='#e8ac52', sig=True), pelvic(B, .5, 2.6, col='#ecb466', sig=True), pectoral(B, .76, .64, 3.0, col=fc('A1'))]
    return F
def spotted_pyrrhulina():
    # set: slim cylindrical surface fish / sand back, pearl flank / dark EYE STRIPE from snout to gill / two loose rows of rust-red
    # dots / BLACK SPOT on the dorsal / long UPPER tail lobe / tangerine anal and pelvic fins
    P = [(0, .32, -.32), (.1, .44, -.42), (.3, .8, -.76), (.5, .98, -.94), (.66, 1, -.96), (.8, .84, -.8), (.9, .56, -.52), (.96, .3, -.28), (1, .06, -.08)]
    F = Fish('spotted_pyrrhulina', 24, 9.0, P, bands('C1', 'C1', 'N1', b1=(0.36, 0.4), b2=(0.84, 0.84)), eye=(0.83, 0.42, 2, '#d89a50'))
    B = F.B; red = '#b8412e'
    F.marks += [m_stripe(B, .74, 1.0, [(.74, .5), (1, .46)], 1.6, '#2a1a0e')]
    F.marks += [m_spot(B, u, t, 0.9, red) for u, t in ((.22, .46), (.38, .46), (.54, .46), (.3, .68), (.46, .68), (.62, .66))]
    dor = dorsal(B, .44, .62, 4.6, 'tri', col=fc('C1'), lean=0.5)
    dor['band'] = [(lambda X, Y, B=B: (X > .49 * B.L) & (X < .57 * B.L) & (Y > B.top(.53 * B.L) + 1.0) & (Y < B.top(.53 * B.L) + 3.0), '#1c120a')]
    F.fins += [caudal(B, 'fork', 7.4, col=fc('C1'), upper=1.35, lower=0.8), dor,
               anal(B, .18, .32, 3.0, 'tri', col='#d8784e', sig=True), pelvic(B, .52, 2.6, col='#dc8656', sig=True), pectoral(B, .78, .62, 3.0, col=fc('N1'))]
    return F
def seminole_killifish():
    # set: big flat-headed killifish with an UPTURNED snout / azure-steel back, pearly flank / a few black dots on the rear half
    # only / dorsal and anal set far back, opposite each other, square tail with a dusky edge
    P = [(0, .36, -.36), (.1, .46, -.46), (.3, .78, -.8), (.5, .94, -1.0), (.66, .96, -.96), (.8, .86, -.8), (.9, .66, -.56), (.96, .44, -.3), (1, .22, -.06)]
    F = Fish('seminole_killifish', 26, 10.0, P, bands('A4', 'A4', 'A1', b1=(0.34, 0.36), b2=(0.82, 0.82)), tilt=22, eye=(0.81, 0.34, 2, '#c8c08a'))
    B = F.B; d = '#16222a'
    F.marks += [m_spot(B, u, t, 0.85, d) for u, t in ((.14, .42), (.24, .56), (.32, .4), (.4, .58), (.48, .44))]
    tail = caudal(B, 'truncate', 6.0, col=fc('A4')); tail['band'] = [(lambda X, Y: X < -4.6, FAM['A4'][2])]
    F.fins += [tail, dorsal(B, .22, .42, 3.8, 'round', col=fc('A4'), lean=0.5), anal(B, .2, .4, 3.6, 'round', col=fc('A4')),
               pelvic(B, .5, 2.4, col=fc('A1')), pectoral(B, .76, .6, 3.2, col=fc('A1'))]
    return F
def swamp_darter():
    # set: tiny bottom darter perched on big FAN PECTORALS / sand body / four square brown SADDLE-BLOTCHES along the side / dark
    # TEARDROP under the eye / a dark bar on the tail base / spiny + soft dorsals
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.74), (.5, .98, -.9), (.66, 1, -.94), (.8, .84, -.8), (.9, .58, -.52), (.96, .32, -.28), (1, .08, -.1)]
    F = Fish('swamp_darter', 22, 8.2, P, bands('C1', 'C1', 'N1', b1=(0.36, 0.4), b2=(0.84, 0.84)), tilt=22, eye=(0.79, 0.36, 2, '#c8b070'))
    B = F.B; d = '#3a2a16'
    F.marks += [m_spot(B, u, .52, 1.0, d, aspect=1.1) for u in (.2, .36, .52, .66)]
    F.marks += [m_bar(B, .85, 1.2, .55, .98, '#20180a', lean=0.8), m_bar(B, .03, 1.4, .25, .75, '#1c160a')]
    F.fins += [caudal(B, 'round', 5.0, col=fc('C1')), dorsal(B, .48, .66, 2.8, 'spiny', col=FAM['C1'][3], lean=0.3), dorsal(B, .22, .44, 2.6, 'round', col=fc('C1'), lean=0.4),
               anal(B, .22, .36, 2.2, 'round', col=fc('N1')), pelvic(B, .6, 2.4, col=fc('N1')), pectoral(B, .74, .5, 4.4, width=0.6, col=fc('N1'))]
    return F
def tidewater_silverside():
    # set: slender glassy pencil / sea-green back, aqua-silver body / bright SILVER RACING STRIPE with a dark upper edge / big eye /
    # two tiny dorsals, long anal, DEEPLY FORKED tail
    P = [(0, .32, -.32), (.1, .42, -.42), (.3, .76, -.78), (.5, .94, -.98), (.66, .98, -.96), (.8, .82, -.78), (.9, .56, -.5), (.96, .32, -.24), (1, .1, -.04)]
    F = Fish('tidewater_silverside', 26, 7.8, P, bands('A3', 'A1', 'A1', b1=(0.34, 0.36), b2=(0.84, 0.84)), tilt=22, eye=(0.83, 0.42, 3, '#d8dcc8'))
    B = F.B
    F.marks += [m_stripe(B, .04, .82, [(0, .52), (.8, .48)], 1.6, '#f4fbf8'), m_stripe(B, .04, .8, [(0, .36), (.8, .32)], 1.0, '#285140')]
    F.fins += [caudal(B, 'deepfork', 6.8, col=fc('A1')), dorsal(B, .5, .58, 2.0, 'tri', col=fc('A1'), lean=0.4), dorsal(B, .3, .42, 2.8, 'tri', col=fc('A1'), lean=0.6),
               anal(B, .2, .48, 2.6, 'long', col=fc('A1')), pelvic(B, .54, 2.0, col=fc('A1')), pectoral(B, .8, .4, 3.0, ang=-15, col=fc('A1'))]
    return F
def florida_flagfish():
    # set: deep square killifish / sea-green body / two continuous red FLAG LINES across the lower flank / one black BLOTCH mid-side
    # under a long rounded dorsal that carries a black spot / tangerine anal / rounded tail
    P = [(0, .4, -.4), (.1, .52, -.5), (.28, .84, -.82), (.46, .99, -.98), (.6, 1, -.98), (.74, .9, -.86), (.86, .66, -.62), (.94, .4, -.36), (1, .1, -.08)]
    F = Fish('florida_flagfish', 25, 13.4, P, bands('A3', 'A3', 'A1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=16, eye=(0.81, 0.38, 2, '#c8b060'))
    B = F.B; red = '#c8402c'
    F.marks += [m_hline(B, .12, .74, y, 1.0, red) for y in (-1.6, -4.2)] + [m_spot(B, .5, .38, 1.7, '#0e1a14')]
    dor = dorsal(B, .24, .64, 4.8, 'round', col=FAM['A3'][3], lean=0.4, n=14)
    dor['band'] = [(lambda X, Y, B=B: (X > .25 * B.L) & (X < .35 * B.L) & (Y > B.top(.3 * B.L) + 1.0) & (Y < B.top(.3 * B.L) + 3.2), '#0e1a14')]
    F.fins += [caudal(B, 'round', 6.4, col=fc('A3')), dor, anal(B, .2, .44, 3.8, 'round', col='#d8865a'),
               pelvic(B, .56, 2.4, col=fc('A1')), pectoral(B, .74, .58, 3.2, col=fc('A1'))]
    return F
def sailfin_molly():
    # set: male molly / azure-steel with a pearly flank and a few soft dark dots / the HUGE SAIL dorsal from the nape - amber rim
    # and three dark spots / rounded tail with an amber edge / small upturned head
    P = [(0, .44, -.44), (.1, .56, -.54), (.3, .84, -.82), (.48, .98, -.96), (.62, 1, -.96), (.76, .9, -.86), (.88, .64, -.58), (.95, .38, -.3), (1, .12, -.06)]
    F = Fish('sailfin_molly', 26, 11.0, P, bands('A4', 'A4', 'A1', b1=(0.34, 0.38), b2=(0.84, 0.84)), tilt=16, eye=(0.82, 0.4, 2, '#d0c070'))
    B = F.B
    F.marks += [m_spot(B, u, t, 0.8, -1) for u, t in ((.2, .4), (.34, .56), (.48, .4), (.62, .56), (.28, .7), (.52, .72))]
    amb = '#e8962e'
    sail = dorsal(B, .3, .86, 8.6, 'sail', col=FAM['A4'][3], lean=-0.2, n=16)
    sail['band'] = [(lambda X, Y, B=B: (Y > B.top(X) + 6.6), amb)] + [(lambda X, Y, B=B, u=u: ((X - u * B.L) ** 2 + (Y - B.top(u * B.L) - 3.8) ** 2) < 1.3, '#1c2834') for u in (.46, .6, .74)]
    tail = caudal(B, 'round', 6.8, col=FAM['A4'][3]); tail['band'] = [(lambda X, Y: X < -5.4, amb)]
    F.fins += [tail, sail, anal(B, .24, .38, 3.0, 'round', col=fc('A4')), pelvic(B, .5, 2.4, col=fc('A1')), pectoral(B, .76, .54, 3.2, col=fc('A1'))]
    return F
def np_r(a, b, n): return [a + (b - a) * i / (n - 1) for i in range(n)]
# Godot scene tuning (BW step 5): water band (y0, y1), speed, animation fps, crowd radius, rest time
SCENE = {
    'buenos_aires_tetra': dict(band=(40, 200), speed=26, fps=10, crowd=45),
    'coastal_shiner': dict(band=(20, 170), speed=30, fps=10, crowd=45),
    'ironcolor_shiner': dict(band=(40, 200), speed=28, fps=10, crowd=45),
    'moenkhausia_bonita': dict(band=(30, 200), speed=26, fps=10, crowd=45),
    'yellowtail_lambari': dict(band=(20, 180), speed=30, fps=10, crowd=50),
    'spotted_pyrrhulina': dict(band=(8, 120), speed=20, fps=9, crowd=45, rest=(0.8, 2.5)),
    'seminole_killifish': dict(band=(4, 110), speed=24, fps=9, crowd=55),
    'swamp_darter': dict(band=(196, 256), speed=12, fps=8, crowd=40, rest=(1.5, 4.0)),
    'tidewater_silverside': dict(band=(0, 80), speed=32, fps=11, crowd=45),
    'florida_flagfish': dict(band=(120, 240), speed=16, fps=8, crowd=50, rest=(0.8, 2.5)),
    'sailfin_molly': dict(band=(0, 120), speed=18, fps=8, crowd=55, rest=(0.6, 2.0)),
}
