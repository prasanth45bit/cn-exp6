import socket
from common.config import TCP_IP, TCP_PORT, UDP_IP, UDP_PORT


def start_udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((UDP_IP, UDP_PORT))
    print(f"[UDP] Server listening on {UDP_IP}:{UDP_PORT}")
    while True:
        msg, addr = udp_socket.recvfrom(1024)
        print(f"[UDP] {addr}: {msg.decode()}")

if __name__ == "__main__":
    start_udp_server()
