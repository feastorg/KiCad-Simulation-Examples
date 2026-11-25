#!/usr/bin/env python3
"""Check that every simulation folder has the files the docs build expects."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# User-local KiCad state, or files no simulation uses.
UNTRACKED_SUFFIXES = (".kicad_prl", ".kicad_pcb")


def check_folder(sim_dir: Path) -> list[str]:
    errors = []
    for pattern in ("*.kicad_sch", "*.kicad_pro"):
        found = list(sim_dir.glob(pattern))
        if len(found) != 1:
            errors.append(f"{sim_dir.name}: expected one {pattern}, found {len(found)}")
    readme = sim_dir / "README.md"
    if not readme.is_file():
        errors.append(f"{sim_dir.name}: missing README.md")
    elif not readme.read_text(encoding="utf-8").startswith("# "):
        errors.append(f"{sim_dir.name}: README.md must start with a '# ' title")
    return errors


def tracked_files() -> list[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--", "simulations"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()


def main() -> int:
    tracked = tracked_files()
    # Folders come from git, so local leftovers that are not committed are ignored.
    sim_dirs = sorted({ROOT / Path(p).parent for p in tracked if Path(p).parent != Path("simulations")})
    if not sim_dirs:
        print("error: no simulation folders found", file=sys.stderr)
        return 1
    errors = [e for d in sim_dirs for e in check_folder(d)]
    errors += [f"{p}: must not be tracked" for p in tracked if p.endswith(UNTRACKED_SUFFIXES)]
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    if errors:
        return 1
    print(f"layout ok: {len(sim_dirs)} simulation folders")
    return 0


if __name__ == "__main__":
    sys.exit(main())
