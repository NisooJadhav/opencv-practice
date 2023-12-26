import cv2

img = cv2.imread("img.jpg")

cv2.imwrite("new_img.jpg", img)