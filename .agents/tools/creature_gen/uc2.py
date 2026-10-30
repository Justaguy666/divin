"""Underwater Cave batch 2 - spadefish, snapper, meagre, forkbeard, groupers, tarpon, sharks, eels, cave brotulas; species names only."""
import numpy as np
from swim import Fish, tooth, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
from tidy import tidy
import pal; pal.use('uc')
from pal import ramp
ALL = ['atlantic_spadefish', 'yellowtail_snapper', 'brown_meagre', 'forkbeard', 'dusky_grouper', 'goliath_grouper', 'atlantic_tarpon',
       'nurse_shark', 'sand_tiger_shark', 'spotted_moray', 'european_conger', 'cuban_cave_cusk_eel', 'black_cave_brotula']
GROUP = [(0, .34, -.34), (.1, .48, -.46), (.3, .84, -.82), (.5, 1, -.98), (.66, 1, -.98), (.8, .9, -.92), (.9, .68, -.76), (.96, .42, -.56), (1, .14, -.36)]
EEL = [(0, .1, -.1), (.06, .5, -.5), (.2, .84, -.84), (.4, .98, -.98), (.6, 1, -1), (.8, .98, -.96), (.9, .86, -.8), (.96, .6, -.56), (1, .26, -.3)]
SHARK = [(0, .24, -.22), (.08, .42, -.36), (.22, .74, -.66), (.42, .98, -.9), (.6, 1, -.92), (.76, .9, -.86), (.88, .66, -.66), (.95, .4, -.46), (1, .14, -.3)]
def atlantic_spadefish():
    # Chaetodipterus faber: deep, nearly round disc, silver-grey with four to six dark vertical bars (the first through the eye), tall
    # pointed lobes at the front of the soft dorsal and anal, a small mouth, slightly concave tail
    P = [(0, .2, -.2), (.08, .4, -.4), (.2, .76, -.76), (.36, .98, -.98), (.52, 1, -1), (.66, .94, -.94), (.78, .8, -.8), (.88, .6, -.58), (.95, .38, -.34), (1, .16, -.12)]
    F = Fish('atlantic_spadefish', 34, 28, P, bands('#5a6268', '#b8bec0', '#d8dcdc'), tilt=13, eye=(0.86, 0.4, 2, '#d0d0c8'))
    B = F.B
    F.marks += [m_bar(B, u, 2.2, .02, .98, '#1e2428') for u in (.84, .62, .42, .24)]
    F.fins += [caudal(B, 'emarg', 6.4, col='#8a9296'), dorsal(B, .52, .7, 3.0, 'spiny', col='#7a8286', lean=0.3, n=8), dorsal(B, .14, .5, 9.0, 'sail', col='#8a9296', lean=0.8, n=12),
               anal(B, .14, .48, 8.0, 'sail', col='#8a9296', lean=0.8, n=12), pelvic(B, .66, 4.4, col='#9aa2a6'), pectoral(B, .78, .56, 3.4, col='#b0b6b8')]
    F.mouth = (.5, 1.0); return F
def yellowtail_snapper():
    # Ocyurus chrysurus: streamlined snapper, blue-grey to violet back speckled yellow, silvery sides, a bright yellow stripe from the
    # snout to the deeply forked, all-yellow tail
    P = [(0, .26, -.26), (.1, .4, -.38), (.28, .8, -.76), (.46, .98, -.94), (.62, 1, -.96), (.76, .9, -.88), (.88, .66, -.64), (.95, .4, -.42), (1, .14, -.24)]
    F = Fish('yellowtail_snapper', 44, 13, P, bands('#4e5a8a', '#c4c8d4', '#e8e8ec'), tilt=12, eye=(0.86, 0.38, 2, '#d8a050'))
    B = F.B; rng = np.random.RandomState(31)
    F.marks += [m_stripe(B, .0, 1.0, [(0, .46), (.6, .44), (1, .5)], 1.6, '#f0c830')] + [m_spot(B, u, t, .45, '#e8c840') for u, t in zip(rng.uniform(.1, .8, 12), rng.uniform(.1, .32, 12))]
    F.fins += [caudal(B, 'deepfork', 10.0, col='#f0c030', sig=True), dorsal(B, .42, .68, 3.8, 'spiny', col='#c8b060', lean=0.3, n=10), dorsal(B, .18, .42, 3.4, 'tri', col='#d0b850', lean=0.5, n=7),
               anal(B, .16, .32, 3.2, 'tri', col='#d8c070', n=6), pelvic(B, .6, 3.2, col='#e0d8b0'), pectoral(B, .78, .58, 3.8, col='#d8d4c8')]
    F.gill = (.78, .22, .85, 1.4); F.mouth = (.56, 2.0); return F
