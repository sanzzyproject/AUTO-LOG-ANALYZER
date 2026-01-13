#!/bin/bash

# === CONFIGURATION ===
# Mendapatkan direktori tempat script ini berada agar path absolut
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."
LOG_FILE="/var/log/nginx/access.log" # Ganti dengan lokasi log asli Anda
OUTPUT_DIR="$PROJECT_ROOT/reports"
PYTHON_SCRIPT="$PROJECT_ROOT/src/main.py"

# Cek apakah folder reports ada, jika tidak buat baru
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
fi

# Cek apakah file log ada (Untuk testing, bisa arahkan ke dummy log di folder project)
# Jika dijalankan di server production, pastikan user memiliki izin baca ke /var/log/
if [ ! -f "$LOG_FILE" ]; then
    echo "[ERROR] Log file tidak ditemukan di $LOG_FILE"
    # Fallback ke sample log untuk testing
    LOG_FILE="$PROJECT_ROOT/logs/access.log"
    echo "[INFO] Menggunakan sample log: $LOG_FILE"
fi

echo "=== Memulai Analisis Log: $(date) ==="

# Menjalankan Python Analyzer
# Menggunakan python3
python3 "$PYTHON_SCRIPT" --file "$LOG_FILE" --format txt --outdir "$OUTPUT_DIR"

# Cek status exit code
if [ $? -eq 0 ]; then
    echo "[SUCCESS] Analisis selesai. Cek folder reports."
else
    echo "[FAIL] Terjadi kesalahan saat menjalankan script Python."
fi

echo "========================================="
