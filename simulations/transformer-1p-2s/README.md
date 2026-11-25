# Transformer 1P 2S

A transformer with one primary and two secondaries, each giving 32.5 V, one of them inverted.

## Circuit

V1, a 325 V peak sine at 50 Hz, drives the primary L1 = 10 H. Two secondaries, L2 and L3 = 100 mH each, feed Rl1 and Rl2 = 1 kΩ. The text directives `K1 L1 L2 1.0`, `K2 L1 L3 1.0` and `K3 L2 L3 1.0` couple all three windings with K = 1. L3 is connected the other way round from L2: its first pin goes to ground. R1 = 1 GΩ gives the primary side a DC path to ground. The transient analysis runs for 100 ms.

## What To Look For

- Each secondary has the ratio √(L1/L2) = √(10 H / 100 mH) = 10, so both peak at 32.5 V.
- Because L3 is reversed, Us2 is the inverse of Us1: it peaks half a cycle, 10 ms, after Us1. Together the two windings act like one 65 V centre-tapped secondary.

The simulation gives 32.5 V on each secondary, with Us2 crossing 20 V 10.0 ms after Us1.

## How To Run

Open `Transformer-1P-2S.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(/Vp), V(Us1) and V(Us2).

## Try This

- Plot V(Us1) − V(Us2): the two windings in series give 65 V peak.
- Reverse L3's connections and Us2 lines up with Us1.
