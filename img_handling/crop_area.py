import cv2

crop = cv2.imread("img.jpg")
# separate X & Y axis with ,
croppedImg = crop[60:360,40:240]

cv2.imshow("Original: "+crop)
cv2.imshow("After Crop: "+croppedImg)

cv2.waitKey(0)