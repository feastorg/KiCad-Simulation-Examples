# RC Bandpass

A high-pass stage followed by a low-pass stage, passing 15.9 Hz to 15.9 kHz.

## Circuit

V1 drives C1 = 100 µF in series with R1 = 100 Ω to ground: the high-pass stage. Its output feeds R2 = 10 Ω in series with C2 = 1 µF to ground: the low-pass stage. Out is C2's voltage. The AC sweep runs from 1 Hz to 100 kHz. The transient analysis drives a 1 V sine at 15.9 Hz, the low corner, for 300 ms.

## What To Look For

- Low corner: 1/(2π · R1 · C1) = 1/(2π · 100 Ω · 100 µF) = 15.9 Hz.
- High corner: 1/(2π · R2 · C2) = 1/(2π · 10 Ω · 1 µF) = 15.9 kHz.
- Between the corners the gain is close to 0 dB. The two capacitors are 100 times apart, so the stages barely load each other, and each corner stays near its own formula.

The simulation gives corners at 16.1 Hz and 15.7 kHz, and a gain of 0.989 (−0.1 dB) at 400 Hz. The small differences are the two stages loading each other.

## How To Run

Open `RC-Bandpass.kicad_sch` in KiCad, click **Simulate**, and run the AC and transient tabs. The AC tab plots the gain of V(In) and V(Out); the transient tab plots both voltages.

## Try This

- Change C1 to 10 µF and the low corner moves up tenfold, to 159 Hz, while the high corner stays at 15.9 kHz.
