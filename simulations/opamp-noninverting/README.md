# OPamp Noninverting

A non-inverting amplifier with a gain of 10, and the bandwidth that gain costs.

## Circuit

U1 runs from ±15 V. V3, a 1 V sine at 1 kHz with an AC value of 1, drives the non-inverting input. R2 = 9 kΩ feeds back from the output to the inverting input, and R1 = 1 kΩ runs from there to ground. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz. The workbook runs an AC sweep from 1 Hz to 100 kHz and a 5 ms transient.

## What To Look For

- The op-amp drives its output until the divider's tap equals V(In), so V(Out) = V(In) · (1 + R2/R1) = 10 · V(In), in phase.
- The closed-loop bandwidth is the gain-bandwidth divided by the gain: 400 kHz / 10 = 40 kHz, where the gain falls 3 dB below 20 dB.

The simulation gives a gain of 9.99 at 1 kHz and a −3 dB point at 39.8 kHz.

## How To Run

Open `OPamp-noninverting.kicad_sch` in KiCad, click **Simulate**, and run the AC and transient tabs. They plot V(In) and V(Out).

## Try This

- Set R2 to 0 Ω and remove R1: it becomes OPamp Voltage Follower.
- Compare OPamp Inverting: a similar gain magnitude, but in phase with the input and with a high input impedance.
