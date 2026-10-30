"""Bayou batch 2 - sunfishes, crappie, bass, drum, buffalo, catfish, bowfin, shad, gars and paddlefish; defined from species names only."""
import numpy as np
from swim import Fish, tooth, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_region, m_poly, m_dash
from sp1 import bands, np_r
import pal; pal.use('by')
from pal import ramp
ALL = ['bluegill', 'redear_sunfish', 'warmouth', 'white_crappie', 'largemouth_bass', 'freshwater_drum', 'bigmouth_buffalo', 'threadfin_shad',
       'channel_catfish', 'flathead_catfish', 'bowfin', 'spotted_gar', 'longnose_gar', 'alligator_gar', 'paddlefish']
SUN = [(0, .34, -.34), (.1, .52, -.5), (.26, .86, -.84), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.84), (.85, .72, -.62), (.93, .46, -.38), (.97, .24, -.24), (1, .06, -.14)]
GAR = lambda snout: [(0, .5, -.5), (.08, .74, -.72), (.2, .92, -.9), (.4, 1, -1), (.56, 1, -.98), (.66, .94, -.9), (1 - snout - .06, .8, -.74), (1 - snout, .52, -.48),
                     (1 - snout * .6, .4, -.38), (1, .3, -.28)]
def sunfins(B, col, d=(.16, .72, 4.8), a=(.12, .4, 4.2), cau=('emarg', 6.8), pel='#888', pec=4.4, pec_w=0.45):
    return [caudal(B, cau[0], cau[1], col=col), dorsal(B, d[0], d[1], d[2], 'round', col=col, lean=0.2, n=16), anal(B, a[0], a[1], a[2], 'round', col=col),
            pelvic(B, .62, 3.6, col=pel), pectoral(B, .72, .58, pec, width=pec_w, col=col)]
def bluegill():
    # Lepomis macrochirus: deep round sunfish, olive-green with five to eight dusky vertical bars, a plain black ear flap, a dark blotch
    # at the rear of the soft dorsal, a purple-blue sheen on the cheek and an orange-yellow breast
    F = Fish('bluegill', 30, 18, SUN, bands('#3a4a34', '#7a8a62', '#d8a050', sig=('belly',)), tilt=15, eye=(0.81, 0.36, 2, '#a85030'))
    B = F.B
    F.marks += [m_bar(B, u, 2.2, .04, .84, -1) for u in np_r(.12, .64, 6)]
    F.marks += [m_region(B, .8, .94, .5, .78, '#6a6e92'), m_spot(B, .73, .36, 1.4, '#0c0e0a')]
    fins = sunfins(B, '#6e7a56', pel='#7a8460')
    fins[1]['band'] = [(lambda X, Y, B=B: (X > .16 * B.L) & (X < .3 * B.L) & (Y < B.top(np.clip(X, 0, B.L)) + 2.8), '#1a1e12')]
    F.fins += fins; F.gill = (.74, .2, .85, 1.5); F.mouth = (.5, 1.2); return F
def redear_sunfish():
    # Lepomis microlophus: deep sunfish, olive-gold with faint darker flecks and bars, a short black ear flap with a bright red-orange
    # rim, pale yellowish belly, long pointed pectoral fins
    F = Fish('redear_sunfish', 32, 18, SUN, bands('#4a4e2c', '#a8a464', '#dccc8c'), tilt=15, eye=(0.81, 0.36, 2, '#c8a050'))
    B = F.B; rng = np.random.RandomState(12)
    F.marks += [m_spot(B, u, t, .5, '#3a3c22') for u, t in zip(rng.uniform(.12, .7, 18), rng.uniform(.14, .7, 18))] + [m_bar(B, u, 2.0, .06, .7, -1) for u in (.24, .44, .62)]
    F.marks += [m_spot(B, .73, .36, 1.6, '#d8402a'), m_spot(B, .73, .36, 1.0, '#0c0e0a')]
    F.fins += sunfins(B, '#8c8a5a', pel='#a09c68', pec=5.6, pec_w=0.3); F.gill = (.74, .2, .85, 1.5); F.mouth = (.5, 1.2); return F
