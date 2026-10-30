---
description: The single process for generator-made creatures - creating a new biome's creatures, adding or replacing a species, fixing wrong sheets, restyling a whole biome - through stage 1 design (v3: colour fitted to the water, one memorable set per species, gaits) and stage 2 reference match (v4: shading, texture, fins and fin motion measured against ac / bw / pf and auto-tuned per species), with Khoi's review rules, commands, acceptance numbers and pitfalls.
trigger: "When creating creatures for a biome that has none, adding or replacing a species, fixing a creature sheet that looks wrong (shape, colour, shading, fins, motion, size, scene), or regenerating / restyling / re-shading a generator-made biome (cs, fs, ms, bb, by, cw, uc); when Khoi says sprites look flat / glossy / too smooth / unlike ac-bw-pf; or when continuing that work."
---

# Creature workflow (generator-made biomes)

This is the only process document for creature sheets made by `.agents/tools/creature_gen` - new biomes, new species,
fixes and restyles (new biomes are made with the generator too); other files hold facts, not process:
`.agents/rules/pixel_art_guidelines.md` (sheet layout, base style, per-biome art direction), `.agents/tools/creature_gen/README.md`
(every script and the species API), and each biome's `assets/creatures/<cat>/<biome>/README_creatures.md` (its water, colour
families, gaits, species sets and what was done to it). When the process changes, change it here and keep those files pointing here.

Every path below uses the same two stages. Their names match the code and the biome READMEs: **stage 1 = design, "v3"
style** (`STYLE=v3`, species modules, families in `pal.py`, gaits in `gait.py`) and **stage 2 = "v4" pass** (`creature_gen/v4/`,
settings in `v4/params/<pre>.json`). v1 / v2 are the earlier styles still found in the v1 biomes and the READMEs' history notes.

## Status
| Biome | Prefix | Modules | Water L (avg) | Stage 1 (v3) | Stage 2 (v4) |
|---|---|---|---|---|---|
| clear spring | `cs` | `sp1-4` | 0.73 (bright cyan) | done (`b85c8ec`) | 30 swimmers installed Oct 2026 (`v4/params/cs.json`) |
| forest stream | `fs` | `fs1-3` | 0.68 (green) | done (`52f5f5b`) | tools smoke-tested on 2 species |
| marsh swamp | `ms` | `ms1-3` | 0.42 (dark olive) | done (`6d8e370`, incl. the v2 fins / gaits) | - |
| billabong | `bb` | `bb1-3` | 0.39 | v1 - next candidate | - |
| bayou | `by` | `by1-3` | 0.36 | v1 | - |
| cold water | `cw` | `cw1-4` | 0.36 | v1 | - |
| underwater cave | `uc` | `uc1-3` | 0.21 | v1 | - |

`pf`, `bw`, `ac` are the accepted references, drawn by hand - never restyle them (their hand process is in
`blackwater/README_creatures.md`). Every other biome has no creatures yet and is made with path A.

## Working agreements (Khoi)
- Talk to Khoi in Vietnamese (short; numbers with their reference range; say plainly what is still off and what was a
  deliberate choice); repo docs and code comments are English.
- Work in batches of 10-16 species (one module at a time). For every batch send the previews, a short table of each species' set
  and the metrics, then **wait for "ok"** before the next batch. Nothing is installed before every batch of the biome is approved.
- Fix what Khoi points out by re-rendering, not by arguing; when a request has more than one reasonable reading, ask once
  (e.g. brightness level of the colour fit: Khoi picked "C", lighter fish, for cs).
- Kept drawings stay kept (hellbender, mudpuppy, axolotl, newts, turtles, siren, amphiuma): recolour them onto a family only.
- No horizontal mouth line on any creature.
- Commits: conventional type, e.g. `style(creatures): redraw <biome> creatures for smoothness and water fit`, body = what
  changed; **no `Co-Authored-By` / `Claude-Session` trailers**; only the biome's `assets/creatures/<cat>/<biome>` and
  `scenes/creatures/<cat>/<biome>` folders; **never push**. Since ms Khoi runs the final check and the commit himself - finish
  with the install and README and hand over the commit message, unless he asks you to commit.
- Reviews show every species with a code (`CS01`.. in module order, `v4/review.py` writes `codes.txt`); Khoi answers by code.
  Fix only what he names, show before / after next to the same-shape neighbours, and do not install before his "ok".

