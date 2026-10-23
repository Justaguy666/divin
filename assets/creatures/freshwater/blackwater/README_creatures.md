# Blackwater – creature style (prefix `bw_`)

Biome look: tannin "tea" water, dim amber light from above, dark humus floor. Every creature follows these rules so the set reads as one biome.

## Colour grade (BW target; apply once to the finished artwork)
- Shadows sink toward warm brown (#2a1408), never navy/black-blue.
- Mid-tones get a light amber cast (#be7c3c, ~12%) and are slightly desaturated.
- Highlights are warm gold (#ffe2a0), never pure white.
- Translucent fins are tinted amber and a bit more transparent than in planted_freshwater.
- EXCEPTION – signature iridescence (cardinal blue line, discus turquoise lines, apisto cheek spangles)
  is NOT graded: it must glow against the dark water.
- Treat these colours as a palette/lighting guide, not a reason to flatten every species into the same hue.
  Keep natural markings and anatomy readable, preserve the signature colours above, and do not stack older
  gloss, dither, sheen or biome-grade passes.

## Shapes / rendering (same base as planted_freshwater)
- Form shading: light from above, rounded per column, 1–2 highlight pixels on back/forehead.
- Outline: per-pixel dark shade of the adjacent body colour, lightly tinted toward warm #1a0e0a; lit top edge one step lighter (never one fixed near-black).
- Soft fins with rays and gradient; hand-placed markings (no repeating noise).
- Eyes: dark pupil + warm highlight + coloured ring (red for discus/altum).

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 25° (small) / 12–20° (deep-bodied).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames. Snails use crawl_R, crawl_L, idle_R, idle_L.
- Sizes: see the roster below (frame size is also in every file name: `bw_<name>_<swim|crawl>_<W>x<H>_4f.png`).
- Every sheet has a matching `bw_<name>.aseprite` with one tag per row and 0.12 s frames.

## Creating a new BW species

Create each species as an individual Aseprite source, exported sheet and Godot scene. There is no shared
species generator in the current pipeline; the audit tool checks assets but does not draw or integrate them.
Use `.agents/rules/pixel_art_guidelines.md` for shared anatomy and sheet rules; this README adds Blackwater
habitat, palette and scene conventions. Treat the headstander note below as a documented legacy conflict.

### 1. Define the species and its job in the biome
- Keep it appropriate to the Amazon / Rio Negro flooded forest, and check this roster and
  `planted_freshwater` before adding it so the species and its silhouette are not duplicated.
- Decide whether it swims or crawls, its characteristic movement, and its vertical water band or floor role.
  Record a likely frame size from the roster; choose a different size only when the anatomy needs it.
- Write down the features that must survive at native scale (body profile, head or mouth shape, fin placement,
  distinctive colour blocks or markings). Do not start from another species' body and only recolour it.

### 2. Draw the silhouette and BW rendering
- Work at the final frame size, pixel scale 1:1. Make the side-view silhouette read first; place the body,
  fins and key appendages so they remain inside the cell. Leave a safety pixel where the anatomy allows it.
- Build a readable back-to-belly value path. Use the BW warm-brown shadows, amber midtones and warm-gold
  highlights as a restrained lighting ramp. The ~12% amber cast is a starting reference, not a mandatory
  overlay to apply repeatedly. Use an outline related to each adjacent body colour, with a warm tint; avoid
  one flat near-black outline around a multi-coloured animal.
- Keep the species' natural signature colours. The cardinal's blue line, discus' turquoise lines and
  apistogramma cheek spangles stay ungraded; other species may also need an ungraded natural marking to remain
  identifiable. Draw markings as intentional clusters instead of adding uniform noise across the roster.
- Draw fins as attached anatomy: show their silhouette, membrane/rays and transparency where appropriate.
  Use warm tint for translucent fins, but preserve distinctive fin colours. Keep the eye and local contrast
  readable without turning nearby spots or mouth pixels into extra eyes.

### 3. Animate the sheet
- **Swimmer:** make six tagged direction rows in this order: `E`, `SE`, `SW`, `W`, `NW`, `NE`; four frames
  per row. Standard poses are level in `E` and `W`. Use the guideline tilt for anatomy (about 25° for small
  fish, 12–20° for deep-bodied fish, 8–10° for very long fish). The normal cycle is A-B-A-C, 0.12 s per
  source frame: keep the body and its markings fixed, and move only fins / tail tips by a small amount.
- **Crawler:** use `walk_R`, `walk_L`, `idle_R`, `idle_L`, four frames per row. Snails use
  `crawl_R`, `crawl_L`, `idle_R`, `idle_L` (the movement prefix changes; the two idle rows remain).
  Keep the body or shell fixed while legs, claws, antennae or foot move. Put the lowest pixel on `y = H-1`;
  draw each crustacean leg clearly rather than merging them into a dark mass.
- Check the directions after rotation or mirroring: eyes, asymmetrical markings, fin attachments and species
  anatomy must still make sense. Keep animation timing in the Aseprite source at 0.12 s; the Godot scene's
  `animation_fps` is a separate runtime tuning value and may differ.

### 4. Save and export
- Save the editable source as `assets/creatures/freshwater/blackwater/bw_<name>.aseprite`.
- Export `bw_<name>_swim_<W>x<H>_4f.png` or `bw_<name>_crawl_<W>x<H>_4f.png`. Arrange four animation
  frames across each row, with one direction/animation row per line. A swimmer sheet is `4W × 6H`; a
  crawler (including a snail) is `4W × 4H`. For example, `32x28` swimmer frames export to
  `128x168` pixels. Keep the filename, Aseprite canvas/frame size and Godot `frame_size` in agreement.

### 5. Add the Godot scene
- Create `scenes/creatures/freshwater/blackwater/bw_<name>.tscn`, inheriting from
  `scenes/creatures/_shared/swimmer_base.tscn` or `crawler_base.tscn`.
- Set the exported sheet, `frame_size = Vector2i(W, H)`, and tune `animation_fps` and `speed` for the animal.
  Swimmers also need an `area` `Rect2` for their water band; tune `crowd_radius` / `rest_time` for large or
  schooling species. Crawlers may need `move_prefix`, `floor_height`, `move_time`, `idle_time` and bob settings.
- Examples to copy from: `bw_cardinal_tetra.tscn` for a swimmer and `bw_apple_snail.tscn` for a crawler
  with `crawl_` movement animations. If the species should appear in the Blackwater showcase, add its PackedScene resource and an
  instance under `Creatures` in `scenes/aquarium/bw_aquarium.tscn`.

### 6. Review before considering it done
- Run `python .agents/tools/creature_audit.py freshwater/blackwater --montage _audit/bw-new-species.png`.
  Check sheet dimensions, swimmer A=C rows and boundary contact; preview the new species at native scale and
  nearest-neighbour enlargement against the Blackwater background and the accepted PF/BW/AC strips.
- Check the creature in its scene: water band or floor placement, facing, edge clipping, readability against
  the dark water, fin attachment and animation stability. Re-export the PNG after any Aseprite change.
- Treat palette counts, body aspect, blend and other audit hints as review prompts, not an art score. Do not
  use `--strict` as a substitute for visual review.

### Legacy exception to avoid copying
The spotted headstander listed below has a head-down pose baked into its existing sheet. This conflicts with
the current shared rule that new swimmers' E/W rows stay level. Preserve its pose when maintaining that legacy
asset, but do not use it as the template for a new species; correct it in a separate art revision if requested.


## Roster (40 species: 30 swimmers, 10 crawlers)
Theme: Amazon / Rio Negro flooded forest. No species overlap with planted_freshwater.

| Group | Species (frame) |
|---|---|
| Small schooling | cardinal tetra, green neon tetra, black phantom tetra, red phantom tetra, black neon tetra, bleeding heart tetra, penguin tetra, diamond tetra, glass bloodfin, ruby tetra (all 32x28), pygmy cory (32x28, hovers mid-water), marbled hatchetfish 32x28, pencilfish 32x28 |
| Dwarf cichlids / medium | apistogramma 32x28, checkerboard cichlid 40x30, festivum 40x40, eartheater 44x32, dwarf pike cichlid 48x24, spotted headstander 36x28 (legacy: head-down pose baked into sheet), hemiodus 40x20, banded leporinus 48x22, silver dollar 40x40, freshwater needlefish 48x14 (surface) |
| Large / showpiece | discus 44x44, altum angelfish 44x52, uaru 48x44, severum 44x40, leaf fish 36x28 (drifts, speed 5), black ghost knifefish 56x16 (ribbon-fin wave), silver arowana 64x24 (surface band only) |
| Crawlers | sterbai cory 32x18, bumblebee catfish 32x18, banjo catfish 40x14, clown pleco 40x18, spotted raphael 36x18, farlowella 44x12, freshwater stingray 56x16, amazon crab 32x20 (front view, walks sideways), apple snail 32x24, wood shrimp 32x16 |

## Swim layers (scene `area`)
- Surface: arowana (y 0–90), needlefish (y 0–50), glass bloodfin, penguin tetra, hatchetfish.
- Mid water: tetras, festivum, silver dollar, hemiodus, uaru, severum.
- Lower: pygmy cory, leporinus, leaf fish, headstander, checkerboard, eartheater, pike cichlid, knifefish (y 220–320).
- Large fish use a bigger `crowd_radius` (uaru/severum 80, knifefish 90, arowana 110).
