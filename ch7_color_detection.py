"""
    Color detection
"""
# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2
import numpy as np


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y], (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                 None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None,scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


def empty_function(arg):
    pass


def trackbar_and_images(img, img_hsv):
    winname = "Trackbars"
    hue_min = "Hue Min"
    hue_max = "Hue Max"
    sat_min = "Sat Min"
    sat_max = "Sat Max"
    val_min = "Val Min"
    val_max = "Val Max"

    cv2.namedWindow(winname)
    cv2.resizeWindow(winname, 640, 240)
    cv2.createTrackbar(hue_min, winname, 0, 179, empty_function)
    cv2.createTrackbar(hue_max, winname, 179, 179, empty_function)
    cv2.createTrackbar(sat_min, winname, 0, 255, empty_function)
    cv2.createTrackbar(sat_max, winname, 255, 255, empty_function)
    cv2.createTrackbar(val_min, winname, 0, 255, empty_function)
    cv2.createTrackbar(val_max, winname, 255, 255, empty_function)

    while True:
        h_min = cv2.getTrackbarPos(hue_min, winname)
        h_max = cv2.getTrackbarPos(hue_max, winname)
        s_min = cv2.getTrackbarPos(sat_min, winname)
        s_max = cv2.getTrackbarPos(sat_max, winname)
        v_min = cv2.getTrackbarPos(val_min, winname)
        v_max = cv2.getTrackbarPos(val_max, winname)
        print(h_min, h_max, s_min, s_max, v_min, v_max)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(img_hsv, lower, upper)

        cv2.imshow("Original", img)
        cv2.imshow("HSV", img_hsv)
        cv2.imshow("Mask", mask)
        cv2.waitKey(1)


img = cv2.imread("resources/lambo.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# TODO trackbar_and_images is used to get lower and upper values
# trackbar_and_images(img, img_hsv)
lower = np.array([0, 110, 153])
upper = np.array([19, 240, 255])
mask = cv2.inRange(img_hsv, lower, upper)
img_with_mask = cv2.bitwise_and(img, img, mask=mask)

img_stack = stack_images(0.6, ([img, img_hsv], [mask, img_with_mask]))
cv2.imshow("Result", img_stack)
cv2.waitKey(0)
