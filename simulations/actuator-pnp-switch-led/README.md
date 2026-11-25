# Actuator PNP Switch LED

A high-side PNP switch: the LED lights while the 3.3 V logic signal is low, the opposite of the NPN version.

## Circuit

V1 stands in for a microcontroller pin: a 0 to 3.3 V square wave, high for 1 ms of every 2 ms. Through Rb1 = 1 kΩ it drives Q1's base. Q1 is a PNP with its emitter on the 3.3 V supply. The LED D1 and Rk1 = 150 Ω run from Q1's collector to ground. The LED uses its own model, `LED.lib`. The transient analysis runs for 20 ms.

## What To Look For

- A PNP turns on when its base is pulled below its emitter. Input low (1 to 2 ms in each period): base current flows out of the base, (3.3 V − 0.85 V) / 1 kΩ ≈ 2.5 mA, and Q1 saturates.
- The LED current is the same as in the NPN version, about 9.9 mA.
- Input high: base and emitter are both at 3.3 V, Q1 is off, and the LED is dark.

The simulation gives 9.86 mA through the LED while the input is low, and −2.46 mA of base current; the minus sign means it flows out of the base.

## How To Run

Open `Actuator-PNP-switch-LED.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots I(D1) and I(Q1:b).

## Try This

- Raise the supply to 5 V while keeping a 3.3 V input: a high input no longer turns Q1 fully off, because the base is still 1.7 V below the emitter. That is why high-side switches from a lower logic voltage need a level shifter.
