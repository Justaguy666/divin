"""Billabong batch 2 - grunters, archerfish, catfish, needlefish, showpieces; defined from species names only."""
import numpy as np
from swim import Fish, tooth, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
import pal; pal.use('bb')
from pal import ramp
ALL = ['spangled_perch', 'banded_grunter', 'sooty_grunter', 'seven_spot_archerfish', 'primitive_archerfish', 'mouth_almighty', 'bony_bream',
       'hyrtls_tandan', 'rendahls_catfish', 'salmon_tailed_catfish', 'freshwater_longtom', 'snub_nosed_garfish', 'barramundi', 'northern_saratoga',
       'oxeye_tarpon', 'australian_lungfish', 'freshwater_sawfish']
GRUNT = [(0, .34, -.34), (.1, .48, -.46), (.28, .84, -.8), (.46, 1, -.96), (.62, 1, -.96), (.76, .9, -.86), (.88, .66, -.62), (.95, .38, -.36), (1, .12, -.16)]
ARCH = [(0, .36, -.36), (.1, .5, -.5), (.28, .8, -.86), (.46, .9, -1.0), (.62, .94, -.98), (.76, .94, -.86), (.86, .86, -.66), (.94, .7, -.4), (1, .46, -.16)]
NEEDLE = [(0, .44, -.44), (.08, .64, -.62), (.2, .9, -.88), (.42, 1, -1), (.6, 1, -.98), (.7, .9, -.88), (.76, .66, -.6), (.8, .5, -.44), (.88, .44, -.36), (.95, .38, -.3), (1, .26, -.2)]
EEL = [(0, .1, -.1), (.08, .44, -.42), (.24, .82, -.78), (.44, .98, -.94), (.62, 1, -.98), (.78, .96, -.92), (.9, .8, -.76), (.96, .52, -.52), (1, .22, -.28)]
def gfins(B, col, d=(.2, .72, 5.0), a=(.14, .32, 4.0), cau=('emarg', 7.4)):
    return [caudal(B, cau[0], cau[1], col=col), dorsal(B, .44, d[1], d[2], 'spiny', col=col, lean=0.2, n=11), dorsal(B, d[0], .44, d[2] * 0.85, 'round', col=col, n=8),
            anal(B, a[0], a[1], a[2], 'round', col=col), pelvic(B, .6, 3.6, col=col), pectoral(B, .76, .58, 4.0, col=col)]
def spangled_perch():
    # Leiopotherapon unicolor: hardy grunter, silvery-olive peppered with small rust-brown spots (spangles), dusky fins
    F = Fish('spangled_perch', 32, 12.8, GRUNT, bands('#56583e', '#b8b49a', '#ccc8b0'), tilt=15, eye=(0.84, 0.4, 2, '#c8a858'))
    B = F.B; rng = np.random.RandomState(3)
    F.marks += [m_spot(B, u, t, .55, '#a8582e') for u, t in zip(rng.uniform(.08, .8, 22), rng.uniform(.14, .76, 22))]
    F.fins += gfins(B, '#a4a088'); F.gill = (.78, .25, .85, 1.5); F.mouth = (.56, 1.6); return F
def banded_grunter():
    # Amniataba percoides: silvery-yellow grunter with six to eight dark vertical bars and a black blotch on the spiny dorsal
    F = Fish('banded_grunter', 30, 12.4, GRUNT, bands('#6a6440', '#d0c48c', '#ddd4ac'), tilt=15, eye=(0.84, 0.4, 2, '#c8a858'))
    B = F.B
    F.marks += [m_bar(B, u, 1.6, .04, .86, '#3a3420') for u in np_r(.1, .74, 7)]
    fins = gfins(B, '#d0c070'); fins[1]['band'] = [(lambda X, Y, B=B: (X > .52 * B.L) & (X < .64 * B.L) & (Y > B.top(np.clip(X, 0, B.L)) + 1.0), '#1a160c')]
    F.fins += fins; F.gill = (.78, .25, .85, 1.5); F.mouth = (.56, 1.6); return F
