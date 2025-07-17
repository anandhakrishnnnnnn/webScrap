
from scapy.all import IP, TCP, sr1

target = input("Enter the target IP address: ")

packet = IP(dst=target)/TCP(dport=80, flags="S")

response = sr1(packet, timeout=2)

if response:
    if response.haslayer(TCP):
        tcp_layer = response.getlayer(TCP)
        if tcp_layer.flags == "SA":
            print("Port 80 is open")
        elif tcp_layer.flags == "RA":
            print("Port 80 is closed")
        else:
            print(f"Recived unexpedted flag: {tcp_layer.flags}")
    else:
        print("No TCP layer found")
else:
    print("NO response , the port may closed or blocked")
