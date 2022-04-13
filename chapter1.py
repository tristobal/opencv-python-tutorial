import cv2


def show_image():
    img = cv2.imread('resources/lena.png')
    cv2.imshow('Output', img)

    # The window shows the image until you press any key on keyboard
    cv2.waitKey(0)


def show_video():
    cap = cv2.VideoCapture('resources/lomi.mp4')
    while True:
        success, img = cap.read()
        cv2.imshow('Video', img)
        # Wait until the q is press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def show_webcam():
    first_webcam_id = 0
    width_id = 3
    height_id = 4
    brightness_id = 10

    cap = cv2.VideoCapture(first_webcam_id)
    cap.set(width_id, 640)
    cap.set(height_id, 480)
    cap.set(brightness_id, 100)
  
    while True:
        success, img = cap.read()
        cv2.imshow('Video', img)
        # Wait until the q is press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

show_webcam()