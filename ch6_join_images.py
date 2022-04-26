"""
    Joining images
"""
# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2
import numpy as np

from utils import stack_images


img = cv2.imread("resources/lena.png")
img_horizontal = np.hstack((img, img))
img_vertical = np.vstack((img, img))

cv2.imshow("Horizontal", img_horizontal)
cv2.imshow("Vertical", img_vertical)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_stack = stack_images(0.5, ([img, img_gray, img], [img, img, img]))
cv2.imshow("Stack", img_stack)
cv2.waitKey(0)
