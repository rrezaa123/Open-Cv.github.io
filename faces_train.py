import os
import cv2 as cv
import numpy as np

people = ['jokowi', 'megawati', 'messi', 'ronaldo', 'windah']
DIR = r'C:\Users\Asus p1412Ce\OneDrive\Documents\#Folder\open cv latihan\Faces'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
lables = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        lable = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)


            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                lables.append(lable)

create_train()
print('Training done ---------------')

features =  np.array(features, dtype='object')
lables = np.array(lables)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train recognizer on the features list and the lables list
face_recognizer.train(features,lables)

face_recognizer.save('face_traind.yml')
np.save('features.npy', features)
np.save('lables.npy', lables)