from scapy.all import *

sport = random.randint(1024,65535)

# SYN
ip=IP(src='172.16.120.5',dst='172.16.100.101')
SYN=TCP(sport=sport,dport=443,flags='S',seq=1000)
SYNACK=sr1(ip/SYN)

# SYN-ACK
ACK=TCP(sport=sport, dport=443, flags='A', seq=SYNACK.ack + 1, ack=SYNACK.seq + 1)
send(ip/ACK)