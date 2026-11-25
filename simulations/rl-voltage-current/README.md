# RL Voltage Current

An RL network driven by a sine at its corner frequency, where the resistor and inductor share the input equally and the inductor voltage leads by 45°.

## Circuit

V1, a 1 V sine at 159.2 kHz, drives R1 = 100 Ω in series with L1 = 100 µH to ground. Out is the inductor voltage, and V(In) − V(Out) is the resistor voltage. The transient analysis runs for 50 µs, almost eight cycles.

## What To Look For

- 159.2 kHz is the corner frequency R1/(2π · L1), where the inductor's reactance 2πfL equals R1 = 100 Ω.
- So the resistor and inductor voltages have the same amplitude, 1 V / √2 = 0.707 V each, 90° apart.
- V(Out) leads V(In) by 45°, one eighth of the 6.28 µs period: 0.785 µs. Compare RC Voltage Current, where the capacitor voltage lags instead.

The simulation gives 0.707 V and a lead of 0.785 µs.

## How To Run

Open `RL-Voltage-Current.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(Out) and V(In) − V(Out).

## Try This

- Lower the frequency tenfold and V(Out) shrinks to about 0.1 V: at low frequency the inductor is nearly a short, the opposite of a capacitor.
