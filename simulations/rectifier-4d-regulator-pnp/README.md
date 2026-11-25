# Rectifier 4D Regulator PNP

The classic LM317 current boost: a PNP transistor takes over most of the load current, while the LM317 still sets the output voltage.

## Circuit

The front end is Rectifier 4D: V1, a 15 V peak, 50 Hz sine across a four-diode bridge, into C1 = 4700 µF and C2 = 1 µF at /Vin. U2, an LM317 (`LM317-N.LIB`), draws its input current through R3 = 5 Ω from /Vin and regulates Out with R1 = 120 Ω and R2 = 744 Ω. C3 = 10 µF bypasses ADJ. Q1, the default PNP, has its emitter on /Vin, its base on the LM317's input, /Ub, and its collector on Out. Rload1 = 8 Ω loads Out. The transient analysis runs for 100 ms.

## What To Look For

- The LM317 regulates Out directly: Vout = 1.25 V × (1 + 744/120) = 8.99 V.
- The LM317's own input current flows through R3. Once it reaches about 0.7 V / 5 Ω ≈ 0.14 A, Q1's base-emitter junction turns on and Q1 supplies the rest of the load current from /Vin straight to Out.
- So of the 1.12 A load current (8.96 V / 8 Ω), Q1 carries about 0.93 A and the LM317 only the remainder, while staying in control of the voltage.

The simulation gives 8.96 V on average (8.82 V to 8.98 V), with Q1 carrying 0.93 A and D1 and D2 conducting 10 ms apart.

## How To Run

Open `Rectifier-4D-Regulator-PNP.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Vin), the source voltage V(In1) − V(In2), and V(Out).

## Try This

- Raise R3 to 10 Ω: Q1 takes over at about half the LM317 current, so it carries a larger share of the load.
- Plot I(Q1:c) and I(Rload1) together to see the split.
