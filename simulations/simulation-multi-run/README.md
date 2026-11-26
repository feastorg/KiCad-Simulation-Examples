# Simulation Multi Run

A tuner in Multi Run mode reruns the simulation once per value of a part: stepping R1 of the RC Charge circuit from 1 kΩ to 4 kΩ moves the 63 % point from 0.1 s to 0.4 s, t63 = R1 · C1.

## Circuit

The RC Charge circuit. V1 steps from 0 to 1 V at t = 2 ns and drives R1 = 1 kΩ in series with C1 = 100 µF to ground; Out is the capacitor voltage. The workbook runs `.tran 1m 500m`, and a text directive on the schematic, `.options interp`, makes ngspice keep its results on that 1 ms grid: 501 points per run. The schematic holds no sweep: the steps come from a tuner you add in the simulator.

## What To Look For

- V(Out) = 1 − e^(−t/(R1 · C1)), so it reaches 1 − 1/e = 0.632 V at t63 = R1 · C1.
- Multi Run spaces its steps evenly: step i of N is Min + (Max − Min) · i / (N − 1), for i = 0 to N − 1. From 1k to 4k in 4 steps that is 1 kΩ, 2 kΩ, 3 kΩ and 4 kΩ.
- t63 = R1 · 100 µF: 0.1 s, 0.2 s, 0.3 s and 0.4 s.
- Before each run the tuner sends ngspice `alter @R1=<value>` with the value in ohms, `alter @R1=2000` for the second step. The schematic itself is never changed.
- Multi Run needs every run to return the same number of points. KiCad keeps the first run's time axis and drops a later run whose length differs (`recordMultiRunData`, simulator_frame_ui.cpp:3754–3778 at tag 10.0.8). Without `.options interp`, ngspice's own time steps give 539 points at 1 kΩ and 538 at 2 kΩ to 4 kΩ, so only the 1 kΩ curve would be drawn; with it, every step has 501. This comes from KiCad's source and is not yet confirmed in its window.
- The run ends at 500 ms, so the slower curves are still rising there: at 4 kΩ, V(Out) = 1 − e^(−0.5/0.4) = 0.713 V, computed.
- A `.step` line does not do this in KiCad. Its netlist exporter passes a schematic text item to ngspice only when one of its lines starts with a directive on a fixed list (`NETLIST_EXPORTER_SPICE::ReadDirectives`, netlist_exporter_spice.cpp:363–400 at tag 10.0.8), and `.step` is not on it. Given a `.step` line, ngspice 44.2 stops with "unimplemented dot command '.step'".

The simulation gives t63 = 0.1000 s, 0.2000 s, 0.3000 s and 0.4000 s.

## How To Run

Open `Simulation-Multi-run.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(Out) and I(C1) at R1 = 1 kΩ; the plot on this page is that single run.

This example's workbook holds no tuner, so add one:

1. Choose **Add Tuned Value...** and click R1 in the schematic. A tuner for R1 appears beside the plot.
2. Set its mode to **Multi Run**, its maximum to 4k, its minimum to 1k, and **Steps** to 4.
3. Run the transient tab again. Each trace is drawn once per step, labelled `R1=` and the step's value.

## Try This

- Leave the tuner's range as KiCad first sets it, half to twice R1's value, with the default 5 steps: 500, 875, 1250, 1625 and 2000 Ω, and t63 from 50 ms to 200 ms in 37.5 ms steps. The simulation gives 50.00 ms at 500 Ω and 162.5 ms at 1625 Ω.
- Tune C1 instead, from 100u to 400u in 4 steps. t63 depends only on R1 · C1, so V(Out) matches the R1 sweep: the simulation gives 0.2000 s at 200 µF and 0.4000 s at 400 µF. I(C1) does not: its peak at the step, 1 V / R1 = 1 mA, does not depend on C1.
