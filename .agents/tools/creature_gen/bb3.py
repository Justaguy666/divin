"""Billabong batch 3 - bottom crawlers: ray, file snake, prawns, crayfish, triops, snail and turtles; defined from species names only."""
import math, numpy as np
from matplotlib.path import Path
from parts import Crawler, part, line, ell, cap
from sp4 import _turtle
from fs3 import _crayfish
import pal; pal.use('bb')
from pal import ramp
ALL = ['freshwater_whipray', 'arafura_file_snake', 'cherabin', 'glass_shrimp', 'redclaw_crayfish', 'tadpole_shrimp', 'notopala_river_snail',
       'northern_snake_necked_turtle', 'northern_snapping_turtle', 'pig_nosed_turtle', 'mary_river_turtle']
EYE = '#0c0e0c'; HI = '#fff0c4'
PH = [0, 1, 0, -1]
def inpoly(pts):
    P = Path(np.array(pts)); return lambda X, Y: P.contains_points(np.stack([X.ravel(), Y.ravel()], 1)).reshape(X.shape)
def freshwater_whipray():
    # Urogymnus dalyensis: huge flat round disc lying on the mud, plain yellowish-brown to grey-brown above with faint darker mottling
    # and a pale cream underside showing along the rim, eyes and spiracles raised on top of the front of the disc, a long thin
    # whip tail trailing far behind; the disc margins ripple as it glides
    top = ramp('#7a6a4c'); tailc = ramp('#5a4c38'); cx, cy, rx = 46.0, 17.6, 18.0
    rng = np.random.RandomState(21)
    mot = [(lambda X, Y, p=p: ((X - p[0]) / 2.2) ** 2 + ((Y - p[1]) / 0.9) ** 2 < 1, -1) for p in zip(rng.uniform(32, 60, 7), rng.uniform(12.6, 16.6, 7))]
    def frame(f, idle):
        ph = PH[f] * (0.5 if idle else 1.0); xs = np.linspace(cx - rx, cx + rx, 56); q = (xs - cx) / rx; s = np.sqrt(np.clip(1 - q * q, 0, 1)); s[0] = s[-1] = 0.0
        rip = 0.7 * ph * np.sin(2 * np.pi * (xs - cx) / 20.0) * (0.3 + 0.7 * np.abs(q))
        sf = np.sqrt(np.clip(1 - ((xs - cx - 4.0) / (rx + 4.0 * np.sign(xs - cx - 4.0) * -1 + 0.0)) ** 2, 0, 1)) * (s > 0)
        up = [(x, cy - 1.0 - 5.6 * si - 0.3 * r) for x, si, r in zip(xs, sf ** 1.4, rip)]; lo = [(x, cy + 0.8 + 1.8 * si + 0.6 * r) for x, si, r in zip(xs[::-1], s[::-1], rip[::-1])]
        rim = [(lambda X, Y: Y > cy + 0.9 + 0.0 * X, '#cec6ae')]
        P = [part(up + lo, top, z=3, name='disc', marks=mot + rim, lightc=(0.25, 0.35, 1.3, 1.2))]
        sw = 0.8 * ph
        P.append(part(cap([(cx - rx + 1.0, cy + 0.4), (20.0, cy + 0.8), (10.0, cy + 1.2 + sw * 0.5), (1.4, cy + 1.0 + sw)], [1.3, 0.8, 0.55, 0.45]), tailc, z=2, shade='flat', tone=2, outline=False, name='tail'))
        P.append(part(ell(cx + 10.6, cy - 3.0, 1.4, 0.9), top, z=3.4, shade='flat', tone=4, outline=False, name='bump'))
        return P, [(cx + 11.0, cy - 3.2, EYE), (cx + 11.0, cy - 4.2, HI), (cx + 8.4, cy - 3.0, '#3a3024')]
    return Crawler('freshwater_whipray', frame, 70, 26)
