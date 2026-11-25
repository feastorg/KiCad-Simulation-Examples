# Rectifier 2D

A full-wave rectifier with two diodes and a centre-tapped source: twice the recharges of Rectifier 1D, so half the ripple.

## Circuit

V1 and V2 are 15 V peak, 50 Hz sines, 180° apart, both referenced to ground: the two halves of a centre-tapped transformer winding. Each feeds its own diode, D1 or D2, into C1 = 3300 µF and R1 = 100 Ω in parallel. The transient analysis runs for 100 ms.

## What To Look For

- D1 conducts on V1's positive peaks and D2 on V2's, so C1 is recharged twice per cycle, every 10 ms.
- Each path has one diode drop, so the output still peaks at about 15 − 0.8 = 14.2 V.
- Twice as many recharges halve the ripple, to about I / (2 · f · C) = 0.42 V, and a little less in the simulation.

The simulation gives a 14.2 V peak, 0.38 V of ripple, and D1 and D2 conducting 10.0 ms apart.

## How To Run

Open `Rectifier-2D.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In1), V(In2) and V(Out).

## Try This

- Compare Rectifier 4D, which reaches full-wave with a single source and four diodes, at the cost of a second diode drop.
