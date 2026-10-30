"""Cold Water batch 1 - small swimmers (gobies, stickleback, pipefish, sandeel, wrasses, poor cod, herring, gunnel); species names only."""
import numpy as np
from swim import Fish, tooth, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
from tidy import tidy
import pal; pal.use('cw')
from pal import ramp
ALL = ['two_spotted_goby', 'fifteen_spined_stickleback', 'snake_pipefish', 'lesser_sandeel', 'atlantic_herring', 'poor_cod', 'goldsinny_wrasse',
       'rock_cook_wrasse', 'corkwing_wrasse', 'cuckoo_wrasse', 'cunner', 'rock_gunnel']
WRASSE = [(0, .36, -.36), (.1, .5, -.48), (.3, .86, -.82), (.5, 1, -.96), (.66, 1, -.96), (.8, .9, -.84), (.9, .68, -.6), (.96, .42, -.38), (1, .16, -.22)]
GAD = [(0, .3, -.3), (.1, .42, -.4), (.28, .78, -.74), (.46, .96, -.92), (.62, 1, -.98), (.76, .94, -.92), (.88, .74, -.74), (.95, .46, -.5), (1, .16, -.28)]
def wfins(B, col, d=(.18, .76, 3.6), a=(.14, .38, 3.2), cau=('round', 6.0), dcol=None, sig=False):
    """wrasse: one long dorsal (spiny front, soft rounded rear), long anal, rounded tail, paddle pectorals"""
    return [caudal(B, cau[0], cau[1], col=col, sig=sig), dorsal(B, .44, d[1], d[2] * 0.85, 'spiny', col=dcol or col, lean=0.2, n=12, sig=sig),
            dorsal(B, d[0], .46, d[2], 'round', col=dcol or col, lean=0.3, n=8, sig=sig), anal(B, a[0], a[1], a[2], 'round', col=col, n=9, sig=sig),
            pelvic(B, .62, 3.0, col=col), pectoral(B, .74, .56, 3.8, width=0.5, col=col)]
def gfins(B, col, s=1.0, cau=('truncate', 6.0)):
    """cod family: three dorsals, two anals, a chin barbel"""
    return [caudal(B, cau[0], cau[1] * s, col=col), dorsal(B, .58, .7, 4.2 * s, 'tri', col=col, lean=0.4, n=6), dorsal(B, .36, .56, 3.6 * s, 'round', col=col, n=8),
            dorsal(B, .12, .34, 3.2 * s, 'round', col=col, n=8), anal(B, .34, .54, 3.0 * s, 'round', col=col, n=8), anal(B, .12, .32, 2.8 * s, 'round', col=col, n=8),
            pelvic(B, .74, 3.0 * s, col=col), pectoral(B, .72, .5, 3.8 * s, col=col), barbel(B, .93, .96, 1.8 * s, -80, col)]
def two_spotted_goby():
    # Gobiusculus flavescens: small hovering goby, reddish-brown back with pale saddles, pale belly, a round dark spot at the tail base,
    # males with a second blue-black spot on the flank behind the pectoral and blue-spotted fins, two dorsals
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .78, -.76), (.5, .96, -.94), (.66, 1, -.96), (.8, .9, -.84), (.9, .66, -.6), (.96, .4, -.34), (1, .14, -.1)]
    F = Fish('two_spotted_goby', 22, 6.8, P, bands('#8a5434', '#c89a76', '#ecdcc8'), tilt=22, eye=(0.82, 0.32, 2, '#c8a070'))
    B = F.B
    F.marks += [m_spot(B, u, .14, .7, '#e8d4b8') for u in (.2, .36, .52)] + [m_spot(B, .04, .5, 1.1, '#141414'), m_spot(B, .66, .5, .9, '#1a2a48')]
    fins = [caudal(B, 'round', 4.8, col='#c09a7a'), dorsal(B, .5, .62, 2.8, 'tri', col='#c09a7a', lean=0.3, n=5), dorsal(B, .2, .44, 2.6, 'round', col='#c09a7a', n=8),
            anal(B, .2, .4, 2.2, 'round', col='#c8a888', n=7), pelvic(B, .66, 2.2, col='#d8c0a8'), pectoral(B, .74, .5, 3.0, col='#d8c4ac')]
    for f in fins[1:4]: f['band'] = [(lambda X, Y: (np.round(X * 1.2) + np.round(Y * 1.2)) % 4 == 0, '#4a7ab8')]
    F.fins += fins; F.mouth = (.5, 1.0); return F
