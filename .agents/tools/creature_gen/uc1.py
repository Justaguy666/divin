"""Underwater Cave batch 1 - small swimmers (soldier- and squirrelfish, bigeyes, sweepers, cardinalfish, comber, anthias, lionfish,
pearlfish); species names only."""
import numpy as np
from swim import Fish, tooth, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
from tidy import tidy
import pal; pal.use('uc')
from pal import ramp
ALL = ['blackbar_soldierfish', 'longspine_squirrelfish', 'glasseye', 'red_bigeye', 'glassy_sweeper', 'golden_sweeper', 'red_cardinalfish',
       'sawcheek_cardinalfish', 'painted_comber', 'swallowtail_seaperch', 'dwarf_lionfish', 'pearlfish']
HOLO = [(0, .3, -.3), (.1, .44, -.42), (.28, .82, -.8), (.46, 1, -.98), (.62, 1, -.98), (.76, .92, -.88), (.87, .72, -.66), (.94, .46, -.42), (1, .16, -.18)]
CARD = [(0, .32, -.32), (.1, .46, -.46), (.3, .84, -.84), (.5, 1, -1), (.66, 1, -.98), (.8, .9, -.86), (.9, .7, -.64), (.96, .44, -.4), (1, .16, -.14)]
SERR = [(0, .32, -.32), (.1, .44, -.42), (.3, .82, -.78), (.48, .98, -.94), (.64, 1, -.96), (.78, .9, -.88), (.88, .7, -.68), (.95, .42, -.44), (1, .14, -.22)]
def holofins(B, col, sig=False, spine=None):
    """soldier/squirrelfish: tall spiny dorsal, soft dorsal and anal at the rear, deeply forked tail"""
    return [caudal(B, 'deepfork', 7.0, col=col, sig=sig), dorsal(B, .4, .72, 4.4, 'spiny', col=col, lean=0.3, n=11, sig=sig), dorsal(B, .2, .38, 4.0, 'tri', col=col, lean=0.5, n=6, sig=sig),
            anal(B, .18, .34, 4.0, 'tri', col=col, lean=0.5, n=6, sig=sig), pelvic(B, .64, 3.4, col=col, sig=sig), pectoral(B, .76, .62, 3.6, col=col, sig=sig)]
def blackbar_soldierfish():
    # Myripristis jacobus: red soldierfish with a huge dark eye, rough scales outlined darker, a broad black bar from the top of the
    # head down behind the gill cover, white leading edges on the red fins
    F = Fish('blackbar_soldierfish', 28, 13, HOLO, bands('#a8302a', '#d8604a', '#ecb0a0', sig=('back', 'flank')), tilt=17, eye=(0.84, 0.4, 3, '#c83a2a'))
    B = F.B
    F.marks += [m_dash(B, .06, .74, t, .6, -1, 1.8, .8, off=k * .9) for k, t in enumerate((.24, .38, .52, .66))] + [m_bar(B, .75, 1.8, .0, .92, '#141010', lean=0.25)]
    F.fins += holofins(B, '#d06048', sig=True); F.mouth = (.56, 1.0); return F
def longspine_squirrelfish():
    # Holocentrus rufus: red and white striped squirrelfish with a big eye, a long sharp spine on the gill cover, a tall spiny dorsal
    # with white spots near its tips, and a very long upper tail lobe
    P = [(0, .3, -.3), (.1, .42, -.4), (.28, .8, -.76), (.46, .98, -.94), (.62, 1, -.96), (.76, .9, -.88), (.87, .7, -.66), (.94, .44, -.42), (1, .16, -.2)]
    F = Fish('longspine_squirrelfish', 32, 12, P, bands('#b0342a', '#d86a52', '#f0d4c8', sig=('back', 'flank')), tilt=16, eye=(0.84, 0.4, 3, '#c83a2a'))
    B = F.B
    F.marks += [m_stripe(B, .04, .82, t, .7, '#f4e8e0') for t in (.3, .46, .62, .78)]
    fins = holofins(B, '#d86a50', sig=True); fins[0] = caudal(B, 'deepfork', 8.0, col='#d86a50', sig=True, upper=1.35, lower=0.95)
    fins[1]['band'] = [(lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 3.0, '#f4ece4')]
    F.fins += fins + [barbel(B, .76, .74, 3.0, 200, '#ecdcd4', thick=0.45)]; F.mouth = (.56, 1.0); return F
