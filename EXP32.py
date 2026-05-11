import cv2
import numpy as np

h, w = 500, 500
img = np.ones((h,w,3), dtype=np.uint8) * 255
s = h//10

img[0:s, 0:s] = (0,0,0)
img[0:s, w-s:w] = (255,0,0)
img[h-s:h, 0:s] = (0,255,0)
img[h-s:h, w-s:w] = (0,0,255)

cv2.imshow("Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()