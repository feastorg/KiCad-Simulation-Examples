#!/usr/bin/env python3
"""Simulate examples with ngspice and check the results their expect.toml promises.

For each simulations/<name>/expect.toml, export the schematic's SPICE netlist with
kicad-cli, add the analysis from the example's .wbk workbook and the meas commands from
expect.toml, run ngspice in batch mode, and compare each measurement with its
expected value.

Usage: simulate.py [EXAMPLE ...]   (default: every example that has an expect.toml)
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIM_ROOT = ROOT / "simulations"
# Workbook lines that only mean something inside KiCad's simulator.
GUI_ONLY = (".kicad", ".save", ".probe")


def analysis_command(wbk: Path, analysis: str) -> str:
    tabs = json.loads(wbk.read_text(encoding="utf-8"))["tabs"]
    for tab in tabs:
        if tab["analysis"].lower() == analysis:
            lines = [c for c in tab["commands"] if not c.lower().startswith(GUI_ONLY)]
            if len(lines) != 1:
                raise ValueError(f"{wbk.name}: {analysis} tab has commands {lines}")
            return lines[0]
    raise ValueError(f"{wbk.name}: no {analysis} tab")


def export_netlist(sch: Path, out: Path) -> str:
    subprocess.run(
        ["kicad-cli", "sch", "export", "netlist", "--format", "spice", "-o", str(out), str(sch)],
        check=True,
    )
    lines = out.read_text(encoding="utf-8").splitlines()
    return "\n".join(line for line in lines if line.strip().lower() != ".end")


def run_ngspice(deck: str, workdir: Path) -> str:
    cir = workdir / "deck.cir"
    cir.write_text(deck, encoding="utf-8")
    # Run from the example folder so relative model paths resolve as they do in KiCad.
    proc = subprocess.run(
        ["ngspice", "-b", str(cir)], cwd=workdir, capture_output=True, text=True
    )
    if proc.returncode != 0:
        raise RuntimeError(f"ngspice exited {proc.returncode}:\n{proc.stdout}{proc.stderr}")
    return proc.stdout


def measured(output: str, name: str) -> float:
    match = re.search(rf"^\s*{re.escape(name)}\s*=\s*([-+0-9.eE]+)", output, re.MULTILINE | re.IGNORECASE)
    if not match:
        raise RuntimeError(f"ngspice printed no value for {name}:\n{output}")
    return float(match.group(1))


def simulate(example: Path) -> list[str]:
    spec = tomllib.loads((example / "expect.toml").read_text(encoding="utf-8"))
    (sch,) = example.glob("*.kicad_sch")
    (wbk,) = example.glob("*.wbk")
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        netlist = export_netlist(sch, Path(tmp) / "netlist.cir")
        by_analysis: dict[str, list[dict]] = {}
        for m in spec["measure"]:
            by_analysis.setdefault(m["analysis"].lower(), []).append(m)
        for analysis, measures in by_analysis.items():
            # Measure after the run, in a control block: a .meas dot-line makes ngspice
            # build its save list from the expression, which it misparses for vdb().
            control = [".control", "run", *(f"meas {analysis} {m['name']} {m['meas']}" for m in measures), ".endc"]
            deck = "\n".join([netlist, analysis_command(wbk, analysis), *control, ".end", ""])
            output = run_ngspice(deck, example)
            for m in measures:
                value = measured(output, m["name"])
                expect, rtol = m["expect"], m["rtol"]
                ok = abs(value - expect) <= rtol * abs(expect)
                print(f"{example.name}: {m['name']} = {value:.4g} (expect {expect:.4g} ± {rtol:.0%}) {'ok' if ok else 'FAIL'}")
                if not ok:
                    failures.append(f"{example.name}: {m['name']} = {value:.4g}, expected {expect:.4g} ± {rtol:.0%}")
    return failures


def main(argv: list[str]) -> int:
    missing = [tool for tool in ("kicad-cli", "ngspice") if shutil.which(tool) is None]
    if missing:
        print(f"error: not found on PATH: {', '.join(missing)}", file=sys.stderr)
        return 1
    if argv:
        examples = [SIM_ROOT / name for name in argv]
    else:
        examples = sorted(p.parent for p in SIM_ROOT.glob("*/expect.toml"))
    if not examples:
        print("error: no example has an expect.toml", file=sys.stderr)
        return 1
    failures = [f for ex in examples for f in simulate(ex)]
    for f in failures:
        print(f"error: {f}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
