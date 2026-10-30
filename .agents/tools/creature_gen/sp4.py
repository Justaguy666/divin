"""Clear Spring batch 4 - bottom dwellers and crawlers, each defined from its species name.
v3 (Oct 2026): the bottom fish are one memorable set each, coloured from the cs colour families (pal.FAM); the part-built
animals keep their drawings and take the v3 colour fit through pal.ramp."""
import math, numpy as np
import swim
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_dash
from pal import ramp, FAM, fc
from v3h import m_hline, scatter, fin_spots
from sp1 import bands, np_r
from parts import Crawler, part, line, ell, cap
ALL = ['cambeva', 'cascarudo', 'cascudo', 'fat_sleeper', 'southern_flounder', 'florida_cave_crayfish', 'pantanal_crab',
       'loggerhead_musk_turtle', 'toad_headed_turtle', 'rasp_elimia']
def _crawlfish(F):
    F.crawl = True; F.tilt = 0
    for f in F.fins:
        if f['kind'] in ('pectoral', 'pelvic'): f['amp'] = 1.6; f['dir'] = np.array([1.0, 0.0]); f['floor'] = True   # paddle fore-aft, the lowest pixel stays put
        if f['kind'] == 'caudal': f['crawl_tail'] = True   # only read by the v2 style
    return F