def brown_meagre():
    # Sciaena umbra: humpbacked croaker, dark bronze-brown with a golden sheen, black pelvic and anal fins with a bright white leading
    # edge, long two-part dorsal, truncate tail, blunt snout
    P = [(0, .3, -.3), (.1, .46, -.42), (.3, .86, -.76), (.5, 1, -.92), (.66, 1, -.92), (.8, .9, -.86), (.9, .7, -.7), (.96, .46, -.5), (1, .2, -.34)]
    F = Fish('brown_meagre', 44, 15, P, bands('#4a3a24', '#8a6a3e', '#c8a870'), tilt=12, eye=(0.86, 0.4, 2, '#c8a050'))
    B = F.B
    F.marks += [m_dash(B, .06, .82, t, .7, 1, 2.0, 1.0, off=k * 1.0) for k, t in enumerate((.3, .46, .62))]
    edge = [(lambda X, Y: X > 1.4, '#f0ece0')]
    pel = pelvic(B, .62, 4.4, col='#1a1612'); pel['band'] = [(lambda X, Y, x0=.62 * B.L: X > x0 + 0.4, '#f0ece0')]
    an = anal(B, .14, .3, 4.2, 'round', col='#1a1612', n=7); an['band'] = [(lambda X, Y, x0=.3 * B.L: X > x0 - 1.0, '#f0ece0')]
    F.fins += [caudal(B, 'truncate', 7.0, col='#6a5232'), dorsal(B, .56, .76, 5.0, 'spiny', col='#5e4a2e', lean=0.3, n=9), dorsal(B, .12, .56, 4.0, 'round', col='#6a5232', n=14),
               an, pel, pectoral(B, .78, .56, 4.2, col='#8a6e48')]
    F.gill = (.8, .2, .85, 1.5); F.mouth = (.7, 1.6); return F
def forkbeard():
    # Phycis phycis: brown cod-like fish with a short first dorsal and a long second dorsal, a long anal, a chin barbel, and pelvic fins
    # reduced to a pair of long trailing filaments, rounded tail, dark spot at the pectoral base
    P = [(0, .26, -.26), (.1, .4, -.38), (.28, .78, -.74), (.46, .98, -.94), (.62, 1, -.98), (.76, .94, -.92), (.88, .72, -.74), (.95, .44, -.5), (1, .16, -.32)]
    F = Fish('forkbeard', 44, 11.4, P, bands('#5a3e2c', '#9a7458', '#d4b8a0'), tilt=11, eye=(0.86, 0.38, 2, '#c8a878'))
    B = F.B
    F.marks += [m_spot(B, .74, .52, .9, '#1e1410')]
    F.fins += [caudal(B, 'round', 5.6, col='#86644a'), dorsal(B, .62, .72, 3.8, 'tri', col='#7e5e46', lean=0.4, n=5), dorsal(B, .06, .6, 2.8, 'flat', col='#86644a', n=22, lean=0.1),
               anal(B, .06, .5, 2.4, 'flat', col='#8e6c50', n=18, lean=0.1), pectoral(B, .78, .56, 3.6, col='#a8866a'),
               barbel(B, .7, 1.0, 7.0, -150, '#c8a888', thick=0.45), barbel(B, .68, 1.0, 6.0, -158, '#b89878', thick=0.45), barbel(B, .95, .96, 2.0, -80, '#c8a888')]
    F.gill = (.8, .2, .85, 1.4); F.mouth = (.6, 1.8); return tidy(F, 4)
def dusky_grouper():
    # Epinephelus marginatus: heavy grouper, dark reddish-brown with irregular pale blotches in rows, a yellowish belly, a big jaw, and
    # pale edges on the rounded tail, soft dorsal and anal
    F = Fish('dusky_grouper', 58, 18, GROUP, bands('#4a2a22', '#7a4a36', '#c8a060'), tilt=11, eye=(0.86, 0.36, 2, '#c89050'))
    B = F.B; rng = np.random.RandomState(32)
    F.marks += [m_spot(B, u, t, 1.4 + .7 * rng.rand(), '#c8a888') for u, t in zip(rng.uniform(.1, .84, 20), rng.uniform(.12, .62, 20))]
    edge = [(lambda X, Y, B=B: (Y > B.top(np.clip(X, 0, B.L)) + 3.4) | (Y < B.bot(np.clip(X, 0, B.L)) - 3.2) | (X < -5.2), '#e8dcc8')]
    tail = caudal(B, 'round', 9.0, col='#6a3c2c'); tail['band'] = edge; d2 = dorsal(B, .16, .44, 5.0, 'round', col='#6a3c2c', n=9); d2['band'] = edge
    an = anal(B, .14, .32, 4.6, 'round', col='#6a3c2c', n=8); an['band'] = edge
    F.fins += [tail, dorsal(B, .44, .76, 4.0, 'spiny', col='#5e3426', lean=0.2, n=11), d2, an, pelvic(B, .64, 4.4, col='#7a4a36'), pectoral(B, .78, .58, 5.2, col='#8a5a42')]
    F.gill = (.78, .2, .85, 1.7); F.mouth = (.62, 4.6); return F
