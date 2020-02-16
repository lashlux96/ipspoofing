########Generating Random Source and Destination IP Addresses with Scapy######

from scapy.all import *

i = 0

while i<100:
    srcIP = RandIP()
    dstIP = RandIP()
    c = 10000
    d = 15000
    payload = "This is a test"
    packet = IP(src = srcIP, dst= dstIP)/ TCP(sport=c, dport=15000) /payload
    send(packet)
    i=i+1

