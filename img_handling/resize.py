import cv2

img = cv2.imread("img.jpg")
resizedImg = cv2.resize(img, (100,390))

cv2.imshow("Original", img)
cv2.imshow("Resized", resizedImg)
cv2.waitKey(0)