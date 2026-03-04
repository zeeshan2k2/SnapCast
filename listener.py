import socket

UDP_PORT = 5000

print("[Listener] Waiting for broadcast packets...")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))


def download_file(ip, port, filename):

    print(f"[Downloader] Connecting to {ip}:{port}")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    save_name = f"received_{filename}"

    with open(save_name, "wb") as f:

        while True:
            data = client.recv(4096)
            if not data:
                break

            f.write(data)

    client.close()

    print(f"[Downloader] File saved as {save_name}")


while True:

    data, addr = sock.recvfrom(1024)
    message = data.decode()

    print(f"\n[Listener] Packet received from {addr}")
    print(message)

    parts = message.split("|")

    if parts[0] == "IMAGE_READY":

        gesture = parts[1]
        timestamp = parts[2]
        ip = parts[3]
        port = int(parts[4])
        filename = parts[5]

        print("\n[Listener] Metadata parsed:")
        print(f"Gesture: {gesture}")
        print(f"Timestamp: {timestamp}")
        print(f"Sender IP: {ip}")
        print(f"Port: {port}")
        print(f"Filename: {filename}")

        download_file(ip, port, filename)