def glasseye():
    # Heteropriacanthus cruentatus: deep, compressed bigeye with an enormous eye, rough red-silver body that can blotch silver-white,
    # a large dark-spotted soft dorsal and anal, rounded-truncate tail, upturned mouth
    P = [(0, .34, -.34), (.1, .5, -.48), (.28, .86, -.84), (.46, 1, -1), (.62, 1, -.98), (.76, .9, -.88), (.86, .72, -.7), (.93, .5, -.46), (1, .26, -.18)]
    F = Fish('glasseye', 28, 14, P, bands('#a83a30', '#d0705c', '#e8c4b8', sig=('back', 'flank')), tilt=16, eye=(0.84, 0.44, 3, '#d8a050'))
    B = F.B
    F.marks += [m_spot(B, u, t, 1.4, '#ecdcd4') for u, t in ((.24, .3), (.44, .44), (.6, .28), (.34, .62))]
    dots = [(lambda X, Y: (np.round(X * .9) + np.round(Y * .9)) % 3 == 0, '#5a1a14')]
    fins = [caudal(B, 'truncate', 6.0, col='#c8604c', sig=True), dorsal(B, .42, .7, 4.0, 'spiny', col='#c8604c', lean=0.3, n=10, sig=True),
            dorsal(B, .16, .42, 4.4, 'round', col='#c8604c', n=9, sig=True), anal(B, .14, .42, 4.0, 'round', col='#c8604c', n=9, sig=True),
            pelvic(B, .66, 4.6, col='#a8402e', sig=True), pectoral(B, .76, .6, 3.4, col='#d8907c')]
    for f in fins[2:4]: f['band'] = dots
    F.fins += fins; F.mouth = (.3, 1.4); return F
def red_bigeye():
    # Priacanthus arenatus: oblong bright red bigeye with a huge eye, a long low spiny-soft dorsal and anal, long dark-tinted pelvic fins,
    # slightly forked tail, steeply upturned mouth
    P = [(0, .3, -.3), (.1, .44, -.42), (.28, .82, -.8), (.46, 1, -.98), (.62, 1, -.98), (.76, .92, -.9), (.86, .74, -.72), (.93, .5, -.46), (1, .24, -.14)]
    F = Fish('red_bigeye', 32, 12, P, bands('#a82c26', '#d45a48', '#ec9a88', sig=('back', 'flank', 'belly')), tilt=15, eye=(0.84, 0.44, 3, '#d8a050'))
    B = F.B
    F.marks += [m_dash(B, .06, .74, .5, .6, '#e8a090', 2.0, 1.0)]
    F.fins += [caudal(B, 'emarg', 6.4, col='#c84c3c', sig=True), dorsal(B, .42, .72, 3.2, 'spiny', col='#c84c3c', lean=0.3, n=10, sig=True),
               dorsal(B, .14, .42, 3.4, 'round', col='#c84c3c', n=9, sig=True), anal(B, .12, .42, 3.2, 'round', col='#c84c3c', n=9, sig=True),
               pelvic(B, .66, 5.0, col='#6a2420'), pectoral(B, .78, .6, 3.0, col='#d8806c')]
    F.mouth = (.3, 1.4); return F
def glassy_sweeper():
    # Pempheris schomburgkii: hatchet-shaped sweeper, deep keeled belly tapering to a slender tail, coppery-bronze and translucent, a
    # dark band along the base of the very long anal fin, a short high dorsal near the front, big eye
    P = [(0, .26, -.24), (.1, .36, -.38), (.28, .64, -.76), (.46, .86, -1.0), (.62, .98, -1), (.74, 1, -.9), (.84, .9, -.72), (.92, .66, -.48), (1, .26, -.14)]
    F = Fish('glassy_sweeper', 28, 13, P, bands('#8a5a34', '#c88c5a', '#e8c4a0'), tilt=15, eye=(0.84, 0.42, 3, '#d8c8a0'))
    B = F.B
    F.marks += [m_stripe(B, .06, .66, [(0, .82), (.66, .86)], 1.0, '#3a2414'), m_dash(B, .1, .76, .44, .6, '#e8c8a8', 1.8, .8)]
    F.fins += [caudal(B, 'fork', 6.0, col='#c08a5c'), dorsal(B, .52, .66, 4.4, 'tri', col='#c08a5c', lean=0.6, n=7), anal(B, .06, .62, 3.0, 'long', col='#c89464', n=18),
               pelvic(B, .7, 2.6, col='#d0a070'), pectoral(B, .78, .56, 3.2, col='#dcb48a')]
    F.mouth = (.4, 1.0); return F
