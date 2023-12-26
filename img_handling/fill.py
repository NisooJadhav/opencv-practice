import cv2

fill = cv2.imread("img.jpg")

cv2.circle(fill, (80,80), 50, (0,255,0), -1)

cv2.imshow("Fill",fill)
cv2.waitKey(0)