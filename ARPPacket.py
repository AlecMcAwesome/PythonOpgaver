import sys
from scapy.all import ARP

packet = Ether()/ARP(op="who-has", hwsrc="00:11:22:33:44:55", psrc="192.168.65.66", pdst="192.168.65.1")

sendp(packet)