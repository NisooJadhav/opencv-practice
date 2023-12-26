import cv2

circle = cv2.imread("img.jpg")

# center coordinates , radius length , color , thickness

cv2.circle(circle,(150,150),50,(0,0,255),3)

cv2.imshow("Circle",circle)
cv2.waitKey(0)