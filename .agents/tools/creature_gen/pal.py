"""Clear Spring palette helpers (OKLab). Habitat: crystal-clear aquamarine spring, strong sun from above, white sand.
Lighting ramp: shadows lean to deep teal, midtones get a faint aqua cast, highlights lean to sunlit cream."""
import numpy as np
import biomes   # biome registry (water lightness)
SHADOW = '#123a44'; CAST = '#5cb8b0'; HIGH = '#fff6dc'; OUT_TINT = '#0c2228'; FIN_TINT = '#a6dcd4'
# habitat lighting per biome (defined from the habitat description only)
BIOMES = {
    'cs': dict(SHADOW='#123a44', CAST='#5cb8b0', HIGH='#fff0c8', OUT_TINT='#0c2228', FIN_TINT='#a6dcd4'),   # HIGH warmed from #fff6dc with the v2 restyle
    # forest stream: shade of the canopy, moss-brown shadows, faint leaf-green cast, warm sun-fleck highlights
    'fs': dict(SHADOW='#1e2c1c', CAST='#7a9a5a', HIGH='#f8ecbe', OUT_TINT='#121a10', FIN_TINT='#bcd4b0'),   # HIGH warmed from #f8f2d2 with the v2 restyle
    # marsh / swamp: still weedy peat water, deep peat-olive shadows, reed-gold cast, hazy pale straw highlights
    'ms': dict(SHADOW='#1c2012', CAST='#9a985a', HIGH='#eeecce', OUT_TINT='#141a0e', FIN_TINT='#c4c8a2'),
    # billabong: tropical oxbow waterhole, clear teal water over red-ochre clay, hot sun: teal-brown shadows, faint ochre cast, sandy highlights
    'bb': dict(SHADOW='#1a2824', CAST='#b08060', HIGH='#f6ecd2', OUT_TINT='#121c18', FIN_TINT='#c4d2c0'),
    'by': dict(SHADOW='#1e1e10', CAST='#a8844a', HIGH='#f2e8c4', OUT_TINT='#14140a', FIN_TINT='#ccc6a0'),
    'cw': dict(SHADOW='#101c26', CAST='#4a7690', HIGH='#eaf0ee', OUT_TINT='#0a141c', FIN_TINT='#b4c8d0'),
    'uc': dict(SHADOW='#0e121a', CAST='#4e5c86', HIGH='#e8ecf2', OUT_TINT='#080a12', FIN_TINT='#b0b8c8'),
}
def use(b):
    g = globals()
    for k, v in BIOMES[b].items(): g[k] = v
    if RAMPSTYLE.get('v3') == b:   # v3 overrides survive a species module calling use() again
        for k, v in BIOMES_V3.get(b, {}).items(): g[k] = v
def h2r(h): h = h.lstrip('#'); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float) / 255
def r2h(c): c = np.clip(np.round(np.asarray(c) * 255), 0, 255).astype(int); return '#%02x%02x%02x' % tuple(c)
def _lin(c): c = np.asarray(c, float); return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
def _gam(c): c = np.clip(c, 0, 1); return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055)
M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]])
M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]])
def lab(h):
    c = _lin(h2r(h) if isinstance(h, str) else h); return M2 @ np.cbrt(M1 @ c)
def hexl(L):
    lms = np.linalg.inv(M2) @ np.asarray(L, float); return r2h(_gam(np.linalg.inv(M1) @ lms ** 3))
def mix(a, b, k):
    A, B = lab(a), lab(b); return hexl(A + (B - A) * k)
# v3 colour fit (Oct 2026): creatures must stand out from their own water the way bw / ac ones do. Per biome: the median
# water lightness behind the swimmers (bg_L), measured from the far+mid+near background, and the light that falls on the
# animals (CAST: sunlight, not the water colour - the water colour stays in the shadows). In v3 no body tone may sit within
# +-gap of the water lightness, so every fish brackets the water: darks below it, lit parts above it.
BG_L = {p: b['water'][1] for p, b in biomes.GEN.items()}   # water lightness from the biome registry (biomes.py)
BIOMES_V3 = {'cs': dict(CAST='#7cc0b4', HIGH='#eef8f2'), 'fs': dict(CAST='#88b890', HIGH='#eef6ec'), 'ms': dict(CAST='#92a67f', HIGH='#f0f4e4')}   # cs: water light (cool white highlights), not warm sun - the scene has no warm colour
FIT_V3 = {'cs': dict(gap=0.12, chroma=1.0, cast=0.08, tone_shift=0.0, hi_mix=0.1, steer=(-176, 45, 110)),
          'fs': dict(gap=0.1, chroma=1.0, cast=0.08, tone_shift=0.0, hi_mix=0.1, steer=(150, 45, 110)),
          'ms': dict(gap=0.06, chroma=1.0, cast=0.08, tone_shift=0.0, hi_mix=0.1, steer=(130, 45, 110), outline=(0.70, 0.64, 0.52, 0.40, 0.36, 0.72))}   # dark water (L 0.42, 0.67 -> 0.29 with depth): as bw / ac, bodies a little above the water, lit well above   # bright water (L 0.73): lighter fish (fit C)
