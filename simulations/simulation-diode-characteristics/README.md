# Simulation Diode Characteristics

A DC sweep traces a diode's exponential current-voltage curve, showing why a silicon diode "turns on" at around 0.6–0.7 V.

## Circuit

V1 drives D1 in series with R1 = 100 Ω to ground. D1 uses KiCad's default diode model: saturation current Is = 10⁻¹⁴ A, emission coefficient n = 1. The workbook sweeps V1 from 0 to 2 V in 10 mV steps and plots I(D1), V(/a), and the diode voltage V(/a) − V(/k).

## What To Look For

- The diode current is I = Is · (e^(Vd/VT) − 1), with VT = kT/q = 25.9 mV at 27 °C. Every 60 mV more across the diode multiplies the current by ten.
- At 1 mA the diode drops VT · ln(1 mA / 10⁻¹⁴ A) = 0.655 V. With R1's 0.1 V on top, V(/a) is 0.755 V.
- At V1 = 2 V the diode drops about 0.72 V and R1 takes the rest: (2 − 0.72) V / 100 Ω = 12.8 mA.

The simulation gives V(/a) = 0.755 V at 1 mA and 12.8 mA at V1 = 2 V.

## How To Run

Open `Simulation-Diode-characteristics.kicad_sch` in KiCad, click **Simulate**, and run the DC tab. It plots I(D1), V(/a) and V(/a) − V(/k) against V1.

## Try This

- Plot I(D1) on a logarithmic axis: the curve becomes a straight line, one decade per 60 mV.
- Replace D1's model with a real part such as a 1N4148 to see a different Is and n.
