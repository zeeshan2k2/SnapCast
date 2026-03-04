import socket

TCP_PORT = 9001


def start_file_server(filepath):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", TCP_PORT))
    server.listen(1)

    print(f"[FileServer] Waiting for connection on port {TCP_PORT}...")

    conn, addr = server.accept()

    print(f"[FileServer] Receiver connected: {addr}")
    print("[FileServer] Sending file...")

    with open(filepath, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            conn.sendall(data)

    conn.close()
    server.close()

    print("[FileServer] File transfer complete")