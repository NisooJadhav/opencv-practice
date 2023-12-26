import cv2

img = cv2.imread("interstellar.jpg",0)
cv2.imshow("canny",cv2.Canny(img,10,255))

cv2.waitKey(0)