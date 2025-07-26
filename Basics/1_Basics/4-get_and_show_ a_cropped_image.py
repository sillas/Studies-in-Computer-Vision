# Experimenta algumas funções básicas do OpenCV.
# Lê uma imagem, recorta um pedaço e mostra na tela.

import cv2 as cv
import sys

img = cv.imread("img1.jpg") 

if( img is None ):
    sys.exit("Could not read the image.")

cropped_img = img[100:500,100:400]

cv.imshow("Display window", (cropped_img))

cv.waitKey(0)
