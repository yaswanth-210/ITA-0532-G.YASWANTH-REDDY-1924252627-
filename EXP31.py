import cv2

img = cv2.imread('testing.jpg', 0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Segmented", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()