# import dlib
# import cv2

# # Load the detector
# detector = dlib.get_frontal_face_detector()

# # Load the image
# img = cv2.imread('Foto/bts.jpg')

# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Detect faces in the image
# faces = detector(gray)

# # Draw a rectangle around each face
# for face in faces:
#     x, y, w, h = face.left(), face.top(), face.width(), face.height()
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Display the image
# cv2.imshow('Detected Faces', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
