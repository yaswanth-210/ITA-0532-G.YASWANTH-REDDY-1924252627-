import cv2
import numpy as np

img = np.ones((500,500,3), dtype=np.uint8) * 255
cv2.rectangle(img, (100,100), (400,300), (0,255,0), 3)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()