def arafura_file_snake():
    # Acrochordus arafurae: heavy, baggy-skinned aquatic snake lying along the bottom, grey-brown with a darker reticulated network of
    # bands, small flat head with eyes on top, body thickest in the middle and tapering to a short tail
    body = ramp('#6e6046')
    net = [(lambda X, Y: np.sin(1.1 * X + 1.6 * np.sin(0.7 * Y + 0.3 * X)) > 0.62, '#3e3426'), (lambda X, Y: (np.round(X) + 2 * np.round(Y)) % 5 == 0, -1)]
    def frame(f, idle):
        ph = PH[f] * (0.4 if idle else 1.0); xs = np.linspace(2.0, 62.0, 41)
        ys = [12.0 - (1.8 * math.sin(2 * math.pi * (x - 6.0 * ph * 0.3) / 26.0) + 0.6) * (0.35 + 0.65 * x / 62.0) for x in xs]
        r = [0.6 + 2.4 * math.sin(math.pi * min(1.0, (x - 2.0) / 50.0)) ** 0.5 if x < 52 else 3.0 - 0.09 * (x - 52) for x in xs]
        sh = 14.4 - max(y + rr for y, rr in zip(ys, r)); ys = [y + sh for y in ys]   # keep the belly on the floor in every frame
        P = [part(cap(list(zip(xs, ys)), r), body, z=3, name='body', marks=net, lightc=(0.3, 0.4, 1.5, 1.3))]
        hy = ys[-1] - 0.4
        P.append(part(ell(65.0, hy - 0.2, 3.8, 2.2, -6), body, z=3.2, name='head', marks=[(lambda X, Y: Y > hy + 1.0, 1)]))
        return P, [(66.8, hy - 1.4, EYE), (66.8, hy - 2.2, '#c8b070')]
    return Crawler('arafura_file_snake', frame, 74, 18)
def cherabin():
    # Macrobrachium spinipes (giant freshwater prawn): arched translucent olive-blue body, long toothed rostrum, banded abdomen ending in
    # a tail fan, very long slender blue second claws held forward, long whip antennae, thin walking legs and swimmerets
    body = ramp('#6a7868'); blue = ramp('#3e6a96', sig=True); leg = ramp('#8a9480'); X0 = 3.0
    S = lambda pts: [(x + X0, y) for x, y in pts]
    shape = S([(1.6, 17.6), (3.0, 15.2), (5.4, 13.0), (8.6, 11.2), (12.4, 10.0), (16.4, 9.6), (20.4, 9.8), (24.0, 10.4), (28.0, 9.4), (32.0, 9.2), (35.6, 9.8),
               (37.8, 11.0), (45.4, 9.2), (38.6, 12.2), (38.4, 13.6), (36.8, 15.6), (32.0, 16.6), (26.0, 17.0), (22.0, 16.2), (18.0, 15.8), (14.0, 15.6),
               (10.4, 16.0), (7.6, 17.0), (5.4, 18.2), (3.4, 19.0)])
    fan = S([(4.0, 17.0), (0.0, 15.2), (-2.4, 17.4), (-0.6, 20.0), (3.6, 19.2)])
    seg = [(lambda X, Y, x0=x0: (np.abs(X - x0 - X0 + (Y - 13) * 0.25) < 0.5), -1) for x0 in (8.6, 12.2, 15.8, 19.4, 23.0)]
    teeth = [(lambda X, Y: (Y < 10.4) & (X > 38 + X0) & ((np.round(X) % 2) == 0), -2)]
    def frame(f, idle):
        ph = PH[f]; o = 0.4 * ph * (0 if idle else 1); sw = (0.3 if idle else 0.7) * ph
        P = [part(shape, body, z=3, name='body', marks=seg + teeth, lightc=(0.3, 0.4, 1.5, 1.3)), part(fan, body, z=2.9, name='fan', tone=2, marks=[(lambda X, Y: np.abs(Y - 17.6) < 0.5, -1)])]
        for k, x in enumerate((34.6, 32.4, 30.2, 28.0)):
            up = 0.8 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line(S([(x, 16.4), (x + 1.4, 19.2 - up), (x + 0.4 + 0.8 * up, 21.6 - up)]), leg[2], z=4))
            P.append(line(S([(x + 0.8, 16.2), (x + 2.2, 19.0), (x + 1.6, 21.6)]), leg[0], z=0.4))
        for k, x in enumerate((10.0, 13.6, 17.2, 20.8)):
            P.append(line(S([(x, 15.8), (x - 0.6 + 0.4 * sw * (1 if k % 2 else -1), 17.6)]), leg[3], z=4))
        def arm(dx, dy, z, rp, tn):
            pts = S([(35.0 + dx, 15.4 + dy), (41.0 + dx, 18.2 + dy), (49.0 + dx, 18.0 + dy), (53.0 + dx, 17.6 + dy)])
            return [part(cap(pts, 0.6), rp, z=z, shade='flat', tone=tn, outline=False, name='arm%d' % z),
                    part(ell(55.4 + dx + X0, 17.4 + dy, 2.6, 0.95, -4), rp, z=z + 0.05, name='claw%d' % z),
                    part(cap(S([(57.6 + dx, 17.0 + dy), (60.0 + dx, 16.6 + dy - o)]), 0.45), rp, z=z + 0.06, shade='flat', tone=tn, outline=False, name='claw%d' % z),
                    part(cap(S([(57.6 + dx, 17.8 + dy), (59.6 + dx, 18.0 + dy + o)]), 0.45), rp, z=z + 0.06, shade='flat', tone=tn - 1, outline=False, name='claw%d' % z)]
        P += arm(-1.2, -1.2, 0.6, ramp(pal.mix('#3e6a96', '#000000', .25)), 2) + arm(0, 0, 5, blue, 3)
        P.append(line(S([(37.6, 11.2), (42.0, 7.6), (48.0, 5.8 + sw), (54.0, 5.4 + sw), (58.4, 6.4 + sw)]), '#4a4e40', z=6))
        P.append(line(S([(37.8, 11.6), (41.6, 10.6), (44.4, 10.6 - sw)]), '#4a4e40', z=6))
        return P, [(37.0 + X0, 11.6, EYE), (37.0 + X0, 10.6, HI)]
    return Crawler('cherabin', frame, 66, 26)