def cambeva():
    # set: long PENCIL catfish with a flat head / sand-bronze with a few irregular dark BLOTCHES / three pairs of whisker BARBELS /
    # tiny eyes on top / dorsal set far back, rounded tail
    P = [(0, .42, -.42), (.1, .6, -.6), (.3, .9, -.9), (.6, 1, -1), (.8, .94, -.98), (.92, .7, -.86), (.98, .38, -.6), (1, .14, -.36)]
    F = Fish('cambeva', 30, 6.6, P, bands('C1', 'C1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.86, 0.24, 1, '#8a7a50'))
    B = F.B
    F.marks += [m_spot(B, u, t, 1.0, '#2a1c10', aspect=1.3) for u, t in scatter(7, .08, .8, .18, .56, seed=0.21, gap=0.09)]
    F.fins += [caudal(B, 'round', 4.6, col=fc('C1')), dorsal(B, .16, .28, 3.0, 'round', col=fc('C1'), n=7), anal(B, .12, .24, 2.6, 'round', col=fc('N1'), n=7),
               pelvic(B, .44, 2.4, col=fc('N1')), pectoral(B, .84, .78, 3.2, ang=-10, col=fc('N1')),
               barbel(B, .97, .2, 2.4, 40, '#e4ccb6'), barbel(B, .995, .6, 3.2, -10, '#e4ccb6'), barbel(B, .97, .78, 2.6, -40, '#e4ccb6')]
    return _crawlfish(F)
def cascarudo():
    # set: ARMOURED catfish / dark charcoal / two rows of big slanted bony PLATES meeting at a pale sea-green
    # midline seam / two pairs of LONG barbels / short spined dorsal and adipose spine, rounded tail
    P = [(0, .44, -.44), (.1, .6, -.6), (.3, .9, -.9), (.55, 1, -1), (.75, .96, -.98), (.88, .8, -.86), (.96, .5, -.6), (1, .22, -.4)]
    F = Fish('cascarudo', 30, 8.6, P, bands('N1', 'N1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.87, 0.34, 1, '#b8a060'))
    B = F.B; F.tone0 = -0.2   # dark armour
    F.marks += [m_bar(B, u, 1.2, .06, .46, -1, lean=-0.6) for u in np_r(.1, .76, 6)] + [m_bar(B, u + .06, 1.2, .54, .94, -1, lean=0.6) for u in np_r(.1, .7, 6)]
    F.marks += [m_stripe(B, .04, .8, .5, 1.0, FAM['A3'][4])]
    F.fins += [caudal(B, 'round', 5.6, col=FAM['A3'][3]), dorsal(B, .5, .62, 3.6, 'tri', col=FAM['A3'][3], n=6), adipose(B, .16, 2.0, 1.6, col=FAM['A3'][3]),
               anal(B, .14, .24, 2.6, 'round', col=fc('N1'), n=6), pelvic(B, .46, 2.6, col=fc('N1')), pectoral(B, .84, .72, 3.8, ang=-8, width=0.3, col=fc('N1')),
               barbel(B, .995, .58, 5.2, -5, '#d4d0ca'), barbel(B, .985, .72, 4.6, -30, '#d4d0ca')]
    return _crawlfish(F)
def cascudo():
    # set: PLECO - flat belly under a high arched back / sand body with sparse round dark spots / a tall SAIL dorsal with dark
    # spots / forked tail with a longer LOWER lobe / sucker mouth, eye high on the head, adipose
    P = [(0, .36, -.3), (.1, .5, -.36), (.3, .86, -.44), (.5, 1, -.48), (.7, .94, -.5), (.84, .74, -.5), (.94, .46, -.44), (1, .14, -.3)]
    F = Fish('cascudo', 36, 13, P, bands('C1', 'C1', 'N1', b1=(0.4, 0.42), b2=(0.8, 0.8)), eye=(0.84, 0.2, 2, '#c8a860'))
    B = F.B; F.tone0 = 0.2
    F.marks += [m_spot(B, u, t, 0.9, '#24180c') for u, t in scatter(14, .06, .9, .1, .74, seed=0.37, gap=0.07)]
    sail = dorsal(B, .46, .76, 7.6, 'tri', col=fc('C1'), lean=0.6, n=12)
    sail['band'] = [fin_spots([(B.L * .62 - 1.0, B.top(B.L * .62) + 2.6), (B.L * .56 - 2.4, B.top(B.L * .56) + 4.6), (B.L * .68 - 2.6, B.top(B.L * .68) + 5.2), (B.L * .5, B.top(B.L * .5) + 1.6)], 0.8, FAM['C1'][1])]
    tail = caudal(B, 'fork', 7.0, col=fc('C1'), upper=0.85, lower=1.25); tail['band'] = [fin_spots([(-2.6, 1.6), (-4.4, -2.4), (-5.6, 0.8), (-3.2, -4.6)], 0.8, FAM['C1'][1])]
    F.fins += [tail, sail, adipose(B, .18, 2.4, 1.8, col=FAM['C1'][3]), anal(B, .16, .26, 2.4, 'round', col=fc('N1'), n=6),
               pelvic(B, .5, 3.4, ang=-20, col=fc('N1')), pectoral(B, .82, .82, 5.4, ang=-6, width=0.35, col=fc('C1'))]
    return _crawlfish(F)
def fat_sleeper():
    # set: chunky DARK sleeper resting on the floor / charcoal-brown with a few pale spots / a bright BLUE SHOULDER SPOT above the
    # pectoral / spiny + soft dorsals / big rounded tail
    P = [(0, .44, -.44), (.1, .58, -.56), (.3, .9, -.88), (.5, 1, -1), (.7, .98, -.96), (.84, .86, -.8), (.94, .6, -.5), (1, .28, -.16)]
    F = Fish('fat_sleeper', 30, 11.6, P, bands('N1', 'N1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.84, 0.32, 2, '#c89a50'))
    B = F.B; F.tone0 = 0.2
    F.marks += [m_spot(B, u, t, 0.8, '#d4d0ca') for u, t in scatter(7, .12, .66, .28, .7, seed=0.53, gap=0.08)] + [m_spot(B, .74, .42, 1.5, '#3a90c8')]
    F.marks += [m_bar(B, u, 2.0, .06, .9, -1) for u in (.26, .5)]
    F.fins += [caudal(B, 'round', 7.0, col=FAM['N1'][3]), dorsal(B, .54, .66, 4.6, 'round', col=FAM['N1'][3], n=7), dorsal(B, .24, .44, 4.8, 'round', col=FAM['N1'][3], n=9),
               anal(B, .2, .4, 4.2, 'round', col=FAM['N1'][3], n=9), pelvic(B, .66, 3.4, col=fc('N1')), pectoral(B, .76, .56, 5.0, width=0.55, col=fc('N1'))]
    return _crawlfish(F)
def southern_flounder():
    # set: flat oval FLATFISH lying on the sand, eyed side up / sand-bronze with a few big soft dark blotches / two pale-ringed dark
    # OCELLI / both eyes close together on the head / fringe dorsal and anal fins rippling along the edges
    P = [(0, .24, -.24), (.08, .5, -.5), (.25, .86, -.86), (.5, 1, -1), (.72, .92, -.92), (.86, .7, -.66), (.95, .42, -.32), (1, .12, -.02)]
    F = Fish('southern_flounder', 32, 14, P, bands('C1', 'C1', 'C1', b1=(0.3, 0.3), b2=(0.7, 0.7)), eye=(0.86, 0.22, 2, '#c8b070'))
    F.lightc = (0.35, 0.35, 1.2, 1.4); F.tone0 = 0.3
    B = F.B
    F.marks += [m_spot(B, u, t, 1.6, -1) for u, t in ((.2, .36), (.36, .62), (.52, .3), (.66, .62))]
    F.marks += [m_spot(B, u, t, 1.7, '#e4ccb6') for u, t in ((.4, .48), (.22, .68))] + [m_spot(B, u, t, 1.2, '#24180c') for u, t in ((.4, .48), (.22, .68))]   # dark ocelli, thin pale ring
    F.marks += [m_spot(B, .9, .12, .7, '#24180c'), m_spot(B, .92, .1, .45, '#f1eee9')]
    df = dorsal(B, .04, .9, 3.0, 'flat', col=FAM['C1'][3], lean=0.0, n=30, amp=0.9); df['wave'] = 3.0
    af = anal(B, .04, .74, 3.0, 'flat', col=FAM['C1'][3], lean=0.0, n=26, amp=0.9); af['wave'] = 2.5
    F.fins += [caudal(B, 'round', 5.0, col=FAM['C1'][3]), df, af, pectoral(B, .78, .4, 3.0, col=fc('C1'))]
    return _crawlfish(F)
# ------------------------------------------------------------------ part-based crawlers
def florida_cave_crayfish():
    # cave crayfish: ghost-white, slightly pink and translucent, eyes reduced to pale nubs, long antennae, slender claws held
    # forward, low body = carapace + segmented abdomen ending in a tail fan, four short walking legs per side drawn one by one
    body = ramp('#e4dad2'); joint = ramp('#dcbcb4'); dark = '#9a8a84'
    shape = [(1.2, 15.2), (2.0, 14.6), (5.0, 15.0), (8.0, 14.6), (12.0, 14.0), (16.0, 13.6), (19.0, 13.2), (22.0, 12.8), (26.0, 12.8), (29.0, 13.6),
             (31.0, 14.8), (34.6, 15.8), (31.0, 17.2), (28.0, 19.2), (22.0, 19.6), (16.0, 19.2), (11.0, 18.8), (7.0, 18.6), (4.0, 18.8), (1.6, 19.6), (0.4, 17.4)]
    seg = [(lambda X, Y, x0=x0: (np.abs(X - x0 - (Y - 16) * 0.2) < 0.5), -1) for x0 in (4.6, 7.4, 10.0, 12.6, 15.2, 17.8)]
    groove = [(lambda X, Y: (np.abs(X - 22.6 - (Y - 16) * 0.3) < 0.5) & (Y < 17.4), -1)]
    def frame(f, idle):
        ph = [0, 1, 0, -1][f]; o = 0.4 * ph
        P = [part(shape, body, z=3, name='body', marks=seg + groove, lightc=(0.3, 0.4, 1.5, 1.3))]
        for k, x in enumerate((27.4, 25.2, 23.0, 20.8)):
            up = 0.8 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line([(x, 19.2), (x + 1.2, 20.4 - up), (x + 0.4 + 0.8 * up, 21.6 - up)], joint[2], z=4))
            P.append(line([(x + 1.0, 19.0), (x + 2.0, 20.2), (x + 1.6, 21.6)], joint[0], z=0.4))
        def claw(dx, dy, z, rp, tn):
            return [part(cap([(29.4 + dx, 18.0 + dy), (32.6 + dx, 18.8 + dy), (35.4 + dx, 17.8 + dy)], 0.9), rp, z=z, shade='flat', tone=tn, outline=False, name='c%d' % z),
                    part(ell(37.8 + dx, 17.4 + dy, 2.9, 1.7, -6), rp, z=z + 0.05, name='c%d' % z),
                    part([(40.0 + dx, 16.4 + dy), (44.0 + dx, 16.4 + dy - o), (40.4 + dx, 17.4 + dy)], rp, z=z + 0.06, shade='flat', tone=tn, outline=False, name='c%d' % z),
                    part([(40.0 + dx, 18.4 + dy), (43.4 + dx, 18.0 + dy + o), (40.1 + dx, 17.6 + dy)], rp, z=z + 0.06, shade='flat', tone=tn - 1, outline=False, name='c%d' % z)]
        P += claw(1.0, -1.4, 0.6, ramp('#c8bab2'), 2) + claw(0, 0, 5, joint, 3)
        sw = (0.6 if not idle else 0.3) * ph
        P.append(line([(32.4, 15.0), (36.4, 12.4), (40.6, 10.6 + sw), (45.4, 10.2 + sw), (48.6, 11.2 + sw)], dark, z=6))
        P.append(line([(32.4, 15.4), (36.0, 14.0), (39.4, 13.6 - sw)], dark, z=6))
        return P, [(31.4, 15.6, '#e8a8a4')]
    return Crawler('florida_cave_crayfish', frame, 54, 26)
def pantanal_crab():
    # Dilocarcinus pagei: freshwater crab from the Pantanal seen from the front, walking sideways: broad red-brown carapace,
    # eyes on short stalks, orange-red claws with dark fingertips, four jointed walking legs on each side
    shell = ramp('#9a4a34'); legr = ramp('#a85a3a'); clawr = ramp('#c8643a', sig=True); tip = '#2e1c14'; cx = 20.0
    def frame(f, idle):
        P = []
        for side in (-1, 1):
            for k in range(4):
                up = 1.4 if (not idle and (k + f + (side > 0)) % 2 == 0 and f % 2 == 1) else 0.0
                hip = (cx + side * (7.0 - k * 0.3), 10.6 + k * 0.9); knee = (cx + side * (11.4 + k * 0.7), 9.0 + k * 1.3 - up * 0.5)
                foot = (cx + side * (13.0 + k * 1.0), 21.6 - up)
                P.append(part(cap([hip, knee], 0.6), legr, z=1 + k * 0.01, shade='flat', tone=2 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
                P.append(part(cap([knee, foot], 0.5), legr, z=1 + k * 0.01, shade='flat', tone=1 + (k % 2), outline=False, name='leg%d%d' % (side, k)))
        P.append(part(ell(cx, 11.6, 8.6, 4.8), shell, z=3, name='shell', marks=[(lambda X, Y: (np.abs(X - cx) > 2.4) & (np.abs(X - cx) < 3.2) & (Y > 9) & (Y < 14), -1),
                                                                                 (lambda X, Y: (np.abs(Y - 11.8) < 0.5) & (np.abs(X - cx) < 2.6), -1)]))
        for side in (-1, 1):
            P.append(part(cap([(cx + side * 2.2, 7.2), (cx + side * 2.6, 5.4)], 0.7), shell, z=2.5, shade='flat', tone=3, name='stalk'))
            P.append(part(cap([(cx + side * 5.6, 14.0), (cx + side * 6.6, 15.6)], 1.2), clawr, z=4, name='arm%d' % side))
            P.append(part(ell(cx + side * 4.6, 16.6, 3.6, 2.4, -side * 12), clawr, z=4.1, name='claw%d' % side))
            o = 0.6 * [0, 1, 0, -1][f] if not idle else 0
            P.append(part([(cx + side * 1.6, 16.0), (cx + side * -0.2, 16.4 - o), (cx + side * 1.4, 17.0)], ramp(tip), z=4.2, shade='flat', tone=3, outline=False, name='tip'))
            P.append(part([(cx + side * 1.6, 17.6), (cx + side * 0.0, 18.2 + o), (cx + side * 1.8, 18.4)], ramp(tip), z=4.2, shade='flat', tone=3, outline=False, name='tip'))
        eyes = [(cx - 2.6, 4.8, '#0c0e0c'), (cx + 2.6, 4.8, '#0c0e0c'), (cx - 2.6, 3.8, '#fff0c4'), (cx + 2.6, 3.8, '#fff0c4')]
        return P, eyes
    return Crawler('pantanal_crab', frame, 42, 26)
def _turtle(name, CW, CH, shell_pts, shell_col, plas_col, skin_col, head, neck, legs, tail, seams, shell_marks, head_marks, eye, extra=None, dy=2.6, neck_r=1.7, neck_marks=()):
    R = lambda c: list(c) if isinstance(c, (list, tuple)) else ramp(c)   # hex base or a ready ramp (colour family)
    sh = R(shell_col); pl = R(plas_col); sk = R(skin_col)
    S = lambda pts: [(x, y + dy) for x, y in pts]
    shell_pts = S(shell_pts); neck = S(neck); tail = S(tail); head = (head[0], head[1] + dy) + tuple(head[2:])
    legs = [((h[0], h[1] + dy), (k[0], k[1] + dy * 0.6), ft, nr) for h, k, ft, nr in legs]
    sh_m = lambda ms: [(lambda X, Y, f=f: f(X, Y - dy), c) for f, c in ms]
    seams = sh_m(seams); shell_marks = sh_m(shell_marks); head_marks = sh_m(head_marks); neck_marks = sh_m(neck_marks)
    def frame(f, idle):
        P = [part(shell_pts, sh, z=3, name='shell', marks=seams + shell_marks, lightc=(0.25, 0.3, 1.4, 1.2))]
        P.append(part(plas_col_shape, pl, z=3.2, name='plas'))
        ph = [0, 1, 0, -1][f] if not idle else 0
        hx = head[0] + (0.0 if not idle else 0.4 * [0, 1, 0, 1][f])
        P.append(part(cap(neck, neck_r), sk, z=2.4, name='neck', marks=neck_marks))
        P.append(part(ell(hx, head[1], head[2], head[3], head[4] if len(head) > 4 else 0), sk, z=2.6, name='head', marks=head_marks))
        for k, (hip, knee, foot, near) in enumerate(legs):
            lift = 1.0 if (ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0; fwd = 0.8 * ph * (1 if k % 2 == 0 else -1)
            pts = [hip, (knee[0] + fwd * 0.5, knee[1] - lift * 0.6), (foot[0] + fwd, foot[1] - lift)]
            P.append(part(cap(pts, [1.5, 1.3, 1.2]), sk, z=4 if near else 1, tone=3 if near else 2, name='leg%d' % k))
        P.append(part(cap(tail, [0.9, 0.4]), sk, z=2, name='tail'))
        if extra: P += extra(f, idle)
        return P, [(hx + eye[0], head[1] + eye[1], '#0c0e0c'), (hx + eye[0], head[1] + eye[1] - 1, '#fff0c4')]
    plas_col_shape = None
    def mk(pshape):
        nonlocal plas_col_shape; plas_col_shape = S(pshape); return Crawler(name, frame, CW, CH)
    return mk
def loggerhead_musk_turtle():
    # Sternotherus minor minor: small turtle with a high keeled carapace, brown-orange shell with dark streaks and dark-edged scutes,
    # oversized head (loggerhead) pinkish-grey with dark spots, small yellowish plastron, short tail
    top = [(9.0, 15.0)] + [(x, 15.0 - 8.2 * math.sqrt(max(0, 1 - ((x - 20.0) / 11.0) ** 2)) - (0.8 if abs(x - 19.5) < 2.5 else 0)) for x in np.linspace(9.2, 30.8, 23)] + [(31.0, 15.0)]
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0 - (Y - 10) * 0.15) < 0.5) & (Y > 8.4), -2) for x0 in (15.0, 20.0, 25.0)] + [(lambda X, Y: np.abs(Y - 13.4) < 0.5, -2)]
    streak = [(lambda X, Y, x0=x0: (np.abs((X - x0) - (Y - 10.5) * 0.5) < 0.45) & (Y > 8.6) & (Y < 13), '#3a2412') for x0 in (12.6, 17.4, 22.6, 27.4)]
    hm = [(lambda X, Y, p=p: (X - p[0]) ** 2 + (Y - p[1]) ** 2 < 0.4, '#3a2e2a') for p in ((33.6, 12.4), (35.2, 14.2), (36.6, 12.8), (34.4, 15.0))]
    legs = [((28.0, 15.4), (29.8, 18.4), (30.6, 21.6), True), ((12.6, 15.4), (11.6, 18.4), (11.2, 21.6), True),
            ((26.4, 15.2), (27.6, 18.2), (28.2, 21.6), False), ((14.4, 15.2), (13.8, 18.2), (13.6, 21.6), False)]
    mk = _turtle('loggerhead_musk_turtle', 44, 26, top, '#8a6038', '#c8b07a', '#9a8c80', (35.4, 13.4, 3.8, 2.8), [(30.0, 14.6), (33.0, 14.0)],
                 legs, [(9.4, 15.4), (6.6, 16.8)], seams, streak, hm, (1.6, -0.8))
    return mk([(9.0, 14.8), (31.0, 14.8), (30.2, 16.6), (10.0, 16.6)])
def toad_headed_turtle():
    # Mesoclemmys toad-headed turtle (side-necked): low, flat oval carapace dark olive-brown, broad flat toad-like head, grey-olive
    # skin, pale yellow jaw and throat with two small chin barbels, yellow plastron
    top = [(8.0, 14.6)] + [(x, 14.6 - 6.0 * math.sqrt(max(0, 1 - ((x - 20.0) / 12.4) ** 2))) for x in np.linspace(8.2, 32.0, 23)] + [(32.2, 14.6)]
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0) < 0.5) & (Y > 9.6), -1) for x0 in (14.6, 20.0, 25.4)] + [(lambda X, Y: np.abs(Y - 13.2) < 0.5, -2)]
    hm = [(lambda X, Y: Y > 14.4, '#d8c890'), (lambda X, Y: (np.abs(Y - 13.4) < 0.5) & (X > 38.0), '#4a4a36')]
    legs = [((29.0, 15.0), (31.0, 18.2), (31.8, 21.6), True), ((11.6, 15.0), (10.6, 18.2), (10.2, 21.6), True),
            ((27.4, 14.8), (28.6, 18.0), (29.2, 21.6), False), ((13.4, 14.8), (12.8, 18.0), (12.6, 21.6), False)]
    def extra(f, idle):
        return [line([(39.4, 18.6), (39.6, 19.8)], '#c8b880', z=2.8), line([(38.2, 18.6), (38.3, 19.6)], '#c8b880', z=2.8)]
    mk = _turtle('toad_headed_turtle', 50, 24, top, '#5a4c34', '#d0b860', '#8a8a6a', (38.6, 14.2, 4.6, 2.2, 4), [(31.0, 14.4), (35.2, 14.2)],
                 legs, [(8.4, 14.8), (5.6, 15.8)], seams, [], hm, (1.8, -0.8), extra)
    return mk([(8.0, 14.4), (32.2, 14.4), (31.2, 16.2), (9.0, 16.2)])
