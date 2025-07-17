from scapy.all import *

packet = IP(dst="8.8.8.8")/TCP(dport=80, flags="S")
packet.show()