class _Glass(Crawler):
    """translucent body: everything except the eye is made see-through after rendering (outline pixels keep a little more cover)."""
    def sheet(s, safety=1):
        sh, W, H, tags = Crawler.sheet(s, safety); a = sh[..., 3] > 0
        rgb = sh[..., :3].astype(float) / 255; L = rgb @ np.array([.3, .59, .11])
        eye = a & (L < 0.08)
        sh[a & ~eye, 3] = np.where(L[a & ~eye] < 0.45, 190, 130).astype(np.uint8)
        return sh, W, H, tags
def glass_shrimp():
    # Paratya australiensis (glass shrimp): tiny see-through shrimp with faint reddish-brown lines and a dark gut line, black eyes,
    # short toothed rostrum, thin legs and antennae
    body = ramp('#c8d2bc')
    shape = [(2.4, 9.4), (4.0, 8.0), (7.0, 7.0), (10.0, 6.8), (13.0, 7.0), (16.0, 7.2), (19.0, 7.6), (21.0, 8.4), (24.4, 7.8), (21.8, 9.2), (21.0, 10.2),
             (18.0, 10.6), (14.0, 10.4), (10.0, 10.2), (7.0, 10.4), (4.6, 11.0), (2.8, 11.6)]
    fan = [(3.2, 9.6), (0.4, 8.6), (-0.6, 10.2), (0.6, 11.8), (3.0, 11.4)]
    mk = [(lambda X, Y: (np.abs(Y - 8.7) < 0.5) & (X > 6) & (X < 17), '#6a5444'), (lambda X, Y: (np.abs(Y - 7.6) < 0.45) & (X > 4) & (X < 19), '#b07a60')]
    def frame(f, idle):
        ph = PH[f]; sw = (0.3 if idle else 0.6) * ph
        P = [part([(x + 1, y) for x, y in shape], body, z=3, name='body', marks=[(lambda X, Y, m=m: m(X - 1, Y), c) for m, c in mk]), part([(x + 1, y) for x, y in fan], body, z=2.9, name='fan', tone=2)]
        for k, x in enumerate((19.0, 17.6, 16.2, 14.8)):
            up = 0.6 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line([(x + 1, 10.2), (x + 1.8, 11.8 - up), (x + 1.4 + 0.6 * up, 13.4 - up)], body[1], z=4))
        P.append(line([(22.0, 8.6), (25.0, 6.2 + sw), (27.6, 5.8 + sw)], '#8a8e7c', z=4))
        return P, [(21.4, 8.4, EYE)]
    return _Glass('glass_shrimp', frame, 30, 16)