## Pick the path
| Task | Path |
|---|---|
| A biome with no creatures yet (empty `assets/creatures/<cat>/<biome>/`; the list is `pixel_art_guidelines.md` 3.5) | **A. New biome** |
| One or a few new or replacement species in a biome that has creatures | **B. New species** |
| Sheets that look wrong (Khoi names species or codes, or an audit finds errors) | **C. Fix** |
| A whole biome on an older look (v1: bb, by, cw, uc; or stage 1 done, stage 2 not) | **D. Restyle**: stage 1 from step 0, install, stage 2 |
| `pf`, `bw`, `ac` | references: never restyle; only a defect Khoi names, by hand (C) |

### A. New biome
1. **Roster first, approved by Khoi.** Research the real fauna of the habitat (region, water type, depth range) and propose
   about 40 species: 25-30 swimmers and 10-15 crawlers / bottom animals; small, medium and large frames (`pixel_art_guidelines.md`
   1); every water band used (surface, mid, low, floor); varied body shapes. One row per species: name, swim / crawl, band, one
   line of real anatomy and markings. Wait for "ok" (he may swap species) before writing code.
2. **Register the biome** in `creature_gen/biomes.py` (one `GEN` entry: category, folder, modules, water hue and lightness,
   preview colour) - every script (build, install, README, study, v4) reads it. The prefix and folder are fixed by
   `scenes/aquarium/<pre>_aquarium.tscn` and `assets/environments/<cat>/<biome>/`; enter a rough water value first (the study
   scripts need the entry to find the backgrounds) and replace it with the `study/bgfit.py` measurement in stage 1 step 1.
   Its colour data then goes in `pal.py` and its gaits in `gait.py` (generator README, "Adding a biome").
3. **Stage 1 from step 1** (no baseline: nothing is installed). Modules `<pre>1.py`, `<pre>2.py`, .. one per batch of 10-16
   species, built like `fs1.py`: `import pal; pal.use("<pre>")`, `ALL` (order = review codes), one function per species whose first
   comment is `# set:`, `SCENE` per species (`band`, `speed`, `fps`, `crowd`; crawlers their own keys). Batches and "ok" as usual.
