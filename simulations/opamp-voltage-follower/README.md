# OPamp Voltage Follower

An op-amp with its output tied to its inverting input: a buffer with a gain of exactly 1.

## Circuit

U1 runs from ±15 V. V3, a 1 V sine at 1 kHz with an AC value of 1, drives the non-inverting input. The output connects straight back to the inverting input. U1 uses `kicad_builtin_opamp.lib`, a single-pole model: open-loop gain 20,000, pole at 20 Hz, 10 mV input offset. The workbook runs an AC sweep from 1 Hz to 100 kHz and a 5 ms transient.

## What To Look For

- The op-amp drives its output until its two inputs match, so V(Out) = V(In): gain 1, 0 dB.
- The output can supply current that the input never has to, which is what makes a follower a buffer.
- The closed-loop bandwidth is the model's gain-bandwidth, 20,000 × 20 Hz = 400 kHz, beyond the end of this sweep.

The simulation gives a gain of 1.000 at 1 kHz.

## How To Run

Open `OPamp-voltage-follower.kicad_sch` in KiCad, click **Simulate**, and run the AC and transient tabs. They plot V(In) and V(Out).

## Try This

- Extend the AC sweep to 10 MHz to find the −3 dB point near 400 kHz.
- Compare OPamp Noninverting: add a feedback divider and the gain rises above 1.
