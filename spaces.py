import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Foto/jokowi.jpg')
cv.imshow('Jokowi', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Hsv', hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(lab, cv.COLOR_HSV2BGR)
cv.imshow('hsv ---> bgr', hsv_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)