def fifteen_spined_stickleback():
    # Spinachia spinachia: very long and thin, a pointed tube-like snout, a row of about fifteen small free spines along the back,
    # olive-brown to green with a pale belly, a long slender tail stalk, small dorsal and anal set far back opposite each other
    P = [(0, .28, -.28), (.08, .34, -.34), (.2, .52, -.52), (.36, .86, -.84), (.5, 1, -.98), (.66, 1, -.98), (.8, .84, -.82), (.9, .56, -.54), (.96, .34, -.3), (1, .2, -.16)]
    F = Fish('fifteen_spined_stickleback', 36, 4.6, P, bands('#4a5a34', '#9aa26e', '#d4d4b4'), tilt=10, eye=(0.86, 0.4, 1, '#c8c08a'))
    B = F.B
    F.marks += [m_dash(B, .2, .84, .5, .7, -1, 2.4, 1.0)]
    F.fins += [tooth(B, u, 0, ln=0.6, gap=0.3, col='#4a5a34') for u in np_r(.36, .84, 9)]
    F.fins += [caudal(B, 'round', 3.6, col='#8a9468'), dorsal(B, .18, .3, 2.2, 'tri', col='#8a9468', n=5), anal(B, .18, .3, 2.0, 'tri', col='#94a072', n=5),
               pelvic(B, .6, 1.6, col='#a4ac80'), pectoral(B, .8, .5, 2.2, col='#b4ba92')]
    F.mouth = (.5, 1.6); return tidy(F, 4)
def snake_pipefish():
    # Entelurus aequoreus: very long, thin, snake-like pipefish, yellow-brown crossed by many narrow pale blue-edged rings, a tube
    # snout, a small dorsal near the middle, the tail tapering almost to a thread with a tiny tail fin
    P = [(0, .5, -.5), (.06, .56, -.56), (.3, .8, -.8), (.55, 1, -1), (.8, 1, -1), (.88, .92, -.92), (.92, 1.05, -1.0), (.95, .62, -.52), (1, .46, -.38)]
    F = Fish('snake_pipefish', 58, 3.6, P, bands('#7a6034', '#c0a060', '#d8c08a'), tilt=6, eye=(0.92, 0.4, 1, '#c8b070'))
    B = F.B
    F.marks += [m_bar(B, u, 1.0, 0, 1, '#b8ccd4') for u in np_r(.06, .86, 16)]
    F.fins += [caudal(B, 'round', 2.4, col='#a08850'), dorsal(B, .52, .64, 1.6, 'flat', col='#b09858', lean=0.2, n=8)]
    F.mouth = (.5, 1.0); return tidy(F)
def lesser_sandeel():
    # Ammodytes tobianus: slender, eel-like silver fish with a sharply pointed head and jutting lower jaw, green-blue back, bright silver
    # sides, a long low dorsal running along most of the back, a long anal, small forked tail
    P = [(0, .3, -.3), (.08, .5, -.5), (.24, .84, -.84), (.46, 1, -1), (.66, 1, -.98), (.8, .9, -.86), (.9, .64, -.6), (.96, .36, -.38), (1, .08, -.22)]
    F = Fish('lesser_sandeel', 34, 4.8, P, bands('#4a7062', '#c8d4cc', '#eef2ec'), tilt=12, eye=(0.86, 0.38, 1, '#d0d8d0'))
    B = F.B
    F.marks += [m_stripe(B, .04, .86, .3, .7, '#6a9484')]
    F.fins += [caudal(B, 'fork', 4.0, col='#a8b8b0'), dorsal(B, .1, .7, 1.8, 'flat', col='#a8b8b0', lean=0.2, n=22), anal(B, .08, .36, 1.6, 'flat', col='#b8c4bc', n=12),
               pectoral(B, .78, .56, 2.2, col='#c8d2cc')]
    F.mouth = (.6, 1.6); return F
def atlantic_herring():
    # Clupea harengus: streamlined silver fish with a blue-green back, bright silver sides and a sharp keeled belly, one dorsal fin in the
    # middle of the back, deeply forked tail, big eye, slightly jutting lower jaw
    P = [(0, .3, -.3), (.1, .44, -.42), (.28, .8, -.82), (.46, .98, -1), (.62, 1, -.98), (.76, .9, -.86), (.88, .66, -.6), (.95, .42, -.34), (1, .16, -.1)]
    F = Fish('atlantic_herring', 34, 9.6, P, bands('#2e5a6a', '#c4d0d0', '#eef2ee'), tilt=14, eye=(0.86, 0.42, 2, '#d8dcd8'))
    B = F.B
    F.marks += [m_stripe(B, .04, .82, t, .6, -1) for t in (.22, .3)] + [m_stripe(B, .04, .82, .44, .6, '#f4f8f4')]
    F.fins += [caudal(B, 'deepfork', 7.6, col='#9aaeb4'), dorsal(B, .42, .56, 3.8, 'tri', col='#92a6ac', lean=0.4, n=7), anal(B, .1, .26, 2.0, 'low', col='#b4c2c4', n=8),
               pelvic(B, .46, 2.4, col='#c8d2d2'), pectoral(B, .8, .7, 3.0, col='#ccd6d6')]
    F.gill = (.8, .2, .85, 1.3); F.mouth = (.42, 1.2); return F
