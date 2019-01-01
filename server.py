#!/usr/bin/env python3.7
from dataclasses import dataclass
import math
from typing import Tuple
import threading
import queue
import socket
import time

from renderer import Renderer

ADDR = ('192.168.0.11', 5000)


@dataclass
class Point:
    x: float
    y: float


class Receiver:
    def __init__(self):
        bind_addr = ADDR
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(bind_addr)
        print(f'Listening on {bind_addr}.')

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[float, float]:
        data, address = self.sock.recvfrom(4096)
        return parse_data(data)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sock.close()


def parse_data(data: bytes) -> Tuple[float, float]:
    return (float(a) for a in data.split(b' '))


def render_points(coord_queue: queue.Queue) -> None:
    rend = Renderer()
    while True:
        point = coord_queue.get()
        rend.render(point.x, point.y)


def calculate_coords(angle: float, distance: float) -> Tuple[float, float]:
    # if (angle > 90 and angle <= 180) or (angle > 270 and angle <= 360):
    #     angle = 90 - angle
    # elif angle > 180 and angle <= 270:
    #     angle = angle - 270

    x = math.cos(math.radians(angle)) * distance
    y = math.sin(math.radians(angle)) * distance
    return (x, y)


def run_server() -> None:
    coord_queue = queue.Queue()
    render_thread = threading.Thread(target=render_points, args=[coord_queue, ])
    render_thread.start()

    with Receiver() as receiver:
        for (angle, distance) in receiver:
            (x, y) = calculate_coords(angle, distance)
            point = Point(x, y)
            coord_queue.put(point)
            coord_queue.task_done()


if __name__ == '__main__':
    run_server()
