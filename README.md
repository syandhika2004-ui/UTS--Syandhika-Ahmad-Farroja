
Deteksi Tepi Menggunakan OpenCV (Edge Detection)

Deskripsi Proyek

Proyek ini merupakan implementasi dari materi Pengolahan Citra Digital, khususnya pada topik Deteksi Tepi (Edge Detection).
Program ini menggunakan Python dan OpenCV untuk mendeteksi batas-batas objek pada citra digital menggunakan dua metode populer, yaitu Sobel Operator dan Canny Edge Detection.
Tujuan utama dari proyek ini adalah memahami bagaimana tepi objek dapat diekstraksi dari gambar melalui perhitungan gradien intensitas piksel dan penghilangan noise.

Contoh Materi

Apa itu Deteksi Tepi?

Deteksi tepi adalah proses menemukan perubahan intensitas yang signifikan di dalam gambar. Tepi ini biasanya menandai batas antara dua area berbeda — misalnya antara objek dan latar belakang.
Dalam pengolahan citra digital, deteksi tepi penting untuk:

•	Segmentasi objek
•	Pengenalan bentuk (shape recognition)
•	Pelacakan objek (object tracking)
•	Kompresi citra dan visi komputer

Algoritma yang Digunakan

1. Gaussian Blur

Sebelum mendeteksi tepi, gambar terlebih dahulu difilter menggunakan Gaussian Blur untuk mengurangi noise.
blur = cv2.GaussianBlur(gambar, (5, 5), 0)

2. Sobel Operator

Sobel menghitung gradien intensitas citra di arah horizontal (x) dan vertikal (y) untuk menentukan lokasi perubahan intensitas terbesar.
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

3. Canny Edge Detection

Metode ini lebih kompleks karena melibatkan beberapa tahap:

1.	Gaussian filter untuk menghilangkan noise
2.	Gradient calculation untuk mencari perubahan intensitas
3.	Non-maximum suppression untuk mempertajam tepi
4.	Double threshold dan edge tracking untuk menghasilkan hasil akhir yang jelas
canny = cv2.Canny(blur, 100, 200)

```Python
Kode Program

import cv2
import numpy as np

# Baca gambar grayscale
gambar = cv2.imread('gambar_input.jpg', cv2.IMREAD_GRAYSCALE)

# Cek apakah gambar ditemukan
if gambar is None:
    print("Gambar tidak ditemukan! Pastikan file 'gambar_input.jpg' ada di folder yang sama.")
    exit()

# Filter Gaussian untuk mengurangi noise
blur = cv2.GaussianBlur(gambar, (5, 5), 0)

# Deteksi tepi menggunakan Sobel
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

# Deteksi tepi menggunakan Canny
canny = cv2.Canny(blur, 100, 200)

# Tampilkan hasil
cv2.imshow("Gambar Asli", gambar)
cv2.imshow("Sobel Edge Detection", sobel / sobel.max())
cv2.imshow("Canny Edge Detection", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

Hasil Output
Program akan menampilkan tiga jendela:

1.	Gambar Asli
2.	Deteksi Tepi Sobel
3.	Deteksi Tepi Canny
Hasilnya akan menunjukkan perbedaan ketajaman dan akurasi antara kedua metode.

Metode	Kelebihan	Kekurangan
Sobel	Sederhana, cepat, cocok untuk pemahaman dasar	Rentan terhadap noise
Canny	Akurat, hasil tajam, kuat terhadap noise	Lebih kompleks dan lambat
		
Kesimpulan

Deteksi tepi adalah salah satu langkah fundamental dalam pengolahan citra digital.

•	Sobel Operator cocok untuk pembelajaran awal karena mudah dipahami secara matematis.
•	Canny Edge Detection lebih unggul untuk aplikasi nyata karena hasilnya lebih bersih dan tajam.

Teknologi yang Digunakan

•	Python 3.x
•	OpenCV (cv2)
•	NumPy

Cara Menjalankan Program

1.	Pastikan Python dan OpenCV sudah terinstal:
2.	pip install opencv-python numpy
3.	Simpan file program dengan nama deteksi_tepi.py
4.	Simpan gambar (misalnya gambar_input.jpg) di folder yang sama
5.	Jalankan:
6.	python deteksi_tepi.py

Kontributor

Nama: Syandhika A.F.

Program Studi: Informatika

Semester: 5 (Lima)

Mata Kuliah: Pengolahan Citra Digital
