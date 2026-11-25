# NMOS Amplifier CS

A common-source MOSFET amplifier with voltage-divider bias, the MOSFET counterpart of NPN Amplifier CE, with a gain of about 16.

## Circuit

On a 10 V supply, R1 = 120 kΩ and R2 = 52 kΩ bias Q1's gate. R3 = 2 kΩ is the drain resistor and R4 = 100 Ω the source resistor. C1 = 1 µF couples in the signal, a 100 mV peak sine at 1 kHz, and C2 = 1 µF couples the output into R5 = 100 kΩ. Q1 is KiCad's default VDMOS model. The transient analysis runs for 5 ms.

## What To Look For

- Bias: the gate draws no current, so the divider is not loaded and the gate sits at 10 V × 52 / 172 = 3.02 V.
- The drain current depends on the MOSFET model's parameters. The simulation gives 2.34 mA, so the source sits at 0.234 V and the drain at 10 V − 2.34 mA × 2 kΩ = 5.32 V, well inside saturation.
- Gain = −R3 / (R4 + 1/gm). The simulated 15.8 puts 1/gm at about 27 Ω for this model at this current.

The simulation gives a 5.32 V drain bias and 3.16 V peak-to-peak at Out from 200 mV in, a gain of 15.8.

## How To Run

Open `NMOS-Amplifier-CS.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Out) and V(Vsig).

## Try This

- Compare NPN Amplifier CE: the same structure, but there the base current loads the bias divider, and here nothing does.
- Swap in a real MOSFET model, such as a 2N7002, and the bias point moves with its threshold voltage. Re-check that the drain stays well above the gate.
