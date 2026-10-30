"""Billabong batch 1 - rainbowfish, blue-eyes, glassfish, gudgeons, hardyhead; defined from species names only."""
import numpy as np
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
import pal; pal.use('bb')
from pal import ramp
ALL = ['checkered_rainbowfish', 'western_rainbowfish', 'exquisite_rainbowfish', 'black_banded_rainbowfish', 'delicate_blue_eye', 'pacific_blue_eye',
       'spotted_blue_eye', 'sailfin_glassfish', 'empire_gudgeon', 'purple_spotted_gudgeon', 'midgleys_carp_gudgeon', 'fly_specked_hardyhead']
RAIN = [(0, .32, -.32), (.1, .46, -.46), (.28, .84, -.84), (.46, 1, -1), (.6, 1, -.98), (.74, .88, -.84), (.86, .66, -.58), (.94, .4, -.32), (1, .08, -.08)]
SLIM = [(0, .32, -.32), (.1, .42, -.42), (.28, .74, -.72), (.45, .94, -.92), (.6, 1, -.98), (.74, .92, -.9), (.86, .7, -.66), (.94, .42, -.38), (1, .08, -.1)]
GUD = [(0, .38, -.38), (.1, .5, -.5), (.3, .84, -.84), (.5, .98, -.98), (.66, 1, -.98), (.8, .9, -.86), (.9, .7, -.62), (.96, .44, -.36), (1, .14, -.12)]
def rfins(B, col, d2col=None, rim=None, sig=False):
    """rainbowfish: small first dorsal, long second dorsal and anal reaching the tail, forked tail"""
    d2 = dorsal(B, .06, .36, 3.4, 'flat', col=d2col or col, lean=0.5, n=12, sig=sig, ray_every=3); a = anal(B, .04, .48, 3.2, 'long', col=d2col or col, lean=0.5, n=14, sig=sig, ray_every=3)
    if rim: d2['band'] = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 2.4, rim)]; a['band'] = [(lambda X, Y, B=B: Y < B.bot(np.clip(X, 0, B.L)) - 2.2, rim)]
    return [caudal(B, 'fork', 6.6, col=col, sig=sig), dorsal(B, .44, .54, 2.8, 'tri', col=col, lean=0.4, n=5, sig=sig), d2, a,
            pelvic(B, .54, 2.6, col=col, sig=sig), pectoral(B, .76, .6, 3.0, col='#d8d8c8')]
def checkered_rainbowfish():
    # Melanotaenia splendida inornata: deep arched rainbowfish, silvery-olive to golden with a dark edge on every scale (a checkered
    # look), faint orange stripes, yellowish fins with red margins
    F = Fish('checkered_rainbowfish', 26, 11.4, RAIN, bands('#5a5a3c', '#c8c094', '#d8d0ac'), tilt=20, eye=(0.82, 0.4, 2, '#d0b060'))
    B = F.B
    F.marks += [m_dash(B, .08, .78, t, .8, '#4a4630', 1.8, .9, off=k * .9) for k, t in enumerate((.22, .34, .46, .58, .7))]
    F.fins += rfins(B, '#d8c070', rim='#c84a30', sig=True); F.mouth = (.56, 1.0); return F
def western_rainbowfish():
    # Melanotaenia australis: yellow-silver with a dark mid-lateral stripe and thin orange-red stripes between the scale rows, red fins
    F = Fish('western_rainbowfish', 26, 10.8, RAIN, bands('#6a5a2c', '#d8c070', '#e0d098', sig=('flank',)), tilt=20, eye=(0.82, 0.4, 2, '#d0b060'))
    B = F.B
    F.marks += [m_stripe(B, .02, .84, .48, 1.4, '#2a2414')] + [m_stripe(B, .06, .8, t, .7, '#d0603a') for t in (.32, .62, .74)]
    F.fins += rfins(B, '#d0503a', sig=True); F.mouth = (.56, 1.0); return F
def exquisite_rainbowfish():
    # Melanotaenia exquisita: slender, iridescent blue-silver, a black mid-lateral stripe, fins yellow with red margins
    F = Fish('exquisite_rainbowfish', 25, 9.6, RAIN, bands('#3e5468', '#a8bccc', '#ccd6dc', sig=('flank',)), tilt=22, eye=(0.82, 0.4, 2, '#d0c070'))
    B = F.B
    F.marks += [m_stripe(B, .02, .84, .5, 1.3, '#141c24'), m_stripe(B, .1, .7, .34, .7, '#c8d8e8')]
    F.fins += rfins(B, '#e0c050', rim='#d0402a', sig=True); F.mouth = (.56, 1.0); return F
