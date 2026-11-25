# RC Charge

A 1 V step charges a 100 µF capacitor through 1 kΩ, showing the exponential rise and the time constant τ = RC.

## Circuit

V1 steps from 0 to 1 V at t = 0 and drives R1 = 1 kΩ in series with C1 = 100 µF to ground. Out is the capacitor voltage. The transient analysis runs for 500 ms, five time constants.

## What To Look For

- τ = R1 · C1 = 1 kΩ · 100 µF = 0.1 s.
- V(Out) rises as 1 − e^(−t/τ): 0.632 V at 100 ms (one τ) and 0.993 V at 500 ms (five τ).
- I(C1) jumps to 1 V / 1 kΩ = 1 mA at the step, when the empty capacitor acts as a short, then decays with the same τ.

The simulation gives 0.632 V, 0.993 V and 1.00 mA.

## How To Run

Open `RC-Charge.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(Out) and I(C1).

## Try This

- Double R1 or C1 and the rise takes twice as long; τ moves to 200 ms.
- The schematic's note gives τ as T = RC; compare it with the time V(Out) takes to reach 0.632 V.
