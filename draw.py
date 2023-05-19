import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

#img = cv.imread('Foto/cat.jpeg')
#cv.imshow('cat', img)

# 1.Paint the image a certain colour  (menggambar dengan warna)
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green',blank)


# # 2.Draw a Rectangle  (menggambar persegi panjang)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) # thickness="ketebalan garis pinggir"
# cv.imshow('Rectangle', blank)


# # 3.Draw a cricle (lingkaran)
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,(0,0,255), thickness=-1)     # (blank.shape[1]//2, blank.shape[0]//2) sama dengan (255,255)
# cv.imshow('Circle', blank)


# # 4.Draw a line (garis)
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('line', blank)

# 5.Write text (Menulis text)
cv.putText (blank, 'Hallo, my name is Reza', (45,255) , cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0))
cv.imshow("text", blank)


cv.waitKey(0)