# LC Series Resonance

A series LC circuit passes everything at its resonant frequency, 159 kHz, where the inductor and capacitor cancel. With a Q of 0.1, the peak is very broad.

## Circuit

V1 drives L1 = 1 µH in series with C1 = 1 µF into R1 = 10 Ω to ground. Out is the voltage across R1. The AC sweep runs from 1 Hz to 10 MHz and plots the gain of V(Out) and of the current I(R1).

## What To Look For

- Resonance: f0 = 1/(2π√(L1·C1)) = 1/(2π√(1 µH · 1 µF)) = 159.2 kHz. The schematic's note gives the same figure.
- At f0 the two reactances are equal and opposite, the LC branch is a short, and all of the input reaches Out: gain 1 (0 dB), current 1 V / 10 Ω = 100 mA.
- Q = (1/R1)·√(L1/C1) = 0.1, so the response is a broad hump rather than a sharp peak. The −3 dB points are f0·(√(1 + 1/(4Q²)) ∓ 1/(2Q)): 15.8 kHz and 1.61 MHz.

The simulation gives a gain of 1.000 and 100.0 mA at f0, and −3 dB points at 15.8 kHz and 1.60 MHz.

## How To Run

Open `LC-Series-resonance.kicad_sch` in KiCad, click **Simulate**, and run the AC tab. It plots the gain of V(Out) and of I(R1).

## Try This

- Change R1 to 0.1 Ω: Q rises to 10, and the curve becomes a sharp peak about 16 kHz wide at 159 kHz.
- Compare LC Parallel Resonance: the same parts arranged as a tank block the signal at f0 instead of passing it.
