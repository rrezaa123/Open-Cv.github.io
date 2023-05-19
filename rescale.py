import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width,height):
     #live video
     capture.set(3,width)
     capture.set(4,height)

capture = cv.VideoCapture('Video/banner.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
           break

capture.release()
cv.destroyAllWindows