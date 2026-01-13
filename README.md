# 📊 Automated Server Log Analyzer

**Automated Log Analyzer** adalah *tools* berbasis Python dan Bash untuk menganalisis log server (seperti NGINX atau Apache) secara otomatis. Alat ini dirancang untuk mendeteksi anomali trafik, mencatat statistik request per jam, dan menghasilkan laporan harian yang dijalankan melalui Cronjob.

## 🚀 Fitur Utama

- **Parsing Otomatis:** Mendukung format standar NGINX/Apache Combined Log.
- **Deteksi Mencurigakan:** Mengidentifikasi IP dengan jumlah request yang tidak wajar (potensi DDoS/Bruteforce).
- **Statistik Trafik:** Menghitung request per jam dan distribusi HTTP status code (200, 404, 500, dll).
- **Format Laporan Fleksibel:** Ekspor laporan dalam bentuk `.txt` (mudah dibaca) atau `.json` (untuk integrasi lain).
- **Otomasi Penuh:** Dilengkapi script Bash untuk penjadwalan menggunakan Cronjob.

## 📂 Struktur Proyek

```text
auto-log-analyzer/
├── src/
│   └── main.py          # Logika analisis (Python)
├── scripts/
│   └── run_daily.sh     # Pipeline untuk Cronjob (Bash)
├── logs/                # Tempat menaruh file log (input)
├── reports/             # Hasil analisis tersimpan di sini
└── README.md
