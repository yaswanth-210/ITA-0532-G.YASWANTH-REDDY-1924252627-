import cv2

img = cv2.imread('testing.jpg')
watermark = cv2.putText(img.copy(), 'WATERMARK', (50,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow("Watermarked", watermark)
cv2.waitKey(0)
cv2.destroyAllWindows()