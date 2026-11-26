# OPamp Relaxation Oscillator

A Schmitt trigger that charges its own input through an RC: the output is a square wave with a period of 2 · R · C · ln 3, 968 Hz for 10 kΩ and 47 nF, and the simulation gives 956.3 Hz.

## Circuit

U1 runs from ±15 V. R1 = 10 kΩ runs from Out back to Ref, U1's non-inverting input, and R2 = 10 kΩ takes Ref to ground, as in OPamp Schmitt Trigger. R3 = 10 kΩ runs from Out to Cap, U1's inverting input, and C1 = 47 nF takes Cap to ground. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, pole at 20 Hz, 10 mV input offset, output clamped at the rails. The workbook runs a 10 ms transient, `.tran 0.1u 10m 0 0.1u`, with the maximum step pinned at 0.1 µs.

The text directive on the schematic has two lines:
- `.ic V(/Cap)=1` starts the oscillation. ngspice solves the operating point with Cap held at 1 V, where Out = 2.02 V and Ref = 1.01 V, then releases it at t = 0, and Out crosses 0 V 5.1 µs later. Without it, the circuit sits at its balance point (Try This).
- `.options method=gear`, as in OPamp Schmitt Trigger. With the maximum step left free, the default trapezoidal method at a 2 µs step gives a period of 1.094 ms, Gear 1.042 ms. It is the pinned maximum step below that makes the result independent of the step: with it, Gear and trapezoidal agree to 0.005 %.

The maximum step is pinned because the output switches in a few microseconds. With a 1 µs maximum step the period comes out 0.4 % short, at 1.0412 ms. From 2 µs up, now and then a cycle overshoots, and with a 10 µs step Cap peaks at 8.48 V, 1 V past the threshold.

KiCad's ideal capacitor has no initial-condition parameter. A `Sim.Params` of `c=47n ic=1` on C1 does reach the netlist, as `C1 /Cap GND c=47n ic=1`, but only because KiCad fails to parse it and falls back to passing the text through as raw SPICE. ngspice then applies the 1 V only with `uic` on the `.tran` line.

## What To Look For

- Ref is a fraction β = R2 / (R1 + R2) = 0.5 of Out. The output saturates at Vsat = 14.990 V, so Ref sits at ±β · Vsat = ±7.495 V.
- R3 charges C1 towards whichever rail Out is on. When Cap reaches Ref the output flips, Ref jumps to the other side, and C1 charges back the other way. Cap swings between the two thresholds, 2 · β · Vsat = 14.99 V peak to peak.
- Each half cycle C1 charges from −β · Vsat towards +Vsat and stops at +β · Vsat, which takes R3 · C1 · ln((1 + β) / (1 − β)). The period is twice that: T = 2 · 10 kΩ · 47 nF · ln 3 = 2 · 470 µs · 1.0986 = 1.0327 ms, a frequency of 968.3 Hz. Vsat cancels out.
- The model's output takes time to swing: its gain-bandwidth is GAIN · POLE = 20,000 · 20 Hz = 400 kHz. C1 keeps charging meanwhile, and peaks at +7.544 V and −7.564 V, beyond the thresholds. That lengthens the period by 1.3 %. With `POLE=2000` (40 MHz) in U1's parameters, the period is 1.0329 ms (968.1 Hz) and Cap peaks at +7.486 V and −7.506 V. A gain of 2,000,000 with the same 400 kHz (`GAIN=2Meg POLE=0.2`) gives 1.0458 ms, and `VOFF=0` gives 1.0457 ms: the 10 mV offset only moves both peaks down 10 mV.

The simulation gives a period of 1.0457 ms (956.3 Hz), and Cap swings 15.11 V peak to peak, between +7.544 V and −7.564 V. Out sits at +14.990 V and −14.990 V.

## How To Run

Open `OPamp-Relaxation-Oscillator.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Cap), V(/Ref) and V(Out): Out is a square wave between the rails, Ref a square wave of half its height, and Cap a train of exponential segments running between Ref's two levels.

## Try This

- Make C1 = 100 nF: the period scales with C1, to 2 · 10 kΩ · 100 nF · ln 3 = 2.197 ms, 455.1 Hz. The simulation gives 2.212 ms, 452.1 Hz.
- Make R1 = 20 kΩ: β drops to 1/3 and ln((1 + β) / (1 − β)) to ln 2, so T = 2 · 470 µs · 0.6931 = 0.6516 ms, 1534.8 Hz, and Cap swings ±β · Vsat = ±5.00 V. The simulation gives 0.6696 ms, 1493.5 Hz, with Cap between +5.087 V and −5.107 V.
- Delete the `.ic` line. The operating point is then the balance point, Out = Cap = −0.020 V, and with the workbook's 0.1 µs step nothing disturbs it: Out stays there for the whole run. Whether a coarser step starts it depends on the step: with the 0.1 µs maximum step kept, which is what changing only the step in KiCad's dialog does, every step from 0.2 to 10 µs starts it (at 5 µs the first switch is at 363 µs); with the maximum step left free, 5 and 10 µs stay at the balance point. That dependence on numerical error is why the schematic gives the kick explicitly.
