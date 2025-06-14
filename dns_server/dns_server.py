
import socket, struct

#Aici vom trimite traficul nedorit
dead_ip="0.0.0.0"
dead_port=53

with open("badnames/wrongip.txt", "r") as input_file:
   bad_ips=input_file.readlines()
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
trash_sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #reclamele sunt gunoi, si merg aici sa moara
sock.bind(("0.0.0.0", 9320)) #vom asculta aici

def dns_checker(data): #e posibil ca acel pachet sa nu fie DNS
    if len(data)<12:
        return False
    try:
        (_, _,
         qdcount,
         _, _, _) = struct.unpack("!6H", data[:12])
        return qdcount>0
    except struct.error:
       return False
while True:
    try:
        outfile=open("blocks.txt", 'w')
        data, addr=sock.recvfrom(512) # a DNS packet won't be larger
        ip=addr[0]
        if ip in bad_ips and dns_checker(data) == True:
            outfile.write(f"blacklisted query from IP {ip}\n")
            #do stats on who sends spam traffic
            trash_sock.sendto(data, (dead_ip, dead_port)) #le aruncam, ca nu asculta pe nimic
    except KeyboardInterrupt:
        print("We killed the server")
        break
