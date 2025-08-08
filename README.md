IP-Spoofing-Detection-Tool

What is IP Spoofing?
IP spoofing is when an attacker sends packets with a fake source IP address to hide their identity or impersonate a trusted source.

A simple tool to detect and log spoofed IP packets in real-time using Python and Scapy. It checks incoming packets, identifies fake (spoofed) IP addresses, logs them, and displays logs via a Flask web interface.

Features
- Real-time network packet sniffing using Scapy
- Detects spoofed IP addresses
- Logs spoofed packets with timestamp
- View logs in a browser using Flask web interface

How to Run files

python detector.py
python webapp.py

after if you want to check the spoofed IP address, detect this system, you want to run the spoof_sender file.

Now you can see and add all IPs and the spoof IPs app to log files.

Check the web dashboard is real-time running using this URL: http://127.0.0.1:5000

