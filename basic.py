import cv2 as cv

img = cv.imread('Foto/Capybara.jpg')
cv.imshow('Capybara', img)

# converting to grayscale // "Konversi ke skala abu-abu"
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur // "membuat gambar menjadi blur"
blur = cv.GaussianBlur(img, (1,1), cv.BORDER_DEFAULT)    # (7,7) Tingkat blur hanya dapat menggunakan angka Ganjil
cv.imshow('Blur', blur)

# Edge cascade // ("algoritma Canny Edge Detection")
canny = cv.Canny(blur, 125, 175)   # dapat di gabungkan dengan blur atau dengan fungsi lainnya
cv.imshow('Canny Edge', canny)

# Dilating the image // "Operasi dilasi pada gambar"
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# eroded // "operasi erosi pada gambar."
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize // "merubah ukuran gambar. "
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)  #Opsi ini mengacu pada metode interpolasi bicubic yang digunakan untuk mengubah ukuran gambar
cv.imshow('Resized', resized)

# Croping // "memotong " img
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)