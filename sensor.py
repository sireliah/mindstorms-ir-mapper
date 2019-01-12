#!/usr/bin/env python3

import math
import socket
import sys
from time import sleep
from typing import Tuple

from ev3dev2.motor import (OUTPUT_B, OUTPUT_C, OUTPUT_D, MediumMotor,
                           MoveSteering, MoveTank, SpeedPercent)
from ev3dev2.sensor.lego import InfraredSensor

from robot_utils import prox_to_cm, robot_degrees_to_rotations

INTERVAL = 0.1
TRACK_RADIUS = 1.8   # cm
SPEED = 15


class Robot:
    def __init__(self):
        self.server_address = (str(sys.argv[1]), 5000)
        self.sensor = InfraredSensor()
        self.motor = MediumMotor(OUTPUT_D)
        self.drive_motor = MoveTank(OUTPUT_B, OUTPUT_C)
        self.turn_motor = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.moved = 0
        self.turned = 0

    def rotate_sensor(self, degrees: int, speed: int) -> None:
        # Motor input degrees are multuplied by 3 because of the gears setup.
        self.motor.on_for_degrees(
            SpeedPercent(speed),
            degrees * 3,
            block=False
        )

    def move_robot(self, distance: int, speed: int) -> None:
        rotations = distance / (2 * math.pi * TRACK_RADIUS)

        speed_percent_l, speed_percent_r = SpeedPercent(speed), SpeedPercent(speed)
        self.drive_motor.on_for_rotations(speed_percent_l, speed_percent_r, -rotations)
        self.moved += distance

    def turn_robot(self, degrees: int, speed: int) -> None:
        rotations = -robot_degrees_to_rotations(degrees)
        self.turn_motor.on_for_rotations(-100, SpeedPercent(speed), rotations)
        self.turned += degrees

    @staticmethod
    def send_data_to_server(data: str, address: Tuple) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(data.encode('utf-8')), address)

    def write_data(self) -> None:
        """
        Collect and send the metrics to the server.
        Please note that angle is divided by 3, because of the gears setup (1/3).
        """
        angle = self.motor.position / 3
        proximity = prox_to_cm(float(self.sensor.proximity))
        metrics = '{} {} {} {}'.format(angle, proximity, float(self.moved), float(self.turned))
        print(metrics)
        self.send_data_to_server(metrics, self.server_address)

    def rotate_and_listen(self, degrees: int, command: str) -> None:
        print(self.motor.position)
        i = 0
        while True:
            self.rotate_sensor(degrees, SPEED)
            while self.motor.is_running:
                self.write_data()

            sleep(0.1)

            self.rotate_sensor(-degrees, SPEED)
            while self.motor.is_running:
                self.write_data()

            sleep(0.1)
            i += 1
            if i == 2:
                if command == 'FORWARD':
                    self.move_robot(5.0, 25)
                elif command == 'TURN':
                    self.turn_robot(90, 25)
                i = 0

    def move(self) -> None:
        try:
            degrees = int(sys.argv[2])
        except IndexError:
            degrees = 90

        try:
            command = str(sys.argv[3])
        except IndexError:
            command = None
        self.rotate_and_listen(degrees, command)


if __name__ == '__main__':
    robot = Robot()
    robot.move()
