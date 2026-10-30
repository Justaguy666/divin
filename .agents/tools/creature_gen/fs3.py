"""Forest Stream batch 3 - bottom dwellers and crawlers, defined from species names only.
v3 (Oct 2026): the three bottom fish are one memorable set each, coloured from the fs colour families (pal.FAM_FS); the
part-built animals keep their drawings and take their colours from the families too."""
import math, numpy as np
import pal; pal.use('fs')
from swim import Fish, dorsal, anal, adipose, caudal, pectoral, pelvic, barbel, m_stripe, m_bar, m_spot, m_dash
from pal import ramp, FAM, fc
from v3h import scatter, fin_spots
from fs1 import low
from sp1 import bands, np_r
from parts import Crawler, part, line, ell, cap
from sp4 import _crawlfish, _turtle
from recol import Recolor
ALL = ['northern_madtom', 'stonecat', 'mottled_sculpin', 'hellbender', 'mudpuppy', 'appalachian_brook_crayfish', 'rusty_crayfish', 'eastern_musk_turtle', 'silty_hornsnail']
CAT = [(0, .44, -.44), (.1, .58, -.58), (.3, .88, -.9), (.55, 1, -1), (.75, .96, -.98), (.88, .8, -.86), (.96, .5, -.62), (1, .22, -.4)]
def cat_fins(B, col, adi_join=True, n_barb=4, barb=None):
    f = [caudal(B, 'round', 5.6, col=col), dorsal(B, .5, .6, 3.6, 'tri', col=col, n=6),
         (dorsal(B, .02, .4, 1.8, 'flat', col=col, n=14, lean=0) if adi_join else adipose(B, .2, 3.0, 1.8, col=col)),
         anal(B, .1, .3, 2.6, 'round', col=col, n=9), pelvic(B, .46, 2.6, col=col), pectoral(B, .84, .74, 3.8, ang=-8, width=0.35, col=col)]
    ang = (-5, -30, -55, 20)
    for i in range(n_barb): f.append(barbel(B, .99 - .02 * (i % 2), .5 + .12 * i if i < 3 else .2, 3.2 - .3 * i, ang[i], barb or FAM['N1'][4]))
    return f
