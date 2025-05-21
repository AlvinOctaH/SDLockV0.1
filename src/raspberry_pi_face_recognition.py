import cv2
import requests
import pigpio  # Ganti dari RPi.GPIO
import time

# === Baca URL dari config.txt ===
with open("config.txt", "r") as f:
    base_url = f.read().strip()

url = base_url + "/face_recognition"

# === Setup pigpio untuk Servo ===
servo_pin = 18  # GPIO18 (Pin 12)
pi = pigpio.pi()
if not pi.connected:
    print("Gagal konek ke pigpio daemon. Jalankan 'sudo pigpiod' dulu.")
    exit()

def set_angle(angle):
    # Sudut 0–180 jadi pulsa 500–2500 µs, dibalik arah
    pulse_width = 500 + ((180 - angle) / 180.0) * 2000
    pi.set_servo_pulsewidth(servo_pin, pulse_width)

# === Mulai kamera ===
cap = cv2.VideoCapture(0)
window_name = "Pengenalan Wajah"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 480, 360)

print("Tekan 'q' untuk keluar.\n")

while True:
    ret, frame = cap.read()
    set_angle(0)
    if not ret:
        print("Gagal menangkap gambar.")
        continue

    cv2.imwrite("frame.jpg", frame)

    start_time = time.time()

    with open("frame.jpg", "rb") as img_file:
        files = {'image': img_file}
        try:
            res = requests.post(url, files=files)
            result = res.json()

            elapsed_time = time.time() - start_time

            if result['status'] == 'success':
                print(f"[✓] Wajah dikenali sebagai: {result['name']}")
                print(f"⏱️ Waktu respon sistem: {elapsed_time:.2f} detik")

                # Gerakkan servo ke 90 derajat, tunggu 5 detik, lalu kembali ke 0
                set_angle(90)
                time.sleep(5)
                set_angle(0)

            else:
                print("[✗] Wajah tidak dikenali atau spoof terdeteksi")
                print(f"⏱️ Waktu respon sistem: {elapsed_time:.2f} detik")
        except Exception as e:
            print("Gagal menghubungi server:", e)

    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Keluar dari sistem.")
        break

# === Bersihkan ===
cap.release()
cv2.destroyAllWindows()
pi.set_servo_pulsewidth(servo_pin, 0)  # Matikan sinyal servo
pi.stop()  # Matikan pigpio connection
