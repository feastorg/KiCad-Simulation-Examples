# Contributing

Fixes are welcome as pull requests. For a new example, or a change to what an existing
circuit does, open an issue first so we can agree on what it should teach.

## Working on it

```sh
just check   # shellcheck, compile the scripts, check the simulation folder layout
just test    # check each expect.toml, then simulate and plot every example (needs kicad-cli, ngspice)
just docs    # build the site artifacts under docs/ (needs KiCad, ngspice, rsvg-convert, Pillow)
```

Run `just check && just test` before every commit. The examples target KiCad 10; open
and save them in KiCad 10.

How to lay out an example and what its README needs is on the site:
[Contributing a Simulation](docs/contributing.md).

## Rules

- Do not commit `.kicad_prl` files. They hold your local window state, KiCad rewrites
  them on every open, and they are gitignored.
- After editing a schematic, export its SPICE netlist before and after the change and
  compare them. The difference should be the change you meant and nothing else:

  ```sh
  kicad-cli sch export netlist --format spice -o before.cir <example>.kicad_sch
  ```

- A README states numbers worked out from the schematic, such as the cutoff, gain or
  ripple, and the formula behind them. The example's `expect.toml` checks the key ones,
  and every figure it checks is stated in the README: each
  `[[measure]]` names an analysis from the `.wbk`, an ngspice `meas` expression, the
  expected value and a tolerance: `rtol`, relative, or `atol`, absolute, for a value that
  should be near zero. For an `op` analysis, `meas` is an expression such as `v(out)`.
  See `simulations/rc-lowpass/expect.toml`.
- SPICE models sit next to the schematic that uses them and are referenced by a path
  relative to the project.
- `docs/index.md`, `docs/simulations/`, `docs/assets/simulations/` and
  `docs/assets/downloads/` are generated. Change the scripts in `scripts/` instead.

## Pull requests

Branch from `main` and open a pull request against it. Pull requests are squash-merged,
and the title and description become the commit, so say what changed and how you know
it works. Titles follow [Conventional Commits](https://www.conventionalcommits.org):
`type(scope): description`.

## Reporting a problem

Open an issue naming the example, your KiCad and ngspice versions, what you expected to
see, and what the simulator showed instead.

## License

The examples are CC0 1.0, and a contribution is made under the same terms. A
third-party SPICE model keeps its own license: say where it came from in the example's
README.