def northern_madtom():
    # set: small madtom catfish / sand-copper with THREE bold black SADDLES (under the dorsal, over the adipose, at the tail base) /
    # dark-mottled head / a dark crescent across the rounded tail / pale barbels
    F = Fish('northern_madtom', 24, 7.2, CAT, bands('R1', 'R1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.86, 0.3, 1, '#a08860'))
    B = F.B; low(F); d = '#1c120a'
    F.marks += [m_bar(B, u, 3.0, 0, .78, d, lean=0.3) for u in (.12, .34, .58)] + [m_spot(B, u, t, .6, d) for u, t in ((.82, .3), (.89, .44), (.78, .52))]
    fins = cat_fins(B, fc('R1')); fins[0]['band'] = [(lambda X, Y: (X < -1.6) & (X > -3.4), '#2a1a10')]
    F.fins += fins; F.mouth = (.62, 1.0); return _crawlfish(F)
def stonecat():
    # set: plain grey catfish with a flat head / a PALE NAPE SADDLE in front of the dorsal and a small pale blotch behind it / long
    # low adipose KEEL running into a square tail with a PALE MARGIN / pale barbels
    F = Fish('stonecat', 32, 8.6, CAT, bands('N1', 'N1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.87, 0.3, 1, '#a89060'))
    B = F.B; F.tone0 = 0.4; pale = FAM['N1'][5]
    F.marks += [(lambda x, y, uu, tt: (uu > .64) & (uu < .72) & (tt < .62), pale), (lambda x, y, uu, tt: (uu > .4) & (uu < .46) & (tt < .46), pale)]
    fc3 = FAM['N1'][3]
    fins = cat_fins(B, fc3); fins[0] = caudal(B, 'truncate', 5.6, col=fc3); fins[0]['band'] = [(lambda X, Y: X < -4.2, FAM['N1'][5])]
    F.fins += fins; F.mouth = (.6, 1.2); return _crawlfish(F)
def mottled_sculpin():
    # set: big FLAT head with high eyes, body tapering to the tail / olive with three dark SADDLES and soft mottling / huge FAN
    # pectorals crossed by dark BARS / spiny first dorsal with a black spot and an ORANGE EDGE
    P = [(0, .36, -.36), (.1, .46, -.46), (.3, .7, -.76), (.5, .86, -.9), (.66, .98, -.98), (.8, 1, -.98), (.9, .84, -.86), (.96, .56, -.6), (1, .22, -.3)]
    F = Fish('mottled_sculpin', 28, 9.4, P, bands('G1', 'G1', 'N1', b1=(0.4, 0.44), b2=(0.86, 0.86)), eye=(0.84, 0.2, 2, '#c8a050'))
    B = F.B; low(F, 0.15); d = '#161a0a'
    F.marks += [m_bar(B, u, 2.6, 0, .74, d, lean=0.4) for u in (.14, .36, .58)] + [m_spot(B, u, t, .8, FAM['G1'][1]) for u, t in scatter(5, .2, .82, .46, .7, seed=0.31, gap=0.12)]
    d1 = dorsal(B, .6, .74, 3.0, 'round', col=FAM['G1'][3], n=7, sig=True)
    d1['band'] = [(lambda X, Y, B=B: Y > B.top(X) + 2.0, '#d16631'), (lambda X, Y, B=B: (Y > B.top(X) + 0.6) & (Y < B.top(X) + 1.8) & (X < .67 * B.L), '#161a0a')]
    x0, y0 = .78 * B.L, B.yat(.78, .56)
    pec = pectoral(B, .78, .56, 6.2, ang=-18, width=0.75, col=FAM['G1'][3], sig=True)
    pec['band'] = [(lambda X, Y: ((np.hypot(X - x0, Y - y0) % 2.2) < 0.9) & (np.hypot(X - x0, Y - y0) > 1.6), FAM['G1'][0])]
    F.fins += [caudal(B, 'round', 5.0, col=fc('G1')), d1, dorsal(B, .22, .58, 3.4, 'round', col=fc('G1'), n=12), anal(B, .2, .5, 2.8, 'round', col=fc('G1'), n=10),
               pelvic(B, .7, 2.6, col=fc('N1')), pec]
    F.mouth = (.56, 1.6); return _crawlfish(F)
# ------------------------------------------------------------------ salamanders (part-based)
def _sal(name, L, H0, top, bot, colr, head_marks, body_marks, legs, gills=None, CW=70, CH=24, eye=None, tailfin=None):
    """long side-view salamander: body outline from top/bottom curves (x from tail tip to snout), four splayed legs."""
    xs = np.linspace(2, L, 40)
    poly = [(x, top(x)) for x in xs] + [(x, bot(x)) for x in xs[::-1]]
    body = ramp(colr)
    def frame(f, idle):
        ph = [0, 1, 0, -1][f]; P = []
        wav = (0 if idle else 0.6) * ph
        pts = [(x, y + wav * math.sin((L - x) / L * math.pi * 1.5) * (1 - x / L)) for x, y in poly]
        P.append(part(pts, body, z=3, name='body', marks=body_marks, lightc=(0.3, 0.4, 1.5, 1.3)))
        if tailfin: P.append(part([(x, y + wav * math.sin((L - x) / L * math.pi * 1.5) * (1 - x / L)) for x, y in tailfin], ramp(pal.mix(colr, '#c8c0a0', .25)), z=2.9, name='body'))
        for k, (hip, knee, foot, near) in enumerate(legs):
            lift = 0.9 if (ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0; fw = 0.8 * ph * (1 if k % 2 == 0 else -1)
            pp = [hip, (knee[0] + fw * .5, knee[1] - lift * .5), (foot[0] + fw, foot[1] - lift)]
            P.append(part(cap(pp, [1.4, 1.1, 0.9]), body, z=4 if near else 1, tone=3 if near else 2, name='leg%d' % k))
            for dx in (-1.0, 0.0, 1.0):
                P.append(line([pp[2], (pp[2][0] + dx + 0.6, pp[2][1] + 0.6)], body[1], z=4.1 if near else 1.1))
        if gills: P += gills(f, idle)
        return P, eye
    return Crawler(name, frame, CW, CH)
def hellbender():
    # set: the existing hellbender drawing (kept by request) - big flat wrinkled salamander, re-mapped onto the copper-brown family:
    # rust-brown body, dark blotches, pale-grey skin folds
    R = FAM['R1']; return Recolor('old_fs/fs_hellbender_crawl_*_4f.png', ['#26120a', R[0], R[1], R[2], R[3], R[4]])   # family shifted one step darker: brown, not salmon
def mudpuppy():
    # set: the existing mudpuppy drawing (kept) re-mapped onto the pool-teal family - slate-teal body with dark spots - so the RED
    # feathery gills stand out as the signature
    G = FAM['G3']; return Recolor('old_fs/fs_mudpuppy_crawl_*_4f.png', ['#061c18', G[0], G[1], G[2], G[3], G[4]], sig=[(330, 50, 0.05, '#b8443a')])
# ------------------------------------------------------------------ crayfish
def _crayfish(name, body_c, joint_c, claw_c, tip_c, marks_fn, claw_w=1.0, rostrum=3.6, claw_marks=()):
    R = lambda c: list(c) if isinstance(c, (list, tuple)) else (list(FAM[c]) if c in FAM else ramp(c))   # ready ramp, family key or hex base
    body = R(body_c); joint = R(joint_c); clawr = R(claw_c)
    if isinstance(body_c, str) and body_c.startswith('#'):   # hex callers (v1 bb / by / cw) keep their original far claw and antennae
        claw_dk = ramp(pal.mix(claw_c, '#000000', .2)); dark = pal.mix(body_c, '#000000', 0.35)
    else: claw_dk = [pal.mix(c, '#000000', .2) for c in clawr]; dark = pal.mix(body[2], '#000000', 0.3)
    shape = [(1.2, 15.2), (2.0, 14.6), (5.0, 15.0), (8.0, 14.6), (12.0, 14.0), (16.0, 13.6), (19.0, 13.2), (22.0, 12.6), (26.0, 12.6), (29.0, 13.4),
             (31.0, 14.6), (31.0 + rostrum, 15.6), (31.0, 17.2), (28.0, 19.2), (22.0, 19.6), (16.0, 19.2), (11.0, 18.8), (7.0, 18.6), (4.0, 18.8), (1.6, 19.6), (0.4, 17.4)]
    seg = [(lambda X, Y, x0=x0: (np.abs(X - x0 - (Y - 16) * 0.2) < 0.5), -1) for x0 in (4.6, 7.4, 10.0, 12.6, 15.2, 17.8)]
    groove = [(lambda X, Y: (np.abs(X - 22.6 - (Y - 16) * 0.3) < 0.5) & (Y < 17.4), -1)]
    def frame(f, idle):
        ph = [0, 1, 0, -1][f]; o = 0.4 * ph
        P = [part(shape, body, z=3, name='body', marks=seg + groove + marks_fn(), lightc=(0.3, 0.4, 1.5, 1.3))]
        for k, x in enumerate((27.4, 25.2, 23.0, 20.8)):
            up = 0.8 if (not idle and ph != 0 and (k % 2 == 0) == (ph > 0)) else 0.0
            P.append(line([(x, 19.2), (x + 1.2, 20.4 - up), (x + 0.4 + 0.8 * up, 21.6 - up)], joint[2], z=4))
            P.append(line([(x + 1.0, 19.0), (x + 2.0, 20.2), (x + 1.6, 21.6)], joint[0], z=0.4))
        def claw(dx, dy, z, rp, tn):
            w = claw_w
            return [part(cap([(29.4 + dx, 18.0 + dy), (32.6 + dx, 18.8 + dy), (35.2 + dx, 17.8 + dy)], 1.0), rp, z=z, shade='flat', tone=tn, outline=False, name='c%d' % z),
                    part(ell(38.0 + dx, 17.4 + dy, 3.0, 1.8 * w, -6), rp, z=z + 0.05, name='c%d' % z, marks=list(claw_marks) if z == 5 else []),
                    part([(40.4 + dx, 16.2 + dy), (44.0 + dx, 16.4 + dy - o), (40.8 + dx, 17.4 + dy)], ramp(tip_c), z=z + 0.06, shade='flat', tone=tn, outline=False, name='c%d' % z),
                    part([(40.4 + dx, 18.6 + dy), (43.6 + dx, 18.0 + dy + o), (40.5 + dx, 17.6 + dy)], ramp(tip_c), z=z + 0.06, shade='flat', tone=tn - 1, outline=False, name='c%d' % z)]
        P += claw(1.0, -1.4, 0.6, claw_dk, 2) + claw(0, 0, 5, clawr, 3)
        sw = (0.6 if not idle else 0.3) * ph
        P.append(line([(32.4, 15.0), (36.4, 12.4), (40.6, 10.6 + sw), (45.4, 10.2 + sw), (48.6, 11.2 + sw)], dark, z=6))
        P.append(line([(32.4, 15.4), (36.0, 14.0), (39.4, 13.6 - sw)], dark, z=6))
        return P, [(31.0, 15.2, '#0c0e0c'), (31.0, 14.2, '#fff0c4')]
    return Crawler(name, frame, 54, 26)
def appalachian_brook_crayfish():
    # set: stream crayfish with a short broad rostrum / OLIVE with darker MOTTLING over the carapace and tail / BROAD heavy claws
    # with brown fingertips
    rng = np.random.RandomState(3); sp = list(zip(rng.uniform(4, 28, 8), rng.uniform(14.6, 17.6, 8)))   # fixed once so the mottling holds still
    mot = lambda: [(lambda X, Y, p=p: (X - p[0]) ** 2 + ((Y - p[1]) * 1.4) ** 2 < 0.9, -1) for p in sp]
    return _crayfish('appalachian_brook_crayfish', 'G1', 'G1', 'G1', FAM['R1'][2], mot, claw_w=1.25, rostrum=2.4)
def rusty_crayfish():
    # set: slim grey crayfish / a RUSTY-RED SPOT on each side of the carapace / big claws with a BLACK BAND near the tips and
    # ORANGE fingertips / long rostrum
    rust = lambda: [(lambda X, Y: ((X - 25.0) / 2.2) ** 2 + ((Y - 16.4) / 1.4) ** 2 < 1, '#9d3629')]
    band = [(lambda X, Y: (X > 39.4) & (X < 40.8), '#14100c')]
    return _crayfish('rusty_crayfish', 'N1', 'N1', 'N1', '#d16631', rust, claw_w=1.15, rostrum=3.8, claw_marks=band)
def eastern_musk_turtle():
    # set: small HIGH-DOMED smooth dark olive shell / dark head with TWO PALE STRIPES (above and below the eye) / pointed snout with
    # chin barbels / small pale plastron
    top = [(10.0, 15.0)] + [(x, 15.0 - 7.6 * math.sqrt(max(0, 1 - ((x - 20.0) / 10.0) ** 2))) for x in np.linspace(10.2, 29.8, 21)] + [(30.0, 15.0)]
    seams = [(lambda X, Y, x0=x0: (np.abs(X - x0) < 0.5) & (Y > 9.0), -1) for x0 in (15.6, 20.0, 24.4)] + [(lambda X, Y: np.abs(Y - 13.6) < 0.5, -1)]
    hm = [(lambda X, Y: np.abs(Y - 12.4) < 0.5, FAM['G1'][5]), (lambda X, Y: (np.abs(Y - 14.4) < 0.5) & (X > 32), FAM['G1'][5])]
    legs = [((27.0, 15.4), (28.6, 18.4), (29.4, 21.6), True), ((13.4, 15.4), (12.4, 18.4), (12.0, 21.6), True),
            ((25.6, 15.2), (26.6, 18.2), (27.2, 21.6), False), ((14.8, 15.2), (14.2, 18.2), (14.0, 21.6), False)]
    extra = lambda f, idle: [line([(35.0, 17.0), (35.2, 18.0)], FAM['N1'][4], z=2.8)]
    mk = _turtle('eastern_musk_turtle', 44, 26, top, FAM['G1'][1], FAM['G1'][4], FAM['G1'][2], (34.0, 13.6, 3.2, 2.2), [(29.4, 14.6), (32.0, 14.0)],
                 legs, [(10.4, 15.4), (8.0, 16.6)], seams, [], hm, (1.4, -0.8), extra)
    return mk([(10.0, 14.8), (30.0, 14.8), (29.2, 16.4), (11.0, 16.4)])
def silty_hornsnail():
    # set: long HORN-shaped conical shell in copper-brown / dark SPIRAL BANDS and pale growth flecks / dark aperture / grey foot
    # and slender tentacles; the shell stays fixed while the foot glides
    shell = ramp(FAM['R1'][2]); foot = ramp(FAM['N1'][3])
    def frame(f, idle):
        ext = 0 if idle else [0, 0.8, 1.6, 0.8][f]; sw = 0.5 * [0, 1, 0, -1][f]
        P = [part(cap([(9.0, 18.6), (20.0 + ext, 18.4), (23.6 + ext, 18.8)], [1.8, 1.8, 1.1]), foot, z=1, name='foot')]
        for i in range(7):
            t = i / 6.0; cx = 15.0 - 11.0 * t; cy = 14.6 - 11.4 * t; r = 4.6 - 3.6 * t
            P.append(part(ell(cx, cy, r, r * 0.66, -42), shell, z=3 - i * 0.1, name='whorl%d' % i, lightc=(0.3, 0.4, 1.5, 1.3),
                          marks=[(lambda X, Y, c=cx: np.abs(((X - Y) * 0.7 % 3.2) - 1.6) < 0.4, -2), (lambda X, Y: (np.round(X) + 2 * np.round(Y)) % 7 == 0, FAM['R1'][4])]))
        P.append(part(ell(18.2, 16.4, 1.6, 1.4), ramp('#2a2014'), z=3.5, shade='flat', tone=3, outline=False, name='ap'))
        P.append(line([(22.4 + ext, 17.4), (25.2 + ext, 14.6 + sw)], FAM['N1'][1], z=4))
        P.append(line([(23.0 + ext, 17.8), (26.4 + ext, 16.6 - sw)], FAM['N1'][1], z=4))
        return P, [(22.6 + ext, 17.0, '#141210')]
    return Crawler('silty_hornsnail', frame, 34, 24, prefix='crawl_')
SCENE = {
    'northern_madtom': dict(speed=8, fps=8, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 5), crowd_radius=(40, 8)),
    'stonecat': dict(speed=8, fps=8, bob_amount=0.5, move_time=(1, 3), idle_time=(2, 6), crowd_radius=(50, 8)),
    'mottled_sculpin': dict(speed=6, fps=7, bob_amount=0.0, move_time=(0.5, 2), idle_time=(2, 6), crowd_radius=(45, 8)),
    'hellbender': dict(speed=5, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(3, 8), crowd_radius=(80, 8)),
    'mudpuppy': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 6), crowd_radius=(60, 8)),
    'appalachian_brook_crayfish': dict(speed=10, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(1, 3), crowd_radius=(50, 8)),
    'rusty_crayfish': dict(speed=10, fps=8, bob_amount=0.5, move_time=(1, 4), idle_time=(1, 3), crowd_radius=(50, 8)),
    'eastern_musk_turtle': dict(speed=6, fps=6, bob_amount=0.5, move_time=(2, 5), idle_time=(2, 5), crowd_radius=(55, 8)),
    'silty_hornsnail': dict(speed=2, fps=5, move_prefix='crawl_', bob_amount=0.0, move_time=(6, 10), idle_time=(2, 6), crowd_radius=(30, 8)),
}