4. **Install** (stage 1 step 5): sheets, `.aseprite`, scenes, `.import` files.
5. **Aquarium.** No tool fills it: add the species to `scenes/aquarium/<pre>_aquarium.tscn` under `Creatures` the way
   `cs_aquarium.tscn` does (one `ext_resource` per species scene; 1-3 instances each - small schooling fish 3, big fish 1 - placed
   inside the species' band, crawlers on the floor) and open it in Godot to look at the tank.
6. **Docs.** `assets/creatures/<cat>/<biome>/README_creatures.md` from the cs / fs / ms template (look, roster, water and colour
   families, rendering, sheets, gaits, species notes, scenes); `readme_sets.py` only refreshes rows that already exist. Add the
   biome to the Status table here and move it from 3.5 to the 3.4 table in `pixel_art_guidelines.md`.
7. **Stage 2** on the installed swimmers, as for any biome.

The commit also takes `scenes/aquarium/<pre>_aquarium.tscn`.

### B. New or replacement species in a biome that has creatures
1. Real anatomy and markings first; check the species notes table so it does not repeat another species' set. For a replacement
   Khoi names the species that goes.
2. Write it in the module of its size / band (`# set:`, family keys, `ALL`, `SCENE`) and add its gait to `gait.py`.
3. Pilot only that species (`PRE=<pre> python3 v3pilot.py <mod> <folder> <name>`), run `check.py`, look at it with
   `sceneband.py` / `pxview.py` next to its same-shape neighbours, send it, wait for "ok".
4. Biome with v4 settings: `tune.py <pre> body <name>`, `tune.py <pre> fins <name>`, `review.py ... --names <name>`, "ok", then
   `export_params.py <pre> <name>` (merges into the params file). Review codes follow `ALL`, so a new species shifts the codes
   after it - say so in the review.
5. Build (`build.py <module>`; a swimmer of a biome with v4 settings then `v4/build_v4.py <pre> <name>` over it), install that
   species only (`install.py <module> <name>`), `mkimport.py`, add its rows to the README roster and species
   notes, run `readme_sets.py`, add it to the aquarium scene.
6. Replacement: remove the old species everywhere - function, `ALL`, `SCENE`, gait entry, params entry, sheet / `.aseprite` /
   `.import`, scene, aquarium instances, README rows (`grep` its name over the repo).

### C. Fix wrong sheets
Start from what Khoi names (species codes or names) or what `creature_audit.py` / `check.py` report. Generator-made sheets are
fixed in their code, never by editing the PNG (the next build would undo it). Find where the problem lives:
| Problem | Fixed in |
|---|---|
| frame size, A = C, edge or floor contact, specks | the species code (tilt, fin sizes) / `tidy.py`; `check.py` confirms |
| anatomy, markings, the species' set | the species function: correct the `# set:` line from the real animal first, then the code |
| colours, fit to the water | the species' band keys / family; a family change in `pal.py` moves every species that uses it - re-check them |
| which fins move, beat | the species' `gait.py` entry (profile, overrides, fps) |
| speed, swim band, crowding | `SCENE` in the module (`install.py` rewrites the scene) |
| shading, texture, fins, fin motion (biomes with v4 settings) | `OV_<name>` + `tune.py` for that species, then `export_params.py <pre> <name>` |
| how many in the tank, where | `scenes/aquarium/<pre>_aquarium.tscn` |

Then pilot that species only, show before / after next to its same-shape neighbours and the refs, wait for "ok", build (as in B5),
install that species only (`install.py <module> <name>`), run `readme_sets.py` if its set or size changed, hand over the commit message.
- v1 biomes (bb, by, cw, uc): build with `STYLE` unset so the species keeps the biome's v1 look; five sheets do not reproduce
  (generator README, "Known differences") - leave those unless the fix is for them.
- `pf`, `bw`, `ac` (hand-drawn references): fix only the defect Khoi names, by hand in the species' `.aseprite`, then re-export
  the sheet; change nothing else (hand process: `blackwater/README_creatures.md`).

## Stage 1 - design (v3): colour fitted to the water, one set per species
Used by A (from step 1), B, D and colour / set fixes in C. "Why" records what the v1 / v2 looks got wrong.

### Why (what the first two styles got wrong)
1. Bodies read as stacked horizontal stripes (three colour bands each with its own tone ramp, 1 px highlight lines, thin
   markings; 2.5 light/dark reversals per column vs 2.0 in bw; ~50 colours per sprite vs 28) and silhouettes had uneven stair runs
   (9-13% of contour steps vs 0% in bw).
2. Fine repeats everywhere: 1 px checker scale rows, checker fin bands, barcode bars, random spot grids.
3. Colours ignored the water. cs/fs fish sat in yellow-olive / ochre - neither the water's hue family nor its complement - so they
   looked pasted on (fs: 45% of fish pixels in that band); ms fish sat at the water's own lightness, hue and 0.8 of its chroma, so
   they melted into it.
4. Many species of a biome shared one template; in bw every species is its own set of body shape + fins + barbels / filaments +
   pattern + colour. Khoi: "mỗi loài ở BW lại là một bộ texture ... rất độc đáo".

### Colour theory
- Measure the water (`study/bgfit.py`, `study/genpal.py`): one hue, its chroma, and L by depth (surface, mid, low, floor).
- **Bracket the water.** Bright water (cs 0.73, fs 0.68): lit parts above the water, body tones below it, outline well below
  (cs +0.13 / -0.21 / -0.36). Dark water (ms 0.42, like bw 0.46 / ac 0.49): the fish read as lighter shapes with a darker outline -
  body a little above the water, lit parts well above, outline below (bw +0.08 / +0.33 / -0.13; ms +0.05 / +0.38 / -0.16). Bottom
  crawlers are measured against the floor water, which is darker than the average.
- **Hue rule** around the water hue: analogous within 45 deg, neutral (chroma < 0.025), complement over 110 deg; the 45-110 deg band
  is discord and is kept off bodies (`pal.ramp` steers stray colours out of it). Complements are muted on bodies and saturated
  only as accents (fins, throats, spots, eyes). What counts as analogous depends on the water: in ms (olive, hue 130) gold and
  brass are analogous and orange is discord; in fs (green, 150) copper is complement and gold is discord.
- **Chroma**: bodies at about half the water's chroma (bw 0.47, ac 0.25); neutrals 30-50% of pixels.
- **Families**: 8-10 families of 6 tones at fixed L, chosen so body tones (0-3) and lit tones (4-5) fall on the right sides of the
  water: cs `0.28 0.40 0.52 0.63 | 0.86 0.95`, fs `0.26 0.37 0.48 0.60 | 0.82 0.93`, ms `0.24 0.36 0.48 0.60 | 0.80 0.92`. Name
  them by role: A/G/O analogous, N neutral, S/M/C/R muted or accent complements, T/B/Y accents. The tables are in `pal.py` and in
  each biome README.
- Highlights become the water's own light (cool water-white), not warm cream; shadows / outline tint stay in the biome's dark.

### Steps
0. **Baseline** (restyle only). `study/tankshot.py <pre> - <pre>_before.png`, `harmony.py <pre>`, `bgfit.py <pre>` (also `KIND=crawl`),
   `jag.py <pre>`; compare with bw / ac / pf (`harmony.py bw` etc.). Write down what is wrong in their terms (lightness, hue band,
   chroma, sameness).
1. **Water analysis + families.** Write `study/<pre>_spec.json` (copy `ms_spec.json`; set `water_hue`, the 6 L tones, families as
   `[name, hue, [6 chromas], role]`), run `genpal.py`, look at the proposal image, adjust. Put the measured water (hue, L)
   in `biomes.py` (`pal.BG_L` reads it) and add `BIOMES_V3`, `FIT_V3`, `FAM_<PRE>`, `FAM_BY_BIOME` in `pal.py`.
2. **Gaits.** If the biome has no table in `gait.py`, add one (profiles: dart, tetra, cruise, power, killi, hover, sail, darter,
   cichlid, sunfish, stalker, gar, deep, catfish, sturgeon, ribbon, riffle, sucker, eel) - match how the real fish swims.
3. **Batch 1 (+ palette).** Write (new biome) or rewrite (restyle) the first module: every species gets a `# set:` comment and family keys. Build
   `PRE=<pre> python3 v3pilot.py <mod> out_<pre>_v3b1`, run `check.py`, `harmony.py <pre>:out_<pre>_v3b1`, `bgfit.py`, `jag.py`,
   and render `sceneband.py`, `pilotview.py`, `pxview.py` (crawlers: `floorscene.py`). Review the images yourself (checklist below),
   iterate, then send the palette proposal + batch previews + set table + metrics. Wait for "ok".
4. **Next batches** the same way (`out_<pre>_v3b2`, `..b3`). A family change made for a later batch must be re-checked on the
   approved batches and reported.
5. **Install** after the last "ok": `STYLE=v3 PRE=<pre> python3 build.py <mod> /tmp/p.png` for every module; compare the
   `_gen/out_<pre>` sheets with the approved pilot folders (must be identical); `install.py` per module; `mkimport.py
   assets/creatures/<cat>/<biome>`; grep the repo for old sheet names that changed size; review the scene diffs (frame size,
   gait fps).
6. **README** of the biome: hand-write the intro "Style v3" paragraph, "Water and colour families (v3)" (measurements, bracketing
   numbers, hue rule, family table with uses, highlight / cast, signature accents, fins), "Rendering (v3)", "Sheets", "Swimming
   gait" (table from `gait.py`); then `PRE=<pre> python3 readme_sets.py <pre>` refreshes frame sizes and the species notes from the
   `# set:` comments. Use the cs / fs / ms READMEs as templates.
7. **Final check**: `creature_audit.py <cat>/<biome> --montage _audit/<pre>-v3.png`, `tankshot.py <pre> <old>,- <pre>_tank.png`
   (old sheets from `git archive HEAD`), metrics on the installed sheets.
8. **Commit message** (or commit, if asked) - see Working agreements.

### Designing a species (rules that came out of the reviews)
- One memorable set per species: body shape + fin set + barbels / filaments + pattern + colour. Two species of one biome may share
  a family, never the whole set. Look at the batch as a group: if three fish in the same band read the same colour, move one.
- At most two or three motifs; nothing finer than 2 px except one defining line; repeats spaced at least their own width; no
  1 px checkers; spots via `scatter()`, not grids; lines along the body straight (`m_hline` / `m_stripe`).
- Signature colours on fins use `sig=True` (denser, rays to the edge) - plain clear fins barely show a band.
- Deep bodies (sunfish, carp) light up over most of their area: lower `tone0` and raise `tspan` to darken them while keeping the
  highlight. Small silver fish: raise the belly with `F.lightc = (0.32, 0.45, 0.9, 1.3)`.
- Light tones of a muted complement family can read salmon / mauve on green water (fs copper, ms mahogany): desaturate its tones
  4-5 or shift the family one step darker (`['#dark', F[0], F[1], F[2], F[3], F[4]]`) for that species.
- Bright accent bellies under belly shading turn mustard: give them a ramp lifted two steps (`ms2.gold_belly`).
- Kept drawings (`Recolor`): if the result is too loud or pale, pass the family shifted one step darker as the base.

### Review checklist (before sending a batch)
- Each fish separates from the water at its own depth (`sceneband`), by value first.
- Nothing in the discord band (harmony 45-90 under ~5%); chroma ratio near half; bracketing numbers on the right sides.
- No pale / washed bodies, no muddy patches, no pink where brown was meant, no body that matches the water L.
- Every `# set:` element is actually visible at 1:1 (`pxview`); if a planned element does not read (e.g. tiny head stripes),
  say so in the message instead of claiming it.
- `check.py` clean (kept drawings may legitimately fail A=C - say which and why).

## Stage 2 - reference match (v4): shading, texture, fins and fin motion
Clear spring went through it in October 2026 (about 15 review rounds; result in its README, "Style v4"). The tools are in
`.agents/tools/creature_gen/v4/` (every script has a docstring).

### Scope and prerequisites
- A biome is ready for v4 when its stage 1 is installed: colour families in `pal.py`, a gait table in `gait.py`, species
  modules with `# set:` comments. v1 biomes (bb, by, cw, uc in Oct 2026) get v3 first.
- v4 covers **swimmers** (`*_swim_*` sheets). Crawlers / part-built animals were not studied; leave them unless Khoi asks.
- v4 never changes anatomy, sets, markings, families or frame sizes. It changes how bodies are lit and textured and how fins
  are drawn and move. Frame sizes stay fixed so file names, `.import` files and scenes stay valid.
- `ac`, `bw`, `pf` are the accepted references - never restyle them. They are three dialects (ac countershaded and muted, bw
  top-lit with a strong hue drift, pf saturated, opaque coloured fin margins); a target must be inside the family, not equal to
  one dialect.

### Khoi's art decisions (binding; they came out of the cs reviews)
1. **No highlight areas.** The refs do not paint a bright spot; light only describes the body's curvature, its pattern and its
   colour. A round / elliptical bright patch on the body is a defect ("vùng sáng chỉ nổi trên 1 vùng").
2. **But do not remove light by capping tones.** Capping every body at a middle tone made bodies flat (one colour over 38% of the
   body vs 14% in the refs). The refs keep their light tones; they climb in small even steps (~0.10 OKLab L, pf 0.085) and sit in the
   upper third of the body, with neighbouring tones mixed in small clusters.
3. **The brightest pixels must not jump out** of their surroundings (bw: the top tenth of the body is ~0.13 above its neighbours;
   our v3 palette jumped 0.23 from tone 3 to tone 4). Study bw when in doubt.
4. **Light near the dorsal fin, not mid-body** for deep-bodied fish (banded cichlid), and the back under the dorsal fin must not be
   darker than the body (pacu, redbreast).
5. **Glossy species can be made matte on request** (pacu, banded cichlid): no light tone above the body tone. A matte body still
   needs visible tone mixing, otherwise it reads as "too smooth" next to its neighbours of the same shape (banded cichlid vs
   chanchito; redbreast) - keep a small but visible step (0.06-0.09) between the mixed tones, not 0.03.
6. **Fins move with their own system per fin kind and per species** (gait), never one motion copied to all fins.
7. Compare like with like: a species against reference fish of the same shape / size; avoid the average trap (see Method).
8. Every review shows previews with **species codes** (CS01..CS30 in module order), the installed sheet, the previous round, the
   pilot and the diagnostic maps; Khoi answers by code.

### Method (why the numbers are trustworthy)
- **Never decide on medians.** A median can sit inside the reference range while every species is clamped to one value (the cs
  bottom outline was identical in all 30 species) or while half the species are off in opposite directions. Report for every
  metric: share of species inside the reference p10-p90 band, which side the misses fall on, the spread ratio (species too alike?)
  and the distance to reference fish of the same shape.
- **Do not trust a rule set you wrote yourself.** The first 17-metric checker said "pilot indistinguishable from a reference
  species" while a 110-feature battery showed flat bodies, missing outline at fin junctions, lone-pixel glints and striped fins.
  One of its rules ("enough 1-pixel marks") had even pushed the tuner to scatter lone pixels. Use the full battery
  (`v4/lib/battery.py`) plus visual checks, and when Khoi points at something, find the metric that captures it before fixing.
- **Calibrate separability.** Each reference dialect is itself ~100% separable from the other two by a classifier, so "the pilot
  is separable" is no failure. Use the kNN distance in feature space next to the dialects' own distances (ac 0.85, bw 0.89,
  pf 1.06 median; cs went 1.10 -> 0.87).
