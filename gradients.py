import cv2 as cv
import numpy as np

img = cv.imread('Foto/udin.jpg')
cv. imshow('Udin', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_soble = cv.bitwise_or(sobelx, sobely)

cv.imshow('Soble x', sobelx)
cv.imshow('Soble y', sobely)
cv.imshow('Combined Soble', combined_soble)

cv.waitKey(0)