def golden_sweeper():
    # Parapriacanthus ransonneti: small translucent golden-yellow sweeper schooling in caves, a golden head shading to a clear pinkish
    # body, the dark spine showing through, a short dorsal near the front, long anal, forked tail
    P = [(0, .26, -.24), (.1, .36, -.38), (.3, .7, -.8), (.5, .92, -1.0), (.66, 1, -.98), (.78, .96, -.84), (.88, .76, -.62), (.95, .48, -.36), (1, .2, -.1)]
    F = Fish('golden_sweeper', 22, 8.4, P, bands('#c89a40', '#e8c06a', '#f0d8b0', sig=('back', 'flank')), tilt=20, eye=(0.84, 0.42, 2, '#e0e0c8'))
    B = F.B
    F.marks += [m_region(B, .0, .5, .2, 1.0, '#e8c8b8'), m_stripe(B, .04, .8, .42, .6, '#8a6a3a')]
    F.fins += [caudal(B, 'fork', 4.8, col='#e0c890'), dorsal(B, .5, .62, 3.0, 'tri', col='#e0c890', lean=0.5, n=5), anal(B, .08, .5, 2.2, 'long', col='#e8d0a0', n=12),
               pelvic(B, .66, 1.8, col='#e8d4a8'), pectoral(B, .78, .56, 2.4, col='#f0dcb4')]
    F.mouth = (.4, .8); return F
def red_cardinalfish():
    # Apogon imberbis: small, stout cardinalfish, bright orange-red, a big eye crossed by two pale lines, two separate dorsals, a dark
    # spot at the tail base, a large mouth
    F = Fish('red_cardinalfish', 22, 9.4, CARD, bands('#b83a2a', '#e06a48', '#f0a888', sig=('back', 'flank', 'belly')), tilt=18, eye=(0.84, 0.4, 3, '#f0e0c0'))
    B = F.B
    F.marks += [m_spot(B, .05, .5, .9, '#4a1410'), m_stripe(B, .86, .99, .32, .5, '#f8dcc8')]
    F.fins += [caudal(B, 'emarg', 5.2, col='#d8644a', sig=True), dorsal(B, .52, .66, 3.4, 'tri', col='#d8644a', lean=0.3, n=6, sig=True),
               dorsal(B, .24, .4, 3.2, 'tri', col='#d8644a', lean=0.4, n=6, sig=True), anal(B, .2, .36, 2.8, 'tri', col='#e07a5c', n=6, sig=True),
               pelvic(B, .64, 2.6, col='#e08a6c'), pectoral(B, .76, .56, 2.8, col='#e8a088')]
    F.mouth = (.5, 1.6); return F
def sawcheek_cardinalfish():
    # Apogon quadrisquamatus: tiny pale, translucent pinkish cardinalfish with a dusky stripe from the snout through the eye, a round dark
    # spot at the tail base, two dorsals, big eye, serrated cheek edge
    F = Fish('sawcheek_cardinalfish', 18, 7.4, CARD, bands('#b8786a', '#e0b0a0', '#f0d8d0'), tilt=20, eye=(0.84, 0.4, 2, '#e8d8c8'))
    B = F.B
    F.marks += [m_spot(B, .05, .5, .9, '#2a1410'), m_stripe(B, .76, 1.0, [(.76, .4), (1.0, .36)], .7, '#6a3a30')]
    F.fins += [caudal(B, 'emarg', 4.2, col='#d8a898'), dorsal(B, .52, .64, 2.8, 'tri', col='#d8a898', lean=0.3, n=5), dorsal(B, .26, .4, 2.6, 'tri', col='#d8a898', lean=0.4, n=5),
               anal(B, .22, .36, 2.2, 'tri', col='#e0b4a4', n=5), pelvic(B, .64, 2.0, col='#e8c0b4'), pectoral(B, .76, .56, 2.2, col='#ecccc0')]
    F.mouth = (.5, 1.2); return F
