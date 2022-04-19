"""
    Resizing and cropping
"""
# Workaround for OpenCV imports in PyCharm
import cv2.cv2 as cv2

img = cv2.imread('resources/lena.png')
# (x, y, number of channels 3 = RGB)
print(f'Original image {img.shape}')

# (x, y)
img_resized = cv2.resize(img, (262, 262))
print(f'Resized image {img_resized.shape}')

# [range of y, range of x]
img_cropped = img[0:262, 0:262]
print(f'Cropped image {img_cropped.shape}')


cv2.imshow("Lena", img)
cv2.imshow("Lena resized", img_resized)
cv2.imshow("Lena cropped", img_cropped)
cv2.waitKey(0)
