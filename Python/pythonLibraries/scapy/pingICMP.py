from scapy.all import*

pkt=IP(dst="8.8.8.8")/ICMP()

responce=sr1(pkt,timeout=2)

if responce:
    print("Replayed")
else:
    print("Not replayed")
