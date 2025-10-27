import cv2
import numpy as np

# Baca gambar
gambar = cv2.imread('walpaper.jpg', cv2.IMREAD_GRAYSCALE)

# Cek apakah gambar berhasil dibaca
if gambar is None:
    print("Gambar tidak ditemukan! Pastikan file 'gambar_input.jpg' ada di folder yang sama.")
    exit()

# --- 1. Filter Gaussian (mengurangi noise) ---
blur = cv2.GaussianBlur(gambar, (5, 5), 0)

# --- 2. Deteksi tepi menggunakan Sobel ---
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

# --- 3. Deteksi tepi menggunakan Canny ---
canny = cv2.Canny(blur, 100, 200)

# --- 4. Tampilkan hasil ---
cv2.imshow("Gambar Asli", gambar)
cv2.imshow("Sobel Edge Detection", sobel / sobel.max())  # Normalisasi agar terlihat jelas
cv2.imshow("Canny Edge Detection", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
