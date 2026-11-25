# OPamp Inverting

An inverting amplifier with a gain of −10, set by two resistors.

## Circuit

U1 runs from ±15 V, with its non-inverting input grounded. V3, a 1 V sine at 1 kHz with an AC value of 1, drives R1 = 1 kΩ into the inverting input. R2 = 10 kΩ feeds back from the output. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz. The workbook runs an AC sweep from 1 Hz to 100 kHz and a 5 ms transient.

## What To Look For

- The inverting input is held at virtual ground, so the current through R1 is V(In) / R1. All of it flows on through R2, giving V(Out) = −V(In) · R2 / R1 = −10 · V(In).
- With a finite open-loop gain A the gain is 10 / |1 + 11/A|. At 1 kHz the model's A is 400 but nearly 90° out of phase, so the error barely shows: 9.996. At 10 kHz A = 40, and the gain drops to 9.64.

The simulation gives 9.991 at 1 kHz and 9.64 at 10 kHz.

## How To Run

Open `OPamp-inverting.kicad_sch` in KiCad, click **Simulate**, and run the AC and transient tabs. They plot V(In) and V(Out).

## Try This

- Change R2 to 47 kΩ for a gain of −47. The bandwidth shrinks to about 400 kHz / 48 ≈ 8.3 kHz.
- In the transient tab, V(Out) is the input turned upside down: ±10 V for ±1 V in.
