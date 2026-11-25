# NMOS Switch Inductive Flyback

A low-side MOSFET switch driving an inductive load: the current ramps to 100 mA with time constant L/R = 83.3 µs, and at turn-off a flyback diode clamps the drain at 12.8 V.

## Circuit

V1 = 12 V feeds the load, L1 = 10 mH in series with R1 = 120 Ω, which runs from the supply to Drain. Q1, an NMOS with KiCad's default VDMOS model, switches Drain to ground. D1, the flyback diode with the default diode model, sits across the load with its cathode on the supply. V2 drives Gate from 0 to 10 V, high from 100 µs to 600 µs. The transient analysis runs for 1 ms.

## What To Look For

- Turn-on: Q1 pulls Drain to ground, and the current rises as Ion · (1 − e^(−t/τ)), with τ = L/R = 10 mH / 120 Ω = 83.3 µs and Ion = Vdd / R = 12 V / 120 Ω = 100 mA. The gate is high for 500 µs, six time constants, so the current reaches 100 mA × (1 − e^−6) = 99.75 mA.
- Turn-off: the inductor keeps its current flowing, so Drain flies up until D1 conducts and carries the current back to the supply. Drain sits one diode drop above Vdd. The default diode (Is = 1e-14 A) drops Vt · ln(I / Is) = 25.9 mV × ln(99.75 mA / 1e-14 A) = 0.774 V, so the clamp is 12 V + 0.774 V = 12.77 V. The drain rings a few tens of millivolts as D1 takes over.
- Decay: in the loop of L1, R1 and D1, L di/dt = −(R i + Vf), so i(t) = (I0 + Vf/R) · e^(−t/τ) − Vf/R, with I0 = 99.75 mA and Vf/R = 0.774 V / 120 Ω = 6.45 mA. Timed from 600.1 µs, where the gate starts to fall, the current reaches 50 mA after τ · ln((I0 + Vf/R) / (50 mA + Vf/R)) = 52.7 µs. The diode drop speeds the decay: the current falls to 36.8 mA (36.8 % of 100 mA) after 74.9 µs, not τ = 83.3 µs, and reaches zero after τ · ln(1 + I0 R / Vf) = 233 µs. These hold Vf at 0.774 V; Vf falls as the current does, so the simulated tail is a little slower.
- Once the current reaches zero, D1 stops conducting and L1 rings with the capacitance at Drain: Drain swings about 12 V, down to 11.50 V at 847 µs, and I(L1) swings by tens of microamps, −74 µA at its lowest, still ringing at 1 ms.
- At turn-on the gate edge couples into Drain through Q1's capacitances and lifts it to 12.71 V for a few tens of nanoseconds, before Q1 pulls it down.

The simulation gives 99.75 mA (Ion = 100 mA) just before turn-off and a 12.80 V peak at Drain after it. Timed from 600.1 µs, the current falls to 50 mA after 52.9 µs, to 36.8 mA after 75.2 µs, and below 1 µA after 242 µs.

## How To Run

Open `NMOS-Switch-Inductive-Flyback.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Drain), V(/Gate) and I(L1).

## Try This

- Delete D1. Nothing carries the inductor current at turn-off, and the simulation drives Drain to about 1670 V. That figure is not physical: the default VDMOS has no breakdown, while a real MOSFET would avalanche at its rated drain voltage, or fail. This is what the flyback diode is for.
- Halve R1 to 60 Ω: Ion doubles to 200 mA and τ doubles to 167 µs, so the 500 µs pulse is only three time constants and the current reaches 200 mA × (1 − e^−3) = 190 mA. The clamp rises only slightly, since Vf grows with the log of the current: Vdd + Vf = 12.79 V by the diode formula, and the simulation peaks at 12.82 V.
- Compare RL Voltage Current, the same L/R pair driven by a sine.
