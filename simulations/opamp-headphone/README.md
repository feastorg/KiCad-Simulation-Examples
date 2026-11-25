# OPamp Headphone

A non-inverting stage with a gain of 5.7, AC-coupled at the input, with its feedback taken after a 47 Ω output resistor.

## Circuit

U1 runs from ±15 V. V3, a 1 V sine at 1 kHz with an AC value of 1, reaches the non-inverting input through C1 = 1 µF, with R1 = 100 kΩ to ground. The op-amp's output goes through R4 = 47 Ω to Out. The feedback comes from Out: R3 = 4.7 kΩ to the inverting input, and R2 = 1 kΩ from there to ground. U1 uses `kicad_builtin_opamp.lib`. The workbook runs an AC sweep from 1 Hz to 100 kHz and a 5 ms transient. No headphone load is connected.

## What To Look For

- Gain = 1 + R3 / R2 = 1 + 4.7 = 5.7 (15.1 dB).
- C1 and R1 block DC at the input: a high-pass corner at 1/(2π · 100 kΩ · 1 µF) = 1.59 Hz, well below the audio band.
- Because the feedback is taken after R4, the loop drives Out itself to the right voltage. The 47 Ω only limits current if the output is shorted or loaded hard.

The simulation gives a gain of 5.70 at 1 kHz and a low corner at 1.59 Hz.

## How To Run

Open `OPamp-headphone.kicad_sch` in KiCad, click **Simulate**, and run the AC and transient tabs. The AC tab plots the gain of V(In) and V(Out); the transient tab plots V(/Vi) and V(Out).

## Try This

- Add a 32 Ω headphone load from Out to ground and lower the input to 0.5 V: the gain holds at 5.7, because the loop corrects for the drop across R4. At 1 V in, the op-amp would need about 16 V behind R4 and the model's 10 Ω output resistance, more than its 15 V rail, so it clips.
- Move R3's connection to the op-amp's output, before R4, and the 47 Ω now divides against the load.
