import cv2
import mediapipe as mp

handModel = mp.solutions.hands
handModelDrawing = mp.solutions.drawing_utils
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Cannot open webcam")
    exit()

with handModel.Hands(
    min_detection_confidence=0.6, min_tracking_confidence=0.5
) as hands:
    while True:
        control, frame = webcam.read()
        if not control:
            print("Cannot receive frame (stream end?). Exiting...")
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        height, width, _ = frame.shape

        cv2.rectangle(frame, (250, 150), (500, 250), (0, 255, 0), 3)

        if result.multi_hand_landmarks:
            for handLandmark in result.multi_hand_landmarks:
                index_finger_point = handLandmark.landmark[8]
                x = int(index_finger_point.x * width)
                y = int(index_finger_point.y * height)
                cv2.circle(frame, (x, y), 4, (0, 255, 0), 6)
                if 250 < x < 500 and 150 < y < 250:
                    cv2.rectangle(frame, (250, 150), (500, 250), (0, 255, 0), -1)
                    cv2.putText(
                        frame,
                        "btn pressed",
                        (50, 50),
                        cv2.FONT_ITALIC,
                        2,
                        (255, 0, 0),
                        2,
                    )
        cv2.imshow("Project", frame)
        if cv2.waitKey(20) == 27:
            break