def redclaw_crayfish():
    # Cherax quadricarinatus: smooth blue-green to olive-blue crayfish with four keels on the head, cream speckles, big blue claws with
    # a bright red patch along the outer margin of each claw
    rng = np.random.RandomState(9); sp = list(zip(rng.uniform(4, 28, 8), rng.uniform(14.4, 17.4, 8)))
    mk = lambda: [(lambda X, Y: (np.abs(Y - 14.4) < 0.5) & (X > 23) & (X < 30), -1)] + [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.3, '#b8c4b0') for p in sp]
    red = [(lambda X, Y: (Y > 17.9) & (X > 35.6), '#c84a32')]
    return _crayfish('redclaw_crayfish', '#4a6670', '#567480', '#4e6e7c', '#3a5662', mk, claw_w=1.3, rostrum=3.0, claw_marks=red)
def tadpole_shrimp():
    # Triops australiensis: flat horseshoe-like shield covering the front half, two close-set eyes on top of the shield, many small
    # leaflike legs beating underneath, a segmented abdomen and two long tail filaments; olive-brown with a paler rim
    shield = ramp('#8a7a4a'); abd = ramp('#9a8a5c')
    sh_mask = lambda X, Y: (((X - 21.0) / 9.4) ** 2 + ((Y - 13.0) / 5.2) ** 2 <= 1) & (Y < 13.2)
    def frame(f, idle):
        ph = PH[f]; sw = (0.3 if idle else 0.8) * ph
        P = [part(sh_mask, shield, z=3, name='shield', lightc=(0.3, 0.4, 1.4, 1.2), marks=[(lambda X, Y: np.abs(X - 21.4 + (Y - 10) * 0.4) < 0.5, -1), (lambda X, Y: Y > 12.2, 1)])]
        P.append(part(cap([(13.0, 12.2), (9.0, 12.6), (5.0, 13.0)], [1.7, 1.2, 0.8]), abd, z=2.6, name='abd', marks=[(lambda X, Y: np.abs((X % 1.6) - 0.8) < 0.3, -1)]))
        P.append(line([(5.0, 13.0), (2.0, 12.0 + sw), (0.4, 11.4 + sw)], abd[2], z=2.5))
        P.append(line([(5.0, 13.2), (2.0, 13.8 - sw), (0.6, 14.2 - sw)], abd[1], z=2.5))
        for k, x in enumerate(np.linspace(14.0, 28.0, 8)):
            d = 0.6 * ph * (1 if k % 2 else -1) * (0.4 if idle else 1)
            P.append(line([(x, 13.0), (x - 0.6 + d, 14.4)], abd[1], z=2.8))
        return P, [(25.6, 8.8, EYE), (27.0, 9.2, EYE)]
    return Crawler('tadpole_shrimp', frame, 36, 18)
