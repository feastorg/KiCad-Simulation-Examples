# OPamp Sallen-Key Lowpass

A second-order active low-pass filter: two resistors, two capacitors and a follower roll off at 40 dB per decade above 1.12 kHz.

## Circuit

U1 runs from ±15 V and is wired as a follower: its output connects straight back to its inverting input. V3, with an AC value of 1, drives In. R1 = 10 kΩ runs from In to N1, and R2 = 10 kΩ from N1 to N2, U1's non-inverting input. C2 = 10 nF takes N2 to ground. C1 = 22 nF takes N1 to Out, so the output feeds back into the middle of the filter. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz, 10 mV input offset. The workbook runs an AC sweep from 10 Hz to 100 kHz.

## What To Look For

- With equal resistors, the natural frequency is f0 = 1/(2π · R · √(C1 · C2)) = 1/(2π · 10 kΩ · 14.8 nF) = 1073 Hz.
- C1, fed back from the output, sets how sharp the corner is: Q = 0.5 · √(C1/C2) = 0.5 · √2.2 = 0.742, a little above the 0.707 of a flat Butterworth response.
- For a second-order low-pass, the −3 dB point is f0 · √(a + √(a² + 1)) with a = 1 − 1/(2Q²) = 0.092, so f−3dB = 1123 Hz.
- Below the corner the follower passes the signal unchanged, 0 dB. Q slightly above 0.707 gives a peak of Q/√(1 − 1/(4Q²)) = 1.004, about +0.04 dB, just under the corner.
- Above the corner the gain falls at 40 dB per decade, twice as fast as RC Lowpass.

The simulation gives the −3 dB point at 1121 Hz and 0.000 dB at 10 Hz.

## How To Run

Open `OPamp-Sallen-Key-Lowpass.kicad_sch` in KiCad, click **Simulate**, and run the AC tab. It plots the gain of V(In) and V(Out).

## Try This

- Make C1 = C2 = 10 nF: f0 rises to 1592 Hz but Q drops to 0.5, so the corner softens and the −3 dB point lands at 0.644 · f0 = 1024 Hz.
- Make C1 = 47 nF: f0 falls to 734 Hz and Q rises to 1.08, so a 1.7 dB peak appears before the roll-off, and the −3 dB point moves out to 965 Hz.
- Swap the positions of the resistors and capacitors to get a Sallen-Key high-pass.
