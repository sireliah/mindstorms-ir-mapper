from typing import Tuple
import socket

ADDRESS = ('localhost', 5000)

def send_data(data: str, address: Tuple) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(data.encode('utf-8')), address)
    response_data, server = sock.recvfrom(4096)
    print(response_data)


if __name__ == '__main__':
    i = 0
    while i < 10000:
        send_data(f'hello {i}', ADDRESS)
        i += 1
