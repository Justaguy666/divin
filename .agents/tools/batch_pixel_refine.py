"""Apply the biome pilot's restrained upper-plane pixel treatment to freshwater sprites.

Dry-run (default):
    python .agents/tools/batch_pixel_refine.py

Apply through the local Aseprite MCP server and refresh PNG sheets:
    python .agents/tools/batch_pixel_refine.py --apply

This is deliberately a selection aid, not a universal color grading pass. It finds
stable, opaque pixels just below a darker back/shell edge, preserves contrasting
markings and only changes coordinates shared by all four frames in a direction.
Sprites without a coherent safe region are reported and left untouched.
"""
from __future__ import annotations

import argparse
import asyncio
import colorsys
from collections import Counter, deque
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_ROOT = ROOT / "assets" / "creatures" / "freshwater"
DOC_ROOT = ROOT / "documents"
BIOMES = ("marsh_swamp", "forest_stream", "clear_spring")
PILOTS = {
    "ms_pumpkinseed_swim_36x32_4f.png",
    "fs_longear_sunfish_swim_38x30_4f.png",
    "cs_pacu_swim_52x38_4f.png",
}
# These narrow silhouettes have one stable, anatomically valid shoulder pixel
# in multiple directions. Keep that persistent pixel instead of rejecting it
# as an isolated sparkle; it is identical through all four animation frames.
ALLOW_STABLE_SINGLETONS = {
    "ms_stone_loach_crawl_42x10_4f.png",
    "cs_tidewater_silverside_swim_34x28_4f.png",
}
BIOME_TINT = {
    "marsh_swamp": (145, 175, 145),
    "forest_stream": (148, 184, 156),
    "clear_spring": (153, 187, 210),
}
BATCH_PRESETS = {
    "bb_by": {
        "biomes": ("billabong", "bayou"),
        "tints": {
            "billabong": (120, 164, 152),
            "bayou": (150, 140, 80),
        },
        "pilots": set(),
    },
}
ARTIFACT_STEM = "pixel_art_batch"
MCP_ROOT = Path(r"E:\GameDev\Tools\aseprite-mcp")
MCP_PYTHON = MCP_ROOT / ".venv" / "Scripts" / "python.exe"
ASEPRITE = Path(r"E:\GameDev\2D\Aseprite\Aseprite.exe")


def luma(c: tuple[int, ...]) -> float:
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def hls(c: tuple[int, ...]) -> tuple[float, float, float]:
    h, l, s = colorsys.rgb_to_hls(*(v / 255 for v in c[:3]))
    return h * 360, l * 100, s * 100


def neighbors(x: int, y: int, width: int, height: int):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx or dy:
                xx, yy = x + dx, y + dy
                if 0 <= xx < width and 0 <= yy < height:
                    yield xx, yy, dx, dy


def frame_info(frame: Image.Image) -> dict[str, Any] | None:
    px = frame.load()
    width, height = frame.size
    opaque = [(x, y) for y in range(height) for x in range(width) if px[x, y][3] >= 160]
    if not opaque:
        return None
    x0 = min(x for x, _ in opaque)
    x1 = max(x for x, _ in opaque)
    y0 = min(y for _, y in opaque)
    y1 = max(y for _, y in opaque)
    bw, bh = x1 - x0 + 1, y1 - y0 + 1
    interior: set[tuple[int, int]] = set()
    for x, y in opaque:
        if px[x, y][3] >= 200 and all(px[xx, yy][3] >= 128 for xx, yy, _, _ in neighbors(x, y, width, height)):
            interior.add((x, y))

    # Read the mode from the upper body plane so a large belly or bright pattern
    # cannot define the color family used for dorsal shading.
    body_colors = []
    for x, y in interior:
        rx = (x - x0) / max(1, bw - 1)
        ry = (y - y0) / max(1, bh - 1)
        color = px[x, y]
        if 0.18 <= rx <= 0.84 and 0.12 <= ry <= 0.68 and 18 <= luma(color) <= 232:
            body_colors.append(color)
    return {
        "px": px,
        "box": (x0, y0, x1, y1),
        "bw": bw,
        "bh": bh,
        "interior": interior,
        "body_colors": body_colors,
        "width": width,
        "height": height,
    }


def dominant_body_color(infos: list[dict[str, Any] | None]) -> tuple[int, ...] | None:
    counts = Counter(color for info in infos if info for color in info["body_colors"])
    return counts.most_common(1)[0][0] if counts else None


