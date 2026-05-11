import cv2

img = cv2.imread('testing.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, bg = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

cv2.imshow("Background", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()