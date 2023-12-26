import cv2

img = cv2.imread("interstellar.jpg")
cv2.imshow("negative",cv2.bitwise_not(img))

cv2.waitKey(0)