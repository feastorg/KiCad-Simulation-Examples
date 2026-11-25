# Simulation Measurements

KiCad's Measurements pane turns a plot into a number on every run: here the 10–90 % rise time of an RC charge, RC·ln 9 = 219.7 ms.

## Circuit

The RC Charge circuit. V1 steps from 0 to 1 V at t = 2 ns and drives R1 = 1 kΩ in series with C1 = 100 µF to ground; Out is the capacitor voltage. The workbook runs `.tran 1m 500m` and holds one measurement:

```text
trig v(out) val=0.1 rise=1 targ v(out) val=0.9 rise=1
```

## What To Look For

- The entry is an ngspice `meas` command without its first three words, `meas`, the analysis and a result name, which KiCad supplies. `trig` starts the clock when V(Out) first rises through 0.1 V, `targ` stops it when V(Out) first rises through 0.9 V, and the result is the time between them.
- V(Out) = 1 − e^(−t/RC) with RC = 1 kΩ · 100 µF = 0.1 s. It reaches 0.1 V at RC·ln(10/9) = 10.54 ms and 0.9 V at RC·ln 10 = 230.26 ms, so the rise time is RC·ln 9 = 0.1 s × 2.1972 = 219.72 ms, the textbook 2.2·RC.
- `val=0.1` and `val=0.9` are volts, not percentages. They are 10 % and 90 % only because the step is 1 V.
- KiCad gives the result the unit of the signal it measures, so the pane labels this time in volts: read 220mV as 220 ms.
- The same expression also works as a `.meas tran t_rise ...` line in the simulation command, but there it is part of the netlist. Run by ngspice 44.2 in batch mode with a control block, as this repository's checks run, that line made ngspice run the transient a second time and warn `can't parse 'out'`; on `vdb(out)` the warning reads `can't parse 'vd'`. The pane runs its command on the finished simulation.

The simulation gives a rise time of 219.72 ms, from 10.54 ms to 230.26 ms.

## How To Run

Open `Simulation-Measurements.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In) and V(Out), and the Measurements pane shows the rise time. Type another entry into the pane's empty row, or right-click a signal in the signals list and choose one of the **Measure** items.

## Try This

- Double C1 to 200 µF: RC doubles and the simulated rise time is 439.4 ms.
- Set V1's high level to 2 V and keep the entry: 0.1 V and 0.9 V are now 5 % and 45 % of the step, and the simulated time between them is RC·ln(1.9/1.1) = 54.65 ms. Change the levels to `val=0.2` and `val=1.8` to measure 10–90 % again: 219.7 ms.
- Right-click V(Out) and choose **Measure Max**. KiCad adds `MAX V(Out)`, the voltage at 500 ms: 1 − e⁻⁵ = 0.993 V, and the simulation agrees.
