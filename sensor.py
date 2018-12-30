
from time import sleep
from ev3dev2.sensor.lego import InfraredSensor

from typing import Tuple
import socket

ADDRESS = ('192.168.0.11', 5000)


def send_data_to_server(data: str, address: Tuple) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(data.encode('utf-8')), address)
    response_data, server = sock.recvfrom(4096)
    print(response_data)


def get_prox() -> str:
    sensor = InfraredSensor()
    while True:
        sleep(0.1)
        prox = str(sensor.proximity)
        send_data_to_server(prox, ADDRESS)


if __name__ == '__main__':
    get_prox()