def rasp_elimia():
    # Elimia floridensis: tall turreted shell with strong spiral cords and axial ribs ("rasp"), olive-brown, dark aperture,
    # grey foot gliding forward, two slender tentacles; the shell stays fixed while the foot and tentacles move
    shell = ramp('#7a6438'); foot = ramp('#8c8678')
    def frame(f, idle):
        ext = 0 if idle else [0, 0.8, 1.6, 0.8][f]; sw = 0.5 * [0, 1, 0, -1][f]
        P = [part(cap([(9.0, 18.6), (20.0 + ext, 18.4), (23.6 + ext, 18.8)], [1.8, 1.8, 1.1]), foot, z=1, name='foot')]
        for i in range(6):
            t = i / 5.0; cx = 15.0 - 9.6 * t; cy = 14.4 - 10.4 * t; r = 5.0 - 3.9 * t
            P.append(part(ell(cx, cy, r, r * 0.72, -38), shell, z=3 - i * 0.1, name='whorl%d' % i, lightc=(0.3, 0.4, 1.5, 1.3),
                          marks=[(lambda X, Y: (np.abs(((Y + 0.7 * X) % 1.8) - 0.9) < 0.36), -1)]))
        P.append(part(ell(18.4, 16.4, 1.8, 1.5), ramp('#2a2014'), z=3.5, shade='flat', tone=3, outline=False, name='ap'))
        P.append(line([(22.4 + ext, 17.4), (25.2 + ext, 14.6 + sw)], '#5e5a50', z=4))
        P.append(line([(23.0 + ext, 17.8), (26.4 + ext, 16.6 - sw)], '#5e5a50', z=4))
        return P, [(22.6 + ext, 17.0, '#141210')]
    return Crawler('rasp_elimia', frame, 34, 24, prefix='crawl_')
