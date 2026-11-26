"""Tests of scripts/simulate.py that need neither kicad-cli nor ngspice."""

import importlib.util
import subprocess
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
spec = importlib.util.spec_from_file_location("simulate", ROOT / "scripts" / "simulate.py")
simulate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(simulate)


class StubbedRun(unittest.TestCase):
    """Run check() and plot() with the netlist export and ngspice stubbed out."""

    def setUp(self):
        self.decks = []

        def run(args, cwd=None, **kwargs):
            self.decks.append((Path(cwd) / "deck.cir").read_text(encoding="utf-8"))
            return subprocess.CompletedProcess(args, 0, "", "")

        self.enterContext(mock.patch.object(simulate, "export_netlist", lambda example, tmp: "* netlist"))
        self.enterContext(mock.patch.object(simulate.subprocess, "run", run))


class WorkbookTabs(StubbedRun):
    def test_every_workbook_has_one_command_entry_per_tab(self):
        for wbk in sorted((ROOT / "simulations").glob("*/*.wbk")):
            with self.subTest(example=wbk.parent.name):
                simulate.workbook_tabs(wbk.parent)

    def test_check_refuses_a_second_command_entry(self):
        with self.assertRaisesRegex(ValueError, r"multi-entry: .*'\.options method=gear'"):
            simulate.check(FIXTURES / "multi-entry")
        self.assertEqual(self.decks, [])

    def test_plot_refuses_a_second_command_entry(self):
        with self.assertRaisesRegex(ValueError, r"multi-entry: .*'\.options method=gear'"):
            simulate.plot(FIXTURES / "multi-entry", Path("unused"))
        self.assertEqual(self.decks, [])


def ngspice_output(name: str) -> str:
    # Captured from ngspice 44.2 in batch mode, -D ngbehavior=ltpsa, on decks built as
    # check() builds them for simulation-pole-zero and simulation-transfer-function.
    return (FIXTURES / "ngspice" / f"{name}.out").read_text(encoding="utf-8")


class Measured(unittest.TestCase):
    def test_reads_a_real_value(self):
        self.assertEqual(simulate.measured(ngspice_output("pz-complex"), "pole_re"), -4.52765e3)

    def test_refuses_a_complex_value(self):
        # pole_2 = -4.52765e+03,4.977370e+03
        with self.assertRaisesRegex(RuntimeError, r"pole_2 is complex"):
            simulate.measured(ngspice_output("pz-complex"), "pole_2")


if __name__ == "__main__":
    unittest.main()
