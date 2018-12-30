import socket

ADDR = ('192.168.0.11', 5000)


def run_server(bind_addr) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(bind_addr)
    print(f'Listening on {bind_addr}.')
    while True:
        data, address = sock.recvfrom(4096)
        print(f'Got {len(data)} bytes from {address}.')
        if data:
            print(str(data))
            sent = sock.sendto(b'Ok!', address)
            print(str(sent))


if __name__ == '__main__':
    run_server(ADDR)
