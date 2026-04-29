import cv2
import numpy as np

img = cv2.imread('testing.jpg')
kernel = np.ones((5,5), np.uint8)
erode = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Erode", erode)
cv2.waitKey(0)
cv2.destroyAllWindows()