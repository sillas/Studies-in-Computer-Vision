import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem em escala de cinza
img = cv2.imread('../images/img5.jpg', cv2.IMREAD_GRAYSCALE)

# Calcula a FFT da imagem
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Mask
# -------------------------------------------------------------------------

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

# Passa baixa
# d = 20
# mask = np.zeros((rows, cols), np.uint8)
# mask[ crow - d : crow + d, ccol - d : ccol + d] = 1

# Passa alta
d = 10
mask = np.ones((rows, cols), np.uint8)
mask[crow - d: crow + d, ccol - d: ccol + d] = 0

fshift = fshift * mask
# -------------------------------------------------------------------------

magnitude_spectrum = 20 * np.log(np.abs(fshift))

# Calcula a IFFT da imagem
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Exibe as imagens
# plt.subplot(221), plt.imshow(img, cmap='gray')
# plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])

# plt.subplot(222)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

# plt.subplot(223), plt.imshow(img_back, cmap='gray')
# plt.title('Imagem Reconstruída'), plt.xticks([]), plt.yticks([])

cv2.imshow("Filtro", np.uint8(img_back * 0.9))
cv2.imshow("Original", img)


plt.show()
