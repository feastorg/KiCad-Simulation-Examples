# Simulation Noise RC

A noise analysis finds the thermal noise a circuit makes: at the output of an RC low-pass it totals √(kT/C) = 64.4 nV rms, whatever the resistor.

## Circuit

The circuit of RC Lowpass: V1 drives R1 = 10 Ω in series with C1 = 1 µF to ground, and Out is the capacitor voltage. The workbook runs `.noise v(Out) V1 dec 20 1 10Meg`: the noise at Out from 1 Hz to 10 MHz, 20 points per decade. V1 is ideal and adds no noise; the analysis names it as the input for the input-referred noise.

## What To Look For

- R1's thermal noise acts as a voltage source in series with it, with density √(4kTR) = √(4 × 4.1440e-21 J × 10 Ω) = 0.4071 nV/√Hz. Here kT is taken at 27 °C, T = 300.15 K.
- Far below fc = 1/(2π · R1 · C1) = 15.9 kHz, Out sees that density unfiltered. Above fc, C1 shorts the noise to ground, and the density falls off as the low-pass gain does.
- The total noise power is the density squared, summed over all frequencies: 4kTR × (π/2) · fc. The noise bandwidth (π/2) · fc = 1/(4 · R1 · C1) = 25.0 kHz, so the total is 0.4071 nV/√Hz × √25.0 kHz = 64.4 nV = √(kT/C) = √(4.1440e-21 J / 1 µF). R1 cancels: a larger resistor has more noise density over a narrower bandwidth.
- The total is right only when the sweep covers the noise. Stopping at f2 leaves out about (2/π) · fc/f2 of the noise power. For the total to come within 1 % of √(kT/C), f2 must reach about 32 fc, 0.51 MHz. The workbook's 10 MHz is 628 fc, which leaves out 0.1 % of the power, 0.05 % of the rms. The sweep must also start well below fc.

The simulation gives a total of 64.3 nV rms, and 0.4071 nV/√Hz at 1 Hz.

## How To Run

Open `Simulation-Noise-RC.kicad_sch` in KiCad, click **Simulate**, and run the NOISE tab. It plots onoise_spectrum, the noise density at Out in V/√Hz. When the run ends, the console lists the totals, onoise_total and inoise_total.

## Try This

- Set R1 to 1 kΩ. The density rises tenfold to 4.071 nV/√Hz and fc falls to 159 Hz, but the simulated total stays at 64.2 nV.
- Set the sweep's stop frequency to 100 kHz, 6.3 fc. The simulated total falls to 61.0 nV, 5 % low.
- Set R1 to 10 kΩ. Now fc is 15.9 Hz, and the 1 Hz start leaves out 4 % of the noise power: the simulated total is 63.1 nV. Start the sweep at 1 mHz and it returns to 64.4 nV.
