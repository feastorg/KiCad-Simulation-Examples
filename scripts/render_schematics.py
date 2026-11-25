#!/usr/bin/env python3
"""
Render each simulation's schematic with kicad-cli.

Outputs, per example:
  docs/assets/simulations/<sim>/schematic.pdf   the full sheet, with title block
  docs/assets/simulations/<sim>/schematic.svg   the drawing alone, without the sheet
  docs/assets/simulations/<sim>/schematic.png   that drawing, cropped to its content
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
SIM_ROOT = ROOT / "simulations"
OUT_ROOT = ROOT / "docs" / "assets" / "simulations"

PNG_WIDTH = 2400  # pixels for the whole sheet before cropping
CROP_MARGIN = 40  # pixels of background kept around the drawing
EDGE = 4  # pixels at the image edge ignored when finding the drawing


def die(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def crop_to_content(png: Path) -> None:
    """Crop a rendered sheet to its drawing: whatever differs from the background colour."""
    image = Image.open(png).convert("RGB")
    width, height = image.size
    background = Image.new("RGB", image.size, image.getpixel((width // 2, EDGE)))
    mask = ImageChops.difference(image, background).convert("L").point(lambda v: 255 if v > 24 else 0)
    box = mask.crop((EDGE, EDGE, width - EDGE, height - EDGE)).getbbox()
    if box is None:
        die(f"{png}: the rendered schematic is empty")
    left, top, right, bottom = (box[0] + EDGE, box[1] + EDGE, box[2] + EDGE, box[3] + EDGE)
    image.crop(
        (
            max(left - CROP_MARGIN, 0),
            max(top - CROP_MARGIN, 0),
            min(right + CROP_MARGIN, width),
            min(bottom + CROP_MARGIN, height),
        )
    ).save(png, optimize=True)


def render_sim(sim_dir: Path) -> None:
    (sch,) = sim_dir.glob("*.kicad_sch")
    out_dir = OUT_ROOT / sim_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        ["kicad-cli", "sch", "export", "pdf", "-o", str(out_dir / "schematic.pdf"), str(sch)],
        check=True,
    )
    # kicad-cli names the SVG after the schematic, so export into a temp dir and rename.
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["kicad-cli", "sch", "export", "svg", "--exclude-drawing-sheet", "-o", tmp, str(sch)],
            check=True,
        )
        shutil.move(Path(tmp) / f"{sch.stem}.svg", out_dir / "schematic.svg")

    png = out_dir / "schematic.png"
    subprocess.run(
        ["rsvg-convert", "-w", str(PNG_WIDTH), str(out_dir / "schematic.svg"), "-o", str(png)],
        check=True,
    )
    crop_to_content(png)
    print(f"{sim_dir.name}: schematic.pdf, schematic.svg, schematic.png")


def main() -> None:
    for tool in ("kicad-cli", "rsvg-convert"):
        if shutil.which(tool) is None:
            die(f"missing required tool: {tool}")
    sim_dirs = sorted(p.parent for p in SIM_ROOT.glob("*/*.kicad_sch"))
    if not sim_dirs:
        die("no simulation schematics found")
    for sim_dir in sim_dirs:
        render_sim(sim_dir)


if __name__ == "__main__":
    main()
