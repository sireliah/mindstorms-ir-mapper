
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
    (_, _) = sock.recvfrom(4096)


def get_prox() -> None:
    speed = SpeedPercent(25)
    degrees = 90
    sensor = InfraredSensor()
    motor = MediumMotor(OUTPUT_D)

    motor.on_for_degrees(speed, degrees, block=False)

    while motor.is_running:
        sleep(INTERVAL)
        metrics = f'{motor.count_per_rot} {sensor.proximity}'
        send_data_to_server(metrics, ADDRESS)


if __name__ == '__main__':
    get_prox()
