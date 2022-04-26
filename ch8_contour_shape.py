"""
    Contours and shape detection
"""
# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2
import numpy as np

from utils import stack_images, BGR_BLUE, BGR_GREEN, BGR_YELLOW


def get_contours(img, img_contour):
    # cv2.RETR_EXTERNAL return the extreme outer contours.
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        # Just a random number to avoid draw little figures
        if area > 500:
            draw_all_contours = -1
            cv2.drawContours(img_contour, contour, draw_all_contours, BGR_BLUE, thickness=3)
            perimeter = cv2.arcLength(contour, True)
            # how many corners have the contours
            # 0.02 A value to play with it
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            obj_corners = len(approx)
            # if obj_corners == 8 we can assume that's a circle
            x, y, w, h = cv2.boundingRect(approx)

            if obj_corners == 3:
                object_type = 'Tri'
            elif obj_corners == 4:
                aspect_ratio = w/float(h)
                if 0.95 < aspect_ratio < 1.05:
                    object_type = 'Sqr'
                else:
                    object_type = 'Rect'
            elif obj_corners > 4:
                object_type = 'Circle'
            else:
                object_type = None
            cv2.rectangle(img_contour, (x, y), (x + w, y + h), BGR_GREEN, thickness=2)
            center_obj = (x + (w // 2) - 10, y + (h // 2) - 10)
            cv2.putText(img_contour, object_type, center_obj, cv2.FONT_HERSHEY_COMPLEX, 0.7, BGR_YELLOW, 2)


img = cv2.imread('resources/shapes.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)

img_contour = np.zeros_like(img)
get_contours(img_canny, img_contour)
img_black = np.zeros_like(img)
img_stack = stack_images(0.8, ([img, img_gray, img_blur], [img_canny, img_contour, img_black]))
cv2.imshow("Stack", img_stack)
cv2.waitKey(0)
