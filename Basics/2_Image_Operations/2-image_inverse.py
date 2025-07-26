# Operações com imagens
# Obtem o inverso da imagem

import sys
import cv2 as cv

img1 = cv.imread("../../images/img1.jpg", cv.IMREAD_GRAYSCALE)

if (img1 is None):
    sys.exit("Could not read the image 1.")

img3 = 255 - img1

cv.imshow("Display", img3)
cv.waitKey(0)