def black_banded_rainbowfish():
    # Melanotaenia nigrans: olive-brown back, golden sides, a bold black band along the middle, fins yellow to red with a dark edge
    F = Fish('black_banded_rainbowfish', 25, 10.2, RAIN, bands('#5a4e2a', '#c8a85c', '#d8c48c'), tilt=20, eye=(0.82, 0.4, 2, '#d0b060'))
    B = F.B
    F.marks += [m_stripe(B, 0, .9, [(0, .5), (.9, .48)], 2.4, '#14120a')]
    F.fins += rfins(B, '#d88a44', rim='#2a1e10', sig=True); F.mouth = (.56, 1.0); return F
def delicate_blue_eye():
    # Pseudomugil tenellus: tiny translucent golden-olive fish with a bright blue upper eye, yellow-and-black edged fins in males
    F = Fish('delicate_blue_eye', 20, 7.0, SLIM, bands('#7a7048', '#d8cc9c', '#e4dcbc'), tilt=25, eye=(0.82, 0.42, 2, '#3a8ad0'))
    B = F.B
    F.marks += [m_stripe(B, .04, .8, .5, .7, -1)]
    d = dorsal(B, .14, .34, 3.4, 'round', col='#e0c860', sig=True, n=8); d['band'] = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 2.4, '#1a1810')]
    F.fins += [caudal(B, 'fork', 5.4, col='#d8cc9c'), dorsal(B, .48, .56, 2.2, 'tri', col='#d8cc9c', n=4), d, anal(B, .12, .36, 3.0, 'round', col='#e0c860', sig=True, n=8),
               pelvic(B, .54, 2.0, col='#e0d8b0'), pectoral(B, .78, .62, 2.6, col='#e4dcc0')]
    F.mouth = (.4, 1.0); return F
def pacific_blue_eye():
    # Pseudomugil signifer: golden-yellow little fish with a blue eye, males with long dorsal and anal fins banded black and yellow
    F = Fish('pacific_blue_eye', 22, 7.6, SLIM, bands('#7a6a30', '#e0c868', '#e8d898', sig=('flank',)), tilt=25, eye=(0.82, 0.42, 2, '#3a8ad0'))
    B = F.B
    bnd = [(lambda X, Y, B=B: (np.floor(np.abs(Y) * 0.8) % 2) == 0, '#1e1a10')]
    d = dorsal(B, .12, .36, 4.4, 'trib', col='#e8d070', sig=True, n=9, lean=0.6); d['band'] = bnd
    a = anal(B, .1, .4, 4.0, 'trib', col='#e8d070', sig=True, n=9, lean=0.6); a['band'] = bnd
    F.fins += [caudal(B, 'fork', 6.0, col='#e0c868', sig=True), dorsal(B, .48, .56, 2.4, 'tri', col='#d8c070', n=4), d, a, pelvic(B, .54, 2.2, col='#e8d898'),
               pectoral(B, .78, .62, 2.6, col='#ecdcb0')]
    F.mouth = (.4, 1.0); return F
def spotted_blue_eye():
    # Pseudomugil gertrudae: yellowish body with dark-edged scales, blue eye, yellow fins covered in black spots
    F = Fish('spotted_blue_eye', 21, 7.8, SLIM, bands('#6a6038', '#d0c084', '#e0d4a8'), tilt=25, eye=(0.82, 0.42, 2, '#3a8ad0'))
    B = F.B
    F.marks += [m_dash(B, .1, .76, t, .7, '#4a4428', 1.8, .8, off=k) for k, t in enumerate((.26, .4, .54))]
    sp = [(lambda X, Y: ((np.round(X * .9) + np.round(Y * .9)) % 3 == 0), '#1a160c')]
    fins = [caudal(B, 'fork', 5.6, col='#e0c460', sig=True), dorsal(B, .48, .56, 2.4, 'tri', col='#d8c070', n=4), dorsal(B, .14, .36, 3.6, 'round', col='#e0c460', sig=True, n=8),
            anal(B, .12, .38, 3.2, 'round', col='#e0c460', sig=True, n=8), pelvic(B, .54, 2.2, col='#e0d4a8'), pectoral(B, .78, .62, 2.6, col='#e4dcc0')]
    for f in (fins[0], fins[2], fins[3]): f['band'] = sp
    F.fins += fins; F.mouth = (.4, 1.0); return F
