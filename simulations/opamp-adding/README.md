# OPamp Adding

An inverting summer: the output is −10 times the sum of two inputs, and the model's input offset shows up as a small DC shift.

## Circuit

U1 runs from ±15 V, with its non-inverting input grounded. V3 (0.25 V peak) and V4 (0.5 V peak), in-phase 1 kHz sines, drive R1 and R2 = 1 kΩ each into the inverting input. R3 = 10 kΩ feeds back from the output. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz, 10 mV input offset. The workbook runs a 5 ms transient and an AC sweep from 1 Hz to 100 kHz.

## What To Look For

- The inverting input is a virtual ground, so the two input currents add in R3: V(Out) = −R3 · (V(In1)/R1 + V(In2)/R2) = −10 · (V(In1) + V(In2)).
- Peak to peak: −10 × (0.25 + 0.5) V peak, a 15 V peak-to-peak swing.
- The model's 10 mV input offset is amplified by the noise gain 1 + R3/(R1 ∥ R2) = 21, so the whole waveform sits about 0.21 V below zero.

The simulation gives 14.96 V peak to peak, centred on −0.21 V.

## How To Run

Open `OPamp-adding.kicad_sch` in KiCad, click **Simulate**, and run the transient and AC tabs. They plot V(In1), V(In2) and V(Out).

## Try This

- Change R2 to 2 kΩ: In2 now counts half as much, so Out swings ±5 V.
- Real op-amps have offsets too. That is why precision summers keep the noise gain low or trim the offset.
