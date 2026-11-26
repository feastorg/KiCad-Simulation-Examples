#!/usr/bin/env python3
"""Simulate examples with ngspice: check their expected results, or plot them.

Each example's SPICE netlist is exported with kicad-cli, and the analysis commands come
from its .wbk workbook, as KiCad's simulator would run them.

Usage:
  simulate.py [EXAMPLE ...]               check each expect.toml (default: every example
                                          that has one)
  simulate.py --plots DIR [EXAMPLE ...]   write DIR/<example>/<analysis>.svg for each
                                          workbook tab (default: every example)
"""

from __future__ import annotations

import argparse
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
# The command entries KiCad 10 writes as a tab's settings. Its workbook loader joins every
# other entry onto the analysis line with no separator (simulator_frame_ui.cpp).
KICAD_ENTRIES = {".kicad adjustpaths", ".kicad esavenone", ".save all", ".probe alli", ".probe allp"}


def workbook_tabs(example: Path) -> list[dict]:
    (wbk,) = example.glob("*.wbk")
    tabs = json.loads(wbk.read_text(encoding="utf-8"))["tabs"]
    for tab in tabs:
        entries = [c for c in tab["commands"] if c not in KICAD_ENTRIES]
        if len(entries) != 1:
            raise ValueError(
                f"{example.name}: the {tab['analysis']} tab has command entries {entries}, "
                f"which KiCad runs as one line: {''.join(c.rstrip() for c in entries)!r}"
            )
    return tabs


def tab_commands(tab: dict) -> list[str]:
    # ".kicad adjustpaths" is KiCad's own directive; .save and .probe are ngspice's.
    return [c for c in tab["commands"] if not c.lower().startswith(".kicad")]


def find_tab(example: Path, analysis: str) -> dict:
    for tab in workbook_tabs(example):
        if tab["analysis"].lower() == analysis:
            return tab
    raise ValueError(f"{example.name}: no {analysis} tab in the workbook")


def export_netlist(example: Path, tmp: Path) -> str:
    (sch,) = example.glob("*.kicad_sch")
    out = tmp / "netlist.cir"
    subprocess.run(
        ["kicad-cli", "sch", "export", "netlist", "--format", "spice", "-o", str(out), str(sch)],
        check=True,
    )
    lines = out.read_text(encoding="utf-8").splitlines()
    return "\n".join(line for line in lines if line.strip().lower() != ".end")


def compatibility_mode(example: Path) -> list[str]:
    """The ngspice behaviour KiCad sets for this project, as ngspice arguments.

    KiCad 10 stores NGSPICE_COMPATIBILITY_MODE as schematic.ngspice.model_mode and
    sends the matching command before loading the netlist (eeschema/sim/ngspice.cpp).
    """
    (pro,) = example.glob("*.kicad_pro")
    settings = json.loads(pro.read_text(encoding="utf-8"))["schematic"].get("ngspice", {})
    mode = settings.get("model_mode", 4)  # KiCad's default is LT_PSPICE
    behaviour = {0: None, 1: None, 2: "psa", 3: "lta", 4: "ltpsa", 5: "hsa"}
    if mode not in behaviour:
        raise ValueError(f"{pro.name}: model_mode {mode} is not supported here")
    return ["-D", f"ngbehavior={behaviour[mode]}"] if behaviour[mode] else []


def run_deck(example: Path, tmp: Path, tab: dict, control: list[str], alter: str | None = None) -> str:
    netlist = export_netlist(example, tmp)
    setup = [f"alter {alter}"] if alter else []
    deck = "\n".join([netlist, *tab_commands(tab), ".control", *setup, "run", *control, ".endc", ".end", ""])
    cir = tmp / "deck.cir"
    cir.write_text(deck, encoding="utf-8")
    # kicad-cli writes model includes as absolute paths, so ngspice can run from the
    # temp directory. Files ngspice writes are named relative to it: in KiCad's
    # compatibility modes ngspice lowercases the deck, paths in commands included.
    proc = subprocess.run(
        ["ngspice", *compatibility_mode(example), "-b", str(cir)],
        cwd=tmp,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"ngspice exited {proc.returncode}:\n{proc.stdout}{proc.stderr}")
    # ngspice reports a refused alter, such as one naming no part in the circuit, only
    # as an error message, and runs on with the schematic's value.
    errors = re.findall(r"^Error.*", proc.stdout + proc.stderr, re.MULTILINE)
    if alter and errors:
        raise RuntimeError(f"ngspice error during run with alter {alter}: {'; '.join(errors)}")
    return proc.stdout


def measured(output: str, name: str) -> float:
    match = re.search(rf"^\s*{re.escape(name)}\s*=\s*([-+0-9.eE]+)", output, re.MULTILINE | re.IGNORECASE)
    if not match:
        raise RuntimeError(f"ngspice printed no value for {name}:\n{output}")
    return float(match.group(1))


