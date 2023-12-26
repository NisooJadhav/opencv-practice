import cv2

img = cv2.imread('img.jpg')

rot_90 = cv2.rotate(img,cv2.ROTATE_180)
rot_90_C = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("original",img)
cv2.imshow("original",rot_90)
cv2.imshow("original",rot_90_C)

cv2.waitKey(0)