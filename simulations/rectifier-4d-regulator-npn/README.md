# Rectifier 4D Regulator NPN

An LM317 regulates the base of an NPN emitter follower. The transistor carries the load current, but sits outside the regulation loop, so the output is one Vbe below the regulated voltage.

## Circuit

The front end is Rectifier 4D: V1, a 15 V peak, 50 Hz sine across a four-diode bridge, into C1 = 4700 µF and C2 = 1 µF at /Vin. U1, an LM317 (`LM317-N.LIB`), regulates its own output, the node /Ub, with R1 = 120 Ω and R2 = 843 Ω. C3 = 10 µF bypasses ADJ. Q1, the default NPN, has its collector on /Vin, its base on /Ub and its emitter at Out, into Rload1 = 8 Ω. The transient analysis runs for 100 ms.

## What To Look For

- The LM317 holds /Ub at 1.25 V × (1 + 843/120) = 10.03 V.
- Q1 follows it one base-emitter drop lower. At the load's 1.1 A, that Vbe is about 0.96 V for the default NPN, so Out ≈ 10.03 − 0.96 = 9.07 V.
- Because Vbe is outside the loop, any change in it, from load current or temperature, appears at the output. In this run the output wanders by 0.14 V as the reservoir ripples.

The simulation gives 9.04 V on average, varying from 8.92 V to 9.06 V.

## How To Run

Open `Rectifier-4D-Regulator-NPN.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Vin), the source voltage V(In1) − V(In2), and V(Out).

## Try This

- Take R1 from Out instead of /Ub, so the LM317 regulates the emitter: Vbe is then inside the loop and the output holds 1.25 × (1 + R2/R1). Check that the LM317 then has enough headroom to drive the base.
- Compare Rectifier 4D Regulator PNP, which boosts current while keeping the LM317 in charge of the output.