- **Stratify** where colour behaves differently: near-neutral (silver / grey, chroma < 0.04) vs coloured species; bright water
  (L >= 0.6: bodies below the water) vs dark water (bodies a little above it).
- **Rules that hold in all three dialects** are targets (fins: no ray alpha, smooth base-to-edge alpha, 10+ fin colours, fin tone
  close to the body, tail moving as one piece). Dialect-specific traits (pf opaque coloured margins, ac very pale fins) are
  choices, not targets.
- **Look at the pixels.** Every round: the review pages at 4x, the nearest-shape reference sheets, the diagnostic maps, the full
  sheets and the motion GIFs. Metrics find candidates; the image decides.

### Commands (run from `.agents/tools/creature_gen`; outputs go to `<repo>/_gen`, gitignored)
| Step | Command | Notes |
|---|---|---|
| baseline | `python3 v4/verify.py <pre> <dir-with-current-sheets>` | e.g. `assets/creatures/<cat>/<biome>`; refs are cached in `_gen/v4_cache` |
| body stage | `python3 v4/tune.py <pre> body [names] [-j 2]` | `_gen/v4_<pre>/body/`; ~3-7 min per species per core |
| fin stage | `python3 v4/tune.py <pre> fins [names]` | `_gen/v4_<pre>/fins/`; starts from the body result, body knobs frozen |
| review | `python3 v4/review.py <pre> _gen/v4_<pre>/fins --prev <previous round dir> --refs 6` | pages, sheets, GIFs, nearest-shape refs, codes.txt |
| verify | `python3 v4/verify.py <pre> _gen/v4_<pre>/fins --prev <dir>` | report.txt: battery, light, profile, fins, motion |
| fix one species | `OV_<name>="tmx=3;dith=1.3;kt=0.7" python3 v4/tune.py <pre> body <name>` | seeds / fixes knobs before the search (see below) |
| freeze | `python3 v4/export_params.py <pre>` | writes `v4/params/<pre>.json` (exact PILOT_* env per species) |
| build | `DIVIN_GEN_OUT=<fresh dir> STYLE=v3 PRE=<pre> python3 build.py <module> /tmp/p.png`, then `DIVIN_GEN_OUT=<same dir> python3 v4/build_v4.py <pre>` | build.py gives the crawlers, build_v4 overwrites every swimmer with the v4 look (sheet + .aseprite in `paths.out_dir(pre)`); the swimmers must equal the approved pilots pixel for pixel |
| install | `DIVIN_GEN_OUT=<same dir> STYLE=v3 PRE=<pre> python3 install.py <module> [names]` | per module; scenes get the gait fps. Without the build.py step pass the swimmer names (install stops at a species missing from the build folder) |

