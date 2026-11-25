# Rectifier 4D

A bridge rectifier: four diodes give full-wave rectification from a single source, with two diode drops in each path.

## Circuit

V1, a 15 V peak sine at 50 Hz, sits between In1 and In2 and floats: neither side is grounded. D1 and D2 run from In1 and In2 to Out; D3 and D4 run from ground to In1 and In2. C1 = 3300 µF and R1 = 100 Ω load Out. The transient analysis runs for 100 ms.

## What To Look For

- On one half-cycle current flows through D1, the load and D4. On the other it flows through D2, the load and D3. Either way it passes through two diodes.
- So the output peaks at the input peak less two diode drops: about 15 − 2 × 0.8 = 13.4 V.
- C1 is recharged twice per cycle, every 10 ms, so the ripple is about I / (2 · f · C) = (13.2 V / 100 Ω) / (2 · 50 Hz · 3300 µF) = 0.40 V, and a little less in the simulation.

The simulation gives a 13.37 V peak, 0.35 V of ripple, and D1 and D2 conducting 10.0 ms apart.

## How To Run

Open `Rectifier-4D.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots the source voltage V(In1) − V(In2) and V(Out).

## Try This

- Compare Rectifier 2D: the same full-wave ripple, but from a centre-tapped source and with one diode drop instead of two.
- The regulator examples (Rectifier 4D Regulator and its variants) start from this bridge.
