import cv2

black = cv2.imread("img.jpg")

# x-coordinate , y-coordinate , color , thickness
cv2.line(black, (120,50),(250,70),(255,0,0),2)

cv2.imshow("Lines ",black)
cv2.waitKey(0)