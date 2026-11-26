#!/usr/bin/env python3
"""Tests for simulate.py that need neither kicad-cli nor ngspice: both are stubbed."""

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import simulate  # noqa: E402


def fake_ngspice(args, cwd=None, **kwargs):
    # Write each file the deck's hardcopy commands name, as ngspice would.
    deck = (Path(cwd) / "deck.cir").read_text(encoding="utf-8")
    for svg in re.findall(r"^hardcopy (\S+)", deck, re.MULTILINE):
        (Path(cwd) / svg).write_text("<svg/>", encoding="utf-8")
    return subprocess.CompletedProcess(args, 0, "", "")


class PlotTraces(unittest.TestCase):
    def plot(self, signals: list[str]) -> tuple[list[str], list[Path]]:
        with tempfile.TemporaryDirectory() as tmp:
            example = Path(tmp) / "fixture"
            example.mkdir()
            tab = {"analysis": "TRAN", "commands": [".tran 1u 1m"], "traces": [{"signal": s} for s in signals]}
            (example / "fixture.wbk").write_text(json.dumps({"tabs": [tab]}), encoding="utf-8")
            (example / "fixture.kicad_pro").write_text(json.dumps({"schematic": {}}), encoding="utf-8")
            out = Path(tmp) / "plots"
            with (
                mock.patch.object(simulate, "export_netlist", return_value="* netlist"),
                mock.patch.object(simulate.subprocess, "run", side_effect=fake_ngspice),
            ):
                errors = simulate.plot(example, out)
            return errors, sorted(p.relative_to(out) for p in out.rglob("*.svg"))

    def test_tab_with_no_translatable_trace_fails(self):
        errors, written = self.plot(["P(R1)"])
        self.assertEqual(errors, ["fixture: tran: no ngspice expression for traces ['P(R1)']"])
        self.assertEqual(written, [])

    def test_partly_translated_tab_fails_and_plots_the_rest(self):
        errors, written = self.plot(["V(/out)", "P(R1)"])
        self.assertEqual(errors, ["fixture: tran: no ngspice expression for traces ['P(R1)']"])
        self.assertEqual(written, [Path("fixture/tran.svg")])

    def test_translated_tab_plots(self):
        errors, written = self.plot(["V(/out)", "I(R1)"])
        self.assertEqual(errors, [])
        self.assertEqual(written, [Path("fixture/tran-current.svg"), Path("fixture/tran.svg")])


if __name__ == "__main__":
    unittest.main()
