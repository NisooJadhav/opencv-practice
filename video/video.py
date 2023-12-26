import cv2

vid = cv2.VideoCapture("video.mp4")

while True:
    control, frame = vid.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(10) == 27:
        break