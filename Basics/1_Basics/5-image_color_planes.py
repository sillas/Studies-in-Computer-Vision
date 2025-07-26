import cv2 as cv
import sys

# Carregando a imagem
img = cv.imread('img1.jpg')
if( img is None ):
    sys.exit("Could not read the image.")

# Mostrando apenas o canal R (vermelho)
cv.imshow("Red Channel", img[:,:,0])

# Mostrando apenas o canal G (verde)
cv.imshow("Green Channel", img[:,:,1])

# Mostrando apenas o canal B (azul)
cv.imshow("Blue Channel", img[:,:,2])

cv.waitKey(0)
cv.destroyAllWindows()
