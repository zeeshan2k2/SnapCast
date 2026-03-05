import socket
import cv2
import mediapipe as mp
import os

UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))

latest_file = None

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

print("[Listener] Waiting for broadcast packets...")


def download_file(ip, port, filename):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    save_path = os.path.join(desktop, filename)

    with open(save_path, "wb") as f:

        while True:
            data = client.recv(4096)
            if not data:
                break
            f.write(data)

    client.close()

    print("[Downloader] Screenshot saved to Desktop")


while True:

    sock.setblocking(False)

    try:
        data, addr = sock.recvfrom(1024)

        message = data.decode()
        parts = message.split("|")

        if parts[0] == "IMAGE_READY":

            ip = parts[3]
            port = int(parts[4])
            filename = parts[5]

            latest_file = (ip, port, filename)

            print("[Listener] Screenshot available")

    except:
        pass


    ret, frame = cap.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks and latest_file:

        print("[Gesture] Receive gesture detected")

        ip, port, filename = latest_file

        download_file(ip, port, filename)

        latest_file = None

    cv2.imshow("Receiver Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
