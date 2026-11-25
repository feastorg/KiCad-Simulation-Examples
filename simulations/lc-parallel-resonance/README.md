# LC Parallel Resonance

A parallel LC tank blocks its resonant frequency, 159 kHz, making a sharp notch with a Q of 10.

## Circuit

V1 drives L1 = 1 µH in parallel with C1 = 1 µF, the tank, in series with R1 = 10 Ω to ground. Out is the voltage across R1. The AC sweep runs from 1 Hz to 1 MHz and plots the gain of V(Out) and of the current I(R1).

## What To Look For

- Resonance: f0 = 1/(2π√(L1·C1)) = 159.2 kHz, the same as LC Series Resonance.
- At f0 the tank's impedance becomes very large, so almost no current flows and V(Out) drops into a deep notch. Far below f0 the inductor is nearly a short and all of the 1 V reaches Out.
- Q = R1·√(C1/L1) = 10, so the notch is narrow: its −3 dB points are 151.4 kHz and 167.3 kHz, a bandwidth of f0/Q = 15.9 kHz.

The simulation puts the −3 dB points at 151.4 kHz and 167.3 kHz, with a gain of 1.000 at 1 kHz.

## How To Run

Open `LC-Parallel-resonance.kicad_sch` in KiCad, click **Simulate**, and run the AC tab. It plots the gain of V(Out) and of I(R1).

## Try This

- Change R1 to 100 Ω: Q rises to 100 and the notch narrows to about 1.6 kHz.
- In this arrangement a larger R1 gives a higher Q. In LC Series Resonance a smaller R1 does.
