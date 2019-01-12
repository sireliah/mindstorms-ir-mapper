#!/usr/bin/env python3.7

import math
import queue
import socket
import sys
import threading
from typing import Tuple

from dataclasses import dataclass
from renderer import Renderer


@dataclass
class Point:
    x: float
    y: float
    traveled: float
    turned: float


class Receiver:
    def __init__(self):
        bind_addr = (str(sys.argv[1]), 5000)
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
        rend.render(point.x, point.y, point.traveled, point.turned)


def calculate_coords(angle: float, distance: float) -> Tuple[float, float]:
    x = math.cos(math.radians(angle)) * distance
    y = math.sin(math.radians(angle)) * distance
    return (x, y)


def run_server() -> None:
    coord_queue = queue.Queue()
    render_thread = threading.Thread(target=render_points, args=[coord_queue, ])
    render_thread.start()

    with Receiver() as receiver:
        for (angle, reading, traveled, turned) in receiver:
            if reading < 56:
                (x, y) = calculate_coords(angle, reading)
                point = Point(x, y, traveled, turned)
                coord_queue.put(point)
                coord_queue.task_done()


if __name__ == '__main__':
    run_server()
