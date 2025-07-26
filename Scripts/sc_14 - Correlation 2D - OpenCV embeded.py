import sys
import cv2 as cv
import numpy as np


def applayFilter(img, kernel):
    out = cv.filter2D(img.astype(np.float32), -1, kernel)
    return (out - out.min()) / (out.max() - out.min())


img = cv.imread("../images/img1.jpg", cv.IMREAD_GRAYSCALE)

if (img is None):
    sys.exit("Could not read the image.")

k = img[100:500, 100:400].astype(np.float32)

out = applayFilter(img, k)

cv.imshow("Original", img)
cv.imshow("Sobel", out)
cv.waitKey(0)
