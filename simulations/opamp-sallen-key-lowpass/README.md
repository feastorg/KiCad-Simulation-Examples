# OPamp Sallen-Key Lowpass

A second-order active low-pass filter: two resistors, two capacitors and a follower put the −3 dB point at 1.12 kHz, then roll off twice as fast as an RC.

## Circuit

U1 runs from ±15 V and is wired as a follower: its output connects straight back to its inverting input. V3, with an AC value of 1, drives In. R1 = 10 kΩ runs from In to N1, and R2 = 10 kΩ from N1 to N2, U1's non-inverting input. C2 = 10 nF takes N2 to ground. C1 = 22 nF takes N1 to Out, so the output feeds back into the middle of the filter. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz, 10 mV input offset, 10 Ω output resistance. The workbook runs an AC sweep from 10 Hz to 100 kHz.

## What To Look For

- With equal resistors, the natural frequency is f0 = 1/(2π · R · √(C1 · C2)) = 1/(2π · 10 kΩ · 14.8 nF) = 1073 Hz.
- C1, fed back from the output, sets how sharp the corner is: Q = 0.5 · √(C1/C2) = 0.5 · √2.2 = 0.742, a little above the 0.707 of a flat Butterworth response.
- For a second-order low-pass, the −3 dB point is f0 · √(a + √(a² + 1)) with a = 1 − 1/(2Q²) = 0.091, so f−3dB = 1123 Hz.
- Well below the corner the follower passes the signal unchanged, 0 dB. Q slightly above 0.707 gives a peak of Q/√(1 − 1/(4Q²)) = 1.004, about +0.04 dB, at f0 · √a = 324 Hz.
- Above the corner the gain falls at 40 dB per decade, twice as fast as RC Lowpass. At 10 kHz the gain is 1/√((1 − x²)² + (x/Q)²) with x = 10 kHz / f0 = 9.32, or −38.8 dB.
- Above about 50 kHz the slope flattens, and the gain levels off near −72 dB around 87 kHz. Current through C1 develops a voltage across the op-amp's 10 Ω output resistance, which the falling loop gain no longer suppresses: the follower's output impedance is about Rout/(1 + A), and A has dropped to about 5 by 87 kHz. With ROUT = 0, or an ideal op-amp, the slope stays at 40 dB per decade.

The simulation gives the −3 dB point at 1121 Hz, 0.000 dB at 10 Hz and −38.8 dB at 10 kHz.

## How To Run

Open `OPamp-Sallen-Key-Lowpass.kicad_sch` in KiCad, click **Simulate**, and run the AC tab. It plots the gain of V(In) and V(Out).

## Try This

- Make C1 = C2 = 10 nF: f0 rises to 1592 Hz but Q drops to 0.5, so the corner softens and the −3 dB point lands at 0.644 · f0 = 1024 Hz.
- Make C1 = 47 nF: f0 falls to 734 Hz and Q rises to 1.08, so a 1.7 dB peak appears before the roll-off, and the −3 dB point moves out to 965 Hz.
- Make R1 = R2 = 4.7 kΩ: f0 rises to 2283 Hz and the −3 dB point to 2389 Hz, while Q stays 0.742, since with equal resistors Q depends only on C1/C2.
