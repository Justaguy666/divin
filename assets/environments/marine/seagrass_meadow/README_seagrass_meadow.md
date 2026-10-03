# Seagrass Meadow – asset notes (marine)

Calm, clear shallow bay carpeted with seagrass: green water, silty sand over a dark rhizome mat ("blue carbon"
peat), eelgrass / turtle grass / manatee grass, drift algae, pen shells, whelks, dugong feeding
trails and oxygen bubbles pearling off the leaves. Viewport 384x216, tile 32x32, filter Nearest. Prefix `sg_`.

## tiles/
- ground/sg_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (silty sand with lying dead
    blades and tiny shoots), rows 19-20 = LIP, rows 21-31 = sand front face.
    Middle tile is clean; variants: pen shell sticking out, dugong feeding trail
  - Row 1: TRANSITION — sand -> rhizome peat, roots hanging in (variants: shell bits, buried blades)
  - Row 2: GROUND — dark peat stitched with rhizomes, repeat vertically (variants: thick rhizome, rootlets)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, shell)
- terrain/sg_sand_slopes_atlas.png (8x2) — sand bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/sg_water_surface_4f.png — calm surface line (4 frames); sg_water_tint.png = light green tint

## vegetation/
- plants: eelgrass tall / medium, sg_eelgrass_sway_4f.png (4 frames side by side, same size, base fixed —
  AnimatedSprite), turtle grass, manatee grass, Caulerpa prolifera, drift red algae ball (can also roll along)
- grass: seagrass carpet wide / small (put in front of the base of bigger clumps to blend them into a meadow),
  seagrass tuft small, paddle grass
- roots: rhizome ledge hide (eroded meadow edge, undercut cave for fish, grass on top)

## decoration/
- shells: pen shell (stands in the sand), bay scallop, lightning whelk, queen conch
- misc: variegated urchin, loggerhead sponge, cushion star, sea cucumber
- debris: whelk egg-case string, seagrass wrack (dead blades), drifting blade
- rocks: limestone rubble, sandstone rock

## background/  (384x216, fixed screen)
- far: green gradient with rays and a distant meadow line
- mid: sand mounds covered by a seagrass meadow silhouette
- near: tall dark seagrass on both sides; centre left open for fish

## effects/
- bubbles: sg_oxygen_pearling_6x24_6f.png (tiny bubble stream rising from a sunlit blade — loop it at a few
  blade tips), sizes strip (2,3,4,6 px; frame = size+2), bubble pop (4f)
- ambient: sg_caustics_64_4f.png, sg_light_ray.png
- particles: drifting blade (20x10, 6f), specks (6 flecks), sand puff (28x18, 5f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