def warmouth():
    # Lepomis gulosus: thick-bodied, big-mouthed sunfish, olive-brown heavily mottled with dark blotches, three or four dark red-brown
    # streaks radiating back from the red eye across the cheek, dark-spotted fins
    P = [(0, .34, -.34), (.1, .5, -.48), (.26, .84, -.82), (.44, 1, -.98), (.6, 1, -.96), (.74, .92, -.88), (.84, .76, -.72), (.92, .52, -.54), (.97, .28, -.4), (1, .1, -.3)]
    F = Fish('warmouth', 30, 15, P, bands('#3e3420', '#86704a', '#c0aa80'), tilt=15, eye=(0.82, 0.36, 2, '#d8241c'))
    B = F.B; rng = np.random.RandomState(5)
    F.marks += [m_spot(B, u, t, 1.3 + .5 * rng.rand(), -1) for u, t in zip(rng.uniform(.1, .7, 9), rng.uniform(.15, .75, 9))]
    F.marks += [m_stripe(B, .84, .98, [(.84, .44 + k * .12), (.98, .4 + k * .1)], .8, '#6a2c1c') for k in range(3)]
    fins = sunfins(B, '#7a6844', pel='#8a7650', cau=('round', 7.0))
    for f in fins[:3]: f['band'] = [(lambda X, Y: (np.round(X * .9) + np.round(Y * .9)) % 3 == 0, '#3a2c18')]
    F.fins += fins; F.gill = (.76, .2, .85, 1.6); F.mouth = (.62, 3.0); return F
def white_crappie():
    # Pomoxis annularis: deep, compressed, silvery-white panfish with a dipped forehead and big upturned mouth, five to ten faint
    # dusky vertical bars (often paired), big dorsal and anal of equal size set far back, both dotted dark
    P = [(0, .32, -.32), (.1, .5, -.5), (.26, .86, -.86), (.44, .98, -1.0), (.6, .96, -.98), (.72, .84, -.88), (.82, .7, -.72), (.9, .56, -.52), (.96, .4, -.32), (1, .2, -.14)]
    F = Fish('white_crappie', 32, 16, P, bands('#5e6450', '#c4c8b8', '#e2e4da'), tilt=14, eye=(0.84, 0.4, 2, '#d0d0c0'))
    B = F.B
    F.marks += [m_bar(B, u + du, .9, .06, .62, -1) for u in (.18, .34, .5, .64) for du in (0, .045)]
    dots = [(lambda X, Y: (np.round(X * .8) % 2 == 0) & (np.round(Y * .8) % 2 == 0), '#3a3e30')]
    d = dorsal(B, .16, .42, 6.4, 'round', col='#a4a894', lean=0.4, n=12); a = anal(B, .12, .44, 6.0, 'round', col='#a4a894', lean=0.4, n=12)
    d['band'] = dots; a['band'] = dots
    F.fins += [caudal(B, 'emarg', 7.4, col='#a4a894'), d, a, pelvic(B, .6, 3.6, col='#c0c4b4'), pectoral(B, .74, .58, 4.2, col='#c8ccbc')]
    F.gill = (.76, .2, .85, 1.4); F.mouth = (.36, 2.6); return F
