# Transformer 1P 1S

Two coupled inductors as an ideal transformer, stepping 325 V peak (230 V RMS) down to 32.5 V with a 10:1 ratio.

## Circuit

V1, a 325 V peak sine at 50 Hz, drives the primary winding L1 = 10 H. The secondary winding L2 = 100 mH feeds Rload1 = 100 Ω. The text directive `K1 L1 L2 1.0` couples the two windings with K = 1, no leakage. R1 = 1 GΩ gives the primary side a DC path to ground. The transient analysis runs for 100 ms, five cycles.

## What To Look For

- For coupled inductors the voltage ratio is √(L1/L2) = √(10 H / 100 mH) = 10, as the schematic's note says. Inductance goes with the square of the turns, so this is a 10:1 turns ratio.
- So the secondary peaks at 325 V / 10 = 32.5 V, and drives 32.5 V / 100 Ω = 325 mA through the load.
- The primary also carries a magnetising current, 325 V / (2π · 50 Hz · 10 H) ≈ 0.1 A peak, set by L1 alone.

The simulation gives 32.5 V and 325 mA on the secondary. The primary current swings between −0.005 A and 0.21 A: because the sine starts at a zero crossing, the magnetising current starts offset by about its own peak, and with no resistance in the primary that offset never decays.

## How To Run

Open `Transformer-1P-1S.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Vp) and V(/Vs).

## Try This

- Change L2 to 400 mH: the ratio becomes √(10/0.4) = 5 and the secondary rises to 65 V.
- Change K1's coupling to 0.9 and see how leakage lowers the secondary voltage under load.
