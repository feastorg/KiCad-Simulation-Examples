# Simulation Temperature Sweep

A DC sweep can step the circuit's temperature instead of a source: a diode carrying 1 mA drops 0.6587 V at 25 °C and 0.5509 V at 85 °C, −1.80 mV/K.

## Circuit

I1 drives a constant 1 mA into D1, from node a to ground. D1 uses KiCad's default diode model, as in Simulation Diode Characteristics: saturation current Is = 10⁻¹⁴ A, emission coefficient n = 1, and the SPICE defaults that set how Is changes with temperature, band gap EG = 1.11 eV and exponent XTI = 3. The workbook runs `.dc TEMP -40 85 5`: the temperature from −40 °C to 85 °C in 5 °C steps.

## What To Look For

- Is is the saturation current at the nominal temperature, 27 °C or T0 = 300.15 K. There Vf0 = VT0 · ln(1 mA / Is) = 25.865 mV × 25.328 = 0.65511 V, with VT = kT/q.
- Is grows quickly with temperature, so at a fixed current the diode's voltage falls. For this model, Vf(T) = EG − (T/T0) · (EG − Vf0) − 3 · VT · ln(T/T0), which gives 0.6587 V at 25 °C and 0.5509 V at 85 °C.
- Between those two points the slope is (0.5509 − 0.6587) V / 60 K = −1.80 mV/K. The formula's derivative is dVf/dT = (Vf − EG − 3 · VT) / T: at 25 °C, (0.6587 − 1.11 − 0.0771) V / 298.15 K = −1.77 mV/K.
- The textbook −2 mV/K belongs to a lower Vf. The same derivative is −2 mV/K at 25 °C when Vf = EG + 3 · VT − 2 mV/K × 298.15 K = 0.591 V.

The simulation gives Vf = 0.6587 V at 25 °C and 0.5509 V at 85 °C.

## How To Run

Open `Simulation-Temperature-sweep.kicad_sch` in KiCad, click **Simulate**, and run the DC tab. It plots V(/a) against temperature. In the tab's simulation command, the DC sweep's source type is TEMP.

## Try This

- Set I1 to 100 µA. Vf at 25 °C falls by VT · ln 10 = 59.2 mV to 0.5995 V, and the simulated slope from 25 °C to 85 °C steepens to −2.00 mV/K.
- Set I1 to 10 mA. The simulated Vf at 25 °C is 0.7178 V, and the slope eases to −1.60 mV/K.
