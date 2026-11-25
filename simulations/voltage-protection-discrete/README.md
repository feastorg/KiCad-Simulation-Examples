# Voltage Protection Discrete

Four ways to protect a load from a supply connected backwards or set too high, built from diodes, MOSFETs and transistors.

## Circuit

V1, a ±12 V sine at 10 Hz, stands for a bad supply: its negative half is a reversed connection, and its 12 V peak is an overvoltage. It feeds four circuits, each into a 5 Ω load:

1. **Out1**, polarity protection with a diode: D2 in series.
2. **Out2**, polarity protection with a P-MOSFET: Q3 in the supply line, gate to ground.
3. **Out3**, diode polarity protection plus overvoltage cut-off: D4, then P-MOSFET Q5. Q5 is switched off by Q4 when the rail passes the 5.6 V zener D3 (via R3 = 4.7 kΩ) plus a Vbe.
4. **Out4**, P-MOSFET polarity protection (Q8) plus the same cut-off (D6, Q6, Q7).

The zeners use the vendor model `BZX84C5V6.spice.txt`. The transient analysis runs for 100 ms, one cycle.

## What To Look For

- All four outputs stay at 0 V through the negative half-cycle: the reversed supply never reaches the load.
- Out1 loses a diode drop, about 0.85 V at 2.2 A, so it peaks at 11.15 V. Out2's MOSFET is fully on once its source rises, and loses only about 0.02 V.
- Out3 and Out4 follow the input until the rail reaches about 5.6 V + 0.6 V. Then Q4 or Q6 turns on, pulls the output MOSFET's gate up, and switches the load off. At the 12 V peak they read under 1 mV.

The simulation gives peaks of 11.15 V, 11.98 V, 5.91 V and 5.90 V, 0 V on the negative half, and 0.6 mV at Out3 and Out4 at the 12 V peak.

## How To Run

Open `Voltage-protection-discrete.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots V(Vdc) and V(Out4). Add V(Out1) to V(Out3) to compare all four.

## Try This

- Compare the heat in D2 and Q3 at 2.2 A: about 0.85 V × 2.2 A ≈ 1.9 W against 0.02 V × 2.4 A ≈ 0.05 W. That is why MOSFET polarity protection is preferred at high currents.
- Change D6 to a higher-voltage zener to raise Out4's cut-off.
