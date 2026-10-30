"""Review package for Khoi (one look per decision; every species has a code <PRE>01.. in module order).
  python3 review.py <pre> <pilot_dir> [--prev <dir>] [--out <dir>] [--names a,b] [--refs N]
Writes into <out> (default <pilot_dir>/review):
  review_<A>-<B>.png   code | installed | prev | pilot | diagnostic prev | diagnostic pilot  (frame E0, 4x) + numbers
  fins_<A>-<B>.png     code | installed | prev | pilot | alpha prev | alpha pilot + fin / motion numbers
  sheets_<mod>.png     full 6 directions x 4 frames, installed | pilot, 2x on the biome's water colour
  motion_<mod>.gif     row E animated, prev | pilot, 3x
  refs_<k>.png         pilot next to its 3 nearest-shape reference fish, natural + diagnostic (--refs N species)
  codes.txt            code -> species
Diagnostic map: grey = lightness, yellow = brightest 10% of the body, red tint = largest one-colour area, magenta = lone pixel
(differs from all 4 neighbours, which agree), cyan = body edge next to a translucent fin."""
import os, sys, glob, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v4env
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from diaglib import fr0, nat, diag
def font(s, b=False):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf' % ('-Bold' if b else ''), 'C:/Windows/Fonts/arial%s.ttf' % ('bd' if b else '')):
        if os.path.exists(p): return ImageFont.truetype(p, s)
    return ImageFont.load_default()
def find(d, pre, n):
    g = glob.glob(os.path.join(d, f'{pre}_{n}_final_swim_*_4f.png')) or glob.glob(os.path.join(d, f'{pre}_{n}_swim_*_4f.png')); return g[0] if g else None
