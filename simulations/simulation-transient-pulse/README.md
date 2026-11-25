# Simulation Transient Pulse

The `.tran` analysis with a pulse source: an RC circuit charging and discharging on a square wave whose half period equals τ.

## Circuit

V1 is a 0 to 1 V pulse, high for 10 ms of every 20 ms. It drives R1 = 1 kΩ in series with C1 = 10 µF to ground; Out is the capacitor voltage. The workbook runs `.tran 100u 100m`: 100 ms with a 100 µs step.

## What To Look For

- τ = R1 · C1 = 1 kΩ · 10 µF = 10 ms, the same as each half of the pulse.
- The first pulse charges C1 for one τ, to 1 − 1/e = 0.632 V.
- After a few cycles the swing settles between 1/(1 + e) = 0.269 V and e/(1 + e) = 0.731 V. Each half period undoes as much as the one before it.

The simulation gives 0.632 V, then a settled swing from 0.268 V to 0.731 V.

## How To Run

Open `Simulation-Transient-pulse.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(In) and V(Out).

## Try This

- Make the pulse ten times slower (pulse width 100 ms, period 200 ms, and extend the run to 1 s): C1 now fully charges and discharges, the same curve as RC Charge.
- Read the pulse fields from the source's Sim.Params, or from the annotated `pulse(...)` line in KiCad Simulation Commands.
