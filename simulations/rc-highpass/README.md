# RC Highpass

A first-order RC high-pass filter with its −3 dB corner at 15.9 Hz.

## Circuit

V1 drives C1 = 100 µF in series with R1 = 100 Ω to ground. Out is the resistor voltage. The AC sweep runs from 1 Hz to 100 kHz. The transient analysis drives a 1 V sine at 15.9 Hz, the corner frequency, for 300 ms.

## What To Look For

- The corner frequency is fc = 1/(2π · R1 · C1) = 1/(2π · 100 Ω · 100 µF) = 15.9 Hz.
- In the AC sweep, the gain rises at 20 dB per decade below fc, is −3 dB at fc, and is flat at 0 dB well above it.
- In the transient run, V(Out) is 0.707 V and leads V(In) by 45°, because the source sits at fc.

The simulation puts the −3 dB point at 15.95 Hz and the gain at 1 kHz at 1.000.

## How To Run

Open `RC-Highpass.kicad_sch` in KiCad, click **Simulate**, and run the AC and transient tabs. The AC tab plots the gain of V(In) and V(Out); the transient tab plots both voltages.

## Try This

- Compare RC Lowpass, which swaps the two parts. Here the capacitor blocks DC and low frequencies.
