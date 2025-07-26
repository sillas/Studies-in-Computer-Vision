import cv2 as cv
import numpy as np

dot_img = np.zeros((500, 500), np.uint8)
r, c = dot_img.shape

step = 5

for i in range(r):
    for j in range(c):
        dot_img[i][j] = 255 if (i % step == 0 and j % step == 0) else 0

cv.imshow('Blended Image', dot_img)

cv.waitKey(0)