def largemouth_bass():
    # Micropterus salmoides: big olive-green bass with a dark ragged band of blotches along the side, pale belly, a jaw reaching past
    # the eye, a deeply notched dorsal (spiny and soft parts almost separate), emarginate tail
    P = [(0, .34, -.34), (.1, .46, -.44), (.3, .82, -.8), (.48, .98, -.96), (.64, 1, -.98), (.78, .9, -.92), (.9, .66, -.74), (.97, .36, -.52), (1, .14, -.38)]
    F = Fish('largemouth_bass', 54, 17, P, bands('#3a4a24', '#8a9a5a', '#d8d4b0'), tilt=11, eye=(0.86, 0.36, 3, '#c8a040'))
    B = F.B
    F.marks += [m_stripe(B, .02, .82, [(u, .5 + (.06 if k % 2 else -.04)) for k, u in enumerate(np_r(0, .82, 9))], 2.6, '#22281a')]
    F.marks += [m_spot(B, u, .5, 1.6, '#22281a') for u in np_r(.12, .72, 6)] + [m_stripe(B, .86, .98, .58, .8, '#2a3020')]
    F.fins += [caudal(B, 'emarg', 10.0, col='#76844c'), dorsal(B, .46, .7, 5.2, 'spiny', col='#6e7c48', lean=0.2, n=10), dorsal(B, .2, .44, 6.2, 'round', col='#76844c', lean=0.3, n=10),
               anal(B, .14, .32, 5.2, 'round', col='#88925c'), pelvic(B, .6, 4.6, col='#a0a474'), pectoral(B, .76, .58, 5.2, col='#b0b488')]
    F.gill = (.78, .22, .85, 1.7); F.mouth = (.6, 6.0); return F
def freshwater_drum():
    # Aplodinotus grunniens: humpbacked silver-grey drum with a blunt rounded snout and low mouth, a long dorsal made of a short spiny
    # part and a very long soft part, the lateral line running out onto the pointed-round tail, pale fins
    P = [(0, .3, -.3), (.1, .46, -.42), (.3, .84, -.76), (.5, 1, -.9), (.66, 1, -.92), (.8, .9, -.86), (.9, .7, -.7), (.96, .46, -.5), (1, .2, -.32)]
    F = Fish('freshwater_drum', 48, 18, P, bands('#5a6060', '#b8bcb6', '#dcdcd4'), tilt=12, eye=(0.86, 0.4, 2, '#d0d0c4'))
    B = F.B
    F.marks += [m_dash(B, .06, .82, t, .8, -1, 2.2, 1.0, off=k * 1.1) for k, t in enumerate((.2, .32, .44, .56, .68))]
    F.marks += [m_stripe(B, .0, .8, [(0, .46), (.4, .3), (.8, .3)], .7, '#e8ece4')]
    F.fins += [caudal(B, 'round', 9.0, col='#a0a49c'), dorsal(B, .58, .74, 6.4, 'spiny', col='#9a9e96', lean=0.3, n=8), dorsal(B, .06, .58, 4.4, 'flat', col='#9a9e96', lean=0.3, n=20),
               anal(B, .14, .26, 4.4, 'tri', col='#b0b4ac', n=6), pelvic(B, .62, 4.2, col='#c0c4bc'), pectoral(B, .78, .58, 5.0, col='#c8ccc4')]
    F.gill = (.8, .2, .85, 1.6); F.mouth = (.74, 1.6); return F
def bigmouth_buffalo():
    # Ictiobus cyprinellus: big, deep-bodied sucker with a large oblique mouth at the tip of the snout, olive-bronze to slate back, brassy
    # sides, a long sickle-shaped dorsal (tall in front, low behind), forked tail, dusky fins
    P = [(0, .34, -.34), (.1, .5, -.46), (.28, .86, -.82), (.46, 1, -.98), (.62, 1, -.98), (.76, .9, -.88), (.86, .74, -.68), (.94, .5, -.4), (.98, .32, -.2), (1, .2, -.06)]
    F = Fish('bigmouth_buffalo', 56, 21, P, bands('#3e3e2e', '#8a8458', '#c8c098'), tilt=11, eye=(0.86, 0.38, 2, '#b8a878'))
    B = F.B
    F.marks += [m_dash(B, .06, .8, t, 1.0, -1, 2.6, 1.2, off=k * 1.3) for k, t in enumerate((.18, .3, .42, .54, .66))]
    sail = dorsal(B, .16, .6, 8.0, 'sail', col='#5e5c44', lean=0.6, n=16)
    F.fins += [caudal(B, 'fork', 11.0, col='#5e5c44'), sail, anal(B, .12, .24, 5.0, 'tri', col='#6a6850', n=6), pelvic(B, .54, 4.6, col='#727058'), pectoral(B, .8, .7, 5.4, col='#8a8668')]
    F.gill = (.78, .2, .85, 1.8); F.mouth = (.24, 3.4); return F