def sooty_grunter():
    # Hephaestus fuliginosus: big deep grunter, uniformly sooty dark brown to black, thick lips, dark fins
    P = [(0, .34, -.34), (.1, .52, -.5), (.28, .88, -.84), (.46, 1, -.98), (.62, 1, -.98), (.76, .92, -.9), (.88, .74, -.7), (.95, .5, -.48), (1, .2, -.26)]
    F = Fish('sooty_grunter', 38, 17, P, bands('#2a2620', '#4e483c', '#5e5848'), tilt=14, eye=(0.84, 0.4, 2, '#a88850'))
    B = F.B
    F.marks += [m_dash(B, .1, .78, t, .8, -1, 2.2, 1.0, off=k) for k, t in enumerate((.26, .4, .54, .68))]
    F.fins += gfins(B, '#5c5646', d=(.18, .72, 6.0), a=(.12, .34, 5.0), cau=('emarg', 9.0)); F.gill = (.78, .25, .85, 1.8); F.mouth = (.56, 2.0); return F
def seven_spot_archerfish():
    # Toxotes chatareus: flat-topped archerfish with a big eye and upturned mouth, silvery white with six or seven black blotches
    # along the upper side (big and small alternating), dorsal set far back over the anal
    F = Fish('seven_spot_archerfish', 32, 14.6, ARCH, bands('#646c5c', '#bcc2b2', '#d0d4c8'), tilt=12, eye=(0.86, 0.36, 2, '#d0c070'))
    B = F.B
    F.marks += [m_spot(B, u, (.24 if k % 2 == 0 else .3), (1.6 if k % 2 == 0 else 1.0), '#1a1e16') for k, u in enumerate(np_r(.12, .78, 7))]
    F.fins += [caudal(B, 'emarg', 7.4, col='#c8ccb8'), dorsal(B, .16, .4, 4.6, 'spiny', col='#2a2e24', n=9), anal(B, .14, .44, 4.6, 'round', col='#c8c8a8', n=10),
               pelvic(B, .56, 3.4, col='#d0d4c4'), pectoral(B, .76, .58, 3.6, col='#dcdfd4')]
    F.mouth = (.3, 2.0); return F
def primitive_archerfish():
    # Toxotes lorentzi: slimmer archerfish, olive-gold with rows of small dark spots along the upper side, dusky dorsal and a dark band
    # at the tail base
    F = Fish('primitive_archerfish', 30, 12, ARCH, bands('#5a5430', '#b8aa6c', '#cfc49a'), tilt=12, eye=(0.86, 0.36, 2, '#d0c070'))
    B = F.B
    F.marks += [m_spot(B, u, t, .6, '#2a2614') for t in (.2, .34) for u in np_r(.14, .78, 8)] + [m_bar(B, .04, 1.6, .1, .9, '#2a2614')]
    F.fins += [caudal(B, 'emarg', 7.0, col='#a89c68'), dorsal(B, .16, .4, 4.2, 'spiny', col='#4a4428', n=9), anal(B, .14, .44, 4.2, 'round', col='#b0a470', n=10),
               pelvic(B, .56, 3.2, col='#c0b484'), pectoral(B, .76, .58, 3.4, col='#d0c49c')]
    F.mouth = (.3, 1.8); return F
def mouth_almighty():
    # Glossamia aprion: cardinalfish with a huge head and mouth, mottled yellow-brown, dark streaks radiating from the eye, two dorsals,
    # rounded tail
    P = [(0, .36, -.36), (.1, .5, -.5), (.28, .84, -.84), (.46, 1, -.98), (.62, 1, -1), (.76, .94, -.96), (.86, .8, -.84), (.94, .56, -.62), (1, .24, -.4)]
    F = Fish('mouth_almighty', 30, 13.4, P, bands('#5a4a2a', '#b09a64', '#c8b88a'), tilt=14, eye=(0.82, 0.38, 2, '#d0a040'))
    B = F.B; rng = np.random.RandomState(11)
    F.marks += [m_spot(B, u, t, 1.0 + rng.rand() * .6, -2) for u, t in zip(rng.uniform(.1, .7, 10), rng.uniform(.18, .7, 10))]
    F.marks += [m_stripe(B, .86, 1.0, [(.86, .5), (1, .6)], .8, '#2a2012'), m_stripe(B, .86, .98, [(.86, .62), (.98, .8)], .8, '#2a2012')]
    F.fins += [caudal(B, 'round', 7.0, col='#a08c5c'), dorsal(B, .52, .66, 4.6, 'tri', col='#9a8658', n=7), dorsal(B, .24, .42, 4.4, 'round', col='#a08c5c', n=8),
               anal(B, .2, .38, 4.0, 'round', col='#a8946a', n=8), pelvic(B, .62, 3.4, col='#b09c72'), pectoral(B, .74, .56, 3.8, col='#c0ac82')]
    F.gill = (.76, .2, .85, 1.6); F.mouth = (.62, 4.0); return F
