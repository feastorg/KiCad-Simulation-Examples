# Rectifier 4D OPamp NPN

A discrete series regulator: an op-amp compares a zener reference with a divided-down output and drives an NPN pass transistor, holding 9 V.

## Circuit

The front end is Rectifier 4D: V1, a 15 V peak, 50 Hz sine across a four-diode bridge, into C1 = 4700 µF and C2 = 1 µF at /Vin. Rz1 = 4.7 kΩ feeds D5, a 5.6 V BZX84C5V6 zener (vendor model `BZX84C5V6.LIB`), which sets the reference /Uz. U1 runs from /Vin and ground, with /Uz on its non-inverting input. Its output drives the base of Q1, the default NPN, which passes current from /Vin to Out. R3 = 1 kΩ from Out and R1 = 1629 Ω to ground feed a fraction of Out back to U1's inverting input. C3 = 1 µF and Rload1 = 8 Ω load Out. The transient analysis runs for 100 ms.

## What To Look For

- The op-amp drives Q1 until the divider's tap equals the zener voltage. So Vout = Vz × (1 + R3/R1) = 5.6 V × (1 + 1000/1629) = 9.04 V.
- Unlike Rectifier 4D Regulator NPN, Q1's Vbe is inside the loop, so the output does not move with it.
- The reservoir still ripples, about 11.4–13.3 V at /Vin, and the output stays flat.

The simulation gives 9.01 V at Out, flat to within a few millivolts.

## How To Run

Open `Rectifier-4D-OPamp-NPN.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Vin), the source voltage V(In1) − V(In2), and V(Out).

## Try This

- R1 is a variable resistor: change it to set the output. 1000 Ω gives 5.6 × 2 = 11.2 V, which is close to the ripple troughs, so expect the output to dip.
- Replace the zener with a precision reference and the output becomes as accurate as the reference and the two resistors.
