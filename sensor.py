
from time import sleep
from typing import Tuple
import socket

from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.motor import MediumMotor, SpeedPercent, OUTPUT_D

ADDRESS = ('192.168.0.11', 5000)
INTERVAL = 0.1


def send_data_to_server(data: str, address: Tuple) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(data.encode('utf-8')), address)
    response_data, server = sock.recvfrom(4096)
    print(response_data)


def run_angle(motor: MediumMotor, speed: SpeedPercent, angle: int) -> None:
    while motor.is_running:
        sleep(INTERVAL)


def get_prox() -> str:
    speed = SpeedPercent(25)
    degrees = 90
    sensor = InfraredSensor()
    motor = MediumMotor(OUTPUT_D)

    motor.on_for_degrees(speed, degrees, block=False)

    while motor.is_running:
        sleep(INTERVAL)
        rotated_degrees = motor.count_per_rot
        metrics = f'{rotated_degrees} {sensor.proximity}'
        send_data_to_server(metrics, ADDRESS)


if __name__ == '__main__':
    get_prox()
