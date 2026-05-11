import cv2
import pytesseract

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture('video.mp4')

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (900, 500))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply threshold for better OCR
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Extract text
    text = pytesseract.image_to_string(thresh)

    text = text.strip()

    # Display detected text
    cv2.putText(frame,
                "Detected: " + text,
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2)

    print("Detected Text:", text)

    cv2.imshow("Video Text Extraction", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()