def painted_comber():
    # Serranus scriba: perch-like comber, reddish-brown with five dark vertical bars, a blue-violet patch on the belly, wavy blue and red
    # scribbles over the head, a yellowish belly, long spiny dorsal, square tail
    F = Fish('painted_comber', 30, 10.6, SERR, bands('#8a4a2c', '#c8845a', '#e0c070'), tilt=16, eye=(0.85, 0.36, 2, '#d8a050'))
    B = F.B
    F.marks += [m_bar(B, u, 2.0, .04, .72, '#4a2214') for u in np_r(.14, .66, 5)] + [m_region(B, .46, .62, .7, .94, '#6a6ac0')]
    F.marks += [m_stripe(B, .82, 1.0, [(.82, t), (.88, t - .06), (.94, t + .04), (1.0, t)], .5, c) for t, c in ((.34, '#5a8ad8'), (.5, '#c8402a'), (.66, '#5a8ad8'))]
    F.fins += [caudal(B, 'truncate', 6.0, col='#b07a50'), dorsal(B, .44, .74, 3.6, 'spiny', col='#a87048', lean=0.3, n=10), dorsal(B, .14, .44, 3.6, 'round', col='#b07a50', n=9),
               anal(B, .14, .32, 3.0, 'round', col='#c08a58', n=7), pelvic(B, .64, 3.0, col='#d0a060'), pectoral(B, .78, .58, 3.4, col='#d8b078')]
    F.gill = (.78, .22, .85, 1.3); F.mouth = (.6, 1.6); return F
def swallowtail_seaperch():
    # Anthias anthias: pink-red anthias with yellow-edged stripes across the snout and cheek, a deeply forked swallow tail with long lobes,
    # very long yellow-tipped pelvic fins, a long third dorsal spine
    P = [(0, .3, -.3), (.1, .44, -.42), (.28, .82, -.8), (.46, 1, -.98), (.62, 1, -.98), (.76, .9, -.88), (.87, .7, -.66), (.94, .44, -.4), (1, .14, -.18)]
    F = Fish('swallowtail_seaperch', 28, 11, P, bands('#b03a4a', '#e0687a', '#f0a8b0', sig=('back', 'flank', 'belly')), tilt=16, eye=(0.84, 0.4, 2, '#e0b060'))
    B = F.B
    F.marks += [m_stripe(B, .8, 1.0, [(.8, .62), (1.0, .4)], .7, '#f0d050'), m_stripe(B, .78, .96, [(.78, .78), (.96, .66)], .6, '#f0d050')]
    tail = caudal(B, 'deepfork', 9.0, col='#d8586a', sig=True, upper=1.3, lower=1.3)
    F.fins += [tail, dorsal(B, .62, .7, 6.0, 'tri', col='#d8586a', lean=0.8, n=4, sig=True), dorsal(B, .2, .62, 3.4, 'flat', col='#d8586a', lean=0.3, n=14, sig=True),
               anal(B, .16, .34, 3.2, 'tri', col='#e07080', n=6, sig=True), pelvic(B, .64, 6.0, ang=-50, col='#f0c050', sig=True), pectoral(B, .78, .58, 3.0, col='#e890a0')]
    F.mouth = (.5, 1.0); return F
