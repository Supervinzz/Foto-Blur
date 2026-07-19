# 📸 Peace Blur - Hand Gesture Blur Effect

Program Python yang otomatis blur layar kamera ketika kamu menunjukkan gesture peace (✌️).

## 🎯 Fitur
- Deteksi hand gesture peace secara real-time
- Auto blur effect ketika gesture terdeteksi
- Tanpa garis-garis tracking yang mengganggu
- Mudah digunakan

## 📋 Requirements
- Python 3.10 atau lebih baru
- Webcam/Kamera
- Windows/Mac/Linux

## 🚀 Cara Install

### 1. Install Python
Pastikan Python sudah terinstall di komputer. Cek dengan:
```bash
python --version
```

### 2. Download Project
Download atau clone repository ini ke komputer kamu.

### 3. Install Dependencies
Buka terminal/command prompt di folder project, lalu jalankan:

```bash
pip install -r requirements.txt
```

**Catatan:** Proses install mungkin memakan waktu karena download model MediaPipe (~10MB).

## 💻 Cara Menggunakan

1. Jalankan program:
```bash
python blur.py
```

2. Kamera akan terbuka otomatis

3. Tunjukkan gesture peace (✌️) ke kamera - layar akan blur otomatis

4. Tekan **ESC** untuk keluar

## 📦 File Structure
```
Foto-Blur/
├── blur.py              # File utama program
├── requirements.txt     # List dependencies
└── README.md           # File ini
```

## 🛠️ Troubleshooting

### Error: "No module named 'cv2'"
```bash
pip install opencv-python
```

### Error: "No module named 'cvzone'"
```bash
pip install cvzone mediapipe
```

### Kamera tidak terbuka
- Pastikan webcam tidak digunakan aplikasi lain
- Coba restart komputer
- Cek permission kamera di settings

### Program lambat
- Tutup aplikasi lain yang menggunakan banyak resource
- Pastikan pencahayaan cukup baik

## 🎮 Gesture yang Terdeteksi
- ✌️ **Peace Sign**: Telunjuk dan jari tengah naik, jari lainnya turun

## 📝 Dependencies
- `opencv-python` - Untuk akses kamera dan image processing
- `cvzone` - Untuk hand detection yang mudah
- `mediapipe` - Engine deteksi tangan dari Google
- `numpy` - Array processing

## 👨‍💻 Developer
Dibuat dengan ❤️ menggunakan Python & MediaPipe

## 📄 License
Free to use - Silakan modifikasi sesuai kebutuhan!

---
**Tips:** Pastikan tangan kamu terlihat jelas di kamera dan pencahayaan cukup untuk deteksi yang optimal! 🌟
