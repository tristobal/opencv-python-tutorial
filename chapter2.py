"""
    Basic Functions
"""

# Workaround for OpenCV imports in Pycharm
import cv2.cv2 as cv2
import numpy as np

img = cv2.imread('resources/lena.png')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/
# Must be odd
gausian_kernel_size = (7, 7)
img_blur = cv2.GaussianBlur(img_grey, gausian_kernel_size, 0)

# https://programarfacil.com/blog/vision-artificial/detector-de-bordes-canny-opencv/
img_canny = cv2.Canny(img, 100, 100)

# https://www.javatpoint.com/opencv-erosion-and-dilation
kernel = np.ones((5, 5), np.uint8)
img_dialation = cv2.dilate(img_canny, kernel, iterations=1)

img_eroded = cv2.erode(img_dialation, kernel, iterations=1)


cv2.imshow("Gray Image", img_grey)
cv2.imshow("Blur Image", img_blur)
cv2.imshow("Canny Image", img_canny)
cv2.imshow("Dialation Image", img_dialation)
cv2.imshow("Eroded Image", img_eroded)

cv2.waitKey(0)
