# OPamp Open Loop

The op-amp model with no feedback, showing its own frequency response: 86 dB of gain, a pole at 20 Hz, and unity gain at 400 kHz.

## Circuit

U1 runs from ±15 V. V3, with an AC value of 1, drives the non-inverting input. The inverting input is grounded, and the output drives R1 = 1 MΩ. U1 uses `kicad_builtin_opamp.lib` with its offset set to zero, `VOFF=0` in U1's Simulation Model parameters (see below). The AC sweep runs from 1 Hz to 10 MHz.

## What To Look For

- The model's parameters are GAIN = 20,000 and POLE = 20 Hz. The gain is 20,000 (86 dB) at low frequency and 3 dB down at 20 Hz.
- Above the pole it falls 20 dB per decade, so gain × frequency stays at 20,000 × 20 Hz = 400 kHz: a gain of 400 at 1 kHz, and 1 at 400 kHz. That product is the gain-bandwidth that sets every closed-loop example's bandwidth.
- Why `VOFF=0`: the model normally adds a 10 mV input offset, as real op-amps have. With no feedback, 10 mV × 20,000 = 200 V would drive the output into the +15 V rail, and the AC sweep would show a saturated amplifier instead of this curve.

The simulation gives 19,967 at 1 Hz, the pole at 20.0 Hz, and unity gain at 400 kHz.

## How To Run

Open `OPamp-open-loop.kicad_sch` in KiCad, click **Simulate**, and run the AC tab. It plots the gain of V(Out).

## Try This

- Delete `VOFF=0` from U1's parameters and rerun: the gain collapses to about 0.026, because the output is pinned at a rail.
- Change POLE or GAIN in U1's parameters and watch the gain-bandwidth move. Then rerun OPamp Noninverting with the same values.
