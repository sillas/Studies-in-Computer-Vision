import sys
import cv2 as cv

img = cv.imread("../images/img1.jpg")

if (img is None):
    sys.exit("Could not read the image.")

print(img.shape)

cropped_img = img[100:500, 100:400]

cv.imshow("Display window", (cropped_img))

cv.waitKey(0)
