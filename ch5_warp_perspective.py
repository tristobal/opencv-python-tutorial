"""
    Warp perspective
"""
# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2
import numpy as np


HEIGHT = 350
WIDTH = 250

card_original_corners = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
card_new_corners = np.float32([[0, 0], [WIDTH, 0], [0, HEIGHT], [WIDTH, HEIGHT]])

img = cv2.imread('resources/cards.jpg')
matrix = cv2.getPerspectiveTransform(card_original_corners, card_new_corners)
img_output = cv2.warpPerspective(img, matrix, (WIDTH, HEIGHT))

cv2.imshow("Cards", img)
cv2.imshow("Cards output", img_output)
cv2.waitKey(0)