def sailfin_glassfish():
    # Ambassis agrammus: deep compressed glassy fish, translucent silver body with the dark spine showing through, a tall spiny
    # "sail" dorsal edged dark, silvery belly and gill
    P = [(0, .3, -.3), (.1, .48, -.46), (.28, .86, -.84), (.46, 1, -1), (.62, 1, -.98), (.76, .9, -.86), (.88, .64, -.58), (.95, .38, -.3), (1, .1, -.08)]
    F = Fish('sailfin_glassfish', 22, 11.6, P, bands('#8a9488', '#c8d0c4', '#dce0d6'), tilt=18, eye=(0.82, 0.42, 2, '#d0d0c0'))
    B = F.B
    F.marks += [m_stripe(B, .02, .76, [(0, .48), (.7, .42)], .8, '#4a5450'), m_region(B, .44, .76, .6, .9, '#eef2ec')]
    sail = dorsal(B, .44, .7, 6.6, 'tri', col='#b8c0b4', lean=0.3, n=9); sail['band'] = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 4.8, '#2a302c')]
    F.fins += [caudal(B, 'fork', 6.4, col='#c8d0c4'), sail, dorsal(B, .2, .4, 4.0, 'round', col='#c0c8bc', n=8), anal(B, .16, .4, 4.0, 'round', col='#c8d0c4', n=8),
               pelvic(B, .58, 2.6, col='#d0d6cc'), pectoral(B, .76, .6, 2.8, col='#dce0d6')]
    F.mouth = (.4, 1.0); return F
def empire_gudgeon():
    # Hypseleotris compressa (male): compressed gudgeon, dark olive body with golden flecks and orange-red spots, two dorsals and an anal
    # banded red with blue-white edges
    F = Fish('empire_gudgeon', 24, 9.0, GUD, bands('#3e3a24', '#8a7a48', '#a89464'), tilt=20, eye=(0.82, 0.38, 2, '#d0a050'))
    B = F.B
    F.marks += [m_spot(B, u, t, .55, '#d8703a') for u, t in ((.2, .4), (.32, .56), (.44, .4), (.56, .58), (.68, .42), (.26, .7), (.5, .72))]
    F.marks += [m_spot(B, u, .26, .5, '#e0c060') for u in np_r(.18, .7, 5)]
    edge = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 2.4, '#8ab4d0')]; edgeb = [(lambda X, Y, B=B: Y < B.bot(np.clip(X, 0, B.L)) - 2.4, '#8ab4d0')]
    d1 = dorsal(B, .5, .64, 3.4, 'round', col='#c8503a', sig=True, n=7); d1['band'] = edge
    d2 = dorsal(B, .18, .44, 3.6, 'round', col='#c8503a', sig=True, n=9); d2['band'] = edge
    a = anal(B, .16, .4, 3.4, 'round', col='#c8503a', sig=True, n=9); a['band'] = edgeb
    F.fins += [caudal(B, 'round', 5.6, col='#a87a4c'), d1, d2, a, pelvic(B, .6, 2.6, col='#b08a58'), pectoral(B, .76, .56, 3.2, col='#c0a878')]
    F.mouth = (.5, 1.2); return F
def purple_spotted_gudgeon():
    # Mogurnda adspersa: stout purple-brown gudgeon with rows of red-orange and blue-violet spots, dark streaks below the eye,
    # fins with red-orange edges and blue lines
    F = Fish('purple_spotted_gudgeon', 25, 9.8, GUD, bands('#3a2a32', '#6a5260', '#86707a'), tilt=20, eye=(0.82, 0.38, 2, '#c87048'))
    B = F.B
    F.marks += [m_spot(B, u, t, .55, '#d8603a') for k, t in enumerate((.3, .46, .62)) for u in np_r(.14 + (k % 2) * .05, .7, 6)]
    F.marks += [m_spot(B, u, t, .5, '#8a80d0') for u, t in ((.24, .38), (.4, .54), (.56, .38), (.34, .7))] + [m_stripe(B, .84, .94, [(.84, .6), (.94, .7)], .8, '#1e141a')]
    edge = [(lambda X, Y, B=B: (Y > B.top(np.clip(X, 0, B.L)) + 2.6) | (Y < B.bot(np.clip(X, 0, B.L)) - 2.6), '#d8603a')]
    fins = [caudal(B, 'round', 5.8, col='#6a5260'), dorsal(B, .5, .64, 3.4, 'round', col='#6a5260', n=7), dorsal(B, .18, .44, 3.6, 'round', col='#6a5260', n=9),
            anal(B, .16, .4, 3.4, 'round', col='#6a5260', n=9), pelvic(B, .6, 2.6, col='#7a6270'), pectoral(B, .76, .56, 3.4, col='#94808a')]
    for f in fins[1:4]: f['band'] = edge
    F.fins += fins; F.mouth = (.5, 1.4); return F
