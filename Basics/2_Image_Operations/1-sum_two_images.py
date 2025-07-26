# Operações com imagens
# Soma de duas imagens

import sys
import cv2 as cv

img1 = cv.imread("../../images/img1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("../../images/img2.jpg", cv.IMREAD_GRAYSCALE)

if (img1 is None):
    sys.exit("Could not read the image 1.")

if (img2 is None):
    sys.exit("Could not read the image 2.")

factor = 2
img3 = img1//factor + img2//factor  # Método 1
img4 = (img1 + img2)//factor   # Método 2

cv.imshow("Method 1", img3)
cv.imshow("Method 2", img4)

cv.waitKey(0)