SCENE = {
    'cambeva': dict(speed=10, fps=8, bob_amount=0.5, move_time=(2, 5), idle_time=(1, 3), crowd_radius=(40, 8)),
    'cascarudo': dict(speed=8, fps=8, bob_amount=0.5, move_time=(2, 5), idle_time=(1, 4), crowd_radius=(45, 8)),
    'cascudo': dict(speed=6, fps=6, bob_amount=0.0, move_time=(2, 5), idle_time=(3, 8), crowd_radius=(55, 8)),
    'fat_sleeper': dict(speed=8, fps=7, bob_amount=0.5, move_time=(1, 3), idle_time=(3, 8), crowd_radius=(50, 8)),
    'southern_flounder': dict(speed=6, fps=6, bob_amount=0.0, move_time=(1, 3), idle_time=(4, 10), crowd_radius=(60, 8)),
    'florida_cave_crayfish': dict(speed=10, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(1, 3), crowd_radius=(50, 8)),
    'pantanal_crab': dict(speed=10, fps=9, bob_amount=0.5, move_time=(1, 3), idle_time=(1, 4), crowd_radius=(45, 8)),
    'loggerhead_musk_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(55, 8)),
    'toad_headed_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(60, 8)),
    'rasp_elimia': dict(speed=2, fps=5, move_prefix='crawl_', bob_amount=0.0, move_time=(6, 10), idle_time=(2, 6), crowd_radius=(30, 8)),
}
