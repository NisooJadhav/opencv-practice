import cv2

rect = cv2.imread('img.jpg')

cv2.rectangle(rect,(100,140),(150,300),(0,255,0),4)

cv2.imshow("Rectangle ", rect)

cv2.waitKey(0)