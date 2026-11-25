# Actuator NPN Switch LED

A low-side NPN switch: a 3.3 V logic signal turns an LED on and off, with the transistor driven hard into saturation.

## Circuit

V1 stands in for a microcontroller pin: a 0 to 3.3 V square wave, high for 1 ms of every 2 ms. Through Rb1 = 1 kΩ it drives Q1's base. The LED D1 and Rk1 = 150 Ω run from the 3.3 V supply to Q1's collector, and the emitter is grounded. The LED uses its own model, `LED.lib`. The transient analysis runs for 10 ms.

## What To Look For

- Input high: the base current is (3.3 V − 0.85 V) / 1 kΩ ≈ 2.5 mA, far more than the LED current divided by β needs. So Q1 saturates and drops only about 0.05 V.
- The LED, about 1.77 V at 10 mA with this model, and Rk1 share the rest: (3.3 − 1.77 − 0.05) V / 150 Ω ≈ 9.9 mA.
- Input low: no base current, Q1 is off, and the LED is dark.

The simulation gives 2.46 mA of base current, 9.86 mA through the LED, and Vce = 0.047 V while on.

## How To Run

Open `Actuator-NPN-switch-LED.kicad_sch` in KiCad, click **Simulate**, and run the transient tab. It plots I(D1) and I(Q1:b).

## Try This

- Change Rk1 to set the LED current: 330 Ω gives about (3.3 − 1.71 − 0.05) V / 330 Ω ≈ 4.7 mA, since the LED drops a little less at the lower current.
- Raise Rb1 until Q1 drops out of saturation: with β = 100, it needs at least about 0.1 mA of base current for 10 mA.
- Compare Actuator PNP Switch LED, which switches the high side and inverts the logic.