def notopala_river_snail():
    # Notopala river snail (viviparid): solid globular shell with a big rounded body whorl, short blunt spire and dark spiral bands on
    # olive-brown, round aperture, grey foot and short tentacles; the shell stays fixed while the foot glides
    shell = ramp('#6e6a3e'); foot = ramp('#7a7466')
    bandm = [(lambda X, Y, k=k: np.abs(Y - 13.2 - k - 0.22 * (X - 13.6)) < 0.45, -1) for k in (-2.2, 0.2, 2.6)]
    def frame(f, idle):
        ext = 0.8 if idle else [0.8, 1.6, 0.8, 0][f]; sw = 0.5 * PH[f]
        P = [part(cap([(7.0, 18.6), (19.0 + ext, 18.4), (22.4 + ext, 18.8)], [1.8, 1.8, 1.1]), foot, z=1, name='foot')]
        P.append(part(ell(13.6, 13.2, 5.6, 5.0, -10), shell, z=3, name='bw', lightc=(0.3, 0.4, 1.5, 1.3), marks=bandm))
        for i in range(3):
            t = (i + 1) / 3.0; cx = 12.2 - 2.8 * t; cy = 9.4 - 2.6 * t; r = 3.6 - 2.3 * t
            P.append(part(ell(cx, cy, r, r * 0.8, -30), shell, z=2.9 - i * 0.1, name='w%d' % i, lightc=(0.3, 0.4, 1.5, 1.3)))
        P.append(part(ell(17.6, 15.2, 2.0, 2.4, 10), ramp('#2a2416'), z=3.5, shade='flat', tone=3, outline=False, name='ap'))
        P.append(line([(21.0 + ext, 17.4), (23.6 + ext, 15.4 + sw)], '#5e5a50', z=4))
        P.append(line([(21.6 + ext, 17.8), (24.6 + ext, 17.0 - sw)], '#5e5a50', z=4))
        return P, [(21.2 + ext, 17.2, '#141210')]
    return Crawler('notopala_river_snail', frame, 30, 24, prefix='crawl_')
def _dome(x0, x1, h, base=15.0, flat=1.0):
    c = (x0 + x1) / 2; r = (x1 - x0) / 2
    return [(x0, base)] + [(x, base - h * max(0, 1 - ((x - c) / r) ** 2) ** (0.5 * flat)) for x in np.linspace(x0 + 0.2, x1 - 0.2, 23)] + [(x1, base)]
def _legs4(xf, xr, base=15.4):
    return [((xf, base), (xf + 1.8, 18.4), (xf + 2.6, 21.6), True), ((xr, base), (xr - 1.0, 18.4), (xr - 1.4, 21.6), True),
            ((xf - 1.4, base - 0.2), (xf - 0.4, 18.2), (xf + 0.2, 21.6), False), ((xr + 1.4, base - 0.2), (xr + 0.8, 18.2), (xr + 0.6, 21.6), False)]
def northern_snake_necked_turtle():
    # Chelodina rugosa: broad, flat, oval dark brown carapace with rugose scutes (growth rings) and a ridged rim of marginal scutes,
    # an extremely long, thick, wrinkled neck nearly as long as the shell (dark above, pale cream-grey below, studded with small
    # tubercles), a broad flat head with forward-set eyes and a pale lower jaw, cream plastron; neck folds sideways (side-necked)
    sc = ((11.6, 12.0), (16.9, 10.9), (22.5, 10.9), (28.0, 12.0))
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0 - (Y - 12) * 0.12) < 0.5) & (Y > 9.6), -1) for x0 in (14.2, 19.7, 25.3)] + [(lambda X, Y: np.abs(Y - 13.6) < 0.5, -1)]
    rings = [(lambda X, Y, c=c: np.abs(np.sqrt(((X - c[0]) / 2.3) ** 2 + ((Y - c[1]) / 1.3) ** 2) - 0.72) < 0.2, -1) for c in sc]
    rim = [(lambda X, Y: (Y > 13.9) & (np.abs((X % 2.6) - 1.3) < 0.4), -1), (lambda X, Y: (Y < 12.6) & ((np.round(X) + 3 * np.round(Y)) % 7 == 0), 1)]
    nx = np.array([30.4, 35.4, 40.4, 45.0]); ny = np.array([14.2, 12.6, 11.8, 11.8]); yc = lambda X: np.interp(X, nx, ny)
    nm = [(lambda X, Y: Y > yc(X) + 1.1, '#a8a286'), (lambda X, Y: Y < yc(X) - 1.0, -1),
          (lambda X, Y: ((3 * np.round(X) + 5 * np.round(Y)) % 4 == 0) & (Y < yc(X) + 0.4), -1)]
    hm = [(lambda X, Y: Y > 12.9, '#b8b294'), (lambda X, Y: (np.abs(Y - 12.4) < 0.4) & (X > 48.6), '#3a3424'), (lambda X, Y: Y < 10.4, -1)]
    mk = _turtle('northern_snake_necked_turtle', 60, 24, _dome(8.0, 32.0, 6.0), '#5a4830', '#d0c08a', '#5e5c48', (48.8, 11.6, 4.2, 2.4, -4),
                 [(x, y) for x, y in zip(nx, ny)], _legs4(27.6, 12.6), [(8.4, 15.2), (5.6, 16.2)], seams, rings + rim, hm, (1.8, -0.8),
                 neck_r=[2.5, 2.3, 2.1, 2.0], neck_marks=nm)
    return mk([(8.0, 14.8), (32.0, 14.8), (31.0, 16.4), (9.0, 16.4)])
