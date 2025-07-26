import cv2 as cv
import numpy as np
import matplotlib.pyplot as plot

img = cv.imread("../images/img1.jpg", cv.IMREAD_GRAYSCALE)

# Transformar a imagem para um array complexo
img_float32 = np.float32(img)

# Calcular a DFT
dft = cv.dft(img_float32, flags=cv.DFT_SCALE | cv.DFT_COMPLEX_OUTPUT)

# Fazer o Shift da imagem para centralizar a frequência zero
dft_shift = np.fft.fftshift(dft)

# Calcular a magnitude da DFT
magnitude_spectrum = 20 * \
    np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

idft = cv.idft(dft_shift)
img_back = cv.magnitude(idft[:, :, 0], idft[:, :, 1])

cv.imshow("Imgage Inversa", img_back)

plot.subplot(121)
plot.imshow(img, cmap='gray')
plot.title('Input Image')
plot.xticks([]), plot.yticks([])

plot.subplot(122)
plot.imshow(magnitude_spectrum, cmap='gray')
plot.title('Magnitude Spectrum')
plot.xticks([]), plot.yticks([])

plot.show()