def bony_bream():
    # Nematalosa erebi: deep compressed herring, dark back, silvery sides with faint lines, a dark spot behind the gill, blunt snout,
    # deeply forked tail, a trailing filament on the last dorsal ray
    P = [(0, .3, -.3), (.1, .46, -.44), (.28, .84, -.86), (.46, 1, -1), (.62, 1, -.98), (.76, .9, -.84), (.88, .66, -.56), (.95, .42, -.28), (1, .16, -.08)]
    F = Fish('bony_bream', 32, 14.6, P, bands('#3e4a4a', '#c0c8c4', '#d4d8d2'), tilt=13, eye=(0.86, 0.42, 2, '#d0d0c0'))
    B = F.B
    F.marks += [m_stripe(B, .06, .78, t, .7, -1) for t in (.24, .36, .48, .6)] + [m_spot(B, .74, .3, 1.1, '#1a2222')]
    d = dorsal(B, .44, .58, 4.6, 'tri', col='#a4acaa', lean=0.4, n=7); fil = barbel(B, .45, 0, 7.0, 160, '#8a9494')
    F.fins += [caudal(B, 'deepfork', 9.0, col='#a4acaa'), d, fil, anal(B, .12, .32, 3.0, 'low', col='#bcc2bc', n=10), pelvic(B, .5, 2.8, col='#c4cac4'), pectoral(B, .8, .66, 3.6, col='#ccd2cc')]
    F.gill = (.8, .2, .85, 1.5); F.mouth = (.5, 1.2); return F
def _eeltail(B, col, nb=4, blen=3.0):
    f = [dorsal(B, .0, .44, 2.4, 'flat', col=col, n=18, lean=0.0), anal(B, .0, .52, 2.4, 'flat', col=col, n=20, lean=0.0), caudal(B, 'lance', 3.6, col=col),
         dorsal(B, .62, .72, 3.6, 'tri', col=col, n=5), pelvic(B, .5, 2.4, col=col), pectoral(B, .8, .7, 3.4, ang=-10, width=0.35, col=col)]
    for i, (t, a) in enumerate(((.5, 0), (.66, -30), (.8, -55), (.3, 25))[:nb]): f.append(barbel(B, .99 - .01 * i, t, blen - .3 * i, a, '#d0c4a8'))
    return f
def hyrtls_tandan():
    # Neosilurus hyrtlii: eel-tailed catfish, body tapering to a point with one continuous fin round the tail, four pairs of barbels,
    # grey-brown to yellowish, short spined first dorsal, no adipose
    F = Fish('hyrtls_tandan', 40, 9.6, EEL, bands('#4e4a3c', '#9a9278', '#b4ac94'), tilt=8, eye=(0.88, 0.34, 1, '#a89870'))
    B = F.B
    F.fins += _eeltail(B, '#8a846c'); F.mouth = (.6, 1.4); return F
def rendahls_catfish():
    # Porochilus rendahli: small eel-tailed catfish, translucent pinkish-brown, long low fin fringe round the tail, short barbels
    F = Fish('rendahls_catfish', 32, 7.6, EEL, bands('#7a6458', '#c8aa9a', '#d8c2b4'), tilt=10, eye=(0.88, 0.34, 1, '#a89070'))
    B = F.B
    F.fins += _eeltail(B, '#c0a494', blen=2.4); F.mouth = (.6, 1.2); return F
