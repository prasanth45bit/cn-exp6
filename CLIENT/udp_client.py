import socket
import time
from common.config import TCP_IP, TCP_PORT, UDP_IP, UDP_PORT


def start_udp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = "typing..."
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
        time.sleep(5)

if __name__ == "__main__":
    start_udp_client()