`python3 cs_v4.py` is the cs shortcut for `v4/build_v4.py cs`.

### Steps
0. **Baseline + study.** `verify.py` on the installed sheets. Read the report as distributions (Method). Make the review package
   of the installed sheets with `--refs` to see each species next to its same-shape references. Write down, in Khoi's terms,
   what is off (flat / glossy / outline / fins / motion) with the numbers.
1. **Body stage** for every swimmer (`tune.py <pre> body`). It tries tone cap 4 and 5, then searches the knobs below against
   `lib/rulecheck4.py` (v2 checks + battery bands + bw light rules). Two cores: ~1.5-2 h for 30 species. Run it in the
   background and keep the session alive (a background process outlives one tool call only in the cloud container, not on the
   device shell).
2. **Fin stage** (`tune.py <pre> fins`) against `lib/fincheck3.py` (rules true in all dialects + motion signature), body knobs
   frozen, body checks kept as a light guard.
3. **Review round** (`review.py` + `verify.py`). Send Khoi: the review pages (installed | previous | pilot | diagnostics), the fin
   pages, the motion GIFs, a short table (reference IQR vs installed vs pilot, share of species inside) and what is still off.
   Ask him to answer by code. Wait for his answer.
4. **Fix by code.** Re-tune or re-render only the named species with `OV_<name>` overrides; check the fix against its
   same-shape neighbours in the biome (CS12 vs CS13) and the references; show the before / after; repeat 3-4.
