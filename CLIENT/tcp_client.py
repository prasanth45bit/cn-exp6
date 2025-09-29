import socket
import threading
from common.config import TCP_IP, TCP_PORT, UDP_IP, UDP_PORT


def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(f"\n[RECEIVED]: {msg}")
        except:
            break

def start_tcp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    while True:
        msg = input("You: ")
        sock.send(msg.encode())

if __name__ == "__main__":
    start_tcp_client()