def up(a, z=4): return Image.fromarray(np.kron(a.astype(np.uint8), np.ones((z, z, 1), np.uint8)))
def amap(fr): a = fr[..., 3]; img = np.stack([a, a, a], -1).astype(np.uint8); img[a == 0] = (60, 0, 0); return img
def page(path, title, sub, heads, rows, lbl=290):
    """rows: [(code, name, [text lines], [PIL images])]"""
    cw = [max(r[3][k].width for r in rows) for k in range(len(heads))]; G = 12
    H = 76 + sum(max(max(im.height for im in r[3]), 40 + 14 * len(r[2])) + G for r in rows) + 10; W = lbl + sum(cw) + G * len(cw)
    pg = Image.new('RGB', (W, H), (16, 16, 16)); d = ImageDraw.Draw(pg)
    d.text((10, 8), title, fill=(255, 255, 255), font=font(16, True)); d.text((10, 32), sub, fill=(200, 200, 200), font=font(12))
    x = lbl
    for k, h in enumerate(heads): d.text((x, 54), h, fill=(255, 220, 120) if 'pilot' in h else (200, 200, 200), font=font(14, True)); x += cw[k] + G
    y = 76
    for c, n, txt, ims in rows:
        rh = max(max(im.height for im in ims), 40 + 14 * len(txt)); d.rectangle([0, y - 4, W, y + rh + 4], fill=(24, 24, 24))
        d.text((10, y + 4), c, fill=(255, 220, 120), font=font(22, True)); d.text((10, y + 32), n, fill=(220, 220, 220), font=font(13))
        for i, t in enumerate(txt): d.text((10, y + 50 + i * 14), t, fill=(160, 160, 160), font=font(11))
        x = lbl
        for k, im in enumerate(ims): pg.paste(im, (x, y + (rh - im.height) // 2)); x += cw[k] + G
        y += rh + G
    pg.save(path)
def main():
    args = sys.argv[1:]; pre, d = args[0], args[1]; opt = lambda k, dv=None: args[args.index(k) + 1] if k in args else dv
    prev = opt('--prev'); out = opt('--out', os.path.join(d, 'review')); os.makedirs(out, exist_ok=True); nref = int(opt('--refs', '6'))
    sp = v4env.species(pre); code = {n: v4env.code(pre, i) for i, (m, n) in enumerate(sp)}
    if opt('--names'): sp = [(m, n) for m, n in sp if n in opt('--names').split(',')]
    sp = [(m, n) for m, n in sp if find(d, pre, n)]
    water = v4env.PREVIEW_BG.get(pre, (60, 60, 60))
    open(os.path.join(out, 'codes.txt'), 'w').write(''.join(f'{code[n]}  {n}  ({m})\n' for m, n in v4env.species(pre)))
    from hlstudy import hl
    import fincheck3 as FC
    R1, R2 = [], []
    for m, n in sp:
        fi, fp = v4env.installed(pre, n), find(d, pre, n); fv = find(prev, pre, n) if prev else fi
        gi, gv, gp = fr0(fi), fr0(fv), fr0(fp); dv, mv = diag(gv); dp, mp = diag(gp); hv, hp = hl(fv), hl(fp)
        R1.append((code[n], n, ['flat %.0f%% -> %.0f%%  (refs <= 26%%)' % (100 * mv['largest'], 100 * mp['largest']),
                                 'light step %.2f -> %.2f  (BW ~0.13)' % (hv['step_ring'], hp['step_ring']),
                                 'light position %.2f -> %.2f  (BW ~0.33, 0 = back)' % (hv['top_t'], hp['top_t'])],
                   [up(nat(gi, water)), up(nat(gv, water)), up(nat(gp, water)), up(dv), up(dp)]))
        sv, sp_ = FC.measure(fv), FC.measure(fp); g = lambda s, a, b: s.get(a, {}).get(b, float('nan'))
        R2.append((code[n], n, ['tail alpha stripes %.2f -> %.2f (refs <= 0.70)' % (g(sv, 'caudal', 'ray_aniso_A'), g(sp_, 'caudal', 'ray_aniso_A')),
                                 'tail colours %s -> %s (refs >= 8)' % (g(sv, 'caudal', 'ncol'), g(sp_, 'caudal', 'ncol')),
                                 'tail pixels changing/frame %.0f%% -> %.0f%% (refs >= 70%%)' % (100 * g(sv, 'caudal', 'm_change'), 100 * g(sp_, 'caudal', 'm_change')),
                                 'dorsal sway %.2f -> %.2f px (refs 0.18-0.42)' % (g(sv, 'dorsal', 'mag'), g(sp_, 'dorsal', 'mag')),
                                 'ventral sway %.2f -> %.2f px (refs 0.25-0.66)' % (g(sv, 'ventral', 'mag'), g(sp_, 'ventral', 'mag'))],
                   [up(nat(gi, water)), up(nat(gv, water)), up(nat(gp, water)), up(amap(gv)), up(amap(gp))]))
    groups = []
    for mod in dict.fromkeys(m for m, n in sp):   # one page per generator module (10-16 species)
        idx = [i for i, (m, n) in enumerate(sp) if m == mod]; groups.append((idx[0], idx[-1] + 1))
    for lo, hi in groups:
        a, b = R1[lo][0], R1[hi - 1][0]
        page(os.path.join(out, f'review_{a}-{b}.png'), f'{pre} - {a}..{b}  (frame E0, 4x)',
             'yellow = brightest 10% | red tint = largest one-colour area | magenta = lone pixel | cyan = body edge next to a translucent fin',
             ['installed', 'prev' if prev else 'installed', 'pilot', 'diagnostic prev', 'diagnostic pilot'], R1[lo:hi])
        page(os.path.join(out, f'fins_{a}-{b}.png'), f'{pre} - fins {a}..{b}  (frame E0, 4x)',
             'alpha: white = opaque, grey = translucent, dark red = empty. Refs: alpha falls smoothly base -> edge, no ray stripes.',
             ['installed', 'prev' if prev else 'installed', 'pilot', 'alpha prev', 'alpha pilot'], R2[lo:hi])
    # full sheets + motion gifs per module
    for mod in sorted(set(m for m, n in sp)):
        names = [n for m, n in sp if m == mod]; cells = []
        for n in names:
            pair = []
            for f in (v4env.installed(pre, n), find(d, pre, n)):
                im = Image.open(f).convert('RGBA'); bg = Image.new('RGBA', im.size, water + (255,)); bg.alpha_composite(im); pair.append(bg.convert('RGB').resize((im.width * 2, im.height * 2), Image.NEAREST))
            c = Image.new('RGB', (pair[0].width + pair[1].width + 40, pair[0].height + 24), (18, 18, 18)); dd = ImageDraw.Draw(c)
            dd.text((4, 4), f'{code[n]} {n}   installed | pilot', fill=(255, 220, 120), font=font(13, True)); c.paste(pair[0], (4, 22)); c.paste(pair[1], (pair[0].width + 30, 22)); cells.append(c)
        W = max(c.width for c in cells); Hh = sum(c.height + 10 for c in cells); pgi = Image.new('RGB', (W, Hh), (10, 10, 10)); y = 0
        for c in cells: pgi.paste(c, (0, y)); y += c.height + 10
        pgi.save(os.path.join(out, f'sheets_{mod}.png'))
        frames = []; S = []
        for n in names:
            a_ = np.array(Image.open(find(prev, pre, n) if prev else v4env.installed(pre, n)).convert('RGBA')); b_ = np.array(Image.open(find(d, pre, n)).convert('RGBA'))
            S.append((n, a_, b_) + v4env.frame_size(find(d, pre, n)))
        cols = 4; cw = max(2 * W_ * 3 + 30 for _, _, _, W_, H_ in S); ch = max(H_ * 3 + 22 for _, _, _, W_, H_ in S); rn = (len(S) + cols - 1) // cols
        for k in range(4):
            cv = Image.new('RGB', (cols * cw, rn * ch), (16, 16, 16)); dd = ImageDraw.Draw(cv)
            for i, (n, a_, b_, W_, H_) in enumerate(S):
                cx, cy = (i % cols) * cw, (i // cols) * ch; dd.text((cx + 4, cy + 2), f'{code[n]} {n}', fill=(255, 220, 120), font=font(12, True))
                for j, s_ in enumerate((a_, b_)):
                    fr = s_[:H_, k * W_:(k + 1) * W_]; cv.paste(up(nat(fr, water), 3), (cx + 4 + j * (W_ * 3 + 8), cy + 18))
            frames.append(cv)
        frames[0].save(os.path.join(out, f'motion_{mod}.gif'), save_all=True, append_images=frames[1:], duration=160, loop=0)
    # nearest-shape references for the first N species (Khoi: compare like with like)
    from battery import feats
    refs = [(p, f) for p, fs in v4env.ref_sheets().items() for f in fs]
    shape = lambda f: (lambda r: np.array([np.log(r['g_BL']) / 0.35, (1 / r['g_aspect']) / 0.08]))(feats(f, 'ac'))
    rs = []
    for p, f in refs:
        try: rs.append((p, f, shape(f)))
        except Exception: pass   # a few tiny / translucent reference sprites have no measurable body
    for k, (m, n) in enumerate(sp[:nref]):
        fp = find(d, pre, n); s0 = shape(fp); nb = sorted(rs, key=lambda r: np.linalg.norm(r[2] - s0))[:3]
        cells = []
        for lab_, f in [(f'{code[n]} pilot', fp)] + [(f'{p} ' + os.path.basename(f).split('_swim')[0], f) for p, f, _ in nb]:
            fr = fr0(f); a_ = up(nat(fr, v4env.PREVIEW_BG.get(lab_[:2], water) if not lab_.startswith(code[n]) else water), 5); b_ = up(diag(fr)[0], 5)
            c = Image.new('RGB', (max(a_.width, b_.width), a_.height + b_.height + 24), (12, 12, 12)); dd = ImageDraw.Draw(c); dd.text((2, 2), lab_, fill=(255, 255, 255), font=font(12, True))
            c.paste(a_, (0, 18)); c.paste(b_, (0, 22 + a_.height)); cells.append(c)
        W = sum(c.width + 8 for c in cells); Hh = max(c.height for c in cells); pgi = Image.new('RGB', (W, Hh), (12, 12, 12)); x = 0
        for c in cells: pgi.paste(c, (x, 0)); x += c.width + 8
        pgi.save(os.path.join(out, f'refs_{code[n]}.png'))
    print('review ->', out, sorted(os.listdir(out)))
if __name__ == '__main__': main()
