# NPN Differential Pair

Two NPNs share a 1 mA tail current and amplify the difference between their bases by gm·RC = 191.40, and a larger difference drives the output toward its ±9.901 V limit.

## Circuit

V1 = 15 V makes VCC = +15 V, and V2 = 15 V, with its + terminal on ground, makes VEE = −15 V, as the simulation gives. I1 is ideal and pulls 1 mA whatever VEE is, so the collectors cannot show a wrong V2: with V2 reversed or set to 5 V they stay exactly where they are, and only VEE moves. R1 = R2 = 10 kΩ run from VCC to the collectors, C1 and C2. Q1 and Q2 are KiCad's Gummel-Poon NPN with its default model: β = 100 and no Early effect. Their emitters join at Tail, and the ideal current source I1 pulls 1 mA from Tail to VEE. V3 sets Vd on In, Q1's base, and Q2's base is grounded. The output is V(C2) − V(C1). The workbook runs `.dc V3 -0.2 0.2 1m`, sweeping Vd from −0.2 V to 0.2 V.

## What To Look For

- Bias: at Vd = 0 the tail current splits evenly. Each collector carries α·Itail/2, with α = β / (β + 1) = 100/101 = 0.990099, so 0.495050 mA, and both collectors sit at 15 V − 10 kΩ × 0.495050 mA = 10.0495 V.
- Gain: each transistor has gm = Ic / VT = 0.495050 mA / 25.8649 mV = 19.1398 mS, where VT = kT/q at 27 °C. A small Vd turns one transistor up and the other down by the same amount, so the differential gain is Ad = gm·RC = 19.1398 mS × 10 kΩ = 191.40.
- Large signal: the collector currents split as α·Itail/2 · (1 ± tanh(Vd / 2VT)), so the output is α·Itail·RC · tanh(Vd / 2VT) = 9.90099 V × tanh(Vd / 51.7298 mV). At Vd = 1 mV, tanh(0.0193312) = 0.0193288: V(C1) = 15 V − 4.950495 V × 1.0193288 = 9.95382 V, V(C2) = 15 V − 4.950495 V × 0.9806712 = 10.14519 V, and the output is 0.19137 V, a gain of 191.37. The curve has already started to bend, so this is just under gm·RC.
- Saturation: the output can never exceed α·Itail·RC = 0.990099 mA × 10 kΩ = 9.90099 V, when all of the tail current flows in one transistor. At Vd = ±4VT = ±103.46 mV it reaches tanh(2) = 96.40 % of that, ±9.5448 V. At Vd = 0.2 V, tanh(3.86624) = 0.999124, so V(C1) = 15 V − 4.950495 V × 1.999124 = 5.10335 V, V(C2) = 14.99566 V, and the output is 9.89231 V.

The simulation gives V(C1) = 9.95382 V and V(C2) = 10.14519 V at Vd = 1 mV, an output of 0.19137 V. At 0.2 V it gives V(C1) = 5.10335 V and an output of 9.89231 V, and at 103.46 mV an output of 9.5448 V.

## How To Run

Open `NPN-Differential-Pair.kicad_sch` in KiCad, click **Simulate**, and run the DC tab. It plots V(/C1), V(/C2) and the output, V(/C2)-V(/C1), against Vd.

## Try This

- Set R2 to 10.5 kΩ, 5 % high. At Vd = 0, C2 drops 0.5 kΩ × 0.495050 mA further than C1, so the output reads −0.24752 V with no input, and the simulation gives the same. A mismatch between the two sides shows up as an offset.
- Replace I1 with the mirror from NPN Current Mirror, without its `vaf=50`: Q3 diode-connected, R3 = 14.3 kΩ from ground into its collector, both emitters on VEE, and Q4's collector on Tail. The simulation gives Iref = 0.994854 mA, so Itail = Iref / (1 + 2/β) = 0.975347 mA. Ad falls to 0.990099 × 0.487674 mA / 25.8649 mV × 10 kΩ = 186.68, and the limit to α·Itail·RC = 9.6569 V. The simulation gives 0.18666 V at Vd = 1 mV and 9.6484 V at 0.2 V.
