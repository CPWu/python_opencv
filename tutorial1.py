import cv2

# Load an image
# CV2 Loads in (b,g,r)
# (-1)cv2.IMREAD_COLOR – It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
# (0)cv2.IMREAD_GRAYSCALE – It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
# (1)cv2.IMREAD_UNCHANGED – It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.
img = cv2.imread("assets/logo.jpg", -1)
# Resize an image by specifying width and height in pixels
img = cv2.resize(img, (400, 400))
# Rotate an image
img = cv2.rotate(img, cv2.ROTATE_180)
# Save an image
cv2.imwrite("new_img.jpg", img)
# Resize by percentage
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# display image
cv2.imshow("Logo", img)
# Waits infinite amount of time for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
