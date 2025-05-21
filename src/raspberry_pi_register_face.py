import cv2
import requests

# === Baca URL ngrok dari config.txt ===
with open("config.txt", "r") as f:
    base_url = f.read().strip()

url = base_url + "/register_face"

# === Buka kamera ===
cap = cv2.VideoCapture(0)
print("Tekan 's' untuk ambil selfie, atau 'q' untuk keluar.")

# === Ukuran tampilan sedang (misalnya 480x360) ===
window_name = "Daftar Wajah"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 480, 360)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca kamera.")
        continue

    cv2.imshow(window_name, frame)
    key = cv2.waitKey(1)

    if key & 0xFF == ord('s'):
        cv2.imwrite("selfie.jpg", frame)
        break
    elif key & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        exit()

cap.release()
cv2.destroyAllWindows()

# === Input nama pengguna ===
username = input("Masukkan nama pengguna: ")

# === Kirim ke server ===
files = {'image': open("selfie.jpg", 'rb')}
data = {'name': username}
response = requests.post(url, files=files, data=data)

print("Respons server:", response.json())
