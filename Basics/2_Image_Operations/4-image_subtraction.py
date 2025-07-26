# Operações com imagens
# Subtrai duas imagens

import sys
import numpy as np
import cv2 as cv

img1 = cv.imread("../../images/img1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("../../images/img2.jpg", cv.IMREAD_GRAYSCALE)

if (img1 is None):
    sys.exit("Could not read the image 1.")

if (img2 is None):
    sys.exit("Could not read the image 2.")

# Método 1: Este método é problemático pois não trata os valores negativos. Gerando regiões saturadas.
img3 = img1 - img2
img4 = img2 - img1

# Método 2: Este método primeiro converte para float, para tratar dos valores negativos.
f_img1 = img1.astype(float)
f_img2 = img2.astype(float)

# no final, corta os valores negativos para zero, e converte novamente para uint8.
img5 = (np.clip((f_img1 - f_img2), 0, 255) +
        np.clip((f_img2 - f_img1), 0, 255)).astype(np.uint8)

# Método 3: OpenCV
img6 = cv.subtract(img1, img2)

cv.imshow("Method 1a", img3)
cv.imshow("Method 1b", img4)
cv.imshow("Method 2", img5)
cv.imshow("Method 3", img6)

cv.waitKey(0)
