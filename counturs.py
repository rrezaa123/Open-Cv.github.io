import cv2 as cv
import numpy as np

img = cv.imread('Foto/cat.jpeg')
cv.imshow('cat', img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125,175)
# cv.imshow('Canny Edges', canny)

ret, tresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('thresh', tresh)

contours, hierarchies = cv.findContours(tresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) ditemukan!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Countours Draw', blank)




cv.waitKey(0)