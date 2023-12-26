import cv2

img = cv2.imread("img.jpg")
print(img)
# reaching color density of a pixel
(blue,green,red) = img[125,50]

print(" blue: "+blue," green: ",green," red: ",red)