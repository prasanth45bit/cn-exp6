import socket
import threading

from common.config import TCP_IP, TCP_PORT, UDP_IP, UDP_PORT


def handle_tcp_client(conn, addr, clients):
    print(f"[TCP] Connected: {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"[TCP] {addr}: {msg}")
            for c in clients:
                if c != conn:
                    c.send(f"{addr}: {msg}".encode())
        except:
            break
    print(f"[TCP] Disconnected: {addr}")
    clients.remove(conn)
    conn.close()

def start_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TCP_IP, TCP_PORT))
    server.listen()
    print(f"[TCP] Server listening on {TCP_IP}:{TCP_PORT}")
    clients = []
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        threading.Thread(target=handle_tcp_client, args=(conn, addr, clients), daemon=True).start()


def start_udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"[UDP] Server listening on {UDP_IP}:{UDP_PORT}")
    while True:
        msg, addr = sock.recvfrom(1024)
        print(f"[UDP] {addr}: {msg.decode()}")
        sock.sendto(f"ACK: {msg.decode()}".encode(), addr)

if __name__ == "__main__":
    threading.Thread(target=start_tcp_server, daemon=True).start()
    start_udp_server()
