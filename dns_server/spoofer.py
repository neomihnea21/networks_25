from scapy.all import IP, UDP, DNS, DNSQR, send
spoofed_ip = "10.0.0.2"  
server_ip = "127.0.0.1" #i'll run the spoofer on localhost     
server_port = 9320          

pkt = IP(src=spoofed_ip, dst=server_ip) / \
      UDP(sport=12000, dport=server_port) / \
      DNS(rd=1, qd=DNSQR(qname="example.com"))

send(pkt)