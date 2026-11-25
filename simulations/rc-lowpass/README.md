# RC Lowpass

A first-order RC low-pass filter with its −3 dB corner at 15.9 kHz.

## Circuit

V1 drives R1 = 10 Ω in series with C1 = 1 µF to ground. Out is the capacitor voltage. The AC sweep runs from 1 Hz to 100 kHz. The transient analysis drives a 1 V sine at 15.9 kHz, the corner frequency, for 300 µs.

## What To Look For

- The corner frequency is fc = 1/(2π · R1 · C1) = 1/(2π · 10 Ω · 1 µF) = 15.9 kHz.
- In the AC sweep, the gain is flat at 0 dB well below fc, −3 dB at fc, and falls by 20 dB per decade above it: about −16 dB at 100 kHz.
- In the transient run, V(Out) is 0.707 V and lags V(In) by 45°, because the source sits at fc.

The simulation puts the −3 dB point at 15.9 kHz.

## How To Run

Open `RC-Lowpass.kicad_sch` in KiCad, click **Simulate**, and run the AC and transient tabs. The AC tab plots the gain of V(In) and V(Out); the transient tab plots both voltages.

## Try This

- Increase R1 or C1 tenfold and fc drops to 1.59 kHz.
- Compare RC Highpass, which swaps the two parts.
