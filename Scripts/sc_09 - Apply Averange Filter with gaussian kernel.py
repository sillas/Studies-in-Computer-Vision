import cv2 as cv
import numpy as np
import matplotlib.pyplot as plot


def gausianKernel(l=5, sig=1.):
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))

    kernel = np.outer(gauss, gauss)
    return (kernel / np.sum(kernel))


dot_img = cv.imread("../images/img1.jpg",
                    cv.IMREAD_GRAYSCALE)  # [100:300,100:300]
filtered_image = np.zeros(dot_img.shape, np.uint8)
r, c = dot_img.shape

filter_shape = 11
sigma = 6
filter_mask = gausianKernel(filter_shape, sigma)

k = int(filter_shape / 2)
uniform_weight = 1/(2 * k + 1)**2

total_of_inter = (r * c) * (filter_shape ** 2)
print(f"Interations: {total_of_inter}")

correction = 100  # Important!!!

for i in range(r):
    print(r - i)
    for j in range(c):

        # -------
        avg = 0

        for u in range(-k, k + 1):
            for v in range(-k, k + 1):
                i_u = i + u
                j_v = j + v

                dot = 1 if (i_u < 0 or j_v < 0 or i_u > r -
                            1 or j_v > c-1) else dot_img[i_u][j_v]

                avg += filter_mask[u + 1][v + 1] * dot
        # -------
        filtered_image[i][j] = uniform_weight * avg * correction

# --- Verificar Isso.
filtered_image = (filtered_image - filtered_image.min()) / \
    (filtered_image.max() - filtered_image.min())

cv.imshow('Original Image', dot_img)
cv.imshow('Filtered Image', filtered_image)

plot.matshow(filter_mask)
plot.show()
