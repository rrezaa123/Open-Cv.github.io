import cv2 as cv 

img = cv.imread('Foto/cat.jpeg')  # membaca gambar

cv.imshow('cat', img)   # menampilkan gambar

cv.waitKey(0)

# membaca video
#capture = cv.VideoCapture('Video/banner.mp4')

#while True:
#    isTrue, frame = capture.read()

#    cv.imshow('video', frame)

#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break

#capture.release()
#cv.destroyAllWindows