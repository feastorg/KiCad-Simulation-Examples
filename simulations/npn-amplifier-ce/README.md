# NPN Amplifier CE

A common-emitter amplifier with voltage-divider bias and emitter degeneration, amplifying a 100 mV signal by about 9.

## Circuit

On a 10 V supply, R1 = 48 kΩ and R2 = 7.2 kΩ bias Q1's base. R3 = 1 kΩ is the collector resistor and R4 = 100 Ω the emitter resistor. C1 = 1 µF couples in the signal, a 100 mV peak sine at 1 kHz, and C2 = 1 µF couples the output into R5 = 100 kΩ. Q1 is KiCad's default NPN model, with β = 100. The transient analysis runs for 5 ms.

## What To Look For

- Bias: the divider alone would give 10 V × 7.2 / 55.2 = 1.30 V. But it has a 6.3 kΩ source resistance and carries about 30 µA of base current, so the base sits near 1.11 V. The emitter is one Vbe lower at about 0.31 V, so Ic ≈ 0.31 V / 100 Ω = 3.1 mA, and the collector rests at 10 V − 3.1 mA × 1 kΩ ≈ 6.9 V.
- Gain ≈ −R3 / (R4 + re), where re = VT / Ic = 25.9 mV / 3.06 mA = 8.5 Ω: −1000 / 108.5 ≈ −9.2. The minus sign means the output is inverted.
- So the 200 mV peak-to-peak input becomes about 1.8 V peak-to-peak at Out.

The simulation gives a 6.95 V collector bias and 1.80 V peak-to-peak at Out, a gain of 9.0.

## How To Run

Open `NPN-Amplifier-CE.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Out) and V(Vsig).

## Try This

- Bypass R4 with a 100 µF capacitor to ground: the bias stays where it is, but at 1 kHz the emitter is now nearly grounded for the signal, and the gain rises to about R3 / (re + 1.6 Ω) ≈ 1000 / 10.1 ≈ 100.
- Raise the input to 1 V peak and watch the output clip as Q1 runs out of headroom.