# cs colour families (Oct 2026, from the background analysis): 6 tones dark->light at L 0.28 0.40 0.52 0.63 | 0.86 0.95 - no
# tone inside the water band the fish swim in (L 0.70-0.82). A = analogous to the water, N = neutral, C = complement (muted for
# bodies, saturated only as accents). Hues 45-110 deg from the water (yellow-olive, lime, violet) are avoided for bodies.
FAM_CS = {k: v.split() for k, v in {
    'A1': '#112e2e #314e4d #556f6e #788e8e #c3d5d5 #e6f1f1',   # aqua silver
    'A2': '#052f35 #284e55 #4e7076 #718f95 #bfd6da #e4f1f4',   # slate teal
    'A3': '#0a3123 #285140 #4a7361 #6d9382 #bdd9cb #e3f3eb',   # sea green
    'A4': '#0f2c3c #2b4c5f #4f6d7f #728e9e #bfd5e2 #e5f0f7',   # azure steel
    'N1': '#2c2822 #4b4741 #6d6861 #8d8881 #d4d0ca #f1eee9',   # pearl / charcoal
    'C1': '#372513 #5b422a #7f6347 #a18366 #e4ccb6 #f8ece1',   # sand bronze
    'C2': '#3d2200 #683c00 #925b00 #b97a13 #fac787 #ffeacb',   # amber gold
    'C3': '#4a1500 #792c00 #a84811 #d16631 #ffbc9a #ffe5d3',   # coral tangerine
    'C4': '#4f0b08 #831b16 #b6322b #dd574b #ffb5a9 #ffe3dc',   # signal red
}.items()}
# fs colour families (Oct 2026): the forest-stream water is green (OKLab hue 150, chroma 0.08-0.10), L 0.74 near the surface,
# 0.68 mid, 0.50 low, 0.42 at the floor, with dark brown roots and orange leaf litter. Tones at L 0.26 0.37 0.48 0.60 | 0.82 0.93
# (no tone inside the upper water band 0.62-0.78; bottom fish lean on the light tones). G = analogous greens / teal, N = neutral,
# R = complement (copper, rust, rose: muted on bodies, saturated as accents), T = turquoise accent at the analogous edge.
# Yellow / gold / ochre and blue (45-110 deg from the water) are kept off bodies.
FAM_FS = {k: v.split() for k, v in {
    'G1': '#22270f #3d4324 #5b623e #7d8563 #c2c8ae #e6eadc',
    'G2': '#122a18 #2c4732 #49664f #6e8872 #b7caba #e1ebe3',
    'G3': '#0d2a26 #2a4642 #4b6360 #6f8682 #b7c9c6 #e0ebe9',
    'N1': '#27231e #433f39 #615d56 #848078 #c7c3bd #ebe7e2',
    'R1': '#381b10 #5d3324 #7f503f #9e7564 #cbc2bc #ebe7e4',
    'R2': '#460b06 #721d14 #9d3629 #c65b4c #f9aea2 #ffdfd8',
    'R3': '#420e1b #6d2032 #9c334b #c4576d #f8acb7 #ffdee2',
    'T1': '#002c2d #004c4d #006e6f #0f9293 #8dd3d2 #d2efee',
}.items()}
# ms colour families (Oct 2026): the marsh water is murky olive green (OKLab hue 130, chroma 0.05-0.08) and dark like bw / ac:
# L 0.67 at the surface, 0.52 mid, 0.35 low, 0.29 at the floor (0.42 on average), with a dark brown cypress trunk and rust cattail
# heads. Tones at L 0.24 0.36 0.48 0.60 | 0.80 0.92: bodies sit a little above the average water and lit tones well above it, as
# in bw / ac. Analogous here includes gold and brass (O, G, Y); orange, amber and cyan / sky blue (45-110 deg) stay off bodies;
# the complement is crimson, rose, violet, indigo and slate (S, M muted for bodies; R, B accents).
FAM_MS = {k: v.split() for k, v in {
    'O1': '#23200b #433e21 #645e3d #87815f #c3bfa3 #e7e5d8',   # brass olive
    'G1': '#172313 #32422d #51644b #75866f #b5c2b1 #e0e7de',   # reed green
    'Y1': '#281e00 #4a3c00 #6f5c00 #957f23 #d0be79 #ede5c7',   # gold (accent)
    'N1': '#201f1a #3e3d37 #5f5e57 #81807a #bfbeb7 #e5e5e0',   # pearl / charcoal
    'N2': '#261e14 #453b30 #675c4f #897e72 #c5bcb3 #e8e4df',   # peat
    'S1': '#18202b #333e4c #525f6f #758191 #b5bfcb #e0e5eb',   # slate
    'M1': '#2e1818 #523432 #775351 #987775 #ccb9b7 #ebe2e1',   # mahogany
    'R1': '#40030c #6f1821 #9d343b #c6585d #f2a7a6 #fedbda',   # crimson (accent)
    'R2': '#360e24 #622344 #8d3d67 #b4608a #e6a9c5 #f8dce8',   # rose (accent)
    'B1': '#0f1e3b #253c67 #3e5c96 #5f80bc #a5bfec #dae5f9',   # indigo (accent)
}.items()}
FAM_BY_BIOME = {'cs': FAM_CS, 'fs': FAM_FS, 'ms': FAM_MS}
FAM = dict(FAM_CS)
def fc(k, i=4): return FAM[k][i]   # a family tone as a fin / mark colour
def use_v3(b):
    RAMPSTYLE['v3'] = b; use(b); g = globals()
    if b in FAM_BY_BIOME: FAM.clear(); FAM.update(FAM_BY_BIOME[b])
    for k, v in BIOMES_V3.get(b, {}).items(): g[k] = v
    f = FIT_V3.get(b, {}); RAMPSTYLE.update(bg_L=BG_L.get(b), gap=f.get('gap', 0.1), chroma=f.get('chroma', 1.15), cast=f.get('cast', 0.15))
    if 'hi_mix' in f: RAMPSTYLE['hi_mix'] = f['hi_mix']
    if 'steer' in f: RAMPSTYLE['steer'] = f['steer']   # lit tones keep the species' own hue (less pull toward the cream highlight)
    return f.get('tone_shift', 0.0)
