# NPN Current Mirror

Two matched NPNs copy a 0.995 mA reference current, and the Early effect makes the copy grow from 1.058 mA at 5 V to 1.155 mA at 10 V.

## Circuit

V1 = 15 V drives the reference current through R1 = 14.3 kΩ into Q1, whose base is tied to its collector at node Ref, so it acts as a diode. Q2's base shares Ref, and its collector, Out, is held by the source V2. The workbook runs `.dc V2 0 15 10m`, sweeping Out from 0 to 15 V. Q1 and Q2 are KiCad's Gummel-Poon NPN with β = 100 and `vaf=50` set in their simulation model parameters. The model's default VAF is infinite, so without that setting there is no Early effect.

## What To Look For

- Reference: Ref sits one Vbe above ground, 0.77358 V in the simulation, so Iref = (15 − 0.77358) / 14.3 kΩ = 0.994855 mA. Iref depends on V2 only through Vbe, which moves little: above the knee Ref stays at 0.77358 V, and even at Vout = 0, where Q2 is saturated and its base draws 0.498 mA, Ref only falls to 0.7559 V and Iref rises 0.12 % to 0.99609 mA.
- Mirror ratio: Iref feeds Q1's collector and both bases. Above the knee, where Q2 is not saturated, Q1 and Q2 share Vbe and draw the same base current, Ic/β, where Ic is Q1's collector current. So Iref = Ic + 2Ic/β, and Ic = Iref / (1 + 2/β) = 0.994855 mA / 1.02 = 0.97535 mA.
- Early effect: Q2's collector current grows with its collector-base voltage, Iout = 0.97535 mA × (1 + (Vout − 0.77358) / 50). At Vout = 0.77358 V the two transistors see the same voltages and Iout equals Q1's 0.97535 mA. At Vout = 5 V, Iout = 0.97535 mA × 1.084528 = 1.0578 mA. At 10 V, 0.97535 mA × 1.184528 = 1.1553 mA, and at 15 V, 0.97535 mA × 1.284528 = 1.2529 mA.
- Output resistance: between 5 V and 10 V, Iout rises by 0.0975 mA, so ro = 5 V / 0.0975 mA = 51.3 kΩ, which is VAF / 0.97535 mA. The textbook estimate VAF / Iout, 50 V / 1.0578 mA = 47.3 kΩ at 5 V, is within 10 % of it.
- Below about 0.14 V Q2 is saturated and the current collapses. At Vout = 0 its base-collector junction is forward biased and the current reverses.

The simulation gives the same Iout at 5, 10 and 15 V to five significant figures, and −0.49 mA at 0 V. ngspice's I(V2) is the current into V2's + terminal on Out, so it reads −Iout.

## How To Run

Open `NPN-Current-Mirror.kicad_sch` in KiCad, click **Simulate**, and run the DC tab. It plots I(Q2:c), the output current, against V2.

## Try This

- Remove `vaf=50` from Q1 and Q2: the curve goes flat at 0.97535 mA above the knee, the ideal mirror.
- Set `vaf=100`: Iout becomes 0.97535 mA × (1 + (Vout − 0.77358) / 100): 0.97535 mA × 1.042264 = 1.0166 mA at 5 V and 0.97535 mA × 1.092264 = 1.0653 mA at 10 V, and ro doubles to 102.5 kΩ.