def salmon_tailed_catfish():
    # Neoarius graeffei: fork-tailed catfish, blue-grey back and silver sides, bony head shield, salmon-pink tail, adipose fin, three
    # pairs of barbels
    P = [(0, .34, -.34), (.1, .48, -.44), (.3, .86, -.8), (.5, 1, -.94), (.68, .98, -.94), (.82, .86, -.84), (.92, .62, -.62), (.97, .36, -.4), (1, .16, -.24)]
    F = Fish('salmon_tailed_catfish', 44, 12, P, bands('#3e4a58', '#a4b0bc', '#c8ccd0'), tilt=10, eye=(0.86, 0.34, 2, '#c8c0a0'))
    B = F.B
    F.marks += [m_region(B, .76, .98, .0, .3, -1)]
    F.fins += [caudal(B, 'fork', 9.0, col='#e08a74', sig=True), dorsal(B, .52, .64, 5.4, 'tri', col='#7c8896', n=6), adipose(B, .22, 3.4, 2.2, col='#7c8896'),
               anal(B, .16, .32, 3.8, 'round', col='#d0907a', sig=True), pelvic(B, .48, 3.2, col='#c8a090', sig=True), pectoral(B, .82, .7, 4.4, ang=-10, width=0.35, col='#9aa4ae'),
               barbel(B, .99, .55, 4.0, -5, '#c8c0b0'), barbel(B, .97, .78, 3.0, -45, '#c8c0b0'), barbel(B, .96, .88, 2.6, -70, '#c8c0b0')]
    F.mouth = (.62, 1.6); return F
def freshwater_longtom():
    # Strongylura krefftii: needlefish with both jaws drawn out into a long toothed beak, olive-green back, silver sides with a dark
    # stripe, dorsal and anal set far back
    F = Fish('freshwater_longtom', 54, 6.6, NEEDLE, bands('#4a5a3a', '#bcc4b0', '#d0d4c6'), tilt=8, eye=(0.73, 0.4, 2, '#d0c890'))
    B = F.B
    F.marks += [m_stripe(B, .04, .72, .48, .9, '#2a3424')]
    F.fins += [caudal(B, 'emarg', 6.0, col='#a8b098'), dorsal(B, .06, .22, 3.6, 'tri', col='#a0a890', n=8), anal(B, .06, .24, 3.4, 'tri', col='#acb49c', n=8),
               pelvic(B, .36, 2.4, col='#b8c0a8'), pectoral(B, .66, .66, 3.0, col='#c4ccb6')]
    F.mouth = (.5, 3.0); return F
def snub_nosed_garfish():
    # Arrhamphus sclerolepis: halfbeak with only a short lower-jaw beak (snub-nosed), silvery-green with a dark stripe along the side,
    # dorsal set far back
    P = [(0, .4, -.4), (.08, .6, -.58), (.2, .88, -.86), (.42, 1, -1), (.6, 1, -.98), (.74, .92, -.9), (.84, .7, -.78), (.92, .46, -.62), (.97, .24, -.54), (1, .1, -.48)]
    F = Fish('snub_nosed_garfish', 38, 7.4, P, bands('#4e6050', '#c4ccc0', '#d6dad2'), tilt=10, eye=(0.84, 0.4, 2, '#d0c890'))
    B = F.B
    F.marks += [m_stripe(B, .04, .8, .48, 1.0, '#26322a'), m_region(B, .96, 1.0, .6, 1.0, '#c84a30')]
    F.fins += [caudal(B, 'fork', 6.4, col='#acb6a8'), dorsal(B, .08, .24, 3.4, 'tri', col='#a4ae9e', n=7), anal(B, .08, .24, 3.2, 'tri', col='#b0baac', n=7),
               pelvic(B, .4, 2.4, col='#bcc4b6'), pectoral(B, .8, .5, 3.0, col='#c8d0c2')]
    F.mouth = (.46, 2.0); return F
def barramundi():
    # Lates calcarifer: big silver-grey perch with an olive-bronze back, concave head profile, big mouth, glowing amber-red eye, two
    # dorsals (spiny and soft), rounded tail
    P = [(0, .34, -.34), (.1, .48, -.46), (.3, .86, -.82), (.48, 1, -.96), (.64, 1, -.96), (.76, .86, -.9), (.86, .64, -.74), (.94, .4, -.5), (1, .16, -.32)]
    F = Fish('barramundi', 52, 17, P, bands('#4a4a34', '#b4b4a4', '#c8c8bc'), tilt=10, eye=(0.86, 0.38, 3, '#d86830'))
    B = F.B
    F.marks += [m_dash(B, .08, .8, t, .8, -1, 2.4, 1.0, off=k * 1.2) for k, t in enumerate((.24, .36, .48, .6, .72))]
    F.fins += [caudal(B, 'round', 10.0, col='#8c8c7a'), dorsal(B, .46, .7, 6.6, 'spiny', col='#848470', lean=0.2, n=12), dorsal(B, .22, .44, 6.0, 'round', col='#8c8c7a', n=9),
               anal(B, .16, .32, 5.0, 'round', col='#9a9a88'), pelvic(B, .62, 4.6, col='#a4a494'), pectoral(B, .78, .56, 5.2, col='#b4b4a4')]
    F.gill = (.78, .2, .85, 2.0); F.mouth = (.66, 4.6); return F
