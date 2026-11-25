# Simulation Transient Sine

The `.tran` analysis with a sine source: a 50 Hz sine through an RC low-pass whose corner is 15.9 Hz, attenuated and delayed.

## Circuit

V1 is a 1 V sine at 50 Hz. It drives R1 = 1 kΩ in series with C1 = 10 µF to ground; Out is the capacitor voltage. The workbook runs `.tran 100u 100m`, five cycles.

## What To Look For

- The corner is fc = 1/(2π · R1 · C1) = 15.9 Hz, so 50 Hz is about three times above it.
- Gain: 1/√(1 + (50/15.9)²) = 0.303, so V(Out) peaks at 0.303 V once the start-up transient has died away.
- Phase: −atan(50/15.9) = −72.3°, a lag of 72.3/360 × 20 ms = 4.02 ms.

The simulation gives 0.304 V and a lag of 4.02 ms.

## How To Run

Open `Simulation-Transient-sine.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In) and V(Out).

## Try This

- The first cycle is lopsided because C1 starts empty. A transient shows the start-up, and an AC sweep shows only the steady state: compare with Simulation AC Sweep.
- Set the frequency to 15.9 Hz and V(Out) settles at 0.707 V with a 45° lag.
