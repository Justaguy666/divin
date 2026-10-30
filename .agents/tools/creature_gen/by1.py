"""Bayou batch 1 - small swimmers (topminnows, killifish, minnows, darter, small sunfish), defined from species names only."""
import numpy as np
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
import pal; pal.use('by')
from pal import ramp
ALL = ['bantam_sunfish', 'flier', 'pirate_perch', 'central_mudminnow', 'blackstripe_topminnow', 'golden_topminnow', 'bluefin_killifish',
       'rainwater_killifish', 'least_killifish', 'western_mosquitofish', 'brook_silverside', 'pugnose_minnow', 'taillight_shiner', 'cypress_darter']
SUN = [(0, .34, -.34), (.1, .52, -.5), (.26, .86, -.84), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.84), (.85, .72, -.62), (.93, .46, -.38), (.97, .24, -.24), (1, .06, -.14)]
KILL = [(0, .36, -.36), (.1, .46, -.46), (.3, .78, -.8), (.5, .94, -1.0), (.66, .96, -.96), (.8, .86, -.8), (.9, .66, -.56), (.96, .44, -.3), (1, .22, -.06)]
MIN = [(0, .32, -.32), (.1, .42, -.42), (.28, .74, -.72), (.45, .94, -.92), (.6, 1, -.98), (.74, .92, -.9), (.86, .7, -.66), (.94, .42, -.38), (1, .08, -.1)]
def _tidy(F):
    """drop specks of fewer than 6 pixels left detached from the animal (a fin tip cut loose by the tilt)"""
    import swim
    from scipy import ndimage
    def sheet(F=F):
        sh, W, H, tags = swim.sheet(F)
        for r in range(sh.shape[0] // H):
            for c in range(4):
                fr = sh[r * H:(r + 1) * H, c * W:(c + 1) * W]; lab, n = ndimage.label(fr[..., 3] > 0, structure=np.ones((3, 3)))
                for k in range(1, n + 1):
                    if (lab == k).sum() < 6: fr[lab == k] = 0
        return sh, W, H, tags
    F.sheet = sheet; return F
def kfins(B, col, d=(.22, .4, 3.2), a=(.2, .4, 3.0), cau=('round', 5.2), dcol=None, acol=None, sig=False):
    """killifish / topminnow: one rounded dorsal set far back over the anal, rounded or truncate tail"""
    return [caudal(B, cau[0], cau[1], col=col, sig=sig), dorsal(B, d[0], d[1], d[2], 'round', col=dcol or col, n=8, sig=sig),
            anal(B, a[0], a[1], a[2], 'round', col=acol or col, n=8, sig=sig), pelvic(B, .5, 2.0, col=col), pectoral(B, .76, .58, 2.8, col=col)]
def bantam_sunfish():
    # Lepomis symmetricus: small, deep, rounded sunfish, olive-green flecked with dark spots and faint bars, a plain black ear spot,
    # a dark blotch at the rear base of the soft dorsal, rounded tail
    F = Fish('bantam_sunfish', 22, 13, SUN, bands('#3e4426', '#7e8450', '#bcb488'), tilt=16, eye=(0.8, 0.38, 2, '#b84a28'))
    B = F.B; rng = np.random.RandomState(1)
    F.marks += [m_spot(B, u, t, .45, '#262a16') for u, t in zip(rng.uniform(.16, .7, 16), rng.uniform(.16, .76, 16))] + [m_bar(B, u, 1.6, .08, .86, -1) for u in (.24, .42, .6)]
    F.marks += [m_spot(B, .73, .36, 1.0, '#10120a')]
    d = dorsal(B, .16, .66, 4.4, 'round', col='#6e7446', lean=0.2, n=14); d['band'] = [(lambda X, Y, B=B: (X > .16 * B.L) & (X < .3 * B.L) & (Y < B.top(np.clip(X, 0, B.L)) + 2.2), '#1c1e10')]
    F.fins += [caudal(B, 'round', 6.0, col='#747a4c'), d, anal(B, .14, .4, 3.8, 'round', col='#7a8050', n=10), pelvic(B, .6, 3.2, col='#888c5c'), pectoral(B, .72, .58, 3.6, col='#a0a274')]
    F.gill = (.74, .22, .85, 1.3); F.mouth = (.5, 1.2); return F
def flier():
    # Centrarchus macropterus: round, compressed sunfish with huge dorsal and anal fins of equal size, olive-silver with rows of dark
    # spots forming lines along the sides, a dark teardrop under the eye, an orange-ringed black eyespot on the soft dorsal
    P = [(0, .34, -.34), (.1, .54, -.52), (.26, .88, -.86), (.44, 1, -1), (.6, 1, -.98), (.74, .9, -.86), (.85, .7, -.66), (.93, .44, -.42), (.97, .24, -.28), (1, .08, -.18)]
    F = Fish('flier', 26, 15.6, P, bands('#5a5a3a', '#b0ae8a', '#d0ccb0'), tilt=15, eye=(0.81, 0.38, 2, '#c8a050'))
    B = F.B
    F.marks += [m_dash(B, .1, .72, t, .8, '#2a2a1a', 1.8, .8, off=k * .9) for k, t in enumerate((.22, .34, .46, .58, .7, .82))]
    F.marks += [m_stripe(B, .78, .84, [(.78, .48), (.84, .9)], 1.0, '#1c1c10')]
    d = dorsal(B, .14, .62, 6.4, 'round', col='#8c8a66', lean=0.4, n=14)
    d['band'] = [(lambda X, Y, B=B: ((X - .22 * B.L) ** 2 + (Y - B.top(.22 * B.L) - 2.6) ** 2) < 1.4, '#141410'), (lambda X, Y, B=B: ((X - .22 * B.L) ** 2 + (Y - B.top(.22 * B.L) - 2.6) ** 2) < 3.4, '#d8782c')]
    F.fins += [caudal(B, 'emarg', 7.0, col='#8c8a66'), d, anal(B, .1, .42, 6.0, 'round', col='#8c8a66', lean=0.4, n=12), pelvic(B, .6, 3.6, col='#9c9a76'), pectoral(B, .72, .58, 4.2, col='#b4b28e')]
    F.gill = (.74, .2, .85, 1.4); F.mouth = (.42, 1.4); return F
def pirate_perch():
    # Aphredoderus sayanus: stout, big-headed little perch, dark purplish-brown peppered with darker specks, a dark bar at the tail
    # base and a dark teardrop under the eye, one dorsal with a few short spines in front, slightly notched tail
    P = [(0, .4, -.4), (.1, .54, -.52), (.3, .86, -.84), (.5, 1, -.98), (.66, 1, -.98), (.8, .92, -.9), (.9, .72, -.7), (.96, .46, -.48), (1, .18, -.28)]
    F = Fish('pirate_perch', 26, 11, P, bands('#3a2c2a', '#6a5650', '#9a8a78'), tilt=18, eye=(0.82, 0.38, 2, '#a88858'))
    B = F.B; rng = np.random.RandomState(4)
    F.marks += [m_spot(B, u, t, .4, '#1e1614') for u, t in zip(rng.uniform(.08, .9, 30), rng.uniform(.1, .8, 30))]
    F.marks += [m_bar(B, .03, 1.6, .06, .94, '#1a1210'), m_stripe(B, .8, .86, [(.8, .5), (.86, .92)], 1.0, '#1a1210')]
    F.fins += [caudal(B, 'emarg', 6.0, col='#5e4c46'), dorsal(B, .3, .56, 3.8, 'round', col='#5a4842', lean=0.3, n=10), anal(B, .16, .32, 3.0, 'round', col='#62504a', n=7),
               pelvic(B, .56, 2.6, col='#6e5c54'), pectoral(B, .74, .58, 3.4, col='#86746a')]
    F.gill = (.76, .22, .85, 1.4); F.mouth = (.56, 1.6); return F
def central_mudminnow():
    # Umbra limi: chunky little cylinder with a blunt head, dark olive-brown with about a dozen faint narrow pale bars, a black bar
    # across the tail base, rounded tail and fins, dorsal set well back over the anal
    P = [(0, .46, -.46), (.1, .58, -.58), (.3, .86, -.86), (.5, .98, -1.0), (.66, 1, -.98), (.8, .9, -.86), (.9, .7, -.64), (.96, .46, -.4), (1, .2, -.18)]
    F = Fish('central_mudminnow', 24, 9.2, P, bands('#3a3420', '#7a6c40', '#aa9c6c'), tilt=20, eye=(0.83, 0.38, 2, '#b89850'))
    B = F.B
    F.marks += [m_bar(B, u, .8, .12, .86, 1) for u in np_r(.1, .74, 11)] + [m_bar(B, .03, 1.8, .02, .98, '#12100a')]
    F.fins += kfins(B, '#6a5e38', d=(.22, .42, 3.4), a=(.2, .34, 2.8), cau=('round', 5.4)); F.gill = (.76, .26, .85, 1.2); F.mouth = (.5, 1.2); return F
def blackstripe_topminnow():
    # Fundulus notatus: slender surface killifish with a flat head and upturned mouth, a broad black stripe from the snout to the tail,
    # pale olive back dotted dark, white belly, a shiny gold spot on top of the head, dorsal set far back
    F = Fish('blackstripe_topminnow', 26, 7.8, KILL, bands('#7a7a50', '#c8c6a4', '#ecead8'), tilt=22, eye=(0.82, 0.38, 2, '#c8c090'))
    B = F.B
    F.marks += [m_stripe(B, .02, 1.0, [(0, .52), (.8, .5), (1, .46)], 1.5, '#18180e')]
    F.marks += [m_spot(B, u, .2, .45, '#3a3a24') for u in np_r(.12, .7, 6)] + [m_spot(B, .88, .04, .7, '#ecd88a')]
    F.fins += kfins(B, '#b0ae8c', cau=('round', 5.4)); F.mouth = (.3, 1.4); return F
def golden_topminnow():
    # Fundulus chrysotus: stocky topminnow, olive-gold sprinkled with shining brassy flecks, males with rows of small red-brown spots,
    # rounded fins with a few red dots, gold spot on the head, dorsal far back
    F = Fish('golden_topminnow', 25, 8.8, KILL, bands('#6a6436', '#bca870', '#dcd0a4'), tilt=22, eye=(0.82, 0.38, 2, '#c8b070'))
    B = F.B; rng = np.random.RandomState(7)
    F.marks += [m_spot(B, u, t, .45, '#f0d878') for u, t in zip(rng.uniform(.1, .8, 14), rng.uniform(.2, .7, 14))]
    F.marks += [m_spot(B, u, t, .45, '#a8482a') for u, t in zip(rng.uniform(.1, .7, 9), rng.uniform(.3, .75, 9))] + [m_spot(B, .88, .04, .7, '#f0dc8a')]
    fins = kfins(B, '#a89c64', cau=('round', 5.4))
    for f in fins[:3]: f['band'] = [(lambda X, Y: (np.round(X * 1.3) + np.round(Y * 1.3)) % 4 == 0, '#a8482a')]
    F.fins += fins; F.mouth = (.3, 1.4); return F
def bluefin_killifish():
    # Lucania goodei: small slender killifish with a dark zigzag stripe from the snout to the tail, straw-olive back, males with
    # brilliant blue dorsal and anal fins edged black and a red-orange tail base
    F = Fish('bluefin_killifish', 22, 6.8, KILL, bands('#7a7448', '#c8c098', '#e6e0c6'), tilt=22, eye=(0.82, 0.4, 2, '#c8c090'))
    B = F.B
    F.marks += [m_stripe(B, .02, .98, [(u, .5 + (.08 if k % 2 else -.08)) for k, u in enumerate(np_r(0, 1, 11))], 1.4, '#1c1a10')]
    blue = '#3a7ad0'
    F.fins += [caudal(B, 'round', 4.8, col='#c8643a', sig=True), dorsal(B, .22, .44, 3.4, 'round', col=blue, n=8, sig=True), anal(B, .2, .42, 3.2, 'round', col=blue, n=8, sig=True),
               pelvic(B, .5, 1.8, col='#c8c0a0'), pectoral(B, .76, .58, 2.6, col='#d4ccae')]
    for f in F.fins[1:3]: f['band'] = [(lambda X, Y, B=B: (Y > B.top(np.clip(X, 0, B.L)) + 2.4) | (Y < B.bot(np.clip(X, 0, B.L)) - 2.2), '#141820')]
    F.mouth = (.3, 1.2); return F
def rainwater_killifish():
    # Lucania parva: small, fairly deep killifish, straw-olive with dark-edged scales giving a crosshatched look, males with an
    # orange-tinted dorsal and anal edged black and a dark spot at the front of the dorsal
    P = [(0, .36, -.36), (.1, .48, -.48), (.3, .82, -.84), (.5, .98, -1.0), (.66, .98, -.96), (.8, .86, -.8), (.9, .64, -.56), (.96, .42, -.32), (1, .2, -.1)]
    F = Fish('rainwater_killifish', 22, 8.8, P, bands('#706a42', '#c0b88c', '#e0d8bc'), tilt=22, eye=(0.82, 0.38, 2, '#c8c090'))
    B = F.B
    F.marks += [m_dash(B, .06, .78, t, .7, '#4a4428', 1.6, .7, off=k * .8) for k, t in enumerate((.2, .32, .44, .56, .68))]
    fins = kfins(B, '#c49a5a', d=(.24, .44, 3.4), a=(.2, .4, 3.0), cau=('round', 5.0), sig=True)
    fins[1]['band'] = [(lambda X, Y, B=B: (X > .38 * B.L), '#141410'), (lambda X, Y, B=B: Y > B.top(np.clip(X, 0, B.L)) + 2.6, '#141410')]
    fins[2]['band'] = [(lambda X, Y, B=B: Y < B.bot(np.clip(X, 0, B.L)) - 2.4, '#141410')]
    F.fins += fins; F.mouth = (.32, 1.2); return F
def least_killifish():
    # Heterandria formosa: one of the tiniest fish, olive-tan with a dark stripe from the eye to the tail crossed by faint narrow bars,
    # a dark spot at the base of the dorsal, rounded tail
    F = Fish('least_killifish', 15, 5.4, KILL, bands('#6e6844', '#bab28c', '#e0d8c0'), tilt=24, eye=(0.82, 0.4, 1, '#c8c090'))
    B = F.B
    F.marks += [m_stripe(B, .04, .9, .5, 1.0, '#26241a')] + [m_bar(B, u, .7, .3, .76, -1) for u in np_r(.16, .66, 5)]
    d = dorsal(B, .34, .5, 2.4, 'round', col='#aca480', n=6); d['band'] = [(lambda X, Y, B=B: Y < B.top(np.clip(X, 0, B.L)) + 1.4, '#1a180e')]
    F.fins += [caudal(B, 'round', 3.6, col='#aca480'), d, anal(B, .28, .4, 2.0, 'round', col='#b4ac88', n=5), pectoral(B, .76, .58, 2.0, col='#c8c0a0')]
    F.mouth = (.32, .8); return F
def western_mosquitofish():
    # Gambusia affinis (female): small and plump-bellied, translucent grey-olive with dark-edged scales, a black teardrop under the
    # eye, a dark gravid spot above the anal fin, dorsal set far back, rounded tail with rows of tiny dots
    P = [(0, .34, -.34), (.1, .44, -.46), (.3, .74, -.86), (.5, .9, -1.0), (.66, .96, -.98), (.8, .88, -.8), (.9, .68, -.56), (.96, .44, -.3), (1, .22, -.08)]
    F = Fish('western_mosquitofish', 20, 7.6, P, bands('#6a6a4c', '#b4b49a', '#dcdccc'), tilt=22, eye=(0.82, 0.38, 2, '#c8c8a0'))
    B = F.B
    F.marks += [m_dash(B, .1, .72, t, .6, -1, 1.6, .7, off=k * .8) for k, t in enumerate((.22, .36, .5))]
    F.marks += [m_stripe(B, .8, .86, [(.8, .52), (.86, .92)], .9, '#16160e'), m_spot(B, .4, .74, 1.1, '#2a2a1e')]
    tail = caudal(B, 'round', 4.8, col='#a8a88c'); tail['band'] = [(lambda X, Y: (np.round(X * 1.2) % 2 == 0) & (np.round(Y * 1.2) % 2 == 0), '#4a4a36')]
    F.fins += [tail, dorsal(B, .24, .38, 2.8, 'round', col='#a8a88c', n=6), anal(B, .3, .42, 2.6, 'round', col='#b0b094', n=6), pelvic(B, .54, 1.8, col='#c0c0a8'), pectoral(B, .76, .58, 2.4, col='#c8c8b2')]
    F.mouth = (.3, 1.0); return F
def brook_silverside():
    # Labidesthes sicculus: very slender, glassy pale green, a bright silver stripe along the side, a long beak-like snout and big eye,
    # two small dorsals, a long sickle-shaped anal, forked tail
    P = [(0, .3, -.3), (.1, .4, -.4), (.3, .74, -.76), (.5, .94, -.98), (.66, .98, -.96), (.78, .84, -.8), (.86, .6, -.54), (.93, .4, -.34), (.97, .26, -.22), (1, .12, -.1)]
    F = Fish('brook_silverside', 30, 6.6, P, bands('#8a9a70', '#d8e0c8', '#f2f4ea'), tilt=20, eye=(0.82, 0.42, 2, '#d8dcc8'))
    B = F.B
    F.marks += [m_stripe(B, .04, .8, [(0, .48), (.8, .44)], 1.2, '#f6faf0'), m_stripe(B, .04, .78, [(0, .36), (.78, .32)], .8, '#5a6a4c')]
    F.fins += [caudal(B, 'deepfork', 6.0, col='#c8d0bc'), dorsal(B, .46, .54, 2.2, 'tri', col='#c4ccb6', lean=0.4, n=4), dorsal(B, .24, .36, 2.6, 'tri', col='#c4ccb6', lean=0.6, n=5),
               anal(B, .14, .46, 2.8, 'long', col='#d0d8c4', n=12), pelvic(B, .54, 1.8, col='#dce2d2'), pectoral(B, .78, .44, 3.0, ang=-15, col='#e0e6d8')]
    F.mouth = (.42, 2.0); return F
def pugnose_minnow():
    # Opsopoeodus emiliae: small minnow with a tiny, almost vertical upturned mouth (pug nose), silvery-olive with a dusky stripe along
    # the side, dark-edged back scales, males with a dark band through the dorsal fin
    F = Fish('pugnose_minnow', 24, 7.6, MIN, bands('#6e7050', '#c4c8b0', '#e6e8dc'), tilt=22, eye=(0.84, 0.4, 2, '#d0d0b8'))
    B = F.B
    F.marks += [m_stripe(B, .04, .9, [(0, .5), (.9, .48)], 1.0, '#3a3c2c')] + [m_dash(B, .1, .7, t, .6, '#4a4c38', 1.6, .7, off=k * .8) for k, t in enumerate((.14, .26))]
    d = dorsal(B, .42, .58, 3.6, 'tri', col='#b0b49a', lean=0.5, n=6); d['band'] = [(lambda X, Y, B=B: np.abs(Y - B.top(np.clip(X, 0, B.L)) - 1.8) < 0.7, '#1c1e14')]
    F.fins += [caudal(B, 'fork', 6.0, col='#b8bca4'), d, anal(B, .2, .32, 2.6, 'tri', col='#c4c8b2', n=6), pelvic(B, .5, 2.0, col='#d0d4c0'), pectoral(B, .78, .58, 2.8, col='#d8dcca')]
    F.mouth = (.26, .8); return F
def taillight_shiner():
    # Notropis maculatus: slender shiner with a big round black spot at the tail base (the taillight), a dusky stripe along the side,
    # breeding males flushed rosy-red on the body and fins
    F = Fish('taillight_shiner', 26, 7.8, MIN, bands('#6e5e48', '#d0aa96', '#ecdcd0'), tilt=22, eye=(0.84, 0.4, 2, '#d0c4b0'))
    B = F.B
    F.marks += [m_stripe(B, .08, .9, [(0, .48), (.9, .46)], .9, '#4a3a30'), m_spot(B, .05, .48, 1.5, '#100c0a')]
    F.fins += [caudal(B, 'fork', 6.2, col='#d06a58', sig=True), dorsal(B, .42, .56, 3.4, 'tri', col='#d06a58', lean=0.5, n=6, sig=True), anal(B, .2, .32, 2.6, 'tri', col='#d07a68', n=6, sig=True),
               pelvic(B, .5, 2.0, col='#d8a090'), pectoral(B, .78, .58, 2.8, col='#e0c0b4')]
    F.mouth = (.4, 1.0); return F
def cypress_darter():
    # Etheostoma proeliare: tiny darter, straw-olive with a row of about nine dark dashes along the side, dark saddles, a dark teardrop
    # under the eye, two dorsals (the first with a row of red-orange spots in males), rounded tail, big fan pectorals
    P = [(0, .34, -.34), (.1, .44, -.42), (.3, .8, -.74), (.5, .98, -.9), (.66, 1, -.94), (.8, .84, -.8), (.9, .58, -.52), (.96, .32, -.28), (1, .08, -.1)]
    F = Fish('cypress_darter', 20, 7.4, P, bands('#6e6036', '#c4b486', '#e8e0c4', b1=(0.36, 0.4)), tilt=22, eye=(0.8, 0.36, 2, '#c8b070'))
    B = F.B; d = '#2e2612'
    F.marks += [m_spot(B, u, .52, .7, d, aspect=1.4) for u in np_r(.08, .72, 9)] + [m_spot(B, u, .1, .6, d) for u in (.24, .42, .6)]
    F.marks += [m_bar(B, .85, .9, .55, .95, d, lean=0.8)]
    d1 = dorsal(B, .48, .66, 2.8, 'spiny', col='#c0b088', lean=0.3, n=8); d1['band'] = [(lambda X, Y, B=B: np.abs(Y - B.top(np.clip(X, 0, B.L)) - 1.3) < 0.6, '#c8502a')]
    F.fins += [caudal(B, 'round', 4.6, col='#c4b48a'), d1, dorsal(B, .22, .44, 2.6, 'round', col='#c8b88e', lean=0.4, n=8),
               anal(B, .22, .36, 2.2, 'round', col='#d4c6a0'), pelvic(B, .6, 2.2, col='#d8cca8'), pectoral(B, .74, .5, 3.6, width=0.55, col='#dcd2b0')]
    F.mouth = (.55, .9); return _tidy(F)
SCENE = {
    'bantam_sunfish': dict(band=(100, 230), speed=14, fps=8, crowd=55),
    'flier': dict(band=(60, 220), speed=16, fps=8, crowd=65),
    'pirate_perch': dict(band=(170, 256), speed=10, fps=7, crowd=55, rest=(2.0, 5.0)),
    'central_mudminnow': dict(band=(170, 256), speed=12, fps=8, crowd=50, rest=(1.0, 3.0)),
    'blackstripe_topminnow': dict(band=(0, 70), speed=22, fps=9, crowd=50),
    'golden_topminnow': dict(band=(0, 80), speed=20, fps=9, crowd=50),
    'bluefin_killifish': dict(band=(40, 180), speed=20, fps=9, crowd=45),
    'rainwater_killifish': dict(band=(30, 170), speed=20, fps=9, crowd=45),
    'least_killifish': dict(band=(20, 150), speed=16, fps=10, crowd=35),
    'western_mosquitofish': dict(band=(0, 80), speed=22, fps=10, crowd=40),
    'brook_silverside': dict(band=(0, 90), speed=30, fps=9, crowd=55),
    'pugnose_minnow': dict(band=(60, 200), speed=24, fps=9, crowd=50),
    'taillight_shiner': dict(band=(40, 190), speed=26, fps=9, crowd=50),
    'cypress_darter': dict(band=(200, 258), speed=12, fps=8, crowd=40, rest=(1.0, 3.0)),
}
