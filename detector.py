# sniffer.py
from scapy.all import sniff, IP
import datetime
import os

# Create logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log files
all_ips_file = "logs/all_ips.txt"
spoof_log_file = "logs/spoof_log.txt"

# Known spoofing IPs (blacklist)
spoofing_ips = [
    "123.123.123.123",
    "10.0.0.99",
    "203.0.113.45"
]

def is_spoofed(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src

        # ✅ Always store every IP seen
        with open(all_ips_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - IP Detected: {src_ip}\n")

        print(f"🔍 IP Detected: {src_ip}")

        # Check if spoofed
        if src_ip in spoofing_ips:
            return True, src_ip
    return False, None

def process_packet(packet):
    spoofed, ip = is_spoofed(packet)
    if spoofed:
        log = f"[{datetime.datetime.now()}] Spoofed Packet Detected from IP: {ip}"
        print(log)
        with open(spoof_log_file, "a") as f:
            f.write(log + "\n")

print("🟢 Starting packet sniffing... Press Ctrl+C to stop.")

# Replace with your correct network interface (e.g., 'Wi-Fi', 'wlan0', 'eth0')
sniff(filter="ip", iface="Wi-Fi", prn=process_packet, store=0)
