from scapy.all import*

ip_base="192.168.1."

for i in range(1,11):
    ip=ip_base + str(i)
    pkt=IP(dst=ip)/ICMP()
    replay=sr1(pkt,timeout=1,verbose=0)

    if replay:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is not reachable")