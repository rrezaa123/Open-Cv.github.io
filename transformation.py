import cv2 as cv
import numpy as np

img = cv.imread("Foto/cat.jpeg")
cv.imshow('cat', img)


# Translation

def translate(img, x, y ):
    transMath = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMath, dimension)

# -x --> kanan
# x --> kiri
# -y --> atas
# y --> bawah

translated = translate(img, 100, 100)
cv.imshow('Translate', translated)


# Rotation 
def rotate(img, angle, rotPoin=None):
    (height,width) = img.shape[:2]

    if rotPoin is None:
        rotPoin = (width//2,height//2)

    rotMath = cv.getRotationMatrix2D(rotPoin, angle, 1.0)
    dimension = (width,height)

    return cv.warpAffine(img, rotMath, dimension)

rotated = rotate(img, -45)
cv.imshow("rotated", rotated)

rotated_rotated = rotate(img, -90)
cv.imshow("Rotated Rotated", rotated_rotated)


# resizing  // ukuran
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)


# Fliping // membalik 
flip = cv.flip(img, 0)   #flipcode -1,0,1
cv.imshow('flip', flip)

# Cropping
crop = img[200:400, 200:400]
cv.imshow("crop", crop)

cv.waitKey(0)