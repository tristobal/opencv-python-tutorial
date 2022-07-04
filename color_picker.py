# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2
import numpy as np
from cv2.cv2 import VideoCapture

import utils


def get_webam_capture() -> VideoCapture:
    first_webcam_id = 0
    width_id = 3
    height_id = 4
    brightness_id = 10

    cap = cv2.VideoCapture(first_webcam_id)
    cap.set(width_id, 640)
    cap.set(height_id, 480)
    cap.set(brightness_id, 0)
    return cap


winname = "Trackbars"
hue_min = "Hue Min"
hue_max = "Hue Max"
sat_min = "Sat Min"
sat_max = "Sat Max"
val_min = "Val Min"
val_max = "Val Max"

cv2.namedWindow(winname)
cv2.resizeWindow(winname, 640, 240)
cv2.createTrackbar(hue_min, winname, 0, 179, utils.empty_function)
cv2.createTrackbar(hue_max, winname, 179, 179, utils.empty_function)
cv2.createTrackbar(sat_min, winname, 0, 255, utils.empty_function)
cv2.createTrackbar(sat_max, winname, 255, 255, utils.empty_function)
cv2.createTrackbar(val_min, winname, 0, 255, utils.empty_function)
cv2.createTrackbar(val_max, winname, 255, 255, utils.empty_function)


webcam = get_webam_capture()
while True:
    _, img = webcam.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos(hue_min, winname)
    h_max = cv2.getTrackbarPos(hue_max, winname)
    s_min = cv2.getTrackbarPos(sat_min, winname)
    s_max = cv2.getTrackbarPos(sat_max, winname)
    v_min = cv2.getTrackbarPos(val_min, winname)
    v_max = cv2.getTrackbarPos(val_max, winname)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower, upper)

    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Bitwise", result)
    cv2.waitKey(1)

    # Wait until the q is press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
