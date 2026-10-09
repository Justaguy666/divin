---
description: Guidelines for creating and grading pixel art assets for creatures in the game, specifically noting biome-specific styles like Blackwater.
trigger: "When generating, evaluating, or discussing pixel art, spritesheets, or creature assets."
---

# Pixel Art Guidelines for Creatures

These rules define the correct way to draw pixel art assets for creatures in the game. All creatures must adhere to strict rendering, shading, and spritesheet layout rules to ensure visual consistency across the project.

## 1. Spritesheet Layouts and Animation
- **Swimmers (Fish)**: 
  - Layout: 6 rows corresponding to directions (E, SE, SW, W, NW, NE).
  - Animation: 4 frames per row.
  - Tilt: 25° for small fish, 12-20° for deep-bodied/larger fish.
- **Crawlers (Bottom-dwellers, snails)**:
  - Layout: 4 rows (walk_R, walk_L, idle_R, idle_L). For snails, use crawl_R/L.
  - Animation: 4 frames per row.
- **Canvas Sizes**: Match the specific creature's form factor (e.g., small fish `32x28`, discus `44x44`, altum `44x52`, stingray `56x16`, etc.).

## 2. Rendering & Shapes (Core Style)
- **Form Shading**: Light always comes from above. Shade forms rounded per column. Add 1-2 highlight pixels on the back or forehead to define volume.
- **Outlines**: Never use pure black. Outline should be a warm near-black (e.g., `#1a0e0a`), with the lit top edge using a lighter shade (e.g., `#5a3420`).
- **Markings & Fins**: Hand-place markings (do NOT use repeating/random noise). Fins should be soft, showing rays and a smooth gradient.
- **Eyes**: Dark pupil + warm highlight + coloured ring (e.g., red ring for discus/altum).

## 3. Biome-Specific Styling: Blackwater (Prefix `bw_`)
Blackwater biomes represent tannin-rich "tea" water, dim amber light from above, and a dark humus floor. 

**Colour Grading Rule**: Every finished frame for a blackwater creature must receive this specific color grade:
- **Shadows**: Must sink toward warm brown (`#2a1408`). NEVER use navy or black-blue for shadows.
- **Mid-tones**: Must have a light amber cast (`#be7c3c`, ~12% opacity) and be slightly desaturated.
- **Highlights**: Must be warm gold (`#ffe2a0`). NEVER use pure white.
- **Translucent Fins**: Must be tinted amber and slightly more transparent than typical freshwater assets.
- **EXCEPTION (Iridescence)**: Signature neon/iridescent lines or markings (e.g., the cardinal tetra's blue line, discus turquoise lines, apistogramma cheek spangles) are **NOT graded**. They must remain pure and bright so they glow against the dark water.
