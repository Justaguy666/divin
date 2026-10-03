# Deep Water – asset notes (marine)

Deep-sea floor (bathyal / abyssal): near-black water with no sunlight, bioluminescence, constant marine snow,
grey ooze with manganese nodules over pillow-lava basalt, cold-water corals, glass sponges, sea lilies,
and a whale fall. Viewport 384x216, tile 32x32, filter Nearest. Prefix `dw_` = deep water.

## tiles/
- ground/dw_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (grey ooze, manganese
    nodules, faint animal tracks) seen slightly from above, rows 19-20 = LIP, rows 21-31 = ooze front face.
    Middle tile is clean; variants: xenophyophore, glowing brittle star
  - Row 1: TRANSITION — ooze -> pillow basalt (variants: nodule layer, sediment layers)
  - Row 2: GROUND — pillow-lava basalt, repeat vertically (variants: glowing mineral vein, vesicles)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: buried bone, nodule)
- terrain/dw_ooze_slopes_atlas.png (8x2) — ooze mound one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/dw_water_surface_4f.png — very dim surface line (only if you show the top at all);
  dw_water_tint.png = heavy dark-blue tint

## vegetation/
- plants: glowing sea pen (blue-tipped), tube anemone (cerianthid, pink glow tips), sea lily (stalked crinoid)
- (grass/ and roots/: none for this biome)

## decoration/
- coral: Lophelia (white cold-water reef coral), black coral
- rocks: pillow basalt L/M/S, manganese nodules
- debris: whale vertebra
- misc: whale skull (fish hide inside), whale-fall ribs, glass sponge tall/short (Venus' flower basket),
  xenophyophore, glowing brittle star, deep-sea red star

## background/  (384x216, fixed screen)
- far: blue-black gradient, abyssal hills, faint bioluminescent pinpricks
- mid: basalt mounds + sponge/sea-pen silhouettes with a few glowing tips
- near: dark rocks framing both sides with glowing specks; centre left open for fish

## effects/
- ambient: dw_darkness_overlay.png (384x216 vignette, put ABOVE fish/props — keeps the centre visible and the
  edges/top pitch dark), glow halos cyan/blue/pink (48x48 — put behind glowing props or a lantern fish)
- particles: bioluminescent pulse (12x12, 6f — spawn when fish swim through), marine snow (6 flecks, use a lot,
  drifting down slowly), silt puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6 px; frame = size+2) — rare down here

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