def goliath_grouper():
    # Epinephelus itajara: enormous grouper with a broad flat head and tiny eyes, yellowish-brown to olive with irregular dark oblique
    # bands and small black spots on the head and fins, rounded fins and tail
    F = Fish('goliath_grouper', 92, 30, GROUP, bands('#4e4426', '#8a7a48', '#c8b88a'), tilt=8, eye=(0.88, 0.34, 2, '#b89a5a'))
    B = F.B; rng = np.random.RandomState(33)
    F.marks += [m_bar(B, u, 4.0, .04, .84, -1, lean=0.6) for u in np_r(.1, .74, 6)]
    F.marks += [m_spot(B, u, t, .5, '#1a160c') for u, t in zip(rng.uniform(.78, .98, 18), rng.uniform(.1, .8, 18))]
    dots = [(lambda X, Y: (np.round(X * .6) + np.round(Y * .6)) % 4 == 0, '#2a2414')]
    tail = caudal(B, 'round', 14.0, col='#7a6c42'); tail['band'] = dots; d2 = dorsal(B, .16, .44, 7.0, 'round', col='#7a6c42', n=9); d2['band'] = dots
    an = anal(B, .14, .32, 6.6, 'round', col='#7a6c42', n=8); an['band'] = dots
    F.fins += [tail, dorsal(B, .44, .76, 5.4, 'spiny', col='#6e6038', lean=0.2, n=11), d2, an, pelvic(B, .64, 6.4, col='#857648'), pectoral(B, .78, .58, 8.0, col='#958656')]
    F.gill = (.8, .2, .85, 2.2); F.mouth = (.62, 7.0); return F
def atlantic_tarpon():
    # Megalops atlanticus: huge, bright silver tarpon with big shiny dark-edged scales, a dark grey-blue back, an upturned bony lower jaw,
    # a long filament trailing from the last dorsal ray, deeply forked tail
    P = [(0, .28, -.28), (.1, .42, -.4), (.28, .8, -.8), (.46, 1, -.98), (.62, 1, -.98), (.76, .9, -.88), (.88, .64, -.66), (.95, .4, -.46), (1, .2, -.32)]
    F = Fish('atlantic_tarpon', 84, 22, P, bands('#3e4c5a', '#c8ccd0', '#e8eaec'), tilt=9, eye=(0.86, 0.42, 3, '#d8d8c8'))
    B = F.B
    F.marks += [m_dash(B, .06, .84, t, .9, -1, 3.4, 1.2, off=k * 1.7) for k, t in enumerate((.22, .36, .5, .64, .78))]
    F.fins += [caudal(B, 'deepfork', 15.0, col='#8a949e'), dorsal(B, .44, .56, 6.0, 'tri', col='#8a949e', lean=0.4, n=7), barbel(B, .45, 0, 12.0, 160, '#7a848e'),
               anal(B, .12, .3, 4.6, 'tri', col='#a8b0b6', n=8), pelvic(B, .5, 4.6, col='#b8bec4'), pectoral(B, .8, .7, 5.6, col='#c4cad0')]
    F.gill = (.8, .2, .85, 2.0); F.mouth = (.2, 5.0); return F