def same_family(color: tuple[int, ...], base: tuple[int, ...]) -> bool:
    hue, light, sat = hls(color)
    base_hue, base_light, base_sat = hls(base)
    hue_delta = abs((hue - base_hue + 180) % 360 - 180)
    if base_sat < 18:
        return sat < 30 and abs(light - base_light) < 30
    return hue_delta <= 22 and abs(sat - base_sat) <= 60


def candidate_pixels(info: dict[str, Any], base: tuple[int, ...]) -> set[tuple[int, int]]:
    px = info["px"]
    x0, y0, x1, y1 = info["box"]
    bw, bh = info["bw"], info["bh"]
    width, height = info["width"], info["height"]
    selected: set[tuple[int, int]] = set()
    if bw < 5 or bh < 5:
        return selected

    for x, y in info["interior"]:
        rx = (x - x0) / max(1, bw - 1)
        ry = (y - y0) / max(1, bh - 1)
        if not (0.18 <= rx <= 0.84 and 0.10 <= ry <= 0.60):
            continue
        color = px[x, y]
        if not same_family(color, base) or not (28 <= luma(color) <= 222):
            continue

        # Exclude single-pixel markings and accents whose local color patch does
        # not belong to the dominant body family.
        family_neighbors = sum(
            1 for xx, yy, _, _ in neighbors(x, y, width, height)
            if px[xx, yy][3] >= 128 and same_family(px[xx, yy], base)
        )
        if family_neighbors < 4:
            continue

        # The highlight belongs just beneath a darker back/shell edge.
        if not any(
            dy < 0 and px[xx, yy][3] >= 128 and luma(px[xx, yy]) <= luma(color) - 9
            for xx, yy, _, dy in neighbors(x, y, width, height)
        ):
            continue
        selected.add((x, y))
    return selected


def lift_color(color: tuple[int, ...], biome: str) -> tuple[int, ...]:
    hue, light, sat = colorsys.rgb_to_hls(*(v / 255 for v in color[:3]))
    tint_hue, _, _ = colorsys.rgb_to_hls(*(v / 255 for v in BIOME_TINT[biome]))
    hue_delta = (tint_hue - hue + 0.5) % 1 - 0.5
    # Keep species hue; only use a tiny shift when already close to the biome hue.
    if abs(hue_delta) <= 0.10:
        hue = (hue + max(-0.006, min(0.006, hue_delta))) % 1
    light = min(0.88, light + 0.027)
    sat = min(1.0, sat * 1.015)
    rgb = tuple(max(0, min(255, round(v * 255))) for v in colorsys.hls_to_rgb(hue, light, sat))
    if rgb == color[:3]:
        rgb = tuple(min(255, v + 1) for v in color[:3])
    return (*rgb, color[3])


def components(points: set[tuple[int, int]]):
    remaining = set(points)
    while remaining:
        seed = remaining.pop()
        group = {seed}
        queue = deque([seed])
        while queue:
            x, y = queue.popleft()
            for point in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if point in remaining:
                    remaining.remove(point)
                    group.add(point)
                    queue.append(point)
        yield group


