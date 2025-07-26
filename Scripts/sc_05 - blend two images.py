import sys
import numpy as np
import cv2 as cv

img1 = cv.imread("../images/img1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("../images/img2.jpg", cv.IMREAD_GRAYSCALE)

if (img1 is None or img2 is None):
    sys.exit("Could not read the images.")

r, c = img1.shape

print(r, c)

blend_img = np.zeros((r, c), np.uint8)

proportion = 0.5

# Method 1:
for i in range(r):
    for j in range(c):
        blend_img[i][j] = (img1[i][j] * proportion) + \
            (img2[i][j] * (1 - proportion))

cv.imshow('Blended Image', blend_img)

# Method 2:
blend_imgx = cv.addWeighted(img1, proportion, img2, 1 - proportion, 0)
cv.imshow('Blended Image x', blend_imgx)

cv.waitKey(0)
