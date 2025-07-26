import cv2 as cv
import numpy as np
import matplotlib.pyplot as plot


def gausianKernel(l=5, sig=1.):
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))

    kernel = np.outer(gauss, gauss)
    return (kernel / np.sum(kernel))


img = cv.imread("../images/img1.jpg",
                cv.IMREAD_GRAYSCALE)  # [100:300,100:300]
r, c = img.shape

filter_shape = 31
sigma = 10
filter_mask = gausianKernel(filter_shape, sigma)
# ------------------------------------------------------------------

filtered_image = cv.filter2D(img.astype(np.float32), -1, filter_mask)
filtered_image = (filtered_image - filtered_image.min()) / \
    (filtered_image.max() - filtered_image.min())  # normalize

# ------------------------------------------------------------------
cv.imshow('Original Image', img)
cv.imshow('Filtered Image', filtered_image)

plot.matshow(filter_mask)
plot.show()