5. **Install after "ok"**: `export_params.py`, `build.py` + `build_v4.py` into a fresh `DIVIN_GEN_OUT`, compare with the approved pilot sheets
   (pixel-identical, all species), `install.py` per module, check `git status` (only the biome's sheets / .aseprite / README; scenes
   unchanged when frame sizes are unchanged), README "Style v4" + "Shading and fins (v4, swimmers)" sections (template: cs),
   hand over the commit message (no trailers, never push).

### Knobs (per species; `v4/tune.py`, read by `swim.py` / `v4/render.py` as `PILOT_<KEY>_<name>`)
| Knob | Env | What it does | Typical |
|---|---|---|---|
| tmx | TMAX | highest body tone (3 = matte, 4, 5) | 4-5; 3 or 4 + small ts for matte |
| ts | TOPSTEP | lightness step of tones 4 / 5 above tone 3 | 0.11 (0.06-0.09 matte-ish; never < 0.06) |
| t0, spk | TONE0, TSPANK | tone offset / span of the light ramp | -0.9..0.6, 0.7..1.6 |
| lc, kt, kb | LIGHTC | light centre (0 = back) and fall-off up / down | lc 0.26-0.40; kt 0.35-0.8 (higher = darker back) |
| dith | DITH | neighbouring-tone mixing in 2 px clusters, lone pixels removed | 0.7-1.8 |
| tk | TAILK | tail darkening | 0.3-0.55 |
| c0 c1 c4 c5, dkc | CS, DKC | chroma per tone, dark-tone desaturation | |
| rl, rd | ROT | hue drift of lights toward yellow / darks away | 10 / 8 |
| olc, flr | OLC, FLOORREL | outline chroma; bottom outline floor relative to the body | 1.0, 0.42 |
| findl, fcd | FINDL, FINDL_CAUD | fin membrane tone vs body (fins stage), tail offset | -0.05..0.05, +0.06 |
| fgr, fms, fml | FINGRAD, FINMOT, FINMOTL | membrane bands base->edge, soft mottle share / strength | 0.12, 0.35, 0.06 |
| raydl, rmx | RAYDL, RAYMIX | ray colour line (no ray alpha) | 0.04, 0.6 |
| famid | FAMID | fin alpha level (base ~180, edge ~155) | 160-185 |
| ampv, ampd, fbw | AMPV, AMPD, FINBASEW | ventral / dorsal sway, tail swings as one piece | 1.0-1.3, 0.8-1.1, 0.5 |

