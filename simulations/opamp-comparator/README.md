# OPamp Comparator

An op-amp used without feedback as a comparator: its output snaps between the supply rails as a light-dependent divider crosses a 0 V threshold.

## Circuit

U1 runs from ±15 V. R2 and R3, 4.7 kΩ each between +15 V and −15 V, hold the inverting input at 0 V. The non-inverting input sits between Rpot1 = 4.7 kΩ, to +15 V, and R1, to −15 V. R1 stands for a light-dependent resistor. The DC sweep steps R1 from 1 kΩ to 10 kΩ, as darkness would. R4 = 10 kΩ loads the output. U1 uses `kicad_builtin_opamp.lib`.

## What To Look For

- V(/Vplus) = −15 V + 30 V · R1 / (R1 + 4.7 kΩ). It crosses 0 V exactly when R1 = Rpot1 = 4.7 kΩ.
- Below that the non-inverting input is lower than the inverting one, and the output sits at the negative rail. Above it the output swings to the positive rail. With a gain of 20,000 and no feedback, there is almost nothing in between.

The simulation gives the crossing at R1 = 4.70 kΩ, and an output of −14.99 V below it and +14.99 V above it.

## How To Run

Open `OPamp-comparator.kicad_sch` in KiCad, click **Simulate**, and run the DC tab. It plots V(/Vmin), V(/Vplus) and V(Out) against R1.

## Try This

- Change Rpot1 to set the switching threshold: the output flips wherever R1 = Rpot1.
- Feed a little of the output back to the non-inverting input through a large resistor, say 1 MΩ, to add hysteresis and stop chatter near the threshold.
