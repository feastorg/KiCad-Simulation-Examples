# OPamp Integrator

An inverting integrator turns a 1 V, 1 kHz sine into a 3.18 V peak-to-peak output, and a 1 MΩ resistor across the capacitor holds the op-amp's offset to −1.01 V.

## Circuit

U1 runs from ±15 V, with its non-inverting input grounded. V3, a 1 V sine at 1 kHz starting at 0 V, drives R1 = 10 kΩ (R) into the inverting input. C1 = 10 nF (C) feeds back from Out, and R2 = 1 MΩ (Rf) sits across it. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz, 10 mV input offset, 10 Ω output resistance. The workbook runs a 100 ms transient.

## What To Look For

- The inverting input is a virtual ground, so R1 carries V(In)/R and that current charges C1: V(Out) = −1/(R·C) · ∫V(In) dt. For a sine of peak Vp the output swings 2 · Vp/(2π · f · R · C) = 2 · 1 V/(2π · 1 kHz · 10 kΩ · 10 nF) = 3.18 V peak to peak.
- At 1 kHz the model's open-loop gain A = 20,000/(1 + j · f/20 Hz) is only 400 in magnitude. With Zf = R2 ∥ C1 the swing becomes 2 · Vp · |Zf/R|/|1 + (1 + Zf/R)/A| = 3.1827 V/1.00403 = 3.170 V peak to peak.
- C1 blocks DC, so without R2 nothing would set the output's DC level. R2 is the only DC path: it makes the stage an inverting amplifier with gain −Rf/R = −100 below the lossy corner 1/(2π · Rf · C) = 1/(2π · 1 MΩ · 10 nF) = 15.9 Hz, and an integrator above it.
- The 10 mV input offset sees a DC gain of 1 + Rf/R = 101, so the output sits at −VOFF · (1 + Rf/R) = −1.01 V. The finite open-loop gain trims that to −1.01 V/(1 + 101/20,000) = −1.005 V.
- Because the sine starts at 0 V, the output also starts with an extra average of −Vp/(2π · f · R · C) = −1.59 V. It decays through R2 with the time constant Rf · C = 10 ms, so the measurements use the last 10 cycles, 90 to 100 ms. The 80 to 90 ms window gives the same figures to four digits.

The simulation gives 3.170 V peak to peak, centred on −1.005 V.

## How To Run

Open `OPamp-integrator.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In) and V(Out).

## Try This

- Change V3 to a pulse source from −1 V to 1 V with 1 µs edges, a 499 µs flat top and a 1 ms period. Each half period the output ramps at Vp/(R · C) = 10 V/ms for 0.5 ms, a 5 V peak-to-peak triangle. The simulation gives 4.97 V, centred on −1.00 V. The flat top must be half the period less one edge: at 500 µs the input averages +2 mV, which the DC gain of −100 turns into −0.2 V more at the output, and the simulation gives −1.20 V.
- Delete R2 for an ideal integrator. With no DC feedback the 10 mV offset meets the full open-loop gain of 20,000, and the output is pinned against the −15 V rail: the simulation gives −15.0 V to −12.0 V instead of a sine centred near −1 V.
