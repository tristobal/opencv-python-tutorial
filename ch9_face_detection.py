"""
    Face detection
"""
# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2

from utils import BGR_BLUE


def detect_from_img(face_cascade):
    img = cv2.imread('resources/lena.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), BGR_BLUE, 2)

    cv2.imshow("Lena", img)
    cv2.waitKey(0)


def detect_from_webcam(face_cascade):
    first_webcam_id = 0
    width_id = 3
    height_id = 4
    brightness_id = 10

    cap = cv2.VideoCapture(first_webcam_id)
    cap.set(width_id, 640)
    cap.set(height_id, 480)
    cap.set(brightness_id, 0)

    while True:
        _, img = cap.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), BGR_BLUE, 2)

        cv2.imshow('Video', img)
        # Wait until the q is press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade_ = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
detect_from_webcam(face_cascade_)
