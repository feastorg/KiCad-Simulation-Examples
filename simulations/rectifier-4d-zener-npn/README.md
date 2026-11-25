# Rectifier 4D Zener NPN

The simplest regulator: a zener sets an NPN emitter follower's base, giving about 4.7 V at 0.58 A.

## Circuit

The front end is Rectifier 4D: V1, a 15 V peak, 50 Hz sine across a four-diode bridge, into C1 = 4700 µF and C2 = 1 µF at /Vin. Rz1 = 470 Ω feeds D5, a 5.6 V BZX84C5V6 zener (vendor model `BZX84C5V6.LIB`), whose voltage /Uz sets the base of Q1, the default NPN. Q1's collector is on /Vin and its emitter at Out, with C3 = 1 µF and Rload1 = 8 Ω. The transient analysis runs for 100 ms.

## What To Look For

- Out sits one base-emitter drop below the zener: Vz − Vbe ≈ 5.6 − 0.94 = 4.66 V. The 0.94 V is the default NPN's Vbe at the load's 0.58 A.
- The zener only has to supply the transistor's base current, about 0.58 A / β, so a small zener can control a large load.
- Nothing corrects for Vbe or for the zener's own slope, so this regulator is simple rather than precise.

The simulation gives 4.66 V at Out while /Vin ripples between 12.3 V and 13.3 V, with D1 and D2 conducting 10 ms apart.

## How To Run

Open `Rectifier-4D-Zener-NPN.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Vin), the source voltage V(In1) − V(In2), and V(Out).

## Try This

- Halve Rload1 to 4 Ω: doubling the current raises Vbe by VT · ln 2 ≈ 18 mV, so the output drops by about that much, plus whatever the zener itself moves.
- Compare Rectifier 4D OPamp NPN, which adds an op-amp to take Vbe out of the result.
