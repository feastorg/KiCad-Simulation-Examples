# Rectifier 4D Regulator

A bridge rectifier followed by an LM317 adjustable regulator: a rippling 11–13 V turned into a steady 9 V at 1.1 A.

## Circuit

The front end is Rectifier 4D: V1, a 15 V peak, 50 Hz sine across a four-diode bridge, into C1 = 4700 µF and C2 = 1 µF at /Vin. U1 is an LM317 (vendor model `LM317-N.LIB`), with R1 = 120 Ω from its output to ADJ and R2 = 746 Ω from ADJ to ground. C3 = 10 µF bypasses ADJ. Rload1 = 8 Ω loads Out. The transient analysis runs for 100 ms.

## What To Look For

- The LM317 holds 1.25 V between its output and ADJ, so Vout = 1.25 V × (1 + R2/R1) = 1.25 × (1 + 746/120) = 9.02 V.
- The 1.1 A load makes the reservoir sag between charging peaks: /Vin swings from about 11.4 V to 13.3 V. Because the regulator needs only a couple of volts of headroom, the output stays flat through it.

The simulation gives 9.00 V at Out while /Vin swings 11.4–13.3 V, with D1 and D2 conducting 10 ms apart.

## How To Run

Open `Rectifier-4D-Regulator.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Vin), the source voltage V(In1) − V(In2), and V(Out).

## Try This

- Change R2 to 1.2 kΩ for 1.25 × (1 + 10) = 13.75 V. Now the dips in /Vin fall below what the LM317 needs, and the output ripples.
- The NPN, PNP and op-amp variants of this example get more current or a different reference from the same bridge.