Fixed switches (all off by default in `swim.py`, so other biomes and `build.py` are untouched): `FIN` / `FIN2` fin models, `FINJ`
outline at fin junctions, `FINLOOP` dorsal / anal loop motion, `STEER` outline hue out of the discord band, pupil / catchlight
tinted by the water (`v4env.eye_colours`).

### Acceptance (targets from ac / bw / pf; `v4/lib/rulecheck4.py`, `v4/lib/fincheck3.py`)
- Body: largest one-colour area <= 26% of the body; top-3 colours <= 59%; brightest 5% at L 0.72-0.91 (matte species excepted);
  no lone pixels (<= 1.4% of the interior); light step around the brightest tenth 0.06-0.18 (bw deep 0.13); light centre 0.26-0.42
  from the back (bw 0.33); back band -0.02..+0.16 vs the body median; profile top->bottom close to the refs
  (-0.06, +0.10, +0.13, +0.05, +0.02, -0.20).
- Outline: outline where the body meets a translucent fin (refs -0.27); bottom outline 0.17-0.40 and varying with the body; pupil
  0.145-0.172; eye contrast <= 0.81.
- Fins: tail alpha stripes (across / along) <= 0.70, alpha falling with distance (<= -0.6), 8+ colours per fin, dorsal / ventral
  tone within -0.06..+0.18 of the body, no linear ray stripes in lightness (<= 1.15).