def northern_saratoga():
    # Scleropages jardinii: long bony-tongue fish, gold-olive with a red-orange crescent on each of its big scales, upturned mouth with
    # two small chin barbels, dorsal and anal set far back, large pectorals
    P = [(0, .36, -.36), (.1, .5, -.5), (.3, .82, -.86), (.5, .94, -1.0), (.7, .98, -.98), (.84, 1, -.86), (.92, .9, -.62), (.97, .72, -.34), (1, .5, -.1)]
    F = Fish('northern_saratoga', 52, 13, P, bands('#5a5a32', '#b8aa6c', '#cbbf92'), tilt=9, eye=(0.86, 0.36, 3, '#d0c070'))
    B = F.B
    F.marks += [m_dash(B, .08, .82, t, .9, '#c85a32', 3.0, 1.2, off=k * 1.5) for k, t in enumerate((.3, .44, .58, .72))]
    F.fins += [caudal(B, 'round', 9.0, col='#a49a64'), dorsal(B, .08, .32, 4.4, 'low', col='#9c925e', n=12), anal(B, .06, .36, 4.2, 'low', col='#a49a64', n=12),
               pelvic(B, .54, 3.6, col='#b0a670'), pectoral(B, .82, .7, 6.0, ang=-15, col='#bcb07c'), barbel(B, .99, .9, 2.2, -60, '#b0a670')]
    F.gill = (.82, .2, .85, 1.6); F.mouth = (.34, 3.0); return F
def oxeye_tarpon():
    # Megalops cyprinoides: bright silver tarpon with a blue-green back, a very big eye, upturned lower jaw, deeply forked tail and a
    # long trailing filament on the last dorsal ray
    P = [(0, .3, -.3), (.1, .44, -.42), (.28, .82, -.82), (.46, 1, -.98), (.62, 1, -.98), (.76, .9, -.88), (.88, .64, -.64), (.95, .4, -.4), (1, .2, -.26)]
    F = Fish('oxeye_tarpon', 46, 15, P, bands('#2e4a4c', '#c4d0cc', '#d6dcd8'), tilt=10, eye=(0.85, 0.42, 3, '#d8d8c8'))
    B = F.B
    F.marks += [m_dash(B, .08, .82, t, .8, -1, 2.6, 1.0, off=k * 1.2) for k, t in enumerate((.24, .38, .52, .66))]
    fil = barbel(B, .45, 0, 10.0, 158, '#7a9090')
    F.fins += [caudal(B, 'deepfork', 11.0, col='#8ca2a2'), dorsal(B, .44, .56, 5.6, 'tri', col='#8ca2a2', lean=0.4, n=7), fil, anal(B, .14, .32, 4.0, 'tri', col='#a8b8b6'),
               pelvic(B, .5, 3.4, col='#b8c4c2'), pectoral(B, .8, .7, 4.4, col='#c4d0cc')]
    F.gill = (.8, .2, .85, 1.6); F.mouth = (.2, 3.0); return F
def australian_lungfish():
    # Neoceratodus forsteri: heavy, elongated living fossil, olive-brown with scattered dark spots, big scales, paddle-shaped lobed
    # pectoral and pelvic fins, a pointed tail edged by one continuous fin, pale orange-pink belly
    P = [(0, .1, -.1), (.08, .46, -.46), (.24, .82, -.82), (.44, .98, -.98), (.62, 1, -1), (.78, .96, -.96), (.9, .8, -.8), (.96, .54, -.54), (1, .24, -.24)]
    F = Fish('australian_lungfish', 62, 11.6, P, bands('#4a4a30', '#8a8058', '#c8a07a', sig=('belly',)), tilt=8, eye=(0.9, 0.36, 2, '#c8a060'))
    B = F.B; rng = np.random.RandomState(13)
    F.marks += [m_spot(B, u, t, .7, '#24241a') for u, t in zip(rng.uniform(.06, .86, 16), rng.uniform(.12, .6, 16))]
    F.marks += [m_dash(B, .08, .86, t, .7, -1, 3.0, 1.2, off=k * 1.5) for k, t in enumerate((.3, .5))]
    lobe = lambda u, ang: pectoral(B, u, .76, 7.0, ang=ang, width=0.34, col='#b09a6c')
    F.fins += [dorsal(B, .0, .5, 3.0, 'flat', col='#7a7050', n=18, lean=0.0), anal(B, .0, .34, 2.8, 'flat', col='#7a7050', n=14, lean=0.0), caudal(B, 'lance', 4.0, col='#7a7050'),
               lobe(.8, 40), lobe(.44, 50)]
    F.mouth = (.56, 2.0); return F
