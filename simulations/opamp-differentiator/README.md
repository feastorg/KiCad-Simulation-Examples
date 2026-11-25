# OPamp Differentiator

An inverting differentiator: the gain rises 20 dB per decade, −4.04 dB at 1 kHz, until the op-amp's gain-bandwidth stops it in a 19.7 dB peak at 24 kHz.

## Circuit

U1 runs from ±15 V, with its non-inverting input grounded. V3, with an AC value of 1, drives In. R1 = 1 kΩ runs from In to N1, and C1 = 10 nF from N1 to the inverting input. R2 = 10 kΩ feeds back from Out. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz, so a gain-bandwidth GBW = 400 kHz, with 10 mV input offset and 10 Ω output resistance. The workbook runs an AC sweep from 10 Hz to 1 MHz.

## What To Look For

- The inverting input is a virtual ground, so C1's current, set by the rate of change of V(In), all flows through R2: V(Out) = −R2 · C1 · dV(In)/dt. In AC terms |H| = 2π · f · R2 · C1, which rises 20 dB per decade: −44.04 dB at 10 Hz and 20 · log10(2π · 1 kHz · 10 kΩ · 10 nF) = 20 · log10(0.628) = −4.04 dB at 1 kHz.
- R1 adds little at 1 kHz: 2π · f · R1 · C1 = 0.063, which lowers the gain by 10 · log10(1 + 0.063²) = 0.017 dB. The op-amp's finite gain raises it by about as much, so the simulation gives −4.040 dB with R1 and −4.023 dB without.
- With an ideal op-amp the gain would level off at R2/R1 = 10, or 20 dB, above f_S = 1/(2π · R1 · C1) = 15.92 kHz. The model's open-loop gain, though, is GBW/f, falling as the differentiator asks for more. Where the two meet, the response peaks and then falls at 20 dB per decade. The peak sits at √(GBW · f_RC), with f_RC = 1/(2π · (R1 + R2) · C1) = 1447 Hz: √(400 kHz · 1447 Hz) = 24.06 kHz. Its gain is (GBW/f_D) / (1 + GBW/f_S), with f_D = 1/(2π · R2 · C1) = 1592 Hz: 251.3 / 26.13 = 9.62, or 19.66 dB.
- R1 is what holds the peak down: it puts GBW/f_S = 25.1 in the denominator. Without it the peak is GBW/f_D = 251.3, or 48.0 dB, at √(GBW · f_D) = 25.23 kHz.

The simulation gives −4.040 dB at 1 kHz and a peak of 19.66 dB at 24.04 kHz.

## How To Run

Open `OPamp-differentiator.kicad_sch` in KiCad, click **Simulate**, and run the AC tab. It plots the gain of V(In) and V(Out).

## Try This

- Replace R1 with a wire. The gain at 1 kHz barely moves, but the peak climbs to 47.9 dB at 25.2 kHz, 0.1 dB under the 48.0 dB worked out above, which leaves out the model's 20 Hz pole.
- Make R1 = 2 kΩ: f_S drops to 7958 Hz, and the peak falls to 251.3 / (1 + 50.26) = 4.902, or 13.81 dB, at √(400 kHz · 1326 Hz) = 23.03 kHz, since f_RC = 1/(2π · 12 kΩ · 10 nF) = 1326 Hz. The simulation gives 13.81 dB at 23.0 kHz.
- In `kicad_builtin_opamp.lib`, set POLE = 40 to double the GBW to 800 kHz. The peak moves up by √2 to √(800 kHz · 1447 Hz) = 34.0 kHz, with a gain of (800 kHz/1592 Hz) / (1 + 800 kHz/15.92 kHz) = 502.5 / 51.25 = 9.80, or 19.8 dB. The simulation gives 19.8 dB at 34.0 kHz.
