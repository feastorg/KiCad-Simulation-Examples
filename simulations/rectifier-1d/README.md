# Rectifier 1D

A half-wave rectifier: one diode and a reservoir capacitor turn a 15 V sine into DC with 0.8 V of ripple.

## Circuit

V1, a 15 V peak sine at 50 Hz, drives D1 into C1 = 3300 µF and R1 = 100 Ω in parallel. Out is the voltage across them. The transient analysis runs for 100 ms, five cycles.

## What To Look For

- D1 only conducts near the top of each positive half-cycle, when V(In) is above V(Out). It recharges C1 to the input peak less one diode drop: 15 − 0.8 = 14.2 V.
- Between those short pulses, C1 feeds R1 on its own and V(Out) sags. The sag repeats once per cycle, every 20 ms.
- The ripple is roughly I / (f · C) = (14 V / 100 Ω) / (50 Hz · 3300 µF) = 0.85 V. In the simulation it is a little lower, because C1 is also topped up during each pulse.

The simulation gives a 14.2 V peak, 0.78 V of ripple and one recharge every 20.0 ms.

## How To Run

Open `Rectifier-1D.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In) and V(Out).

## Try This

- Remove C1 and V(Out) becomes the bare half-wave: positive humps with gaps between them.
- Compare Rectifier 2D: with two diodes and a centre-tapped source the ripple halves.
