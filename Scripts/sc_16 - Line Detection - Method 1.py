import sys
import cv2 as cv
from math import inf

img = cv.imread("one_line.jpg", cv.IMREAD_GRAYSCALE)


if (img is None):
    sys.exit("Could not read the image.")

i, j = img.shape
hough = {}

for x in range(i):
    for y in range(j):

        if (img[x][y] > 100):

            for a in range(500):
                b = int(-a * x + y)

                if ((a, b) in hough):
                    hough[(a, b)] += 1

                else:
                    hough[(a, b)] = 1


max_x = max_y = -inf
min_x = min_y = inf

for i, j in hough:
    if (i > max_x):
        max_x = i
    if (i < min_x):
        min_x = i

    if (j > max_y):
        max_y = j
    if (j < min_y):
        min_y = j

print((min_x, min_y))
print((max_x, max_y))

# cv.imshow("Image", img)
# cv.imshow("Hough", hough)
cv.waitKey(0)
