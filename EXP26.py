import cv2

# Open video
cap = cv2.VideoCapture("traffic.mp4")

frames = []

# Read frames
while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (700, 500))

    frames.append(frame)

cap.release()

print("Frames Loaded Successfully")

# Reverse playback
for i in range(len(frames)-1, -1, -1):

    cv2.imshow("Reverse Video", frames[i])

    # Fast playback
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()