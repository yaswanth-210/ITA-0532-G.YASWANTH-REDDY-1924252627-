import cv2

# Load face cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Read image
img = cv2.imread("face (2).jpg")

# Resize image
img = cv2.resize(img, (700, 500))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4
)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 3)

# Show output
cv2.imshow("Face Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()