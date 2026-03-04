import cv2
import mediapipe as mp
import subprocess

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

print("[Gesture] Waiting for grab gesture...")

while True:

    ret, frame = cap.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        # simple trigger: any hand detected
        print("[Gesture] Hand detected - triggering screenshot")

        subprocess.run(["python3", "main.py"])

        break

    cv2.imshow("Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()