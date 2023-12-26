import cv2

img = cv2.imread('img.jpg')
width = 200
height = 200

center_point = (width/2 , height/2)

rotate = cv2.getRotationMatrix2D(center_point, -30, 1.0)

rotated = cv2.warpAffine(img, rotate, (width, height))

cv2.imshow("original", img)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)