def threadfin_shad():
    # Dorosoma petenense: small silvery shad, blue-grey back, a dark spot behind the gill, a long thread trailing from the last dorsal
    # ray, bright yellow tail and fins, deeply forked tail, protruding lower jaw
    P = [(0, .28, -.28), (.1, .44, -.42), (.28, .82, -.86), (.46, 1, -1), (.62, 1, -.98), (.76, .9, -.84), (.88, .66, -.54), (.95, .42, -.3), (1, .16, -.08)]
    F = Fish('threadfin_shad', 30, 12, P, bands('#4a5a62', '#c8ccc6', '#e4e6e0'), tilt=14, eye=(0.86, 0.42, 2, '#d8d8cc'))
    B = F.B
    F.marks += [m_spot(B, .74, .3, 1.0, '#1a2026')] + [m_stripe(B, .06, .78, t, .6, -1) for t in (.24, .36)]
    F.fins += [caudal(B, 'deepfork', 7.6, col='#d8c050', sig=True), dorsal(B, .44, .56, 3.8, 'tri', col='#b8b490', lean=0.4, n=6), barbel(B, .45, 0, 6.0, 160, '#a8a484'),
               anal(B, .1, .32, 2.4, 'low', col='#d0c070', n=10), pelvic(B, .5, 2.4, col='#d0c890'), pectoral(B, .8, .66, 3.0, col='#d8d4b4')]
    F.gill = (.8, .2, .85, 1.3); F.mouth = (.4, 1.0); return F
def channel_catfish():
    # Ictalurus punctatus: slim catfish with a deeply forked tail, blue-grey to olive back and silver-white belly, scattered small black
    # spots, four pairs of barbels (long ones at the mouth corners), adipose fin, spined dorsal and pectorals
    P = [(0, .34, -.34), (.1, .48, -.44), (.3, .86, -.8), (.5, 1, -.94), (.68, .98, -.94), (.82, .86, -.84), (.92, .62, -.62), (.97, .36, -.4), (1, .16, -.24)]
    F = Fish('channel_catfish', 52, 12.4, P, bands('#3c4850', '#9aa4a4', '#dcdcd2'), tilt=10, eye=(0.86, 0.34, 2, '#b8b8a8'))
    B = F.B; rng = np.random.RandomState(8)
    F.marks += [m_spot(B, u, t, .45, '#141a1e') for u, t in zip(rng.uniform(.1, .8, 18), rng.uniform(.18, .62, 18))]
    F.fins += [caudal(B, 'deepfork', 9.6, col='#6c7880'), dorsal(B, .52, .64, 5.6, 'tri', col='#5e6a72', n=6), adipose(B, .2, 3.4, 2.2, col='#5e6a72'),
               anal(B, .1, .32, 3.6, 'round', col='#7a868c', n=10), pelvic(B, .46, 3.2, col='#8a949a'), pectoral(B, .82, .7, 4.6, ang=-10, width=0.35, col='#7c888e'),
               barbel(B, .99, .55, 6.0, -5, '#2a3034'), barbel(B, .97, .8, 3.6, -45, '#c8c8bc'), barbel(B, .95, .9, 3.0, -75, '#c8c8bc'), barbel(B, .97, .25, 2.4, 30, '#2a3034')]
    F.mouth = (.62, 1.6); return F
