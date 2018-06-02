import sys;
from scapy.all import send, IP, ICMP, TCP

for i in range(4000, 4009):
    for j in range(1, 10):
        packet = IP(src="192.168.0."+str(j), dst="192.168.10.132")/TCP(sport=i,dport=80,flags="S")
        send(packet)