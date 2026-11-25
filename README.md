# KiCad Simulation Examples

[![CI](https://github.com/feastorg/KiCad-Simulation-Examples/actions/workflows/ci.yml/badge.svg)](https://github.com/feastorg/KiCad-Simulation-Examples/actions/workflows/ci.yml)

40 KiCad 10 schematics that teach circuit simulation with KiCad's built-in ngspice
simulator, from an RC filter to a regulated power supply. Each one is ready to simulate,
and its README states what it should show, with the numbers worked out from the circuit.

<p>
  <img src="https://feastorg.github.io/KiCad-Simulation-Examples/assets/simulations/rc-lowpass/schematic.png" alt="RC Lowpass schematic: a 10 ohm resistor feeding a 1 uF capacitor" width="48%">
  <img src="https://feastorg.github.io/KiCad-Simulation-Examples/assets/simulations/rc-lowpass/ac.svg" alt="RC Lowpass AC sweep: gain flat to about 1 kHz, -3 dB near 16 kHz, then falling" width="48%">
</p>

*[RC Lowpass](https://feastorg.github.io/KiCad-Simulation-Examples/simulations/rc-lowpass/): 10 Ω and 1 µF put the −3 dB corner at 1/(2πRC) = 15.9 kHz. The simulation puts it at 15.9 kHz.*

## What's Inside

Browse it all on the site: **https://feastorg.github.io/KiCad-Simulation-Examples/**

| Chapter | Examples |
|---|---|
| [Simulator Basics](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/simulator-basics/): operating point, DC sweep, AC sweep, transient | 6 |
| [Passive RC and RL](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/passive-rc-rl/): time constants, corners, phase | 7 |
| [Resonance and Magnetics](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/resonance-magnetics/): LC resonance, transformers | 4 |
| [Diodes and Rectifiers](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/diodes-rectifiers/): diode curve, half-wave to three-phase bridge | 5 |
| [Transistors](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/transistors/): BJT curves, switches, amplifiers | 5 |
| [Op-Amps](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/op-amps/): followers, amplifiers, summer, comparator, open loop | 7 |
| [Power Supplies](https://feastorg.github.io/KiCad-Simulation-Examples/chapters/power-supplies/): linear regulators, polarity and overvoltage protection | 6 |

## Checked by Simulation

On every pull request, CI exports each example's netlist with kicad-cli, runs its analyses
in ngspice, and checks the figures its README states against `expect.toml`. One example,
KiCad Simulation Commands, is a cheat sheet with no analysis set up, so it has nothing to
check.

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
