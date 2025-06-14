import socket
with open("badnames/adservers.txt", 'r') as input_file:
    lines=input_file.readlines()
list_urls=[line.split()[1] for line in lines]

output_file=open("badnames/wrongip.txt", "w")
counted_ips=0
for url in list_urls:
      print(counted_ips)
      counted_ips+=1
      try:
        ip = socket.gethostbyname(url)
        output_file.write(ip + "\n")
      except socket.gaierror:
        print("url dead")