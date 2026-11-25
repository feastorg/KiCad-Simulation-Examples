# RLC Step Response

A 1 V step into two series RLC circuits: with ζ = 0.158 the capacitor voltage overshoots to 1.605 V and rings at 4970 Hz, and with ζ = 1 it rises to 1 V without overshoot.

## Circuit

V1 is a pulse from 0 to 1 V with a 10 µs delay and 10 ns edges, which stays high for the whole run. It drives two series RLC branches, each with L = 1 mH and C = 1 µF. In the first, R1 = 10 Ω, L1 and C1 to ground, and Out_U is the voltage across C1. In the second, R2 = 63.2 Ω, L2 and C2 to ground, and Out_C is the voltage across C2. The workbook runs `.tran 0.5u 2m`: 2 ms with a 0.5 µs step.

## What To Look For

- Both branches share ω0 = 1/√(LC) = 31.6 krad/s, f0 = ω0/2π = 5033 Hz, as the schematic's note says. The damping ratio is ζ = (R/2)·√(C/L).
- Underdamped, R1 = 10 Ω: ζ = 0.158. Out_U overshoots by exp(−πζ/√(1 − ζ²)) = 60.5 %, a peak of 1.605 V, about 100 µs after the step. It rings at fd = f0·√(1 − ζ²) = 4970 Hz, a period of 201.2 µs, and the ringing dies away with τ = 2L/R1 = 200 µs.
- Critically damped, R2 = 2√(L/C) = 63.2 Ω: ζ = 1. Out_C follows 1 − (1 + ω0·t)·e^(−ω0·t), so it never exceeds 1 V. It reaches 90 % at ω0·t = 3.89: 123 µs after the step, 133 µs from the start.

The simulation gives a peak of 1.605 V on Out_U and a ringing period of 201.2 µs between its rising crossings of 1 V. Out_C tops out at 1.000 V and crosses 0.9 V at 132.9 µs.

## How To Run

Open `RLC-Step-Response.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(Out_U) and V(Out_C).

## Try This

- Change R1 to 1 Ω: ζ falls to 0.0158, the overshoot rises to 95.2 %, and the ringing takes ten times longer to die away, τ = 2 ms.
- Halve both capacitors to 0.5 µF: f0 rises by √2 to 7118 Hz, and critical damping now needs R2 = 2√(L/C) = 89.4 Ω.
