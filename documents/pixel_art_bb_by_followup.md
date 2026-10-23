# Batch pixel-art refinement: Billabong and Bayou

**Date:** 2026-10-23  
**Branch:** `codex`  
**Scope:** 80 freshwater sheets: 40 Billabong (`bb_`) and 40 Bayou (`by_`), with matching Aseprite sources.

## Result

Applied a restrained, species-local upper-plane highlight to **76/80** assets through Aseprite MCP: 37 Billabong and 39 Bayou. The tool declined four sprites because it could not find a safe body-family patch: `bb_glass_shrimp` has no opaque body anchor, while `bb_notopala_river_snail`, `bb_western_rainbowfish` and `by_mississippi_grass_shrimp` did not produce a sufficiently coherent mask shared by all four frames. These four remain untouched.

The mask selects a small coherent patch in the upper body or shell, just below a darker edge. It preserves the species' dominant hue, limits any hue shift to 2.16° when already near the biome tint, and raises lightness by at most 2.7 HSL points. A coordinate is edited only when its opaque color is identical in all four frames of that tag. No geometry, markings, alpha, or frame metadata is intentionally changed.

| Biome | Edited | Swimmer RGB colours, median | Swimmer L* range, mean | Crawler RGB colours, median | Partial-alpha mean |
|---|---:|---:|---:|---:|---:|
| Billabong | 37/40 | 47.5 → 51.5 | 64.44 → 64.87 | 33.5 → 38.0 | 11.6% → 11.6% |
| Bayou | 39/40 | 45.0 → 50.0 | 68.64 → 69.41 | 28.0 → 32.0 | 14.0% → 14.0% |

Distinct RGB counts and L* ranges are audit descriptors, not quality targets. Their small increases are consistent with adding a local highlight; they do not imply that a sprite is better by score.

## Safeguards and validation

- The batch made **83,448 frame-pixel writes** across the 76 edited sheets. Repeated writes are the same stable coordinates across four frames.
- Compared with the unmodified `HEAD` PNGs, **0 alpha pixels changed** across all 80 sheets. All 80 retained their named dimensions.
- Aseprite MCP preflight checked every edited source: canvas size, 24 swimmer / 16 crawler frames, tag ranges, 120 ms durations, and one flat art layer. The MCP export then refreshed each edited PNG sheet.
- Existing animation diagnostics did not worsen: Billabong remains at 24/180 A=C-mismatched swimmer rows and 60/180 rows touching a cell boundary; Bayou remains at 6/180 and 84/180 respectively. These were present before this batch and the selected RGB-only masks leave them unchanged.
- The advisory count is 23/40 sprites for Billabong and 22/40 for Bayou after the edit. These advisories combine coarse background-distance and hard-edge heuristics; they are review prompts, not failures.

The treatment follows the guideline's per-species palette and marking guidance and its requirement to keep static body pixels consistent across all four frames. It does not force one palette across the roster or apply a biome-wide grade. The four rejected masks are left for manual art review rather than widened automatically.

## Review files

- Before/after contact sheet: [pixel_art_bb_by_preview.png](pixel_art_bb_by_preview.png)
- Per-sprite edit manifest and masks: [pixel_art_bb_by_manifest.json](pixel_art_bb_by_manifest.json)
- Billabong audit montage before / after: [before](billabong_audit_before.png), [after](billabong_audit_after.png)
- Bayou audit montage before / after: [before](bayou_audit_before.png), [after](bayou_audit_after.png)
- Style and structure reference: [pixel_art_guidelines.md](../.agents/rules/pixel_art_guidelines.md)
- Batch runner: [batch_pixel_refine.py](../.agents/tools/batch_pixel_refine.py)
