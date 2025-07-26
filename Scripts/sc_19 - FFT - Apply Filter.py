import cv2
import numpy as np


def highpass_filter(img, d=30):
    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)

    # Mask
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow-d:crow+d, ccol-d:ccol+d] = 1

    fft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    fft_shift = np.fft.fftshift(fft)

    # Apply Mask
    fft_shift = fft_shift * mask

    fft_ishift = np.fft.ifftshift(fft_shift)
    img_back = cv2.idft(fft_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    return img_back


img = cv2.imread('../images/img3.jpg', cv2.IMREAD_GRAYSCALE)
img_highpass = highpass_filter(img)

cv2.imshow("Display", img_highpass)
cv2.waitKey(0)
