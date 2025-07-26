import sys
import cv2 as cv
import numpy as np


def applayFilter(img, kernel):
    out = cv.filter2D(img.astype(np.float32), -1, kernel)
    return (out - out.min()) / (out.max() - out.min())


img = cv.imread("../images/img1.jpg")

if (img is None):
    sys.exit("Could not read the image.")

sobel = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1],
], np.float32) / 8
"""
sobel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
], np.float32) / 8
"""

out = applayFilter(img, sobel)

cv.imshow("Original", img)
cv.imshow("Sobel", out)
cv.waitKey(0)