- Motion: tail swings up-down as one piece (>= 60% of tail pixels change per frame; refs 83-93%); dorsal / ventral move at the
  tips (base change <= 0.36 / 0.45), sway 0.18-0.42 / 0.25-0.66 px, and do not mirror the tail (refs: only 23-47% swing
  symmetric). Ripple fins can show ~0 centroid sway while their margin moves - check the GIF. Frames A = C; no pixel on the
  frame border that the installed sheet does not have.
- Whole sprite: kNN distance to the references not farther than a dialect is from the others (p90 <= ~1.3); features outside the
  reference p10-p90 per species not above the refs' own count (median 15).
- Known open gaps after cs (candidates for the next biome): fewer colours used only once (0.29 vs 0.35-0.61), fin alpha levels
  (15 vs 19-42), the anal fin follows the tail's vertical direction in 54% of species (refs 80-92%).

## Pitfalls met
### Stage 1
- An edit that appends `# comment` inside a replaced line can swallow the rest of the line - check the result.
- Changing a shared helper (`fs3._crayfish`, `fs3.cat_fins`, `sp4._turtle`, `recol.Recolor`) affects other biomes; keep hex
  callers on their old path and rebuild the biomes that import it to confirm nothing else changed.
- The FS family change for batch 2 (R1 light tones) altered four approved batch-1 species slightly - report such knock-on effects.

### Stage 2
- Rebuilding a v4 biome with `build.py` alone puts the v3 look back: `install.py` copies whatever is in the build folder -> always
  run `build_v4.py` after `build.py` for that biome.
- Capping tones to kill a highlight flattens the body -> use small even steps + tone mixing; cap only for an explicit matte request.
- A matte cap at tone 3 leaves no room to mix tones in the upper body -> use tmx 4 with ts 0.06-0.09 and dith 1.5-1.8 (CS12, CS16).
- Too-small light step (0.06) reads smooth at 1:1 -> 0.09 (CS16).
- High kt darkens the band under the dorsal fin (pacu kt 1.2 -> 0.7).
- Whole-fin sway applied to dorsal / anal makes all fins move alike -> only the tail sways whole; dorsal / anal keep the gait.
- Single-pixel "texture glints" are not how the refs texture bodies -> lone pixels are a defect; texture = mixed neighbouring tones.
- Small / tiny reference sprites can fail measurement (ac small_golomyanka) -> scripts skip them.
- A metric that is the "brightest 10%" of the body always marks 10% (or more when colours tie): read the diagnostic maps for shape,
  not area.
- `e_pupil_L` / `eyedom` measure the darkest pixel in the head zone: species with a black eye stripe or mask (blacknose dace,
  pike cichlid) can fail them by design - check the eye in the 4x page instead of chasing the number.
- Signature patterns (lateral silver / pale stripes, red tails with bars) legitimately fail light-step or fin-texture rules; say so in
  the review instead of tuning them away (cs: silverside, ironcolor shiner, piraputanga).

### Tools and environment
- Device shell (Claude desktop bridge): 180 s per call, background processes die when the call ends, files cannot be deleted
  without a permission grant (build / tar fail on overwrite-by-delete) -> run tuning in the cloud container, build on the device
  into a fresh `DIVIN_GEN_OUT`, copy with `cp -f` from a temp folder, never rely on `rm`.
- Re-sending a file to the device under a staged name used before can deliver the old content -> stage every new version under a
  new name and re-check the content on the device (`grep` a value) before building.
- Preview images were cached by file name: write every iteration to a new name.
- Deleting old-size sheets in the project folder can need a permission grant; `install.py` stops half way without it.
- `git` in the project folder: a stale `.git/index.lock` blocks commits; remove it only when no git process runs.