RAMPSTYLE = dict(hi_mix=0.2, hi_lift=0.0)   # shipped look; the study proposal uses hi_mix 0.28, hi_lift 0.02
def ramp(base, n=6, step=0.1, sig=False, cast=0.07):
    """n tones dark->light, base sits at index n//2. sig=True keeps the hue (signature colour, ungraded)."""
    B = lab(base); S = lab(SHADOW); Hh = lab(HIGH); C = lab(CAST)
    if not sig: B = B.copy(); B[1:] += (C[1:] - B[1:]) * RAMPSTYLE.get('cast', cast); B[1:] *= RAMPSTYLE.get('chroma', 1.0)
    if not sig and RAMPSTYLE.get('steer'):   # colour harmony with the water: no body hue in the discord band between analogous and complementary
        bh, lo, hi = RAMPSTYLE['steer']; Cb = np.hypot(B[1], B[2])
        if Cb > 0.015:
            h = np.degrees(np.arctan2(B[2], B[1])); dh = ((h - bh + 180) % 360) - 180
            if lo < abs(dh) < hi:
                nd = np.sign(dh) * (lo if abs(dh) - lo < hi - abs(dh) else hi); nh = np.radians(bh + nd); B[1], B[2] = Cb * np.cos(nh), Cb * np.sin(nh)
    out = []; bgL = RAMPSTYLE.get('bg_L'); gap = RAMPSTYLE.get('gap', 0.0)
    for i in range(n):
        d = i - n // 2; c = B.copy(); c[0] = np.clip(B[0] + d * step, 0.10, 0.97)
        if d > 0 and RAMPSTYLE['hi_lift']: c[0] = np.clip(c[0] + RAMPSTYLE['hi_lift'] * d, 0.10, 0.97)
        if bgL is not None and abs(c[0] - bgL) < gap:   # keep out of the water's own lightness: lit tones above it, the rest below
            c[0] = min(0.97, bgL + gap) if (d > 0 or (d == 0 and c[0] >= bgL)) else bgL - gap
        if not sig:
            if d < 0: c[1:] += (S[1:] - c[1:]) * min(0.5, 0.16 * -d)
            if d > 0: c[1:] += (Hh[1:] - c[1:]) * min(0.75, RAMPSTYLE['hi_mix'] * d)
        else:
            c[1:] *= (1 - 0.06 * abs(d))
        out.append(hexl(c))
    return out
def shade(h, k=0.55, lit=False):
    """outline: dark shade of the adjacent colour, tinted toward the outline tint; lit edge one step lighter."""
    c = lab(h); t = lab(OUT_TINT); k = 0.72 if lit else k
    o = c.copy(); o[0] = max(0.12, c[0] * k); o[1:] = c[1:] * 0.9
    return hexl(o + (t - o) * 0.18)
FINSTYLE = dict(tint=0.35, lift=0.0, ray_dL=0.2)   # shipped look; the study proposal uses tint 0.15, lift 0.06, ray_dL 0.09
def fin(base, sig=False):
    """fin membrane / ray / rim colours (translucent fins get an aqua tint)."""
    b = base if sig else mix(base, FIN_TINT, FINSTYLE['tint'])
    L = lab(b)
    if FINSTYLE['lift'] and not sig: L[0] = min(0.92, L[0] + FINSTYLE['lift']); b = hexl(L)
    if sig and FINSTYLE.get('sig_dL'): L[0] -= FINSTYLE['sig_dL']; L[1:] *= 1.05; b = hexl(L)   # signature colour sits a touch deeper so it still reads through the alpha
    ray = L.copy(); ray[0] -= (max(FINSTYLE['ray_dL'], 0.17) if sig else FINSTYLE['ray_dL']); ray[1:] *= 1.1; rim = L.copy(); rim[0] -= 0.08   # signature fins keep deep rays: they carry the colour
    return dict(mem=b, ray=hexl(ray), rim=hexl(rim))