def flathead_catfish():
    # Pylodictis olivaris: heavy catfish with a broad flat head and a jutting lower jaw, mottled yellow-brown and olive, a square tail
    # with a pale tip on the upper lobe, short barbels, large adipose fin, small eyes
    P = [(0, .36, -.36), (.1, .5, -.48), (.3, .84, -.84), (.5, .98, -.98), (.66, 1, -1), (.8, .88, -.94), (.9, .64, -.86), (.96, .38, -.74), (1, .16, -.6)]
    F = Fish('flathead_catfish', 58, 14, P, bands('#4a3e22', '#8e7a48', '#d0c08c'), tilt=9, eye=(0.88, 0.3, 1, '#b8a070'))
    B = F.B; rng = np.random.RandomState(9)
    F.marks += [m_spot(B, u, t, 1.3 + .6 * rng.rand(), -1) for u, t in zip(rng.uniform(.06, .86, 16), rng.uniform(.12, .66, 16))]
    t = caudal(B, 'truncate', 9.0, col='#6e6038'); t['band'] = [(lambda X, Y, B=B: Y > 2.6, '#d8cc9c')]
    F.fins += [t, dorsal(B, .54, .66, 5.4, 'round', col='#6e6038', n=6), adipose(B, .16, 5.4, 2.8, col='#6e6038'), anal(B, .1, .28, 4.0, 'round', col='#7a6c42', n=9),
               pelvic(B, .46, 3.6, col='#867850'), pectoral(B, .82, .76, 5.0, ang=-6, width=0.35, col='#8a7c52'),
               barbel(B, .98, .5, 3.4, 0, '#3a3220'), barbel(B, .96, .82, 2.4, -50, '#c8b888'), barbel(B, .94, .9, 2.2, -78, '#c8b888')]
    F.mouth = (.66, 2.4); return F
def bowfin():
    # Amia calva: long cylindrical living fossil, olive-green mottled darker, pale belly, a long low dorsal fin rippling along most of
    # the back, rounded tail with a black eyespot ringed orange at its upper base, big head with a bony plate and short tube nostrils
    P = [(0, .48, -.48), (.08, .66, -.64), (.22, .88, -.86), (.42, 1, -.98), (.6, 1, -.98), (.76, .94, -.92), (.88, .78, -.72), (.95, .54, -.48), (1, .3, -.28)]
    F = Fish('bowfin', 58, 13, P, bands('#2e3a20', '#6a7a46', '#c8c08c'), tilt=9, eye=(0.88, 0.36, 2, '#b8a050'))
    B = F.B; rng = np.random.RandomState(10)
    F.marks += [m_spot(B, u, t, 1.2 + .6 * rng.rand(), -1) for u, t in zip(rng.uniform(.06, .82, 14), rng.uniform(.12, .66, 14))]
    F.marks += [m_spot(B, .03, .32, 1.7, '#d8782c'), m_spot(B, .03, .32, 1.1, '#0c0e08')]
    df = dorsal(B, .18, .7, 3.6, 'flat', col='#566a3a', lean=0.0, n=30, amp=0.9); df['wave'] = 3.0
    F.fins += [caudal(B, 'round', 9.4, col='#566a3a'), df, anal(B, .1, .2, 3.4, 'round', col='#6a7a48', n=6), pelvic(B, .5, 3.2, col='#7a8a56'),
               pectoral(B, .82, .72, 4.6, ang=-10, width=0.4, col='#7e8c5a'), barbel(B, .995, .3, 1.6, 40, '#3a4428')]
    F.gill = (.82, .2, .85, 1.6); F.mouth = (.56, 3.0); return F
