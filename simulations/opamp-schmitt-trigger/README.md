# OPamp Schmitt Trigger

A comparator with positive feedback: the output switches low when the input rises past +7.5 V, and back high only when it falls past −7.5 V.

## Circuit

U1 runs from ±15 V. V3 drives In, U1's inverting input, with a ±10 V triangle at 100 Hz: 4.5 ms up, 0.5 ms at +10 V, 4.5 ms down, 0.5 ms at −10 V. R1 = 10 kΩ runs from Out back to Ref, U1's non-inverting input, and R2 = 10 kΩ takes Ref to ground. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000, 10 mV input offset, output clamped at the rails. The workbook runs a 20 ms transient, two periods.

V3's flat tops are there for ngspice: with `tw=0` it treats the hold time as unset and stays at +10 V until the end of the period, so the falling ramp never happens.

The text directive `.options method=gear noopiter` on the schematic is there for ngspice too, because of the model's sharp output clamp:
- Gear integration keeps the result independent of the time step. With ngspice's default trapezoidal method, a 5 µs step makes Out fall at In = −6.66 V, far from either threshold.
- `noopiter` sends the operating point straight to gmin stepping. Without it, ngspice reports Out = −15 V at the start, a point that does not balance the currents inside the model. With In = −10 V, the only DC solution is Out = +15 V, and with these resistors gmin stepping finds it. It isn't a general cure: with R1 = 20 kΩ (Try This) the operating point still starts on −15 V and the transient corrects it within a microsecond, which is why the lower-threshold check skips the first millisecond.

## What To Look For

- Ref is a fraction β = R2 / (R1 + R2) = 0.5 of Out. The output saturates at Vsat = 14.999 V, so Ref sits at +7.50 V while Out is high and −7.50 V while it is low.
- The input has to cross Ref to switch the output, and the switch moves Ref to the other side. The upper threshold is +β · Vsat = 0.5 × 14.999 V = +7.50 V, the lower −7.50 V, a window 2 · β · Vsat = 15.00 V wide. An input that wanders inside the window cannot make the output chatter.
- The model's 10 mV offset moves both thresholds down 10 mV, to +7.49 V and −7.51 V. With a triangle ten times slower (45 ms ramps), the simulated thresholds are +7.490 V and −7.510 V, on the formula, and +7.500 V and −7.500 V with `VOFF=0`.
- At this triangle's 20 V / 4.5 ms = 4.44 V/ms, each threshold lands further out than the formula. With a 0.1 µs step it is 25 mV out on each side, and with the workbook's 1 µs step 15 mV. Since the slower triangle removes the gap, it comes from the ramp rate.

The simulation gives the upper threshold at +7.504 V and the lower at −7.525 V, a window 15.03 V wide, with Out at +14.999 V and −14.999 V.

## How To Run

Open `OPamp-Schmitt-Trigger.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(/Ref) and V(Out): Out falls at 3.94 ms, as In passes +7.5 V on the way up, and rises at 8.94 ms, as In passes −7.5 V on the way down.

## Try This

- Make R1 = 20 kΩ: β drops to 1/3 and the thresholds close in to ±β · 15 V = ±5.00 V. The simulation gives +5.019 V and −5.038 V.
- Shrink the triangle to ±7 V, inside the window: Out never switches, and stays at +15 V for the whole run.
- Set `VOFF=0` in U1's parameters: the thresholds become symmetric, +7.515 V and −7.514 V.
- Swap U1's inputs, so R1 feeds back to the inverting input: the circuit becomes a non-inverting amplifier with a gain of 1 + R1/R2 = 2, and the hysteresis is gone. Out follows In, −2.25 V at In = −1.11 V, and crosses 0 V within 14 mV of In = 0 V in both directions.
