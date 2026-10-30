# Creature sprite generator (`creature_gen`)

Procedural generator for the creature sheets of the generator-made biomes: clear spring (`cs`), forest stream (`fs`), marsh swamp
(`ms`), billabong (`bb`), bayou (`by`), cold water (`cw`) and underwater cave (`uc`). Every species is code: a body profile, colour
bands, markings and fins (or, for crawlers, hand-placed parts), rendered at 1:1 into the 6-row swimmer / 4-row crawler sheets the
game uses, plus an `.aseprite` per sheet and the Godot scene. The process that uses these tools is in
`.agents/rules/creature_workflow.md` (new biome, new species, fixes, restyles; stage 1 = v3 design, stage 2 = v4 pass); read it
first.

Verified in October 2026: `STYLE=v3` builds reproduce the installed `fs` and `ms` sheets and the `cs` crawlers pixel for pixel,
`v4/build_v4.py cs` the 30 `cs` swimmers, and the v1 biomes (`bb`, `by`, `cw`, `uc`) reproduce except five sheets (see "Known
differences"). **A biome with v4 settings (`v4/params/<pre>.json`; today `cs`) takes its swimmers from `v4/build_v4.py`:
`build.py` alone renders the older v3 look, and `install.py` installs whatever is in the build folder.**

## Setup
- Python 3.10+ with `numpy`, `scipy`, `pillow`, `matplotlib`.
- Run everything from this folder (`cd .agents/tools/creature_gen`); the study scripts can be run from anywhere.
- `paths.py` resolves all locations from this folder - no home-folder paths:
  - `paths.REPO` the Godot project root (override `DIVIN_ROOT`)
  - `paths.WORK` build and pilot output, default `<repo>/_gen` (gitignored; override `DIVIN_GEN_OUT`)
  - `paths.PREVIEW` review images, default `<repo>/Claude outputs` (gitignored; override `DIVIN_PREVIEW`)
- Environment switches used by every script: `PRE=<prefix>` (biome) and `STYLE=v3` (current style; omit = v1, `v2` = v2).

## Files
| File | Role |
|---|---|
| `swim.py` | swimmer renderer: `Fish`, body geometry `Body`, fin builders (`dorsal`, `anal`, `caudal`, `pectoral`, `pelvic`, `adipose`, `barbel`, `tooth`), markings (`m_stripe`, `m_bar`, `m_spot`, `m_dash`, `m_region`, `m_poly`), `sheet(F)`; `STYLE` + `STYLE_V2` / `STYLE_V3`, `use_v2()`, `use_v3(pre)` |
| `biomes.py` | the biome registry - the one list of biomes every script reads: prefix -> category / folder, species modules, water hue and lightness, preview colours; `REFS` = the hand-drawn references (pf, bw, ac) |
| `pal.py` | colour: OKLab helpers (`lab`, `hexl`, `mix`), `ramp()`, per-biome grades `BIOMES`, v3 fit `BG_L` / `BIOMES_V3` / `FIT_V3`, colour families `FAM_CS` / `FAM_FS` / `FAM_MS`, active `FAM` and `fc(key, i=4)` |
| `gait.py` | swimming gaits: profiles `P` and per-biome tables (`CS`, `FS`, `MS`); `lookup(pre, name)` |
| `v3h.py` | v3 design helpers: `m_hline` (straight line), `scatter` (natural spot layout), `fin_spots` (spots on fins), `trail` (trailing fin lobes) |
| `parts.py` | part-built crawlers: `Crawler(name, frame_fn, W, H, prefix)`, `part`, `line`, `ell`, `cap` |
| `recol.py` | `Recolor(src, base, sig=..., tags=...)`: re-maps a kept older drawing (in `old_*/`) onto a ramp / family |
| `tidy.py`, `ase.py` | sheet clean-up; `.aseprite` writer |
| `sp1-4.py`, `fs1-3.py`, `ms1-3.py`, `bb1-3.py`, `by1-3.py`, `cw1-4.py`, `uc1-3.py` | species modules: `ALL` (order), one function per species, `SCENE` (band / speed / fps / crowd per species) |
| `old_fs/`, `old_ms/`, `old_by/` | kept drawings used by `Recolor` (hellbender, mudpuppy, axolotl, newts, turtles, siren, amphiuma) |
| `v3pilot.py` | build species of one module into a pilot folder for review |
| `build.py` | build a module into `paths.out_dir(pre)` (+ `.aseprite`, + preview pngs) - the install hand-off |
| `cs_v4.py` | shortcut for `v4/build_v4.py cs` (clear spring v4 build) |
| `install.py` | copy built sheets into `assets/creatures/<cat>/<biome>/`, remove old-size sheets, write the scenes from `SCENE` + gait fps |
| `mkimport.py` | write Godot `.import` files for new sheet names |
| `check.py` | structural sheet check (size, A=C frames, edge contact, crawler floor contact, specks) |
| `readme_sets.py` | refresh the biome README's roster frame sizes and species-notes table (sheet size + the `# set:` text) |
| `study/` | analysis and preview scripts (next section) |

## Commands (from this folder)
```sh
# pilot: build some or all species of a module for review (folder is inside paths.WORK)
PRE=ms python3 v3pilot.py ms1 out_ms_v3b1 [name,name,...]
python3 check.py "../../../_gen/out_ms_v3b1/*_4f.png"

# install hand-off
STYLE=v3 PRE=ms python3 build.py ms1 /tmp/prev.png        # -> _gen/out_ms (+ .aseprite)
PRE=ms STYLE=v3 python3 install.py ms1                   # sheets + scenes into the project
python3 mkimport.py assets/creatures/freshwater/marsh_swamp
PRE=ms python3 readme_sets.py ms

# biome with v4 settings (cs): build the module, then the v4 swimmers over it, then install
STYLE=v3 PRE=cs python3 build.py sp4 /tmp/prev.png        # crawlers (+ v3 swimmers, overwritten next)
python3 v4/build_v4.py cs                                # all cs swimmers in the v4 look -> _gen/out_cs
PRE=cs STYLE=v3 python3 install.py sp4
```
`install.py` deletes the old sheet when a frame size changes; on a machine where deleting in the project folder needs permission,
grant it first or the install stops half way (re-run it after granting).

## Study scripts (`study/`)
Folder arguments are pilot folders inside `paths.WORK` (or absolute); `pre:folder` measures a folder instead of the installed
sheets; output images go to `paths.PREVIEW`.
| Script | Use |
|---|---|
| `harmony.py <pre> [pre:folder]` | hue share vs the water: neutral (C < 0.025) / analogous (within 45 deg) / discord (45-90) / opposite, chroma vs water. `KIND=crawl` or `KIND='*'` for crawlers |
| `bgfit.py <pre> [pre:folder]` | water L / chroma / hue and the creatures' body, lit and edge lightness relative to it (`KIND` as above) |
| `jag.py <pre> [pre:folder]` | silhouette stair irregularity ("jaggies") per contour step |
| `genpal.py <spec.json>` | water analysis sheet + proposed colour families (prints the family hex tables); specs: `fs_spec.json`, `ms_spec.json` (`cspal.py` for cs) |
| `sceneband.py <pre> <mods> <folder> <names> <out>` | current vs new, each species at the middle of its own swim band over the real background |
| `pilotview.py <pre> <cat/biome> <folder> <r,g,b> <names> <out>` | current / new / value views side by side |
| `pxview.py <folder> <names> <out> [r,g,b]` | first frame of every row at 6x on a water colour (best for pixel review) |
| `floorscene.py <pre> <-,folder> <names> <out>` | crawlers on the real floor, current row above the new row |
| `tankshot.py <pre> <-,folder> <out>` | the whole roster in one tank per folder (`-` = installed) - before / after |
| `metrics.py` | shared OKLab helpers (exec'd by the others) |
The repo-wide audit is `.agents/tools/creature_audit.py <cat>/<biome> --montage _audit/<pre>.png`.

Preview files are cached by name in some viewers: write each review iteration to a new file name (`..._a.png`, `..._b.png`).

## Writing a species (v3)
```python
def rudd():
    # set: deep compressed cyprinid with an upturned mouth / reed-green back over a brass flank / blazing CRIMSON pelvic, anal and tail
    # fins / red-orange eye / dorsal set behind the pelvics
    F = Fish('rudd', 32, 13.6, CARP, bands('G1', 'O1', 'N1', b1=(0.34, 0.38), b2=(0.86, 0.86)), tilt=15, eye=(0.84, 0.42, 2, '#d8501c'))
    B = F.B; F.tone0, F.tspan = -0.1, 4.0; red = FAM['R1'][3]
    F.fins += [caudal(B, 'fork', 8.0, col=red, sig=True), dorsal(B, .32, .48, 5.0, 'tri', col=FAM['G1'][3], lean=0.5),
               anal(B, .14, .32, 4.0, 'tri', col=red, sig=True), pelvic(B, .56, 3.6, col=red, sig=True), pectoral(B, .78, .66, 4.0, col=fc('N1'))]
    return F
```
- `Fish(name, length_px, depth_px, profile, bands, tilt, eye=(u, t, size, iris))`; profile = `[(u, top, bottom), ...]` with
  `u` 0 at the tail tip and 1 at the snout. In markings `u` runs the same way and `t` is 0 at the back, 1 at the belly.
- `bands(back, flank, belly, b1, b2, sig=())`: family keys (`'G1'`) or hex bases; a band list can also be built by hand
  `[(t_end_tail, t_end_head, ramp6), ...]` when a lifted / darker ramp is needed.
- The first comment line must be `# set:` - the species' defining set (shape / fins / barbels / pattern / colour). It is the
  design brief, the review table row and (via `readme_sets.py`) the README text.
- Value: `tone = round(tone0 + v * tspan)` with `v` = 1 at the light centre. `tone0` (default 1.0) moves the whole fish; to darken
  a body but keep its highlight lower `tone0` and raise `tspan` together (e.g. `-0.4, 4.4`). Bottom-band fish over dark water
  lean light with `low(F, k)` (`F.tone0 += k`) in biomes where the low water is darker than the body tones.
- `F.marks += [(fn(x, y, u, t) -> mask, colour_or_int)]`: a hex colour, or an int = body tone shift (-1 darker).
- `F.patches += [(fn(X, Y, U, T) -> mask, ramp6)]`: signature regions (throats, breasts, heads) - clamped to tones 2-3.
- Fin dicts: `col` (light family tone for clear fins, saturated for signature fins with `sig=True`), `band` = list of
  `(fn(X, Y) -> mask, colour)` drawn through the margin, `wave` for ribbon fins, `alpha`.
- Bottom fish that walk the floor: `return _crawlfish(F)` (from `sp4`). Part-built animals: `Crawler` + `parts`. Kept drawings:
  `Recolor('old_xx/<file>_*_4f.png', base, sig=[(hue0, hue1, min_chroma, hex[, max_tone])])` where `base` is a family key, a
  6-tone list (e.g. the family shifted one step darker) or a hex.
- Gaits: add the species to the biome table in `gait.py` (`'name': 'profile'` or `('profile', dict(overrides))`); `build.py` /
  `install.py` apply it when `STYLE` is v2 / v3 and the scene takes its `fps`.

## Adding a biome
0. `biomes.py`: one `GEN` entry - `cat`, `folder` (as in `assets/creatures/<cat>/<folder>`), `modules`, `water` = (OKLab hue,
   mean L) from `study/bgfit.py` (`pal.BG_L` is taken from it), `preview` RGB. Every script finds the biome through it.
1. `pal.BIOMES[pre]` - shadow / cast / highlight / outline / fin tints (copy the closest biome; v3 overrides cast and highlight).
2. `BIOMES_V3[pre] = dict(CAST=..., HIGH=...)` - mid-tone cast (water hue, L ~0.7) and the highlight (water-light white).
3. `FIT_V3[pre] = dict(gap, chroma=1.0, cast=0.08, tone_shift=0.0, hi_mix=0.1, steer=(water_hue, 45, 110)[, outline=(...)])` -
   `steer` keeps any non-family colour out of the 45-110 deg discord band; dark water takes a deeper `outline`
   (ms: `(0.70, 0.64, 0.52, 0.40, 0.36, 0.72)`; v2 default `(0.80, 0.74, 0.62, 0.48, 0.42, 0.80)`).
4. `FAM_<PRE>` - the approved families (6 hex tones each) and `FAM_BY_BIOME[pre]`.
5. `gait.py` - a table for the biome's swimmers and its entry in `TABLE`.

## Known differences (v1 biomes)
`by_hogchoker` (32x26), `cw_atlantic_halibut` (70x34) and `cw_shorthorn_sculpin` (40x20) build 4 px shorter than the installed
sheets, and `uc_blue_devilfish` / `uc_common_octopus` are not produced by the generator (older assets kept, commit `164db77`).
Check these by eye when those biomes are redone.

## v4 pass: shading and fins matched to ac / bw / pf (`v4/`)
Process: `.agents/rules/creature_workflow.md`, stage 2. All v4 switches in `swim.py` are `PILOT_*` environment values that default off,
so `build.py` and every biome without v4 settings render exactly as before.
| Script | Does |
|---|---|
| `v4/tune.py <pre> body|fins [names] [-j N]` | auto-tunes each swimmer against the reference bands (body stage, then fins); `_gen/v4_<pre>/<stage>/` |
| `v4/render.py <pre> <module> <name> <tag>` | one render with the current environment (used by the tuner) |
| `v4/review.py <pre> <dir> [--prev dir] [--refs N]` | review pages with species codes + diagnostic maps, fin / alpha pages, full sheets, motion GIFs, nearest-shape reference sheets |
| `v4/verify.py <pre> <dir> [--prev dir]` | distribution report vs the refs: 110-feature battery, kNN calibration, light rules, light profile, fin rules, fin motion |
| `v4/export_params.py <pre>` | freezes the tuned settings into `v4/params/<pre>.json` |
| `v4/build_v4.py <pre> [names]` | builds the approved sheets (+ .aseprite) into `paths.out_dir(pre)` from `v4/params/<pre>.json`; then `install.py` |
| `v4/lib/` | measurement code: `battery.py` (110 features), `rulecheck*.py` (body bands), `hlstudy.py` (light handling), `finstudy.py` / `rimstudy.py` / `phase.py` / `fincheck3.py` (fins and their motion), `diaglib.py` (diagnostic map) |
| `v4/params/cs.json` | clear spring settings (Oct 2026) |
Run from this folder; `DIVIN_GEN_OUT=<fresh folder>` when old build output cannot be deleted (Claude desktop device shell).
