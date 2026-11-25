# RC Discharge

A 100 µF capacitor charged to 100 V discharges through 1 kΩ, showing the exponential decay and the time constant τ = RC.

## Circuit

V1 holds 100 V before t = 0, so C1 = 100 µF starts fully charged, then steps to 0 V. C1 discharges through R1 = 1 kΩ into V1. Out is the capacitor voltage. The transient analysis runs for 500 ms.

## What To Look For

- τ = R1 · C1 = 1 kΩ · 100 µF = 0.1 s.
- V(Out) falls as 100 V · e^(−t/τ): 36.8 V at 100 ms (one τ) and 0.67 V at 500 ms (five τ).
- I(C1) jumps to −100 V / 1 kΩ = −100 mA at the step, negative because current flows out of the capacitor, then decays with the same τ.

The simulation gives 36.8 V and −100 mA.

## How To Run

Open `RC-Discharge.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(Out) and I(C1).

## Try This

- This is RC Charge run backwards, at 100 V instead of 1 V. Compare the two curves: each covers 63 % of the remaining distance in every τ.
