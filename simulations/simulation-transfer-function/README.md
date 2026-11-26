# Simulation Transfer Function

A transfer-function analysis (`.tf`) finds a circuit's DC gain, input impedance and output impedance in one run: for an inverting amplifier of gain −4.7, it gives −4.69866, 10,002.35 Ω and 2.85 mΩ.

## Circuit

U1 runs from ±15 V, with its non-inverting input grounded. V1 drives R1 = 10 kΩ into the inverting input, and R2 = 47 kΩ feeds back from Out. U1 uses `kicad_builtin_opamp.lib`: open-loop gain A = 20,000, output resistance ROUT = 10 Ω. The workbook runs `.tf v(Out) V1`: the small-signal transfer from V1 to V(Out), at the DC operating point. V1 only names the input: replaced by a 1 V DC source, it gives the same three figures.

## What To Look For

- `.tf` reports three numbers: the gain V(Out)/V1 as `transfer_function`, the resistance V1 sees as `v1#input_impedance`, and the resistance looking back into Out as `output_impedance_at_v(out)`.
- With an ideal op-amp they would be −R2/R1 = −47 kΩ / 10 kΩ = −4.70, R1 = 10 kΩ, and 0.
- U1's gain is finite. The feedback fraction is β = R1 / (R1 + R2) = 10/57 = 0.1754, so the loop gain is T = A · β = 3508.8, and the gain falls to −4.70 / (1 + 1/T) = −4.69866.
- The inverting input is held near ground only to within 1/A, so from there R2 looks like R2 / (1 + A) = 47 kΩ / 20,001 = 2.35 Ω. The input impedance is R1 + 2.35 Ω = 10,002.35 Ω.
- Feedback divides U1's output resistance by 1 + T: 10 Ω / 3509.8 = 2.85 mΩ.

The simulation gives a gain of −4.69866, an input impedance of 10,002.35 Ω and an output impedance of 2.850 mΩ.

## How To Run

Open `Simulation-Transfer-Function.kicad_sch` in KiCad, click **Simulate**, and run the TF tab. KiCad's analysis dialog has no transfer-function type, so the tab is a Custom one holding `.tf v(Out) V1`. It draws no plot, and points to the console for the results.

## Try This

- Set R1 to 4.7 kΩ for an ideal gain of −10. Now T = 20,000 × 4.7/51.7 = 1818.2, so the gain is −10 / (1 + 1/1818.2) = −9.99450, the input impedance 4,702.35 Ω and the output impedance 10 Ω / 1819.2 = 5.50 mΩ. The simulation gives the same.
- Set R2 to 100 kΩ instead, with R1 back at 10 kΩ. β is again 1/11, so the gain and output impedance are as above, but the input impedance stays near R1: 10 kΩ + 100 kΩ / 20,001 = 10,005.00 Ω. The simulation gives the same.
