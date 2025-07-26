# Experimenta algumas funções básicas do OpenCV.
# Lê uma imagem e salva uma cópia no disco.

import cv2 as cv
import sys

img = cv.imread("img1.jpg") 

if( img is None ):
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
cv.waitKey(0)

cv.imwrite("img1-copy.png", img)
