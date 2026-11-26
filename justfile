# KiCad Simulation Examples task runner

set dotenv-load := false

# Show available recipes
default:
    @just --list

# Lint the shell and Python scripts and the simulation folder layout (CI-equivalent)
check:
    shellcheck scripts/*.sh
    python3 -m py_compile scripts/*.py
    python3 scripts/check_layout.py

# Test the harness, check every expect.toml, then simulate and plot every example into build/plots (needs kicad-cli, ngspice)
test:
    python3 scripts/test_simulate.py
    python3 scripts/simulate.py
    python3 scripts/simulate.py --plots build/plots

# Build the docs site artifacts under docs/ (needs KiCad, ngspice, rsvg-convert and Pillow)
docs:
    bash scripts/build_docs.sh
