import sys
import cv2 as cv

img = cv.imread("../images/img1.jpg", cv.IMREAD_GRAYSCALE)

if (img is None):
    sys.exit("Could not read the image.")

print(img.shape)

cv.imshow("Display window", img)
cv.waitKey(0)
