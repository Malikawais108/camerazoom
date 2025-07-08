import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# 👇 Insert this check here
if not cap.isOpened():
    print("❌ Could not access the camera. Is it connected and available?")
    exit(1)
else:
    print("✅ Camera detected. Launching app...")

zoom_factor = 1.0

def get_finger_distance(lm1, lm2):
    return math.hypot(lm2.x - lm1.x, lm2.y - lm1.y)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]

    # (You might want to add zoom/resize logic here, later)
    cv2.imshow("Camera Zoom", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
