# KiCad Simulation Commands

A cheat sheet: the same sources written the KiCad way and the PSPICE/LTspice way, the four main analysis commands, and an annotated key to their fields.

## Circuit

Ten 1 kΩ resistors, each driven by its own source, in pairs:

| Row | Left (KiCad fields) | Right (PSPICE text) | Directive |
|---|---|---|---|
| 1 | V1: 100 V, 50 Hz sine | V2: `sin(0 100 50 0 0 0)` | `.tran .1m 100m` |
| 2 | V3: ±50 V pulse, 10 ms on, 20 ms period | V4: `pulse(-50 50 0 0 0 10m 20m)` | `.tran .1m 100m` |
| 3 | V5: 1 V, 1 kHz sine, `ac=1` | V6: `dc 0 ac 1` | `.ac dec 1000 1 1meg` |
| 4 | V7: 5 V DC | V8: 5 V DC | `.op` |
| 5 | V9: 5 V DC | V10: 5 V DC | `.dc R9 10 1k 10` |

The right-hand panel spells out what each field of `sin(...)`, `pulse(...)`, `.dc`, `.ac` and `.tran` means.

## What To Look For

- Both ways describe the same waveform. KiCad builds V1's line from its fields, `DC 0 SIN( 0 100 50 0 0 0 ) AC 1`, and passes V2's text through as written, `sin(0 100 50 0 0 0)`.
- Every directive on the sheet starts with `;`, which makes it a comment, so this schematic has no analysis set up and nothing runs until you choose one.

## How To Run

Open `KiCad-Simulation-commands.kicad_sch` in KiCad. Delete the `;` in front of one directive, for example `;.tran .1m 100m`, then click **Simulate** and run it. Probe the Out net of the row that directive belongs to. Put the `;` back before trying the next one.

## Try This

- Run the `.dc R9 10 1k 10` row: it sweeps a resistor instead of a source, from 10 Ω to 1 kΩ, and the current through R9 traces 5 V / R.
- Compare a source's fields in its Simulation Model dialog with the PSPICE text beside it.