def poor_cod():
    # Trisopterus minutus: small cod, coppery-bronze back fading to silvery sides and belly, a small dark spot at the base of the
    # pectoral, three dorsals and two anals, a chin barbel, big eye
    F = Fish('poor_cod', 26, 8.4, GAD, bands('#7a5634', '#c8a682', '#ecdcc8'), tilt=16, eye=(0.86, 0.38, 2, '#c8b898'))
    B = F.B
    F.marks += [m_spot(B, .75, .5, .8, '#1a1410')]
    F.fins += gfins(B, '#b8987a', s=0.8); F.gill = (.78, .22, .85, 1.3); F.mouth = (.62, 1.2); return F
def goldsinny_wrasse():
    # Ctenolabrus rupestris: small slender wrasse, golden-brown to reddish, a black spot on the top of the tail base and another at the
    # front of the dorsal fin, pale belly, pointed snout
    F = Fish('goldsinny_wrasse', 24, 8.0, WRASSE, bands('#8a5a2c', '#c89a5a', '#e8d4b0'), tilt=20, eye=(0.84, 0.36, 2, '#c8a060'))
    B = F.B
    F.marks += [m_spot(B, .05, .12, 1.0, '#141210')]
    fins = wfins(B, '#c09060')
    fins[1]['band'] = [(lambda X, Y, B=B: X > .66 * B.L, '#1a1410')]
    F.fins += fins; F.gill = (.76, .22, .85, 1.2); F.mouth = (.56, 1.0); return F
def rock_cook_wrasse():
    # Centrolabrus exoletus: small stocky wrasse, greenish-brown with a bluish sheen, rows of reddish dots, a broad dark band across the
    # middle of the tail fin, males with blue lines on the head
    F = Fish('rock_cook_wrasse', 22, 8.6, WRASSE, bands('#4a5a40', '#8a9a74', '#d0d4bc'), tilt=20, eye=(0.84, 0.36, 2, '#c87a40'))
    B = F.B
    F.marks += [m_dash(B, .1, .7, t, .6, '#a85a3a', 1.6, .7, off=k * .8) for k, t in enumerate((.36, .5, .64))]
    F.marks += [m_stripe(B, .82, .98, [(.82, .56), (.98, .5)], .7, '#4a8ac8')]
    fins = wfins(B, '#7a8a66', cau=('truncate', 5.4)); fins[0]['band'] = [(lambda X, Y: (X < -1.6) & (X > -3.6), '#1a2018')]
    F.fins += fins; F.gill = (.76, .22, .85, 1.2); F.mouth = (.56, 1.0); return F
def corkwing_wrasse():
    # Symphodus melops: deep-bodied wrasse, mottled greenish-brown with darker bars, a dark spot in the middle of the tail base and a
    # dark comma behind the eye, males with wavy blue-green lines over the head and gill cover
    F = Fish('corkwing_wrasse', 26, 10, WRASSE, bands('#4a4a2c', '#8a8452', '#c8c094'), tilt=18, eye=(0.84, 0.36, 2, '#c87a40'))
    B = F.B
    F.marks += [m_bar(B, u, 1.6, .06, .8, -1) for u in np_r(.16, .64, 5)] + [m_spot(B, .04, .5, 1.0, '#141410')]
    F.marks += [m_stripe(B, .77, .8, [(.77, .3), (.8, .62)], .8, '#141410')] + [m_stripe(B, .82, .99, [(.82, t), (.9, t - .06), (.99, t)], .6, '#3a9a8a') for t in (.5, .64)]
    F.fins += wfins(B, '#7e7a50'); F.gill = (.76, .2, .85, 1.3); F.mouth = (.56, 1.0); return F
