import socket
import threading
from common.config import TCP_IP, TCP_PORT, UDP_IP, UDP_PORT


clients = []

def handle_client(conn, addr):
    print(f"[TCP] New connection from {addr}")
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            print(f"[TCP] {addr}: {message.decode()}")
            broadcast(message, conn)
        except:
            break
    conn.close()
    clients.remove(conn)

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

def start_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TCP_IP, TCP_PORT))
    server.listen()
    print(f"[TCP] Server listening on {TCP_IP}:{TCP_PORT}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_tcp_server()
