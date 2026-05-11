import cv2

# Load face cascade
face = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

# Read image
img = cv2.imread('GROUP.jpg')

# Resize image
img = cv2.resize(img, (800, 600))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face.detectMultiScale(gray, 1.1, 3)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img,
                  (x, y),
                  (x+w, y+h),
                  (0,255,0),
                  2)

# Print count
print("Number of Faces:", len(faces))

# Show output
cv2.imshow("Face Count", img)

cv2.waitKey(0)
cv2.destroyAllWindows()