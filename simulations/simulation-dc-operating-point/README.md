# Simulation DC Operating Point

The `.op` analysis: one DC solution of every node voltage and branch current, shown on a 12 V divider.

## Circuit

V1 = 12 V drives R1 = 100 Ω in series with R2 = 100 Ω to ground. Out is the junction. The workbook runs `.op`.

## What To Look For

- An operating point solves the circuit once, with every source at its DC value and every capacitor open and inductor shorted. There is no plot, only numbers.
- Out = 12 V × R2 / (R1 + R2) = 6 V.
- The current through both resistors is 12 V / 200 Ω = 60 mA.

The simulation gives 6.000 V and 60.00 mA.

## How To Run

Open `Simulation-DC-operating-point.kicad_sch` in KiCad, click **Simulate**, and run the operating point tab. KiCad lists the node voltages and branch currents, and can show them on the schematic itself.

## Try This

- Change R2 to 300 Ω: Out moves to 12 V × 300 / 400 = 9 V and the current to 30 mA.
- Every other analysis starts from an operating point, so when a transient or AC result looks wrong, run `.op` first.