def northern_snapping_turtle():
    # Elseya dentata: big olive-brown turtle with a broad, moderately domed carapace whose rear edge is serrated, a large head with a
    # strong hooked jaw, cream-yellow lower jaw and throat, grey-olive skin and a cream plastron
    top = _dome(8.0, 33.0, 7.4)
    top = [(x, y + (0.8 if (i % 2 == 0 and x < 12.6 and i > 0) else 0.0)) for i, (x, y) in enumerate(top)]
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0 - (Y - 10) * 0.12) < 0.5) & (Y > 8.6), -1) for x0 in (14.6, 20.4, 26.2)] + [(lambda X, Y: np.abs(Y - 13.4) < 0.5, -1)]
    hm = [(lambda X, Y: (Y > 13.8) & (X > 35.6), '#d8c88c'), (lambda X, Y: (np.abs(Y - 13.6) < 0.5) & (X > 37.6), '#3a3224')]
    mk = _turtle('northern_snapping_turtle', 48, 26, top, '#5a4a30', '#d0c08a', '#6e6a52', (37.2, 13.0, 4.2, 2.9), [(31.0, 14.4), (34.0, 13.6)],
                 _legs4(28.6, 12.6), [(8.4, 15.2), (5.4, 16.6)], seams, [], hm, (1.8, -1.0))
    return mk([(8.0, 14.8), (33.0, 14.8), (32.0, 16.6), (9.0, 16.6)])
def pig_nosed_turtle():
    # Carettochelys insculpta: grey-olive leathery shell without scutes, finely pitted, a pale rim; rests low on its plastron and rows
    # with long paddle flippers like a sea turtle's, a fleshy pig-like snout with nostrils at the tip, a pale patch behind the eye
    rng = np.random.RandomState(31)
    pits = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.3, -1) for p in zip(rng.uniform(10, 30, 16), rng.uniform(9.6, 13.6, 16))]
    rim = [(lambda X, Y: Y > 14.0, 1)]
    hm = [(lambda X, Y: (X > 35.0) & (X < 36.4) & (Y < 13.4), '#c8c6b4')]
    skin = ramp('#8a8c7e'); skd = ramp(pal.mix('#7a7c70', '#000000', .2)); D = 4.4
    def extra(f, idle):
        a = PH[f] * (0 if idle else 1)
        fl = lambda pts, w, z, rp, tn: part(cap(pts, w), rp, z=z, tone=tn, name='fl%d' % z)
        return [fl([(28.4, 19.2), (24.6 - 0.6 * a, 20.2), (19.8 - 1.2 * a, 21.0 - 0.3 * a)], [1.0, 1.7, 0.6], 4, skin, 3),
                fl([(29.4, 18.8), (32.4 + 0.6 * a, 19.8), (35.2 + 1.0 * a, 20.6)], [0.9, 1.4, 0.5], 1, skd, 2),
                fl([(12.6, 19.4), (10.0 + 0.4 * a, 20.4), (7.8 + 0.6 * a, 20.9)], [0.9, 1.2, 0.5], 4, skin, 3),
                fl([(14.0, 19.0), (15.8 - 0.4 * a, 20.2), (17.0 - 0.6 * a, 20.8)], [0.8, 1.0, 0.45], 1, skd, 2),
                part(cap([(38.8, 14.2 + D), (41.0, 14.6 + D)], [1.4, 1.1]), skin, z=2.7, name='head')]
    mk = _turtle('pig_nosed_turtle', 50, 26, _dome(8.0, 32.0, 6.6), '#6a6e62', '#d8d0b4', '#7a7c70', (36.2, 13.8, 3.4, 2.3), [(30.6, 14.6), (33.6, 14.0)],
                 [], [(8.4, 15.2), (6.0, 16.2)], [], pits + rim, hm, (1.2, -0.8), extra, dy=D)
    F = mk([(8.0, 14.8), (32.0, 14.8), (31.0, 16.6), (9.0, 16.6)])
    fr = F.frame
    def frame2(f, idle):
        P, E = fr(f, idle); return P, E + [(41.6, 14.0 + D, '#2a2620')]
    F.frame = frame2
    return F