def nurse_shark():
    # Ginglymostoma cirratum: sluggish yellow-brown to tan shark, two rounded dorsal fins set far back and nearly equal in size, a pair of
    # fleshy barbels at the nostrils, small eyes, a long upper tail lobe with almost no lower lobe
    P = [(0, .3, -.3), (.08, .46, -.46), (.22, .76, -.76), (.42, .98, -.96), (.6, 1, -.98), (.76, .94, -.94), (.88, .76, -.8), (.95, .52, -.62), (1, .3, -.46)]
    F = Fish('nurse_shark', 88, 14, P, bands('#6a5432', '#a88a5a', '#d0bc94'), tilt=7, eye=(0.88, 0.34, 1, '#c8a060'))
    B = F.B
    F.fins += [caudal(B, 'hetero', 14.0, col='#8a7048', upper=1.4, lower=0.25), dorsal(B, .42, .52, 5.4, 'round', col='#7e6642', lean=0.4, n=7),
               dorsal(B, .28, .38, 4.6, 'round', col='#7e6642', lean=0.4, n=6), anal(B, .2, .3, 3.4, 'round', col='#8a7048', n=6), pelvic(B, .38, 3.6, col='#8a7048'),
               pectoral(B, .74, .8, 7.0, ang=30, width=0.45, col='#8a7048'), barbel(B, .99, .7, 2.4, -70, '#c8a878', thick=0.55)]
    F.mouth = (.8, 2.0); return F
def sand_tiger_shark():
    # Carcharias taurus: bulky light grey-brown shark with scattered rusty-brown spots, a pointed snout, ragged needle teeth sticking out
    # of the mouth, two large dorsal fins of nearly equal size set well back, a long upper tail lobe
    F = Fish('sand_tiger_shark', 96, 15, SHARK, bands('#6a6458', '#a8a294', '#dcd8cc'), tilt=7, eye=(0.88, 0.38, 2, '#c8b890'))
    B = F.B; rng = np.random.RandomState(34)
    F.marks += [m_spot(B, u, t, .8 + .4 * rng.rand(), '#7a4a32') for u, t in zip(rng.uniform(.1, .7, 22), rng.uniform(.2, .66, 22))]
    F.fins += [caudal(B, 'hetero', 15.0, col='#8a8478', upper=1.35, lower=0.6), dorsal(B, .5, .62, 7.0, 'tri', col='#7e786c', lean=0.6, n=7),
               dorsal(B, .3, .42, 6.4, 'tri', col='#7e786c', lean=0.6, n=7), anal(B, .24, .34, 4.6, 'tri', col='#8a8478', n=6), pelvic(B, .4, 4.6, col='#8a8478'),
               pectoral(B, .72, .8, 9.0, ang=35, width=0.4, col='#8a8478')]
    F.fins += [tooth(B, u, 1.0, ln=0.4, gap=0.0, col='#f0ece4') for u in (.95, .97)]
    F.mouth = (.84, 4.0); return tidy(F, 4)
def spotted_moray():
    # Gymnothorax moringa: moray eel, pale yellowish-white densely covered in dark brown-black spots and blotches, a continuous dorsal fin
    # starting on the head, no pectoral fins, a gaping mouth and a big head
    F = Fish('spotted_moray', 70, 9.4, EEL, bands('#b8a868', '#e0d4a0', '#ece4c4'), tilt=7, eye=(0.92, 0.36, 2, '#e0d070'))
    B = F.B; rng = np.random.RandomState(35)
    F.marks += [m_spot(B, u, t, .7 + .6 * rng.rand(), '#2a2014') for u, t in zip(rng.uniform(.02, .98, 60), rng.uniform(.06, .94, 60))]
    spots = [(lambda X, Y: (np.round(X * .8) * 2 + np.round(Y * .8)) % 3 == 0, '#2a2014')]
    df = dorsal(B, .0, .9, 2.4, 'flat', col='#c8b880', n=34, lean=0.0); df['band'] = spots
    af = anal(B, .0, .5, 2.2, 'flat', col='#c8b880', n=20, lean=0.0); af['band'] = spots
    F.fins += [df, af, caudal(B, 'round', 3.0, col='#c8b880')]
    F.mouth = (.56, 3.0); return F
def european_conger():
    # Conger conger: big scaleless eel, slate grey-blue to near black above, pale grey below, a dorsal fin starting just behind the
    # pectoral and edged black, big eyes, thick lips, pointed pectoral fins
    F = Fish('european_conger', 80, 10, EEL, bands('#3a4450', '#7a8490', '#c8ccd0'), tilt=7, eye=(0.92, 0.36, 2, '#c8c8c0'))
    B = F.B
    black = [(lambda X, Y, B=B: (Y > B.top(np.clip(X, 0, B.L)) + 1.6) | (Y < B.bot(np.clip(X, 0, B.L)) - 1.4), '#141820')]
    df = dorsal(B, .0, .74, 2.4, 'flat', col='#5a6470', n=30, lean=0.0); df['band'] = black
    af = anal(B, .0, .5, 2.2, 'flat', col='#6a7480', n=20, lean=0.0); af['band'] = black
    F.fins += [df, af, caudal(B, 'round', 3.0, col='#5a6470'), pectoral(B, .82, .6, 3.6, width=0.4, col='#8a949c')]
    F.mouth = (.6, 3.0); return F
