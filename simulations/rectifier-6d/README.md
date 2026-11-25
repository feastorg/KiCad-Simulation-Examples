# Rectifier 6D

A three-phase bridge rectifier: six diodes on three phases recharge the output six times per cycle, giving 24 V with very little ripple.

## Circuit

V1, V2 and V3 are 15 V peak, 50 Hz sines, 120° apart, joined at a floating star point N: a three-phase supply. D1 to D3 run from each phase to Out, and D4 to D6 from ground to each phase. C1 = 3300 µF and R1 = 100 Ω load Out. The transient analysis runs for 100 ms.

## What To Look For

- At every moment the highest phase feeds Out through one of D1 to D3, and the lowest phase returns through one of D4 to D6. So the output follows the largest line-to-line voltage, whose peak is 15 V × √3 = 26.0 V.
- Less two diode drops, the output peaks at about 24.3 V.
- The conducting pair changes six times per 20 ms cycle, so the ripple repeats every 3.33 ms and is much smaller than in the single-phase rectifiers.

The simulation gives a peak of 24.33 V and a ripple period of 3.33 ms.

## How To Run

Open `Rectifier-6D.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots the three phase voltages V(Inx) − V(N) and V(Out).

## Try This

- Remove C1: even without a reservoir capacitor, the output never drops below 26.0 V × cos 30° = 22.5 V, less the diode drops.
