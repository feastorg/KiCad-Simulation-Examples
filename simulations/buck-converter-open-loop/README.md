# Buck Converter Open Loop

A PMOS switch, a freewheeling diode and an LC filter step 12 V down to 5.197 V at 1.04 A, with 0.31 A of inductor ripple and 38 mV of output ripple at 100 kHz.

## Circuit

V1 = 12 V feeds In. Q1, a P-channel VDMOS (`vto=-2 kp=5 rd=20m rs=10m`), connects In to SW. V2 drives Gate with a 100 kHz pulse from 12 V down to 2 V: low for 4.5 µs of each 10 µs period, with 10 ns edges. Q1 conducts while Gate is low, since its source sits at 12 V. D1 (`is=1e-6 rs=10m`) runs from ground to SW and carries the inductor current while Q1 is off. L1 = 100 µH runs from SW to Out, where C1 = 10 µF and the load R1 = 5 Ω sit to ground. There is no feedback: the duty cycle is fixed, so this is the power stage of a buck regulator with the controller left out.

The transient analysis runs `.tran 100n 2m`. A directive on the sheet sets `.options reltol=1e-4 method=gear`, for the reasons under How To Run.

## What To Look For

- Duty cycle: SW is high for 4.521 µs of each 10 µs period, the 4.5 µs pulse plus 21 ns around its edges, so D = 0.4521 (simulated, from SW's crossings of 6 V).
- Switch drop: with 10 V of gate drive, Q1 is a resistance Ron = rd + rs + 1/(kp·(|Vgs| − |Vto|)) = 20 mΩ + 10 mΩ + 1/(5 × (10 − 2)) = 55 mΩ. While it is on, SW = Vin − Iout·Ron = 12 V − 1.04 A × 55 mΩ = 11.943 V; the simulation averages 11.943 V.
- Diode drop: while Q1 is off, D1 holds SW at −Vf, with Vf = Vt·ln(I/Is) + I·rs = 25.86 mV × ln(1.04 A / 1 µA) + 1.04 A × 10 mΩ = 0.369 V; the simulation averages −0.369 V.
- Output voltage: L1 has no DC drop, so Vout is the average of SW: Vout = D·Vin − (1 − D)·Vf − D·Iout·Ron = 5.425 V − 0.202 V − 0.026 V = 5.197 V. The ideal buck would give D·Vin = 5.425 V; the diode costs 202 mV and the switch 26 mV. Each loss shows when its cause goes: with an ideal switch (rd = rs = 0, kp = 1e6) the simulation gives 5.224 V, 27 mV more; with a near-ideal diode (n = 0.05, rs = 0, so Vf = 18 mV) it gives 5.388 V, 191 mV more, against (1 − D) × (0.369 − 0.018) V = 0.192 V.
- Output current: Iout = Vout/R1 = 5.197 V / 5 Ω = 1.039 A, the average of I(L1).
- Inductor ripple: while Q1 is on, L1 sees 11.943 V − 5.197 V, so ΔI = (Vin − Iout·Ron − Vout)·D/(L·f) = (11.943 − 5.197) × 0.4521 / (100 µH × 100 kHz) = 0.305 A. I(L1) runs between 0.887 A and 1.192 A.
- Output ripple: C1 takes the ripple current, so ΔV = ΔI/(8·f·C) = 0.3055 A / (8 × 100 kHz × 10 µF) = 38.19 mV. The simulation finds the ripple from its sampled points, so it relies on the tab's 100 ns step: with the step capped at 1 µs instead, the peak is clipped and ΔV reads 37.43 mV.
- Start-up: averaged over a cycle, SW steps from 0 to 5.2 V, and L1 with C1 and R1 is a second-order low-pass, as in RLC Step Response. With Q = R1·√(C1/L1) = 5 × √(10 µF / 100 µH) = 1.58, the step overshoots by exp(−π/√(4Q² − 1)) = 35 %, and the ringing decays with τ = 2·R1·C1 = 100 µs: over the 209 µs to the next peak the excess should shrink by e^(209/100) = 8.1. By 1.5 ms, 15 τ, it is gone.

The simulation gives Vout = 5.197 V and I(L1) = 1.039 A averaged over 1.8–2 ms, and ΔI = 0.3055 A and ΔV = 38.19 mV over the last cycle. Earlier windows, 1.5–1.7 ms for Vout and the cycle ending at 1.8 ms for ΔV, agree to within 3 µV. At start-up Out peaks at 7.00 V at 98 µs, 34.6 % above its final value, and at 5.43 V at 307 µs: the excess shrinks from 1.80 V to 0.23 V, by 7.9.

## How To Run

Open `Buck-Converter-Open-Loop.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Out) and I(L1); add V(/SW) and zoom in to a few cycles to see the switch node.

The run takes about 0.3 s in ngspice 44.2. Two settings keep it honest:

- `method=gear`: with ngspice's default trapezoidal integration, the current in D1 swings from one time step to the next instead of following L1, which carries it (0.585 A in D1 against 1.054 A in L1 at 1.807 ms). With Gear integration the two agree to 1 µA. `reltol=1e-4` tightens the time steps: the two ripple windows agree to 0.01 %, against 0.12 % at the default.
- Save all currents and Save all power dissipations stay off in the analysis settings. Either one puts a 0 V source in series with every pin, and with them ngspice stops at 85 µs with "timestep too small". I(L1) is saved without them.

## Try This

- Change V2's `tw` to 4.725u, 5 % longer: D rises by 0.0225 and the simulation gives Vout = 5.471 V. Vout follows the duty cycle, which is why a real buck closes the loop around it.
- Change R1 to 4.5 Ω: Iout rises to 1.154 A but Vout barely moves, because only the losses depend on the load. Vout falls by D·Ron + (1 − D)·(Vt/I + rs) = 0.044 Ω per ampere, to 5.192 V computed; the simulation gives 5.191 V. ΔI and ΔV stay where they were.
- Change C1 to 100 µF: ΔV falls tenfold to 0.3055 A / (8 × 100 kHz × 100 µF) = 3.82 mV and Q rises to 5, but τ = 2·R1·C1 becomes 1 ms, so the 2 ms run ends before the start-up ringing has died away (computed).
