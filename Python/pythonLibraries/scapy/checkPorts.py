from scapy.all import*
    
ip="192.168.1.3"

ports=[22,21,23,80,443]

for port in ports:
    pkt=IP(dst=ip)/TCP(dport=port,flags="S")
    replay=sr1(pkt,timeout=1,verbose=0)

    if replay:
        if replay.haslayer(TCP):
            if replay[TCP].flags=="SA":
                 print(f"Port {port} is open ")
            elif replay[TCP].flags=="RA":
                print(f"Port {port} is closed")
        else:
            print(f"Port {port} responded, But no TCP layer found")
    else:
        print(f"{port} not found")

