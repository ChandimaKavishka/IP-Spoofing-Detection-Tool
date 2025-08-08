from scapy.all import IP, send

your_ip = "192.168.1.55"

# Send a fake (spoofed) IP packet
packet = IP(src="123.123.123.123", dst=your_ip)
send(packet)
