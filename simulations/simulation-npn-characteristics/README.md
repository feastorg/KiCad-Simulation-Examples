# Simulation NPN Characteristics

A nested DC sweep draws a transistor's family of output curves: collector current against voltage, one curve per base current.

## Circuit

V1 drives Q1's collector through R1 = 100 Ω; the emitter is grounded. I1 feeds the base. The workbook runs `.dc V1 0 2 20m I1 0 100u 10u`: V1 from 0 to 2 V, repeated for each base current from 0 to 100 µA in 10 µA steps. Q1 is KiCad's default NPN model, with β = 100.

## What To Look For

- Each curve rises steeply while Q1 is saturated, then flattens once Vce passes a few tenths of a volt: the active region, where Ic depends on Ib and hardly on Vce.
- In the active region Ic = β · Ib, so the curves are evenly spaced 1 mA apart, and the top one, Ib = 100 µA, levels off at 10 mA.
- At V1 = 2 V and 10 mA, R1 drops 1 V, leaving Vce = 1 V. So even the top curve is still in the active region at the end of the sweep.

The simulation's top curve levels off at 10.0 mA.

## How To Run

Open `Simulation-NPN-characteristics.kicad_sch` in KiCad, click **Simulate**, and run the DC tab. It plots I(Q1:c) against V1, one trace per base current.

## Try This

- The default model has no Early effect, so the active-region curves are perfectly flat. Give the model `VAF=50` and they tilt upward.
- Plot V(/Vce) instead of V1 on the x-axis to get the textbook Ic–Vce curves.
