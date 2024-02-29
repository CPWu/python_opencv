import cv2
import numpy as np

# Number of the video device
cap = cv2.VideoCapture(0)

while True:
    # Get ret, frame from video capture device
    ret, frame = cap.read()
    # determine height,weight of original frame.
    # returns the width of the frame
    width = int(cap.get(3))
    # returns the height of the frame
    height = int(cap.get(4))

    # Drawes a line using: source image, start pos, end pos, line color, line thickness)
    img = cv2.line(frame, (0, 0), (width, height), (255, 255, 255), 10)
    img = cv2.line(img, (0, height), (width, 0), (255, 255, 255), 10)

    # Draw a rectangle using: top left, bottom right, color, line thickness
    img = cv2.rectangle(img, (100, 100), (200, 200), (255, 255, 0), 5)

    # Draw a circle using: center, radius, color, line thickness
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    # Draw a text using: image, text, bottom left, font, font scale, radius, color, line thickness, line type
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(
        img, "Hello World", (200, height - 10), font, 4, (0, 0, 0), 3, cv2.LINE_AA
    )
    cv2.imshow("Frame", img)

    # Wait 1ms to see if we press q.
    if cv2.waitKey(1) == ord("q"):
        break

# Releases the camera resource
cap.release()
cv2.destroyAllWindows()
