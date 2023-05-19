import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['jokowi', 'megawati', 'messi', 'ronaldo', 'windah']
# features = np.load('features.npy', allow_pickle=True)
# lables = np.load('lables.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_traind.yml')

img = cv.imread(r'C:\Users\Asus p1412Ce\OneDrive\Documents\#Folder\open cv latihan\var\leomessi\messi2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the img
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)


for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h, x:x+h]
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    lable,confidence = face_recognizer.predict(faces_roi)
    print(f'lable = {people[lable]} with a confidence of {confidence}')

    cv.putText(img, str(people[lable]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)


# prediction inaccuracy due to the lack of data used in training
# ketidak akuratan perdiksi karena kurang banyaknya data yang digunakan dalam pelatihan