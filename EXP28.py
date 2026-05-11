import cv2

# Load classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

# Read video
cap = cv2.VideoCapture('traffic.mp4')

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (900, 600))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=2
    )

    # Draw rectangles
    for (x, y, w, h) in cars:

        cv2.rectangle(frame,
                      (x, y),
                      (x+w, y+h),
                      (0,255,0),
                      2)

        cv2.putText(frame,
                    "Vehicle",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0,255,0),
                    2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()