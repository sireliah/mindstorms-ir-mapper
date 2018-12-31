
import math
from typing import Tuple
import socket

ADDR = ('192.168.0.11', 5000)


def parse_data(data: bytes) -> Tuple[int, int]:
    return (int(a) for a in data.split(b' '))


def calculate_coords(angle: int, distance: int) -> Tuple[float, float]:
    if (angle > 90 and angle <= 180) or (angle > 270 and angle <= 360):
        angle = 90 - angle
    elif angle > 180 and angle <= 270:
        angle = angle - 270

    x = math.cos(math.radians(angle)) * distance
    y = math.sin(math.radians(angle)) * distance
    return (x, y)


def receive_data(sock) -> bytes:
    data, address = sock.recvfrom(4096)
    print(f'Got {len(data)} bytes from {address}.')
    if data:
        print(str(data))
        return parse_data(data)


def run_server(bind_addr) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(bind_addr)
    print(f'Listening on {bind_addr}.')
    while True:
        (angle, distance) = receive_data(sock)
        print(angle, distance)


if __name__ == '__main__':
    run_server(ADDR)
