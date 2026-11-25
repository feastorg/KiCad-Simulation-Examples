# RC Voltage Current

An RC network driven by a sine at its corner frequency, where the resistor and capacitor share the input equally and the capacitor voltage lags by 45°.

## Circuit

V1, a 1 V sine at 159.2 Hz, drives R1 = 1 kΩ in series with C1 = 1 µF to ground. Out is the capacitor voltage, and V(In) − V(Out) is the resistor voltage. The transient analysis runs for 30 ms, almost five cycles.

## What To Look For

- 159.2 Hz is the corner frequency 1/(2π · R1 · C1), where the capacitor's reactance 1/(2πfC) equals R1 = 1 kΩ.
- So the resistor and capacitor voltages have the same amplitude, 1 V / √2 = 0.707 V each. They are 90° apart, which is why they don't add up to 1 V at any one instant.
- V(Out) lags V(In) by 45°, one eighth of the 6.28 ms period: 0.785 ms.

The simulation gives 0.707 V and a lag of 0.785 ms.

## How To Run

Open `RC-Voltage-Current.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(Out) and V(In) − V(Out).

## Try This

- The resistor voltage is proportional to the current, so V(In) − V(Out) shows the current leading the capacitor voltage by 90°.
- Raise the frequency tenfold and V(Out) shrinks to about 0.1 V with a lag close to 90°: the capacitor is now nearly a short.
