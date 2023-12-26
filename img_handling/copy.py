'''
import cv2

img = cv2.imread("img.jpg")
new_img = img.copy()

cv2.imshow("original",img)
cv2.imshow("copy",new_img)

cv2.waitKey(0)
'''