def cuban_cave_cusk_eel():
    # Lucifuga dentata: blind cave fish with tiny skin-covered eyes, pale pinkish-violet to brown, an eel-like body tapering to a pointed
    # tail joined to the long dorsal and anal fins, pelvic fins reduced to thin filaments under the throat, a big blunt head
    P = [(0, .1, -.1), (.08, .4, -.4), (.24, .74, -.74), (.44, .94, -.94), (.62, 1, -1), (.78, 1, -1), (.88, .9, -.92), (.95, .66, -.72), (1, .34, -.46)]
    F = Fish('cuban_cave_cusk_eel', 40, 8.4, P, bands('#8a6a72', '#c8a0a4', '#e4ccc8'), tilt=10, eye=None)
    B = F.B
    F.marks += [m_spot(B, .9, .36, .6, '#b08890')]
    F.fins += [dorsal(B, .0, .62, 2.2, 'flat', col='#b8949a', n=22, lean=0.0), anal(B, .0, .5, 2.0, 'flat', col='#b8949a', n=18, lean=0.0), caudal(B, 'lance', 3.0, col='#b8949a'),
               pectoral(B, .82, .6, 2.8, col='#d0b0b4'), barbel(B, .86, 1.0, 3.0, -150, '#d8bcbc', thick=0.45)]
    F.mouth = (.6, 1.6); return F
def black_cave_brotula():
    # cave brotula: eel-like, velvety dark brown-black fish of cave crevices, small eyes, a long dorsal and anal running into the
    # rounded tail, thread-like pelvic fins under the throat, a short barbel-fringed snout
    P = [(0, .14, -.14), (.08, .44, -.44), (.24, .78, -.78), (.44, .96, -.96), (.62, 1, -1), (.78, 1, -.98), (.88, .88, -.88), (.95, .64, -.66), (1, .3, -.4)]
    F = Fish('black_cave_brotula', 44, 9.0, P, bands('#3a3432', '#625a56', '#8a8078'), tilt=10, eye=(0.9, 0.36, 1, '#8a8a7a'))
    B = F.B
    F.fins += [dorsal(B, .0, .66, 2.4, 'flat', col='#5a524e', n=24, lean=0.0), anal(B, .0, .52, 2.2, 'flat', col='#5a524e', n=20, lean=0.0), caudal(B, 'round', 3.2, col='#5a524e'),
               pectoral(B, .82, .6, 3.0, col='#5a5250'), barbel(B, .86, 1.0, 3.4, -150, '#8a807a', thick=0.45), barbel(B, .99, .7, 1.2, -60, '#8a807a')]
    F.mouth = (.6, 1.4); return F
SCENE = {
    'atlantic_spadefish': dict(band=(40, 200), speed=14, fps=8, crowd=80),
    'yellowtail_snapper': dict(band=(40, 210), speed=24, fps=8, crowd=80),
    'brown_meagre': dict(band=(120, 245), speed=12, fps=8, crowd=85, rest=(1.5, 4.0)),
    'forkbeard': dict(band=(170, 250), speed=12, fps=8, crowd=85, rest=(1.5, 4.0)),
    'dusky_grouper': dict(band=(130, 250), speed=12, fps=7, crowd=110, rest=(2.0, 5.0)),
    'goliath_grouper': dict(band=(150, 250), speed=8, fps=6, crowd=170, rest=(3.0, 7.0)),
    'atlantic_tarpon': dict(band=(20, 200), speed=20, fps=7, crowd=150, rest=(1.0, 3.0)),
    'nurse_shark': dict(band=(210, 258), speed=10, fps=6, crowd=150, rest=(3.0, 7.0)),
    'sand_tiger_shark': dict(band=(60, 230), speed=14, fps=6, crowd=160, rest=(1.0, 3.0)),
    'spotted_moray': dict(band=(200, 258), speed=8, fps=6, crowd=110, rest=(2.0, 6.0)),
    'european_conger': dict(band=(200, 258), speed=10, fps=6, crowd=120, rest=(2.0, 6.0)),
    'cuban_cave_cusk_eel': dict(band=(190, 258), speed=8, fps=7, crowd=70, rest=(1.5, 4.0)),
    'black_cave_brotula': dict(band=(190, 258), speed=8, fps=7, crowd=70, rest=(1.5, 4.0)),
}
