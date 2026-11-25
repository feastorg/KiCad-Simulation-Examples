# NMOS Switch Inductive Flyback

A low-side MOSFET switch driving an inductive load: the current ramps to 100 mA with time constant L/R = 83.3 µs, and at turn-off a flyback diode clamps the drain at 12.8 V.

## Circuit

V1 = 12 V feeds the load, L1 = 10 mH in series with R1 = 120 Ω, which runs from the supply to Drain. Q1, an NMOS with KiCad's default VDMOS model, switches Drain to ground. D1, the flyback diode with the default diode model, sits across the load with its cathode on the supply. V2 drives Gate from 0 to 10 V, high from 100 µs to 600 µs. The transient analysis runs for 1 ms.

## What To Look For

- Turn-on: Q1 pulls Drain to ground, and the current rises as Ion · (1 − e^(−t/τ)), with τ = L/R = 10 mH / 120 Ω = 83.3 µs and Ion = Vdd / R = 12 V / 120 Ω = 100 mA. The gate is high for 500 µs, six time constants, so the current reaches 100 mA × (1 − e^−6) = 99.75 mA.
- Turn-off: the inductor keeps its current flowing, so Drain flies up until D1 conducts and carries the current back to the supply. Drain sits one diode drop above Vdd. The default diode (Is = 1e-14 A) drops Vt · ln(I / Is) = 25.9 mV × ln(99.75 mA / 1e-14 A) = 0.774 V, so the clamp is 12 V + 0.774 V = 12.77 V. The drain rings a few tens of millivolts as D1 takes over.
- Decay: in the loop of L1, R1 and D1, L di/dt = −(R i + Vf), so i(t) = (Ion + Vf/R) · e^(−t/τ) − Vf/R, with Vf/R = 0.774 V / 120 Ω = 6.45 mA. The diode drop speeds the decay: the current falls to 36.8 % of Ion after τ · ln((Ion + Vf/R) / (0.368 Ion + Vf/R)) = 75.0 µs, not 83.3 µs, and reaches zero after τ · ln(1 + Ion R / Vf) = 233 µs. Vf falls as the current does, so the simulated tail is a little slower.
- At turn-on the gate edge couples into Drain through Q1's capacitances and lifts it to 12.71 V for a few tens of nanoseconds, before Q1 pulls it down.

The simulation gives 99.75 mA (Ion = 100 mA) just before turn-off and a 12.80 V peak at Drain after it. The current falls to 36.8 % 75.1 µs after the gate starts to fall, and to zero after 242 µs.

## How To Run

Open `NMOS-Switch-Inductive-Flyback.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Drain), V(/Gate) and I(L1).

## Try This

- Delete D1. Nothing carries the inductor current at turn-off, and the simulation drives Drain to about 1670 V. That figure is not physical: the default VDMOS has no breakdown, while a real MOSFET would avalanche at its rated drain voltage, or fail. This is what the flyback diode is for.
- Halve R1 to 60 Ω: Ion doubles to 200 mA and τ doubles to 167 µs, so the 500 µs pulse is only three time constants and the current reaches 200 mA × (1 − e^−3) = 190 mA. The clamp rises only slightly, to about 12.79 V, since Vf grows with the log of the current.
- Compare RL Voltage Current, the same L/R pair driven by a sine.
