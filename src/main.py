import re
import sys
import json
import argparse
from datetime import datetime
from collections import Counter, defaultdict

# Konfigurasi Threshold untuk "Suspicious IP"
SUSPICIOUS_THRESHOLD = 50  # IP dianggap mencurigakan jika request > 50 kali (bisa disesuaikan)

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        # Regex untuk Nginx/Apache Combined Log Format
        self.log_pattern = re.compile(
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<path>.*?) .*?" (?P<status>\d+) (?P<size>\d+)'
        )
        self.data = {
            "total_requests": 0,
            "status_codes": Counter(),
            "ip_addresses": Counter(),
            "hourly_traffic": defaultdict(int),
            "suspicious_ips": []
        }

    def parse_log(self):
        """Membaca file log baris demi baris"""
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    match = self.log_pattern.search(line)
                    if match:
                        self._process_match(match)
        except FileNotFoundError:
            print(f"Error: File {self.log_file} tidak ditemukan.")
            sys.exit(1)

    def _process_match(self, match):
        """Memproses data dari regex"""
        self.data["total_requests"] += 1
        
        ip = match.group("ip")
        status = match.group("status")
        timestamp_str = match.group("date")
        
        # Hitung IP dan Status
        self.data["ip_addresses"][ip] += 1
        self.data["status_codes"][status] += 1

        # Hitung Traffic per Jam
        # Format date log biasanya: 10/Oct/2000:13:55:36 -0700
        try:
            dt_object = datetime.strptime(timestamp_str.split()[0], "%d/%b/%Y:%H:%M:%S")
            hour_key = dt_object.strftime("%Y-%m-%d %H:00")
            self.data["hourly_traffic"][hour_key] += 1
        except ValueError:
            pass

    def detect_suspicious(self):
        """Mendeteksi IP yang melakukan request berlebihan"""
        for ip, count in self.data["ip_addresses"].items():
            if count > SUSPICIOUS_THRESHOLD:
                self.data["suspicious_ips"].append({"ip": ip, "count": count})

    def export_report(self, output_format="txt", output_path="report"):
        """Export hasil ke JSON atau TXT"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_path}/log_report_{timestamp}.{output_format}"

        if output_format == "json":
            with open(filename, 'w') as f:
                json.dump(self.data, f, indent=4, default=str)
        else:
            with open(filename, 'w') as f:
                f.write("=== SERVER LOG ANALYSIS REPORT ===\n")
                f.write(f"Generated at: {datetime.now()}\n")
                f.write(f"Total Requests: {self.data['total_requests']}\n\n")
                
                f.write("--- Suspicious IPs (Potential DDoS/Bruteforce) ---\n")
                if not self.data["suspicious_ips"]:
                    f.write("No suspicious activity detected.\n")
                for item in self.data["suspicious_ips"]:
                    f.write(f"IP: {item['ip']} - Requests: {item['count']}\n")

                f.write("\n--- Status Code Distribution ---\n")
                for code, count in self.data["status_codes"].most_common():
                    f.write(f"{code}: {count}\n")
                
                f.write("\n--- Top 5 Active IPs ---\n")
                for ip, count in self.data["ip_addresses"].most_common(5):
                    f.write(f"{ip}: {count}\n")

        print(f"Laporan berhasil dibuat: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Server Log Analyzer")
    parser.add_argument("--file", required=True, help="Path ke file log (access.log)")
    parser.add_argument("--format", choices=["json", "txt"], default="txt", help="Format output laporan")
    parser.add_argument("--outdir", default="./reports", help="Folder tujuan laporan")
    
    args = parser.parse_args()

    analyzer = LogAnalyzer(args.file)
    analyzer.parse_log()
    analyzer.detect_suspicious()
    analyzer.export_report(args.format, args.outdir)
