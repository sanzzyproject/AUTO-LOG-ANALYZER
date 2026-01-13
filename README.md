# 🛡️ Automated Log Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20Server-green?style=for-the-badge&logo=linux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen?style=for-the-badge)

**Automated Log Analyzer** adalah solusi ringan dan efisien untuk memantau kesehatan server Linux. Proyek ini menggabungkan kekuatan **Python** untuk analisis data statistik dan regex, dengan **Bash Scripting** untuk otomatisasi pipeline sistem.

Alat ini dirancang untuk membaca log akses web server (NGINX/Apache), mendeteksi anomali (seperti potensi serangan DDoS atau Brute Force), dan mengirimkan laporan harian secara otomatis tanpa intervensi manual.

---

## 🛠️ Prasyarat (Requirements)

Sebelum memulai, pastikan server atau lingkungan lokal Anda memiliki:

1.  **Sistem Operasi:** Linux (Ubuntu, Debian, CentOS, atau macOS).
2.  **Bahasa Pemrograman:** Python 3.6 atau lebih baru.
3.  **Akses:** Izin baca (*Read Permission*) ke file log server (biasanya di `/var/log/nginx/` atau `/var/log/apache2/`).

---

## 📥 Instalasi

Ikuti langkah-langkah berikut untuk memasang proyek ini di server Anda:

### 1. Clone Repository
```bash
git clone [https://github.com/username-anda/auto-log-analyzer.git](https://github.com/username-anda/auto-log-analyzer.git)
cd auto-log-analyzer


## 🚀 Fitur Utama

* **🔍 Deep Parsing:** Menggunakan Regex yang dioptimalkan untuk membaca format *Nginx/Apache Combined Log*.
* **🛡️ Threat Detection:** Otomatis mendeteksi alamat IP yang melakukan permintaan berlebihan (*Suspicious Activity*).
* **📊 Traffic Analytics:** Menghitung total request, distribusi HTTP status code (200, 404, 500), dan *peak hours* (trafik per jam).
* **📑 Multi-Format Report:** Mendukung ekspor laporan dalam format `.txt` (human-readable) dan `.json` (untuk integrasi API/Dashboard).
* **⏰ Zero-Touch Automation:** Terintegrasi penuh dengan Linux Cronjob untuk berjalan di latar belakang.

---

## 📂 Struktur Proyek

```text
auto-log-analyzer/
├── 📂 logs/                # Direktori input (contoh access.log)
├── 📂 reports/             # Direktori output (laporan tersimpan di sini)
├── 📂 scripts/
│   └── run_daily.sh        # Entry point untuk Cronjob/Automation
├── 📂 src/
│   └── main.py             # Core logic analisis (Python)
├── .gitignore
└── README.md
