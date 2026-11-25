# Simulation DC Sweep

The `.dc` analysis: repeat the operating point while stepping a source, shown on a divider swept from 0 to 12 V.

## Circuit

V1 drives R1 = 100 Ω in series with R2 = 100 Ω to ground; Out is the junction. The workbook runs `.dc V1 0 12 1`: V1 from 0 V to 12 V in 1 V steps.

## What To Look For

- A DC sweep plots each node against the swept source instead of against time.
- Out is always V1 / 2, so the plot is a straight line from 0 V to 6 V: 2 V at V1 = 4 V, 6 V at V1 = 12 V.

The simulation gives 2.000 V and 6.000 V.

## How To Run

Open `Simulation-DC-sweep.kicad_sch` in KiCad, click **Simulate**, and run the DC tab. It plots V(In) and V(Out) against V1.

## Try This

- A divider is linear, so this sweep only draws straight lines. The same analysis traces a diode's or a transistor's curves: see Simulation Diode Characteristics and Simulation NPN Characteristics.
- A `.dc` can also sweep a resistor's value. The KiCad Simulation Commands example shows `.dc R9 10 1k 10`.