def spotted_gar():
    # Lepisosteus oculatus: long gar with a medium-length snout, olive-brown back, pale belly, round dark spots all over the head, body
    # and fins, dorsal and anal far back opposite each other, rounded spotted tail
    F = Fish('spotted_gar', 62, 10, GAR(.16), bands('#4a4428', '#988c5e', '#d0c49a'), tilt=8, eye=(0.79, 0.36, 2, '#c8a040'))
    B = F.B; sp = '#1c1a0e'
    F.marks += [m_spot(B, u, t, .7, sp) for t, us in ((.24, np_r(.06, .76, 12)), (.48, np_r(.1, .74, 11)), (.7, np_r(.06, .72, 11))) for u in us]
    tail = caudal(B, 'round', 8.4, col='#988c5e'); tail['band'] = [(lambda X, Y: (np.round(X * .6) + np.round(Y * .6)) % 2 == 0, '#2e2a16')]
    F.fins += [tail, dorsal(B, .06, .16, 4.6, 'round', col='#8e8458', n=7), anal(B, .04, .15, 4.4, 'round', col='#988c5e', n=7), pelvic(B, .4, 3.4, col='#a69a6a'), pectoral(B, .74, .78, 3.6, col='#b0a476')]
    F.gill = (.76, .25, .85, 1.0); F.mouth = (.5, 4.0); return F
def longnose_gar():
    # Lepisosteus osseus: slender gar with a very long, narrow beak (about twice the head length), olive-brown back, silvery-white belly,
    # a few dark spots on the rear body and the dorsal, anal and tail fins
    P = [(0, .5, -.5), (.08, .74, -.72), (.2, .92, -.9), (.4, 1, -1), (.56, 1, -.98), (.64, .94, -.9), (.68, .76, -.72), (.72, .52, -.46), (.78, .4, -.36), (.9, .36, -.32), (1, .3, -.26)]
    F = Fish('longnose_gar', 76, 9.4, P, bands('#4a4a2c', '#a8a47c', '#e0dcc8'), tilt=8, eye=(0.69, 0.36, 2, '#c8a848'))
    B = F.B; sp = '#20200e'
    F.marks += [m_spot(B, u, t, .7, sp) for u, t in ((.06, .3), (.12, .6), (.18, .36), (.24, .62), (.08, .5), (.3, .3))]
    spots = [(lambda X, Y: (np.round(X * .6) + np.round(Y * .6)) % 3 == 0, '#2a2a16')]
    tail = caudal(B, 'round', 8.0, col='#9c9872'); tail['band'] = spots; d = dorsal(B, .05, .14, 4.4, 'round', col='#94906a', n=7); d['band'] = spots
    F.fins += [tail, d, anal(B, .04, .13, 4.2, 'round', col='#9c9872', n=7), pelvic(B, .36, 3.4, col='#b0ac88'), pectoral(B, .62, .78, 3.4, col='#bcb898')]
    F.gill = (.62, .25, .85, 1.0); F.mouth = (.5, 2.0); return F
def alligator_gar():
    # Atractosteus spatula: giant gar with a short, broad alligator-like snout lined with a double row of teeth, heavy body, olive-brown
    # back mottled darker, pale yellowish belly, dark blotches on the rear fins, rounded tail
    F = Fish('alligator_gar', 96, 15, GAR(.13), bands('#3e3a24', '#867c56', '#cec29a'), tilt=7, eye=(0.83, 0.34, 2, '#c8a040'))
    B = F.B; rng = np.random.RandomState(14)
    F.marks += [m_spot(B, u, t, 1.4 + .8 * rng.rand(), -1) for u, t in zip(rng.uniform(.04, .8, 22), rng.uniform(.12, .7, 22))]
    F.marks += [m_dash(B, .04, .8, t, .8, -1, 3.0, 1.2, off=k * 1.4) for k, t in enumerate((.32, .5))]
    F.marks += [m_stripe(B, .88, 1.0, .5, .7, '#2a2616')]
    blot = [(lambda X, Y: (np.round(X * .5) + np.round(Y * .5)) % 2 == 0, '#2e2a18')]
    tail = caudal(B, 'round', 13.0, col='#867c56'); tail['band'] = blot; d = dorsal(B, .06, .15, 6.4, 'round', col='#7e7450', n=7); d['band'] = blot
    a = anal(B, .04, .14, 6.0, 'round', col='#867c56', n=7); a['band'] = blot
    F.fins += [tail, d, a, pelvic(B, .4, 5.0, col='#988e66'), pectoral(B, .78, .8, 5.4, col='#a49a72')]
    F.gill = (.8, .25, .85, 1.4); F.mouth = (.52, 9.0); return F
