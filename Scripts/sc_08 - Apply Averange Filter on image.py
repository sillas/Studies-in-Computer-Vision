import cv2 as cv
import numpy as np

dot_img = cv.imread("../images/img1.jpg", cv.IMREAD_GRAYSCALE)
r, c = dot_img.shape
cv.imshow('Blended Image', dot_img)

filter_mask = np.array([
    [0,  0,  1,  0,  0],
    [0,  1,  2,  1,  0],
    [1,  2,  5,  2,  1],
    [0,  1,  2,  1,  0],
    [0,  0,  1,  0,  0]])

k = 2
uniform_weight = 1/(2 * k + 1)**2

print(r, c)

for i in range(r):
    for j in range(c):

        # -------
        avg = 0

        for u in range(-k, k + 1):
            for v in range(-k, k + 1):
                i_u = i + u
                j_v = j + v

                dot = 0 if (i_u < 0 or j_v < 0 or i_u > r -
                            1 or j_v > c-1) else dot_img[i_u][j_v]

                avg += filter_mask[u + 1][v + 1] * dot

        # -------
        dot_img[i][j] = uniform_weight * avg

cv.imshow('Blended Image 2', dot_img)

cv.waitKey(0)
