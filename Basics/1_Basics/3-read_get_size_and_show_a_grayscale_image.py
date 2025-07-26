# Experimenta algumas funções básicas do OpenCV.
# Lê a imagem em escala de cinza, e mostra na tela

import cv2 as cv
import sys

img = cv.imread("img1.jpg", cv.IMREAD_GRAYSCALE)

if( img is None ):
    sys.exit("Could not read the image.")

print( img.shape ) 

cv.imshow("Display window", img)
cv.waitKey(0)
