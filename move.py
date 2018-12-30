#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B


motor = LargeMotor(OUTPUT_B)
motor.on_for_rotations(SpeedPercent(25), 2)