def cuckoo_wrasse():
    # Labrus mixtus (male): long wrasse, bright orange body with an electric-blue head and blue stripes running back along the upper
    # side, blue-edged orange fins
    F = Fish('cuckoo_wrasse', 34, 10, WRASSE, bands('#c06a2a', '#e09040', '#f0c070', sig=('back', 'flank', 'belly')), tilt=16, eye=(0.85, 0.36, 2, '#d8a050'))
    B = F.B
    F.marks += [m_region(B, .78, 1.0, .0, .85, '#3a6ac8'), m_stripe(B, .3, .8, [(.3, .3), (.8, .26)], .9, '#3a6ac8'), m_stripe(B, .1, .78, [(.1, .5), (.78, .46)], .7, '#3a6ac8')]
    fins = wfins(B, '#d88a44', sig=True)
    for f in fins[:4]: f['band'] = [(lambda X, Y, B=B: (Y > B.top(np.clip(X, 0, B.L)) + 2.8) | (Y < B.bot(np.clip(X, 0, B.L)) - 2.6) | (X < -4.4), '#3a6ac8')]
    F.fins += fins; F.gill = (.76, .2, .85, 1.3); F.mouth = (.56, 1.2); return F
def cunner():
    # Tautogolabrus adspersus: stout wrasse, olive-brown to reddish mottled with darker blotches, pointed snout with thick lips, a long
    # spiny-soft dorsal, rounded tail, pale-blotched fins
    F = Fish('cunner', 28, 11, WRASSE, bands('#4a3a2c', '#8a6a4c', '#c0a080'), tilt=17, eye=(0.84, 0.36, 2, '#b88a50'))
    B = F.B; rng = np.random.RandomState(3)
    F.marks += [m_spot(B, u, t, 1.2 + .6 * rng.rand(), -1) for u, t in zip(rng.uniform(.1, .7, 10), rng.uniform(.15, .75, 10))]
    F.fins += wfins(B, '#7a604a'); F.gill = (.76, .2, .85, 1.3); F.mouth = (.58, 1.2); return F
def rock_gunnel():
    # Pholis gunnellus (butterfish): compressed eel-like fish, yellow-brown mottled darker, a row of about a dozen black spots ringed
    # pale along the base of the long dorsal fin, a dark bar slanting down through the eye, tiny pelvic fins, rounded tail
    P = [(0, .36, -.36), (.06, .62, -.62), (.2, .9, -.9), (.4, 1, -1), (.6, 1, -1), (.78, .96, -.96), (.9, .8, -.78), (.96, .54, -.5), (1, .24, -.2)]
    F = Fish('rock_gunnel', 40, 6.4, P, bands('#6a5030', '#a88a5a', '#d0bc90'), tilt=9, eye=(0.92, 0.4, 1, '#c8a060'))
    B = F.B; rng = np.random.RandomState(6)
    F.marks += [m_spot(B, u, t, 1.0, -1) for u, t in zip(rng.uniform(.05, .85, 12), rng.uniform(.3, .8, 12))]
    F.marks += [m_spot(B, u, .1, .9, '#e8dcc0') for u in np_r(.08, .86, 11)] + [m_spot(B, u, .1, .55, '#141210') for u in np_r(.08, .86, 11)]
    F.marks += [m_stripe(B, .9, .94, [(.9, .1), (.94, .9)], .9, '#1a1410')]
    df = dorsal(B, .02, .9, 2.2, 'flat', col='#8a7048', lean=0.0, n=26)
    F.fins += [caudal(B, 'round', 3.4, col='#8a7048'), df, anal(B, .02, .5, 2.0, 'flat', col='#9a8058', n=16), pectoral(B, .86, .64, 2.4, col='#b09870')]
    F.mouth = (.5, 1.0); return F
SCENE = {
    'two_spotted_goby': dict(band=(60, 220), speed=16, fps=9, crowd=40, rest=(0.8, 2.5)),
    'fifteen_spined_stickleback': dict(band=(100, 240), speed=12, fps=8, crowd=55, rest=(1.0, 3.0)),
    'snake_pipefish': dict(band=(80, 230), speed=8, fps=6, crowd=80, rest=(2.0, 5.0)),
    'lesser_sandeel': dict(band=(20, 200), speed=30, fps=9, crowd=55),
    'atlantic_herring': dict(band=(0, 140), speed=32, fps=9, crowd=55),
    'poor_cod': dict(band=(120, 245), speed=18, fps=8, crowd=55),
    'goldsinny_wrasse': dict(band=(140, 250), speed=16, fps=8, crowd=50),
    'rock_cook_wrasse': dict(band=(140, 250), speed=16, fps=8, crowd=50),
    'corkwing_wrasse': dict(band=(130, 250), speed=16, fps=8, crowd=55),
    'cuckoo_wrasse': dict(band=(100, 240), speed=18, fps=8, crowd=65),
    'cunner': dict(band=(130, 250), speed=14, fps=8, crowd=60),
    'rock_gunnel': dict(band=(210, 258), speed=10, fps=7, crowd=60, rest=(1.5, 4.0)),
}
