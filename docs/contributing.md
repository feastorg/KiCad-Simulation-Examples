---
layout: default
title: Contributing a Simulation
parent: KiCad Simulation Examples
nav_order: 10
---

Thanks for helping expand the KiCad Simulation Examples library. This site is built directly
from the contents of each simulation folder, so a clean structure and a clear README are the
most important parts of a good contribution.

## Required Files

Each simulation must live under `simulations/<name>/` and include:

- One `*.kicad_sch` schematic and its `*.kicad_pro` project file
- The `*.wbk` simulator workbook, which holds the analysis commands and plotted traces
- `README.md` with a single H1 title and a short first paragraph
- Any required SPICE models (`.lib`, `.spice`, etc.) stored alongside the schematic

Do not commit the `*.kicad_prl` file: it holds your local KiCad window state.

Add the folder's name to one chapter in `simulations/chapters.toml`, in the place a reader
should meet it. The site is built in that order. Run `just check` to confirm the folder
layout and that every example is in exactly one chapter.

## README Template

Use this as a starting point for each simulation README. The RC examples, such as
`simulations/rc-charge/README.md`, follow it.

```markdown
# Title of Simulation

One sentence: what the circuit shows, with its key figure.

## Circuit

The source, the parts with their values, which node is Out, and what each analysis in
the workbook runs.

## What To Look For

Each figure the simulation should show, with the formula and the values that give it.
End with the numbers the simulation actually gives.

## How To Run

Open `<schematic>.kicad_sch` in KiCad, click **Simulate**, and run the configured tabs.
Say which traces each tab plots.

## Try This

A change to make and what it does, worked out from the same formulas.
```

The key single-number figures in What To Look For also go in the example's
`expect.toml`, which CI checks on every pull request. Every figure `expect.toml` checks
should appear in the README, so a reader can see what is being held to. See
`CONTRIBUTING.md` in the repository for its format.

## Naming

- Use lowercase kebab-case for folder names (for example: `rc-lowpass`).
- Keep names short but descriptive.

## Assets

CI renders the schematic and simulates the workbook's analyses, and the site shows both
under each example's README. Add other images only when they show something those don't,
with relative paths under the same simulation directory.
