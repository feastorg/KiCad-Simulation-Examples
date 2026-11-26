# Simulation Pole-Zero

A pole-zero analysis finds the poles of a circuit's transfer function: the Sallen-Key low-pass has a complex pair at −4528 ± j4977 rad/s.

## Circuit

The circuit of OPamp Sallen-Key Lowpass: V3 drives In, R1 = R2 = 10 kΩ run from In through N1 to N2, C2 = 10 nF takes N2 to ground, C1 = 22 nF takes N1 to Out, and U1 is a follower from N2 to Out. U1 uses `kicad_builtin_opamp.lib`: open-loop gain 20,000 and a pole at 20 Hz. The workbook runs `.pz In GND Out GND vol pol`: the poles of the voltage transfer function from In to Out, both measured against GND. In the dialog, the transfer function is (output voltage) / (input voltage), and Find is set to Poles.

## What To Look For

- A second-order low-pass has the transfer function ω0² / (s² + (ω0/Q) · s + ω0²). Its poles, the roots of the denominator, are s = −ω0/(2Q) ± j · ω0 · √(1 − 1/(4Q²)), in rad/s. They are complex when Q > 0.5.
- With R1 = R2 = R, ω0/(2Q) = 1/(R · C1), and the poles are s = −1/(R · C1) ± j · √(C1/C2 − 1)/(R · C1) = −4545 ± j4979 rad/s for an ideal op-amp, with ω0 = 1/(R · √(C1 · C2)) = 6742 rad/s, 1073 Hz, and Q = 0.5 · √(C1/C2) = 0.742.
- Going back the other way, a pole's distance from the origin is ω0, and Q = |s| / (2 · |Re s|). The simulated poles give |s| = 6729 rad/s, 1071 Hz, and Q = 0.743.
- ngspice lists the poles as pole(1), pole(2) and pole(3), each as real,imaginary. The op-amp model brings a third pole: pole(1), at −2.517 × 10⁶ rad/s, 401 kHz, near the model's gain-bandwidth of 20,000 × 20 Hz = 400 kHz. pole(2) and pole(3) are the filter's pair. That order held in every variation run for this example, including those in Try This.
- The simulated real part is 0.4 % smaller than the ideal one. The op-amp's finite gain-bandwidth causes it: raising the model's pole a thousandfold (Try This) puts the filter's poles back on the ideal values.

The simulation gives the filter's poles at −4528 ± j4977 rad/s.

## How To Run

Open `Simulation-Pole-Zero.kicad_sch` in KiCad, click **Simulate**, and run the PZ tab. There is no plot: when the run ends, the console lists pole(1) to pole(3). ngspice also warns "Pole-zero iteration limit reached"; the poles it lists still agree, to the six digits printed, with a hand solution of this circuit, op-amp model included.

## Try This

- Make C1 = 47 nF: Q rises to 1.08, and the poles move toward the imaginary axis, computed at −2128 ± j4093 rad/s for an ideal op-amp. The simulation gives −2119 ± j4087 rad/s.
- Make C1 = 4.7 nF: Q falls to 0.343, below 0.5, and the pair splits into two real poles, computed at −36766 and −5787 rad/s. The simulation gives −36592 and −5791 rad/s, as pole(2) and pole(3).
- Set U1's POLE parameter to 20k, in its simulation model: the model's gain-bandwidth rises to 400 MHz. pole(1) moves out to −2.507 × 10⁹ rad/s, and the filter's poles to −4546 ± j4979 rad/s, within 0.01 % of the ideal values.
