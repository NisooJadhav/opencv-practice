import cv2

text = cv2.imread("img.jpg")
cv2.putText(text, "hello", (250,140), cv2.FONT_ITALIC, 2, (255,0,0), 4)

cv2.imshow("Text on img", text)
cv2.waitKey(0)