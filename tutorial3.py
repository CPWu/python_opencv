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

    # Creates an empty canvas by taking the frame shape and filling it with Zero
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # paste in top left
    image[: height // 2, : width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # paste in bottom left
    image[height // 2 :, : width // 2] = smaller_frame

    # paste in top right
    image[: height // 2, width // 2 :] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # paste in bottom left
    image[height // 2 :, width // 2 :] = smaller_frame

    cv2.imshow("Frame", image)

    # Wait 1ms to see if we press q.
    if cv2.waitKey(1) == ord("q"):
        break

# Releases the camera resource
cap.release()
cv2.destroyAllWindows()