def process_sheet(path: Path, biome: str):
    match = re.search(r"_(\d+)x(\d+)_4f\.png$", path.name)
    if not match:
        raise ValueError(f"Unrecognized spritesheet name: {path.name}")
    cell_w, cell_h = map(int, match.groups())
    crawler = "crawl" in path.name
    rows = 4 if crawler else 6
    source = Image.open(path).convert("RGBA")
    if path.name in PILOTS:
        return source.copy(), {
            "file": path.name,
            "kind": "crawler" if crawler else "swimmer",
            "status": "pilot_existing",
            "changed_pixels": 0,
            "tag_rows": [],
            "groups": [],
        }
    expected_size = (cell_w * 4, cell_h * rows)
    if source.size != expected_size:
        raise ValueError(f"{path.name}: expected sheet {expected_size}, found {source.size}")
    frames = [
        source.crop((col * cell_w, row * cell_h, (col + 1) * cell_w, (row + 1) * cell_h))
        for row in range(rows) for col in range(4)
    ]
    infos = [frame_info(frame) for frame in frames]
    base = dominant_body_color(infos)
    result = source.copy()
    manifest_groups = []
    if base is None:
        return result, {"file": path.name, "kind": "crawler" if crawler else "swimmer", "status": "no_body_color", "changed_pixels": 0, "groups": []}

    out_px = result.load()
    changed_count = 0
    for row in range(rows):
        frame_indices = [row * 4 + col for col in range(4)]
        candidates = [candidate_pixels(infos[index], base) if infos[index] else set() for index in frame_indices]
        stable = set.intersection(*candidates) if candidates else set()
        # Only alter pixels that retain their exact color at the same coordinate
        # across all four frames. This prevents shimmer and preserves A=C parity.
        stable = {
            xy for xy in stable
            if len({infos[index]["px"][xy[0], xy[1]] for index in frame_indices}) == 1
        }
        min_component = 1 if path.name in ALLOW_STABLE_SINGLETONS else 2
        chosen = set().union(*(group for group in components(stable) if len(group) >= min_component))
        edits = []
        for x, y in sorted(chosen, key=lambda q: (q[1], q[0])):
            old = infos[frame_indices[0]]["px"][x, y]
            new = lift_color(old, biome)
            if new != old:
                edits.append([x, y, *old, *new])
                for frame_index in frame_indices:
                    out_px[(frame_index % 4) * cell_w + x, (frame_index // 4) * cell_h + y] = new
        changed_count += 4 * len(edits)
        manifest_groups.append({"tag_row": row, "edits": edits})

    status = "pilot_existing" if path.name in PILOTS else ("ready" if changed_count else "no_safe_region")
    return result, {
        "file": path.name,
        "kind": "crawler" if crawler else "swimmer",
        "status": status,
        "base_rgb": list(base),
        "changed_pixels": changed_count,
        "tag_rows": [len(group["edits"]) for group in manifest_groups],
        "groups": manifest_groups,
    }


def inventory():
    for biome in BIOMES:
        files = sorted((ASSET_ROOT / biome).glob("*_4f.png"))
        if len(files) != 40:
            raise ValueError(f"{biome}: expected 40 sheets, found {len(files)}")
        for png in files:
            if not png.with_name(re.sub(r"_(?:swim|crawl)_\d+x\d+_4f\.png$", ".aseprite", png.name)).exists():
                raise ValueError(f"No matching Aseprite source for {png.name}")
            yield biome, png


def build_plan():
    plans = []
    for biome, path in inventory():
        preview, record = process_sheet(path, biome)
        plans.append({
            "biome": biome,
            "png": str(path),
            "aseprite": str(path.with_name(re.sub(r"_(?:swim|crawl)_\d+x\d+_4f\.png$", ".aseprite", path.name))),
            "before": Image.open(path).convert("RGBA"),
            "preview": preview,
            "record": record,
        })
    return plans


def write_review_artifacts(plans, batch_applied: bool = False):
    DOC_ROOT.mkdir(parents=True, exist_ok=True)
    manifest_path = DOC_ROOT / f"{ARTIFACT_STEM}_manifest.json"
    manifest = [{k: v for k, v in item["record"].items() if k != "groups"} | {"biome": item["biome"]} for item in plans]
    manifest_path.write_text(json.dumps({
        "batch_applied": batch_applied,
        "method": "Aseprite MCP; restrained per-species upper shoulder/shell highlight; stable mask across each four-frame tag; alpha unchanged",
        "biomes": list(BIOMES),
        "sprites": manifest,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    # Two matching 120-sprite panels, first frame only, nearest-neighbor scaled.
    tile_w, tile_h, cols = 120, 82, 10
    rows = (len(plans) + cols - 1) // cols
    font = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 8)
    panel_w, panel_h = cols * tile_w, rows * tile_h
    output = Image.new("RGB", (panel_w * 2, panel_h), (24, 29, 35))
    draw = ImageDraw.Draw(output)
    draw.text((8, 4), "BASELINE", fill=(236, 238, 240), font=font)
    draw.text((panel_w + 8, 4), "AFTER", fill=(236, 238, 240), font=font)
    for i, item in enumerate(plans):
        match = re.search(r"_(\d+)x(\d+)_4f\.png$", item["record"]["file"])
        w, h = map(int, match.groups())
        x = (i % cols) * tile_w
        y = (i // cols) * tile_h + 18
        label = item["record"]["file"].replace("_4f.png", "")
        for panel, image in enumerate((item["before"], item["preview"])):
            frame = image.crop((0, 0, w, h))
            scale = min(3, 102 / w, 55 / h)
            size = (round(w * scale), round(h * scale))
            sprite = frame.resize(size, Image.Resampling.NEAREST)
            bg = Image.new("RGBA", size, (24, 29, 35, 255))
            bg.alpha_composite(sprite)
            px = panel * panel_w + x + (tile_w - size[0]) // 2
            output.paste(bg.convert("RGB"), (px, y))
            if panel == 0:
                draw.text((x + 2, y + 57), label[:24], fill=(230, 235, 238), font=font)
    preview_path = DOC_ROOT / f"{ARTIFACT_STEM}_preview.png"
    output.save(preview_path)
    return manifest_path, preview_path


def make_lua(record: dict[str, Any]) -> str:
    rows = record["tag_rows"]
    frame_count = 4 * len(rows)
    if not frame_count:
        return ""
    entries = []
    for group in record["groups"]:
        row = group["tag_row"]
        for x, y, _or, _og, _ob, alpha, nr, ng, nb, na in group["edits"]:
            entries.append(f"{{{row + 1},{x},{y},{nr},{ng},{nb},{na}}}")
    lua_edits = ",".join(entries)
    return f'''local spr = app.activeSprite
if not spr then print("ERROR:no active sprite") return end
if #spr.frames ~= {frame_count} then print("ERROR:unexpected frame count") return end
local leaves = {{}}
local function walk(layers)
  for _, layer in ipairs(layers) do
    if layer.isGroup then walk(layer.layers) else leaves[#leaves + 1] = layer end
  end
end
walk(spr.layers)
if #leaves ~= 1 then print("ERROR:expected one art layer, found " .. #leaves) return end
local layer = leaves[1]
local edits = {{{lua_edits}}}
local changed = 0
for _, e in ipairs(edits) do
  local row, x, y, r, g, b, a = e[1], e[2], e[3], e[4], e[5], e[6], e[7]
  for col = 0, 3 do
    local cel = layer:cel((row - 1) * 4 + col + 1)
    if not cel then print("ERROR:missing cel") return end
    local lx, ly = x - cel.position.x, y - cel.position.y
    if lx < 0 or ly < 0 or lx >= cel.image.width or ly >= cel.image.height then
      print("ERROR:pixel outside cel") return
    end
    cel.image:putPixel(lx, ly, Color{{r=r, g=g, b=b, a=a}})
    changed = changed + 1
  end
end
spr:saveAs(spr.filename)
print("OK:" .. changed)
'''


async def apply_with_mcp(plans):
    if not MCP_PYTHON.exists() or not ASEPRITE.exists():
        raise RuntimeError("Aseprite MCP or Aseprite executable was not found")
    import sys
    sys.path.insert(0, str(MCP_ROOT))
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    params = StdioServerParameters(
        command=str(MCP_PYTHON),
        args=["-m", "aseprite_mcp"],
        cwd=str(MCP_ROOT),
        env={**os.environ, "ASEPRITE_PATH": str(ASEPRITE)},
    )
    to_apply = [item for item in plans if item["record"]["status"] == "ready"]
    out_dir = Path(tempfile.gettempdir()) / "divin_pixel_batch_exports"
    out_dir.mkdir(parents=True, exist_ok=True)

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            for index, item in enumerate(to_apply, 1):
                record = item["record"]
                match = re.search(r"_(\d+)x(\d+)_4f\.png$", record["file"])
                cell_w, cell_h = map(int, match.groups())
                rows = 4 if record["kind"] == "crawler" else 6
                info_result = await session.call_tool("get_sprite_info", {"filename": item["aseprite"]})
                info_text = "\n".join(c.text for c in info_result.content if c.type == "text")
                try:
                    info = json.loads(info_text)
                except json.JSONDecodeError as exc:
                    raise RuntimeError(f"Could not read Aseprite metadata for {record['file']}: {info_text}") from exc
                expected_ranges = [(row * 4 + 1, row * 4 + 4) for row in range(rows)]
                actual_ranges = [(tag.get("from"), tag.get("to")) for tag in info.get("tags", [])]
                if (info.get("width"), info.get("height"), info.get("frames")) != (cell_w, cell_h, rows * 4):
                    raise RuntimeError(f"Unexpected Aseprite canvas/frame count for {record['file']}: {info}")
                if actual_ranges != expected_ranges:
                    raise RuntimeError(f"Unexpected Aseprite tag ranges for {record['file']}: {actual_ranges}")
                if len(info.get("layers", [])) != 1 or info["layers"][0].get("is_group"):
                    raise RuntimeError(f"Expected one flat art layer for {record['file']}")
                if any(duration != 120 for duration in info.get("durations_ms", [])):
                    raise RuntimeError(f"Unexpected frame duration for {record['file']}")
                result = await session.call_tool("run_lua_script", {"filename": item["aseprite"], "script": make_lua(record)})
                texts = [c.text for c in result.content if c.type == "text"]
                response = "\n".join(texts)
                expected = sum(record["tag_rows"]) * 4
                if result.isError or "ERROR:" in response or f"OK:{expected}" not in response:
                    raise RuntimeError(f"MCP edit failed for {record['file']}: {response}")

                # Export the saved Aseprite source and rebuild the established
                # 4-column PNG sheet from the MCP-rendered frame strip.
                temp_png = out_dir / (Path(item["aseprite"]).stem + ".png")
                exported = await session.call_tool("export_spritesheet", {"filename": item["aseprite"], "output_filename": str(temp_png), "sheet_type": "horizontal", "scale": 1})
                export_text = "\n".join(c.text for c in exported.content if c.type == "text")
                if exported.isError or not temp_png.exists():
                    raise RuntimeError(f"MCP export failed for {record['file']}: {export_text}")
                strip = Image.open(temp_png).convert("RGBA")
                expected_strip = (cell_w * (4 * rows), cell_h)
                if strip.size != expected_strip:
                    raise RuntimeError(f"Unexpected MCP export dimensions for {record['file']}: {strip.size}, expected {expected_strip}")
                sheet = Image.new("RGBA", (cell_w * 4, cell_h * rows))
                for frame in range(4 * rows):
                    sheet.paste(strip.crop((frame * cell_w, 0, (frame + 1) * cell_w, cell_h)), ((frame % 4) * cell_w, (frame // 4) * cell_h))
                sheet.save(item["png"])
                # Keep a copy for visual QA and the summary preview.
                item["preview"] = sheet
                record["status"] = "applied"
                print(f"[{index}/{len(to_apply)}] {record['file']}: {expected} pixels via Aseprite MCP", flush=True)


def print_summary(plans):
    counts = Counter(item["record"]["status"] for item in plans)
    print(f"inventory: {len(plans)} sprites; {dict(counts)}")
    for biome in BIOMES:
        selected = [item["record"] for item in plans if item["biome"] == biome]
        print(biome, "ready", sum(r["status"] == "ready" for r in selected),
              "pilot_existing", sum(r["status"] == "pilot_existing" for r in selected),
              "no_safe_region", sum(r["status"] == "no_safe_region" for r in selected),
              "pixel_changes", sum(r["changed_pixels"] for r in selected))
    for item in plans:
        if item["record"]["status"] == "no_safe_region":
            print("NO SAFE REGION:", item["record"]["file"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", choices=sorted(BATCH_PRESETS), help="select an additional, separately guarded biome batch")
    parser.add_argument("--apply", action="store_true", help="write to Aseprite sources via MCP and refresh PNG sheets")
    args = parser.parse_args()
    global BIOMES, BIOME_TINT, PILOTS, ARTIFACT_STEM
    if args.batch:
        preset = BATCH_PRESETS[args.batch]
        BIOMES = preset["biomes"]
        BIOME_TINT = preset["tints"]
        PILOTS = preset["pilots"]
        ARTIFACT_STEM = f"pixel_art_{args.batch}"
    manifest_path = DOC_ROOT / f"{ARTIFACT_STEM}_manifest.json"
    was_applied = False
    if manifest_path.exists():
        try:
            previous = json.loads(manifest_path.read_text(encoding="utf-8"))
            was_applied = bool(previous.get("batch_applied")) if isinstance(previous, dict) else False
        except (OSError, json.JSONDecodeError):
            was_applied = False
    if args.apply and was_applied:
        raise SystemExit(f"{args.batch or 'default'} batch is already applied; refusing to add a second tonal pass.")
    if was_applied:
        print(f"Batch is already applied. Review {DOC_ROOT / 'pixel_art_batch_preview.png'} and {manifest_path}.")
        return
    plans = build_plan()
    print_summary(plans)
    manifest, preview = write_review_artifacts(plans, batch_applied=was_applied)
    print(f"manifest: {manifest}")
    print(f"preview: {preview}")
    if args.apply:
        asyncio.run(apply_with_mcp(plans))
        manifest, preview = write_review_artifacts(plans, batch_applied=True)
        print("Aseprite MCP batch applied and PNG sheets refreshed")
        print(f"updated preview: {preview}")


if __name__ == "__main__":
    main()
