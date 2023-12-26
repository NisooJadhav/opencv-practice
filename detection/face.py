import cv2 

face_detection = cv2.CascadeClassifier("face.xml")
eye_detection = cv2.CascadeClassifier("eye.xml")

face = cv2.imread("face.png")
gray = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
faceResult = face_detection.detectMultiScale(gray, 1.1, 4)
eyeResult = eye_detection.detectMultiScale(gray, 1.1, 4)

for(x,y,w,h) in faceResult:
    cv2.rectangle(face,(x,y),(x+w,y+h),(255,0,0),3)

for(x,y,w,h) in eyeResult:
    cv2.rectangle(face,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("detection", face)
cv2.waitKey(0)