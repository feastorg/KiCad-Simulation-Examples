# KiCad Simulation Examples

[![CI](https://github.com/feastorg/KiCad-Simulation-Examples/actions/workflows/ci.yml/badge.svg)](https://github.com/feastorg/KiCad-Simulation-Examples/actions/workflows/ci.yml)

58 KiCad 10 schematics that teach circuit simulation with KiCad's built-in ngspice
simulator, from an RC filter to a buck converter. Each README states what the
example should show, with the numbers worked out from the circuit, and 57 of the 58 come
with their analyses already set up; the 58th is a cheat sheet of simulator commands.

<p>
  <img src="https://feastorg.github.io/KiCad-Simulation-Examples/assets/simulations/rc-lowpass/schematic.png" alt="RC Lowpass schematic: a 10 ohm resistor feeding a 1 uF capacitor" width="32%">
  <img src="https://feastorg.github.io/KiCad-Simulation-Examples/assets/simulations/rc-lowpass/ac.svg" alt="RC Lowpass AC sweep: gain flat to about 1 kHz, -3 dB near 16 kHz, then falling" width="64%">
</p>

*[RC Lowpass](https://feastorg.github.io/KiCad-Simulation-Examples/simulations/rc-lowpass/): 10 Ω and 1 µF put the −3 dB corner at 1/(2πRC) = 15.9 kHz. The simulation puts it at 15.9 kHz.*

## What's Inside

Browse it all on the site: **https://feastorg.github.io/KiCad-Simulation-Examples/**

| Chapter | Examples |
|---|---|
| [Simulator Basics](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/simulator-basics/): operating point, DC sweep, AC sweep, transient, behavioral and PWL sources | 7 |
| [Passive RC and RL](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/passive-rc-rl/): time constants, corners, phase | 7 |
| [Resonance and Magnetics](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/resonance-magnetics/): LC resonance, RLC step response, transformers | 5 |
| [Diodes and Rectifiers](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/diodes-rectifiers/): diode curve, half-wave to three-phase bridge | 5 |
| [Transistors](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/transistors/): BJT curves, switches, amplifiers, current mirror, differential pair | 8 |
| [Op-Amps](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/op-amps/): followers, amplifiers, summer, integrator, differentiator, active filter, comparator, Schmitt trigger, oscillator, open loop | 12 |
| [Power Supplies](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/power-supplies/): linear regulators, polarity and overvoltage protection, a buck converter | 7 |
| [Analysis Techniques](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/analysis-techniques/): temperature sweep, noise, pole-zero, transfer function, measurements, vendor models, Multi Run | 7 |

## Checked by Simulation

On every pull request, CI exports each example's netlist with kicad-cli, runs its analyses
in ngspice, and checks the key figures its README states, the ones listed in its
`expect.toml`. One example, KiCad Simulation Commands, is a cheat sheet with no analysis
set up, so it has nothing to check.

## Getting Started

1. Open an example's `.kicad_sch` from [`simulations/`](simulations/) in KiCad 10.
2. Click **Simulate** and run the analyses already set up in its workbook.

Or download everything: [all schematics as PDFs](https://feastorg.github.io/KiCad-Simulation-Examples/assets/downloads/schematics-pdf.zip),
or [the full kit](https://feastorg.github.io/KiCad-Simulation-Examples/assets/downloads/schematics-kit.zip)
with every KiCad project, workbook and model.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits and License

The examples were created by Ole Johan (GitHub: OJStuff) and first published in the
OJStuff/Schematics-Examples repository. That repository is no longer available on GitHub.
This collection continues from its last commit, `03500e1` (2025-04-03), which is part of
this repository's history.

The work is released under CC0 1.0, except for third-party SPICE model files, which keep
their authors' copyright. See [LICENSE.md](LICENSE.md).
