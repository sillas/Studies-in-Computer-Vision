import cv2 as cv
import numpy as np
import matplotlib.pyplot as plot


img = cv.imread("../images/img1.jpg", cv.IMREAD_GRAYSCALE)
r, c = img.shape

posx = 0
posy = 0
sz = 31

filter_mask = img[posx: posx+sz, posy:posy+sz]
# ------------------------------------------------------------------

filtered_image = cv.filter2D(img.astype(np.float32), -1, filter_mask)
filtered_image = (filtered_image - filtered_image.min()) / \
    (filtered_image.max() - filtered_image.min())  # normalize

# ------------------------------------------------------------------
cv.imshow('Original Image', img)
cv.imshow('Filtered Image', filtered_image)

plot.matshow(filter_mask)
plot.show()