def dwarf_lionfish():
    # Dendrochirus brachypterus: small, stocky lionfish banded red-brown and cream, huge fan-like pectoral fins banded dark, a tall spiny
    # dorsal, fleshy tabs above the eyes and on the chin, slow hovering
    P = [(0, .32, -.32), (.1, .46, -.44), (.3, .82, -.8), (.5, .98, -.96), (.66, 1, -.98), (.8, .92, -.92), (.9, .74, -.74), (.96, .48, -.5), (1, .2, -.26)]
    F = Fish('dwarf_lionfish', 26, 11, P, bands('#7a3424', '#c8805a', '#e8c8a8'), tilt=14, eye=(0.84, 0.32, 2, '#d8a050'))
    B = F.B
    F.marks += [m_bar(B, u, 1.4, 0, 1, '#4a1a12', lean=0.3) for u in np_r(.08, .78, 7)]
    band = [(lambda X, Y: (np.round(np.hypot(X, Y) * .7) % 2) == 0, '#5a2014')]
    pec = pectoral(B, .72, .6, 8.0, ang=20, width=0.9, col='#d89a74'); pec['band'] = band
    d = dorsal(B, .34, .78, 6.0, 'spiny', col='#c87a58', lean=0.3, n=12); d['band'] = band
    F.fins += [caudal(B, 'round', 5.6, col='#c87a58'), d, dorsal(B, .14, .34, 3.4, 'round', col='#c87a58', n=6), anal(B, .14, .3, 3.0, 'round', col='#c87a58', n=6), pec,
               pelvic(B, .66, 3.0, col='#d89a74'), barbel(B, .86, 0.0, 2.0, 80, '#e8c8a8', thick=0.6), barbel(B, .96, 1.0, 1.4, -80, '#e8c8a8', thick=0.6)]
    F.mouth = (.6, 1.4); return F
def pearlfish():
    # Carapus acus: slender, eel-like, translucent pearly-white fish that hides inside sea cucumbers, silvery gut and organs showing as a
    # pearly sheen, faint reddish spots along the back, tapering to a thin point, long low fins along back and belly
    P = [(0, .1, -.1), (.1, .36, -.36), (.3, .7, -.7), (.5, .92, -.92), (.7, 1, -1), (.84, 1, -.98), (.92, .84, -.8), (.97, .54, -.5), (1, .22, -.2)]
    F = Fish('pearlfish', 36, 6.0, P, bands('#c0b4b0', '#e4dcd8', '#f2eeec'), tilt=10, eye=(0.9, 0.4, 2, '#d8d0d0'))
    B = F.B
    F.marks += [m_stripe(B, .5, .86, .62, 1.2, '#c8c8cc')] + [m_spot(B, u, .12, .45, '#d07a6a') for u in np_r(.2, .8, 6)]
    F.fins += [dorsal(B, .0, .6, 1.6, 'flat', col='#d8d0cc', n=20, lean=0.0), anal(B, .0, .8, 1.8, 'flat', col='#d8d0cc', n=24, lean=0.0), pectoral(B, .84, .5, 2.2, col='#e0d8d4')]
    F.mouth = (.56, 1.0); return F
SCENE = {
    'blackbar_soldierfish': dict(band=(80, 230), speed=12, fps=8, crowd=55, rest=(1.0, 3.0)),
    'longspine_squirrelfish': dict(band=(80, 230), speed=12, fps=8, crowd=60, rest=(1.0, 3.0)),
    'glasseye': dict(band=(100, 240), speed=10, fps=7, crowd=60, rest=(1.5, 4.0)),
    'red_bigeye': dict(band=(80, 230), speed=12, fps=8, crowd=60, rest=(1.0, 3.0)),
    'glassy_sweeper': dict(band=(40, 200), speed=16, fps=9, crowd=50),
    'golden_sweeper': dict(band=(30, 190), speed=18, fps=9, crowd=40),
    'red_cardinalfish': dict(band=(100, 240), speed=10, fps=8, crowd=45, rest=(1.5, 4.0)),
    'sawcheek_cardinalfish': dict(band=(100, 240), speed=10, fps=8, crowd=40, rest=(1.5, 4.0)),
    'painted_comber': dict(band=(150, 250), speed=14, fps=8, crowd=55, rest=(1.0, 3.0)),
    'swallowtail_seaperch': dict(band=(60, 220), speed=14, fps=8, crowd=55),
    'dwarf_lionfish': dict(band=(140, 245), speed=6, fps=6, crowd=60, rest=(2.0, 5.0)),
    'pearlfish': dict(band=(180, 250), speed=10, fps=7, crowd=50, rest=(1.5, 4.0)),
}