def mary_river_turtle():
    # Elusor macrurus: streamlined, elongated brown carapace often carrying green algae tufts, a very long thick tail, two long fleshy
    # barbels under the chin, olive-grey skin with a pinkish throat, cream plastron
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0) < 0.5) & (Y > 9.8), -1) for x0 in (15.0, 20.4, 25.8)] + [(lambda X, Y: np.abs(Y - 13.6) < 0.5, -1)]
    algae = [(lambda X, Y, p=p: ((X - p[0]) / 1.6) ** 2 + ((Y - p[1]) / 0.8) ** 2 < 1, '#6a8a3a') for p in ((16.0, 9.6), (23.4, 9.2), (19.6, 10.4))]
    hm = [(lambda X, Y: (Y > 15.0) & (X > 34.0), '#c09c8c')]
    skin = ramp('#6e6a58')
    def extra(f, idle):
        sw = 0.5 * PH[f] * (0.3 if idle else 1); dy = 2.6
        return [part(cap([(10.0, 14.6 + dy), (5.0, 15.8 + dy + sw * 0.5), (0.8, 16.8 + dy + sw)], [1.7, 1.2, 0.5]), skin, z=2.1, tone=2, name='tail2'),
                line([(37.6, 15.6 + dy), (38.0, 17.6 + dy)], '#c8b8a0', z=2.8), line([(36.4, 15.6 + dy), (36.6, 17.4 + dy)], '#c8b8a0', z=2.8)]
    mk = _turtle('mary_river_turtle', 48, 26, _dome(9.0, 32.0, 6.0, flat=1.3), '#5e4a30', '#d8c8a0', '#6e6a58', (36.2, 13.6, 3.4, 2.3), [(30.8, 14.6), (33.4, 14.0)],
                 _legs4(27.8, 13.4), [(9.6, 15.2), (7.0, 16.0)], seams, algae, hm, (1.4, -0.8), extra)
    return mk([(9.0, 14.8), (32.0, 14.8), (31.0, 16.4), (10.0, 16.4)])
SCENE = {
    'freshwater_whipray': dict(speed=6, fps=5, bob_amount=0.0, move_time=(2, 5), idle_time=(3, 8), crowd_radius=(90, 8)),
    'arafura_file_snake': dict(speed=6, fps=5, bob_amount=0.0, move_time=(3, 6), idle_time=(3, 8), crowd_radius=(90, 8)),
    'cherabin': dict(speed=8, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(2, 5), crowd_radius=(70, 8)),
    'glass_shrimp': dict(speed=8, fps=9, bob_amount=0.5, move_time=(1, 3), idle_time=(1, 3), crowd_radius=(25, 8)),
    'redclaw_crayfish': dict(speed=10, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(1, 3), crowd_radius=(50, 8)),
    'tadpole_shrimp': dict(speed=10, fps=10, bob_amount=0.0, move_time=(2, 5), idle_time=(1, 2), crowd_radius=(30, 8)),
    'notopala_river_snail': dict(speed=2, fps=5, move_prefix='crawl_', bob_amount=0.0, move_time=(6, 10), idle_time=(2, 6), crowd_radius=(25, 8)),
    'northern_snake_necked_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(65, 8)),
    'northern_snapping_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(60, 8)),
    'pig_nosed_turtle': dict(speed=7, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(60, 8)),
    'mary_river_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(60, 8)),
}
