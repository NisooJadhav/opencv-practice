import cv2

# read img
img = cv2.imread("img.jpg")

# display img
# window name + matrix var
cv2.imshow('Image', img)
# display for 10 seconds
cv2.waitKey(10000)
#display whole time
cv2.waitKey(10000)