def paddlefish():
    # Polyodon spathula: shark-like grey fish with a long flat paddle-shaped snout (a third of its length), a tiny eye, a huge pointed
    # gill flap reaching back along the side, smooth scaleless skin, small dorsal set far back, forked tail with a longer upper lobe
    P = [(0, .26, -.24), (.08, .44, -.4), (.2, .76, -.7), (.36, .98, -.9), (.5, 1, -.92), (.6, .9, -.86), (.66, .62, -.6), (.7, .42, -.4), (.76, .34, -.32), (.9, .34, -.32), (.97, .4, -.36), (1, .32, -.28)]
    F = Fish('paddlefish', 92, 14, P, bands('#4a5254', '#9ca2a0', '#d4d6d0'), tilt=8, eye=(0.665, 0.4, 1, '#c8c8bc'))
    B = F.B
    F.marks += [m_poly(B, [(.6, .2), (.44, .5), (.6, .84), (.63, .5)], -1)]
    F.marks += [m_spot(B, u, .5, .5, -1) for u in np_r(.74, .98, 8)]
    F.fins += [caudal(B, 'hetero', 13.0, col='#7a8282', upper=1.3, lower=0.9), dorsal(B, .18, .3, 6.0, 'tri', col='#747c7c', lean=0.6, n=7), anal(B, .14, .26, 5.0, 'tri', col='#848c8c', n=6),
               pelvic(B, .36, 4.0, col='#949a98'), pectoral(B, .58, .78, 5.6, ang=-20, width=0.4, col='#949a98')]
    F.mouth = (.7, 2.0); return F
SCENE = {
    'bluegill': dict(band=(60, 220), speed=16, fps=8, crowd=70),
    'redear_sunfish': dict(band=(120, 240), speed=14, fps=8, crowd=70),
    'warmouth': dict(band=(140, 250), speed=12, fps=8, crowd=65, rest=(1.0, 3.0)),
    'white_crappie': dict(band=(40, 200), speed=16, fps=8, crowd=75, rest=(0.8, 2.5)),
    'largemouth_bass': dict(band=(40, 220), speed=20, fps=8, crowd=110, rest=(1.0, 3.0)),
    'freshwater_drum': dict(band=(150, 250), speed=16, fps=8, crowd=100),
    'bigmouth_buffalo': dict(band=(60, 220), speed=16, fps=7, crowd=120),
    'threadfin_shad': dict(band=(0, 110), speed=28, fps=9, crowd=60),
    'channel_catfish': dict(band=(190, 256), speed=16, fps=8, crowd=110, rest=(1.0, 3.0)),
    'flathead_catfish': dict(band=(200, 258), speed=12, fps=7, crowd=120, rest=(2.0, 5.0)),
    'bowfin': dict(band=(130, 250), speed=14, fps=8, crowd=110, rest=(1.0, 3.0)),
    'spotted_gar': dict(band=(0, 120), speed=14, fps=7, crowd=110, rest=(2.0, 5.0)),
    'longnose_gar': dict(band=(0, 130), speed=16, fps=7, crowd=120, rest=(1.5, 4.0)),
    'alligator_gar': dict(band=(20, 200), speed=12, fps=6, crowd=160, rest=(2.0, 5.0)),
    'paddlefish': dict(band=(60, 230), speed=14, fps=6, crowd=150, rest=(1.0, 3.0)),
}
