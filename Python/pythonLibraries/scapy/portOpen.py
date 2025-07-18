from scapy.all import*

port=int(input("Enter the port ").strip())

pkt=IP(dst="8.8.8.8")/TCP(dport=port,flags="S")

response=sr1(pkt,timeout=1)

if response.haslayer(TCP):
    target_layer=response.getlayer(TCP)
    if target_layer.flags=="SA":
        print(f"port {port} is open")
    elif target_layer.flags=="RA":
        print(f"Port {port} is closed")
else:
    print("NO tcp layer found")
        
  
    

