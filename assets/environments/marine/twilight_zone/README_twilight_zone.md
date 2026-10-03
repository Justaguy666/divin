# Twilight Zone – asset notes (marine)

The mesopelagic "twilight zone" (~200-1000 m): OPEN WATER — no sea floor, no walls. The last dim blue light fades
from above into black below, marine snow drifts down constantly, and bioluminescence flashes in the dark. The
deep scattering layer (a haze of countless tiny animals) hangs as a band across the scene.
Viewport 384x216, filter Nearest. Prefix `tz_`.
(No floor tiles on purpose. Fish, jellies, siphonophores etc. are left for the game's own creatures — everything
here is non-living or light/particles.)

## tiles/
- none — this biome has no floor, slopes or visible surface.

## decoration/drifting/  (place anywhere in the water; let them sink / drift slowly)
- tz_marine_snow_clump_large / small — fluffy clumps of marine snow (sink slowly, drift sideways)
- tz_larvacean_house_large / small — abandoned larvacean mucus "houses": big translucent balloons carrying snow
- tz_mucus_strand — long faint mucus string sinking vertically

## background/  (384x216, fixed screen)
- far: dim indigo at the top fading to black at the bottom, distant bioluminescent specks (more deeper down)
- mid: deep scattering layer — a hazy horizontal band with glowing specks (alpha)
- near: a few large out-of-focus snow flakes close to the camera (alpha — put it above fish for depth)

## effects/
- ambient: tz_downwelling_glow.png (384x216 — the last sunlight from above, put over far/mid),
  tz_darkness_overlay.png (384x216 — fades to black toward the bottom/sides, above fish),
  tz_scattering_layer_band_64x24.png (tileable haze band — scroll slowly / bob it for a living layer)
- particles: biolum flash (12x12, 6f), glow burst (32x32, 8f — bigger ring of sparks), glow wake
  (56x10, 6f — trail behind a passing fish), marine snow (7 flecks — use LOTS, all sinking slowly)
- bubbles: tiny bubbles (2,3,4 px) — rare at this depth
