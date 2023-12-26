import cv2

img = cv2.imread("img.jpg")
height,width,channels = img.shape
# channel = color saturation, RGB = 3, CMYK = 4
print(height, width, channels)