def check(example: Path) -> list[str]:
    spec = tomllib.loads((example / "expect.toml").read_text(encoding="utf-8"))
    # One run per analysis and alter: a measure's alter applies to its own run only.
    by_run: dict[tuple[str, str | None], list[dict]] = {}
    for m in spec["measure"]:
        by_run.setdefault((m["analysis"].lower(), m.get("alter")), []).append(m)
    failures = []
    for (analysis, alter), measures in by_run.items():
        # Measure in the control block, after the run: a .meas dot-line makes ngspice
        # build its save list from the expression, which it misparses for vdb().
        # meas has no operating-point, noise, pole-zero or transfer-function form, so for
        # "op", "noise", "pz" and "tf" the entry's meas is an expression, printed after the
        # run as "name = value". After a noise run the current plot holds the totals,
        # onoise_total and inoise_total. A pole is complex and prints as "re,im", so a pz
        # entry measures real(pole(n)) or imag(pole(n)). A tf run's results are scalars
        # such as transfer_function and v1#input_impedance.
        if analysis in ("op", "noise", "pz", "tf"):
            control = [c for m in measures for c in (f"let {m['name']} = {m['meas']}", f"print {m['name']}")]
        else:
            control = [f"meas {analysis} {m['name']} {m['meas']}" for m in measures]
        with tempfile.TemporaryDirectory() as tmp:
            output = run_deck(example, Path(tmp), find_tab(example, analysis), control, alter)
        for m in measures:
            value = measured(output, m["name"])
            expect = m["expect"]
            # rtol is relative to expect; atol is absolute, for values that should be ~0.
            if "atol" in m:
                tol, shown = m["atol"], f"± {m['atol']:g}"
            else:
                tol, shown = m["rtol"] * abs(expect), f"± {m['rtol'] * 100:g}%"
            ok = abs(value - expect) <= tol
            print(f"{example.name}: {m['name']} = {value:.4g} (expect {expect:.4g} {shown}) {'ok' if ok else 'FAIL'}")
            if not ok:
                failures.append(f"{example.name}: {m['name']} = {value:.4g}, expected {expect:.4g} {shown}")
    return failures


def trace_expression(signal: str) -> str | None:
    """Translate a KiCad trace name into an ngspice expression, or None if unknown.

    V(x) stays as it is; I(R1) and I(Q1:c) are the branch currents ngspice records
    under .probe alli; "... (gain)" is the AC magnitude in dB. A noise analysis's
    spectra live in its first plot, noise1; the second holds the totals.
    """
    if signal in ("onoise_spectrum", "inoise_spectrum"):
        return f"noise1.{signal}"
    expr, gain = re.subn(r"\s*\(gain\)$", "", signal)
    expr = re.sub(r"\bI\(([^()]+)\)", lambda m: f"{m.group(1).lower()}#branch", expr)
    term = r"(?:V\([^()]+\)|[\w:]+#branch)"
    if not re.fullmatch(rf"{term}(?:\s*[-+]\s*{term})*", expr):
        return None
    return f"db({expr})" if gain else expr


def plot(example: Path, out_dir: Path) -> list[str]:
    tabs = [t for t in workbook_tabs(example) if t.get("traces")]
    if not tabs:
        print(f"{example.name}: no traces in the workbook, nothing to plot")
        return []
    errors = []
    for tab in tabs:
        analysis = tab["analysis"].lower()
        exprs, skipped = [], []
        for trace in tab["traces"]:
            expr = trace_expression(trace["signal"])
            (exprs if expr else skipped).append(expr or trace["signal"])
        if skipped:
            print(f"{example.name}: {analysis}: skipped traces {skipped}")
        # One axis per plot, so currents (often mA) get their own beside the voltages.
        plots = {
            f"{analysis}.svg": [e for e in exprs if "#branch" not in e],
            f"{analysis}-current.svg": [e for e in exprs if "#branch" in e],
        }
        plots = {svg: group for svg, group in plots.items() if group}
        if not plots:
            continue
        control = ["set hcopydevtype=svg", "set color0=white", "set color1=black"]
        control += [f"hardcopy {svg} {' '.join(group)}" for svg, group in plots.items()]
        with tempfile.TemporaryDirectory() as tmp:
            try:
                run_deck(example, Path(tmp), tab, control)
            except (RuntimeError, subprocess.CalledProcessError) as e:
                errors.append(f"{example.name}: {analysis}: {e}")
                continue
            for svg in plots:
                if not (Path(tmp) / svg).is_file():
                    errors.append(f"{example.name}: {analysis}: ngspice wrote no {svg}")
                    continue
                dest = out_dir / example.name / svg
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(Path(tmp) / svg, dest)
                print(f"{example.name}: {analysis}: {dest.relative_to(out_dir)}")
    return errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--plots", type=Path, metavar="DIR", help="write plots under DIR")
    parser.add_argument("examples", nargs="*", help="example folder names")
    args = parser.parse_args(argv)

    missing = [tool for tool in ("kicad-cli", "ngspice") if shutil.which(tool) is None]
    if missing:
        print(f"error: not found on PATH: {', '.join(missing)}", file=sys.stderr)
        return 1
    if args.examples:
        examples = [SIM_ROOT / name for name in args.examples]
    elif args.plots:
        examples = sorted(p.parent for p in SIM_ROOT.glob("*/*.wbk"))
    else:
        examples = sorted(p.parent for p in SIM_ROOT.glob("*/expect.toml"))
    if not examples:
        print("error: no examples to run", file=sys.stderr)
        return 1

    if args.plots:
        failures = [f for ex in examples for f in plot(ex, args.plots)]
    else:
        failures = [f for ex in examples for f in check(ex)]
    for f in failures:
        print(f"error: {f}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
