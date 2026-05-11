import cv2
import time

# Open video
cap = cv2.VideoCapture('traffic.mp4')

frames = []

# Read frames
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame to reduce memory usage
    frame = cv2.resize(frame, (500, 300))

    frames.append(frame)

cap.release()

print("Frames Loaded")

# Play reverse slow motion
for frame in reversed(frames):

    cv2.imshow("Reverse Slow", frame)

    time.sleep(0.03)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(1)
cv2.destroyAllWindows()