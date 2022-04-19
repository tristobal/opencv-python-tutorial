"""
    Shapes and text
"""
# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2
import numpy as np

BGR_BLUE = (255, 0, 0)
BGR_GREEN = (0, 255, 0)
BGR_RED = (0, 0, 255)


def show_image_with_shape(img):
    img[200:300, 100:300] = BGR_BLUE
    print(f'Image size: {img.shape}')
    cv2.imshow("Image", img)


def show_image_with_line(img):
    start = (0, 0)
    end = (300, 300)
    thickness = 3
    cv2.line(img, start, end, BGR_GREEN, thickness)
    cv2.imshow("Image with a line", img)


def show_image_with_rectangle(img):
    start = (0, 0)
    end = (250, 350)
    thickness = cv2.FILLED
    cv2.rectangle(img, start, end, BGR_RED, thickness)
    cv2.imshow("Image with a rectangle", img)


def show_image_with_circle(img):
    center = (400, 50)
    radius = 30
    thickness = 5
    cv2.circle(img, center, radius, BGR_RED, thickness)
    cv2.imshow("Image with a circle", img)


def show_image_with_text(img):
    start = (300, 200)
    font_scale = 0.5
    thickness = 1
    cv2.putText(img, 'Hello world', start, cv2.FONT_HERSHEY_COMPLEX, font_scale, BGR_RED, thickness)
    cv2.imshow("Image with text", img)


img_ = np.zeros((512, 512, 3), np.uint8)
show_image_with_text(img_)
cv2.waitKey(0)
