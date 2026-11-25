# Simulation Behavioral and PWL Sources

Two behavioral sources driven by a piecewise-linear ramp: a squarer gives 0.25 V when the ramp is at 0.5 V, and a limiter steps from 0 to 1 V at 0.5 ms.

## Circuit

V1 is a PWL source, `PWL(0 0 1m 1 2m 1 3m 0)`: In ramps from 0 V to 1 V over the first millisecond, holds at 1 V until 2 ms, and ramps back to 0 V at 3 ms. B1 and B2 are behavioral (B) sources whose output is an expression of v(in); they read In by name, so no wire joins them to V1. B1 is the squarer, `V=v(in)*v(in)`, on Sq. B2 is the limiter, `V = v(in) > 0.5 ? 1 : 0`, on Lim. Each expression sits in the source's Sim.Params field, and KiCad's netlist carries it unchanged, as `B2 Lim GND V = v(in) > 0.5 ? 1 : 0`. The name inside `v()` is the netlist's node name: the global label In exports as `In`, but a local label would export as `/In`, leave `v(in)` pointing at a node nothing drives, and stop ngspice with a singular matrix. ERC warns `isolated_pin_label` on In because the B-sources read it by name rather than through a wire, and on Sq and Lim because nothing reads them. Its `power_pin_not_driven` error on #PWR01 is the same one Simulation Transient Sine shows, and none of the three warnings or the error stops the simulation. The workbook runs `.tran 1u 3m`: 3 ms with a 1 µs step.

## What To Look For

- The ramp rises at 1 V/ms, so In is 0.5 V at 0.5 ms and Sq is 0.5² = 0.25 V. At 0.25 ms Sq is 0.25² = 0.0625 V, a quarter of that, where a straight line would give half. Sq is a parabola up to 1 V, flat while In holds at 1 V, and a parabola back down.
- The limiter's condition turns true when In passes 0.5 V, at 0.5 V / (1 V/ms) = 0.5 ms, and false again on the way down, at 2 ms + 0.5 ms = 2.5 ms. The expression has only two values, so Lim is a 1 V pulse, not a ramp.

The simulation gives Sq = 0.2500 V at 0.5 ms and 0.0625 V at 0.25 ms, a peak of 1.000 V, and Lim reaching 1.000 V, rising at 0.4998 ms and falling at 2.500 ms.

## How To Run

Open `Simulation-Behavioral-pwl.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In), V(Sq) and V(Lim).

## Try This

- Change B2's threshold to 0.6: Lim now rises at 0.6 ms and falls at 2.4 ms. The simulation gives 0.5998 ms and 2.400 ms.
- Set the workbook's step to 10 µs, `.tran 10u 3m`. Lim still jumps in a single step, but the simulation only has a point every 10 µs to find it by, and the rise reads 0.4978 ms instead of 0.4998 ms.
- Make B1 a cuber, `V=v(in)*v(in)*v(in)`: at 0.5 ms Sq is 0.5³ = 0.125 V (computed).
