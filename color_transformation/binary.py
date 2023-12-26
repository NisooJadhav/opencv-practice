import cv2

img = cv2.imread("img.jpg")

thresh,binary = cv2.threshold(img, 125, 125, cv2.THRESH_BINARY)

cv2.imshow("original", img)
cv2.imshow("binary", binary)

cv2.waitKey(0)