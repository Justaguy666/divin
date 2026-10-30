# Divin - notes for agents

Divin is a 2D pixel-art aquarium game in Godot 4 (GL Compatibility; tank / viewport 640x360, sprites at 1:1). The owner is Khoi;
talk to him in Vietnamese, write repo docs and code comments in English.

## Where to look first
- `.agents/rules/pixel_art_guidelines.md` - creature sheet layout, base rendering style, per-biome art direction.
- `.agents/rules/creature_workflow.md` - the single creature process: new biome, new or replacement species, fixing wrong sheets,
  restyling a biome; stage 1 design (v3 colours, sets, gaits) and stage 2 reference match (v4 shading, fins and fin motion vs
  ac / bw / pf), with Khoi's approval at each step, plus status per biome. Other docs hold facts and point here.
- `.agents/tools/creature_gen/README.md` - the creature sprite generator (species are code) and its analysis / preview scripts.
- `.agents/tools/creature_audit.py` - sheet audit and montage for any biome.
- `assets/creatures/<freshwater|marine|special>/<biome>/README_creatures.md` - each biome's style, roster and species notes;
  sheets and `.aseprite` files live next to it, scenes in `scenes/creatures/<cat>/<biome>/`.
- `assets/environments/<cat>/<biome>/background/{far,mid,near}` - the backgrounds creatures are judged against.

## Working agreements
- Show previews and wait for Khoi's "ok" before installing or replacing assets.
- Commit messages: conventional type (`style(creatures): ...`, `feat(...)`, `fix(...)`), no `Co-Authored-By` or session trailers;
  commit only the folders of the task; never push. Khoi often runs the final check and the commit himself - then hand over the
  message.
- Scratch output goes to gitignored folders: `Claude outputs/` (previews), `_gen/` (generator builds), `_audit/`.
