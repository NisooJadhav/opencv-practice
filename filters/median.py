import cv2

img = cv2.imread('interstellar.jpg')

median = cv2.medianBlur(img, 7)

cv2.imshow("median",median)

cv2.waitKey(0)