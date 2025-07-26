import sys
import cv2 as cv

img = cv.imread("../images/img1.jpg")

if (img is None):
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
cv.waitKey(0)

cv.imwrite("img2.png", img)
