import cv2
import mediapipe as mp

from screenshot import take_screenshot
from broadcaster import broadcast_file
from file_server import start_file_server


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

print("[Gesture] Waiting for grab gesture...")


def is_fist(hand):
    tips = [8, 12, 16, 20]
    pip = [6, 10, 14, 18]

    closed = 0

    for tip, joint in zip(tips, pip):
        if hand.landmark[tip].y > hand.landmark[joint].y:
            closed += 1

    return closed >= 3


while True:

    ret, frame = cap.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_fist(hand_landmarks):

                print("[Gesture] Grab detected")

                filepath = take_screenshot()

                if filepath:
                    broadcast_file(filepath)
                    start_file_server(filepath)

                cap.release()
                cv2.destroyAllWindows()
                exit()

    cv2.imshow("Sender Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()