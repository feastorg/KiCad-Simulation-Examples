# Simulation AC Sweep

The `.ac` analysis: the small-signal response across frequency, shown on an RC low-pass with its corner at 159 Hz.

## Circuit

V1 drives R1 = 100 Ω in series with C1 = 10 µF to ground. Out is the capacitor voltage. The workbook runs `.ac dec 1000 1 10k`: 1000 points per decade from 1 Hz to 10 kHz.

## What To Look For

- An AC sweep uses only the source's `ac` value, here 1, and ignores its sine and DC settings. With a 1 V input, V(Out) in dB is the circuit's gain.
- The corner is fc = 1/(2π · R1 · C1) = 1/(2π · 100 Ω · 10 µF) = 159 Hz. The gain is −3 dB there and falls 20 dB per decade above it: 0.0995 (−20 dB) at 1.59 kHz.

The simulation gives a −3 dB point at 158.8 Hz and a gain of 0.0995 at 1.59 kHz.

## How To Run

Open `Simulation-AC-sweep.kicad_sch` in KiCad, click **Simulate**, and run the AC tab. It plots the gain of V(In) and V(Out).

## Try This

- RC Lowpass is the same circuit with R and C chosen for a 15.9 kHz corner. This example is about reading the AC plot; that one is about the filter.
- Plot the phase of V(Out) as well: it passes −45° at the corner.
