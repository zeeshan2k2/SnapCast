import socket
import time
import os

BROADCAST_IP = "255.255.255.255"
UDP_PORT = 5000
TCP_PORT = 9001


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def broadcast_file(filepath, gesture="gesture1"):

    filename = os.path.basename(filepath)
    timestamp = int(time.time())
    sender_ip = get_local_ip()

    message = f"IMAGE_READY|{gesture}|{timestamp}|{sender_ip}|{TCP_PORT}|{filename}"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sock.sendto(message.encode(), (BROADCAST_IP, UDP_PORT))

    print("[Broadcaster] Sent packet:")
    print(message)

    sock.close()