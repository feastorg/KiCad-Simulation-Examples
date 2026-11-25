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

# Run every simulation and assert its expected results
test:
    @echo "test: SKIPPED, no simulation harness yet (issue #4)"

# Build the docs site artifacts under docs/ (needs KiBot, KiCad and rsvg-convert)
docs:
    bash scripts/build_docs.sh
