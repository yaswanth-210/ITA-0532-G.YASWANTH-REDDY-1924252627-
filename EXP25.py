import cv2

# Read image
img = cv2.imread("watch.jpg")

# Resize image for proper display
img = cv2.resize(img, (500, 700))

# Draw rectangle around watch
cv2.rectangle(img, (120, 220), (330, 520), (0,255,0), 3)

# Add label
cv2.putText(img,
            "Watch Detected",
            (100, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2)

# Show output
cv2.imshow("Object Recognition - Watch", img)

cv2.waitKey(0)
cv2.destroyAllWindows()