def freshwater_sawfish():
    # Pristis pristis: shark-like ray with a long flat saw-snout lined with teeth, yellow-brown to olive-grey, flat head, two big dorsal
    # fins, large pectoral fins, shark-like tail
    P = [(0, .32, -.3), (.08, .5, -.46), (.2, .8, -.72), (.36, .98, -.88), (.5, 1, -.9), (.6, .88, -.84), (.66, .62, -.58), (.7, .38, -.34), (.8, .3, -.28), (.92, .28, -.26), (1, .26, -.24)]
    F = Fish('freshwater_sawfish', 72, 12.4, P, bands('#5a5440', '#a09a7c', '#c8c2a8'), tilt=8, eye=(0.62, 0.32, 2, '#c8b880'))
    B = F.B
    F.fins += [tooth(B, .745 + .036 * i, s_, ln=0.2, gap=0.6) for i in range(7) for s_ in (0, 1)]
    F.fins += [caudal(B, 'hetero', 11.0, col='#8a8468', upper=1.3, lower=0.8), dorsal(B, .42, .52, 6.6, 'tri', col='#847e62', lean=0.6, n=7), dorsal(B, .16, .26, 5.0, 'tri', col='#847e62', lean=0.6, n=6),
               pelvic(B, .36, 3.6, col='#948e72'), pectoral(B, .56, .76, 7.0, ang=-25, width=0.5, col='#948e72')]
    F.mouth = (.7, 1.6); return F
SCENE = {
    'spangled_perch': dict(band=(60, 230), speed=20, fps=9, crowd=65),
    'banded_grunter': dict(band=(70, 230), speed=18, fps=9, crowd=65),
    'sooty_grunter': dict(band=(110, 245), speed=16, fps=8, crowd=85, rest=(1.0, 3.0)),
    'seven_spot_archerfish': dict(band=(0, 90), speed=18, fps=9, crowd=70, rest=(0.8, 2.5)),
    'primitive_archerfish': dict(band=(0, 100), speed=18, fps=9, crowd=65, rest=(0.8, 2.5)),
    'mouth_almighty': dict(band=(150, 250), speed=10, fps=8, crowd=60, rest=(2.0, 5.0)),
    'bony_bream': dict(band=(30, 200), speed=24, fps=9, crowd=65),
    'hyrtls_tandan': dict(band=(200, 258), speed=12, fps=8, crowd=65, rest=(1.0, 3.0)),
    'rendahls_catfish': dict(band=(200, 258), speed=12, fps=8, crowd=50, rest=(1.0, 3.0)),
    'salmon_tailed_catfish': dict(band=(180, 256), speed=16, fps=8, crowd=85),
    'freshwater_longtom': dict(band=(0, 60), speed=18, fps=8, crowd=90, rest=(1.5, 4.0)),
    'snub_nosed_garfish': dict(band=(0, 70), speed=22, fps=9, crowd=60),
    'barramundi': dict(band=(80, 240), speed=20, fps=8, crowd=120, rest=(1.0, 3.0)),
    'northern_saratoga': dict(band=(0, 90), speed=18, fps=8, crowd=110, rest=(1.0, 3.0)),
    'oxeye_tarpon': dict(band=(20, 180), speed=24, fps=8, crowd=100),
    'australian_lungfish': dict(band=(200, 256), speed=10, fps=6, crowd=130, rest=(2.0, 5.0)),
    'freshwater_sawfish': dict(band=(200, 256), speed=12, fps=6, crowd=140, rest=(1.5, 4.0)),
}
