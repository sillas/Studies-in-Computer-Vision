import sys
import cv2 as cv

img1 = cv.imread("../../images/img1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("../../images/img2.jpg", cv.IMREAD_GRAYSCALE)

if (img1 is None or img2 is None):
    sys.exit("Could not read the images.")

r, c = img1.shape

# Method 1:
alpha = 0.7
blend_img1 = img1

# SLOW!
for i in range(r):
    for j in range(c):
        blend_img1[i][j] = (alpha * img1[i][j]) + ((1 - alpha) * img2[i][j])

# Method 2:
alpha = 0.3
blend_img2 = cv.addWeighted(img1, alpha, img2, 1 - alpha, 0)

cv.imshow('Blended Image - Method 1', blend_img1)
cv.imshow('Blended Image - Method 2', blend_img2)

cv.waitKey(0)
