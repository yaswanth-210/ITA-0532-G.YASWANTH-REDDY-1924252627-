import cv2

img = cv2.imread('testing.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, fg = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Foreground", fg)
cv2.waitKey(0)
cv2.destroyAllWindows()