def midgleys_carp_gudgeon():
    # Hypseleotris sp. (Midgley's): small translucent olive-tan gudgeon, faint dark marks along the side, males with orange-red dorsal
    # and anal fins edged white
    F = Fish('midgleys_carp_gudgeon', 22, 8.0, GUD, bands('#6a6040', '#c0b088', '#d0c4a2'), tilt=22, eye=(0.82, 0.38, 2, '#d0a050'))
    B = F.B
    F.marks += [m_spot(B, u, .5, .8, '#4a4028', aspect=1.4) for u in np_r(.12, .66, 5)]
    edge = [(lambda X, Y, B=B: (Y > B.top(np.clip(X, 0, B.L)) + 2.4) | (Y < B.bot(np.clip(X, 0, B.L)) - 2.4), '#f0ece0')]
    fins = [caudal(B, 'round', 5.2, col='#c0b088'), dorsal(B, .5, .62, 3.0, 'round', col='#d8703a', sig=True, n=6), dorsal(B, .18, .42, 3.2, 'round', col='#d8703a', sig=True, n=8),
            anal(B, .16, .38, 3.0, 'round', col='#d8703a', sig=True, n=8), pelvic(B, .6, 2.4, col='#c8b892'), pectoral(B, .76, .56, 3.0, col='#d4c8a8')]
    for f in fins[1:4]: f['band'] = edge
    F.fins += fins; F.mouth = (.5, 1.2); return F
def fly_specked_hardyhead():
    # Craterocephalus stercusmuscarum: slim silvery-green fish peppered with dark "fly specks", a bright silver stripe along the side,
    # two small dorsal fins
    F = Fish('fly_specked_hardyhead', 23, 7.6, SLIM, bands('#5a6a5a', '#c4ccbc', '#d8dcd0'), tilt=25, eye=(0.82, 0.42, 2, '#d0d0b0'))
    B = F.B; rng = np.random.RandomState(7)
    F.marks += [m_spot(B, u, t, .45, '#2a3428') for u, t in zip(rng.uniform(.08, .82, 16), rng.uniform(.12, .44, 16))] + [m_stripe(B, .04, .84, .52, 1.2, '#eef2ea')]
    F.fins += [caudal(B, 'fork', 5.8, col='#c0c8b8'), dorsal(B, .5, .58, 2.4, 'tri', col='#b8c0b0', n=4), dorsal(B, .24, .36, 2.8, 'tri', col='#b8c0b0', n=5),
               anal(B, .18, .36, 2.6, 'tri', col='#c8d0c0', n=6), pelvic(B, .54, 2.2, col='#ccd4c6'), pectoral(B, .78, .62, 2.8, col='#d4dacc')]
    F.mouth = (.5, 1.0); return F
SCENE = {
    'checkered_rainbowfish': dict(band=(40, 200), speed=24, fps=10, crowd=50),
    'western_rainbowfish': dict(band=(40, 200), speed=24, fps=10, crowd=50),
    'exquisite_rainbowfish': dict(band=(30, 190), speed=26, fps=10, crowd=45),
    'black_banded_rainbowfish': dict(band=(50, 210), speed=24, fps=10, crowd=50),
    'delicate_blue_eye': dict(band=(0, 90), speed=24, fps=11, crowd=35),
    'pacific_blue_eye': dict(band=(0, 100), speed=24, fps=11, crowd=40),
    'spotted_blue_eye': dict(band=(0, 110), speed=22, fps=11, crowd=40),
    'sailfin_glassfish': dict(band=(60, 210), speed=18, fps=9, crowd=45, rest=(0.8, 2.5)),
    'empire_gudgeon': dict(band=(120, 245), speed=16, fps=9, crowd=45, rest=(1.0, 3.0)),
    'purple_spotted_gudgeon': dict(band=(190, 256), speed=12, fps=8, crowd=45, rest=(1.5, 4.0)),
    'midgleys_carp_gudgeon': dict(band=(130, 245), speed=16, fps=9, crowd=40, rest=(1.0, 3.0)),
    'fly_specked_hardyhead': dict(band=(0, 120), speed=28, fps=10, crowd=40),
}
