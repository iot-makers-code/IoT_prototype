#listener.py
import socket
host="0.0.0.0"
port=20001
u = socket.socket(family=socket.AF_INET,
                   type=socket.SOCK_DGRAM)
u.bind((host, port))
print("UDP server up and listening")
while(True):
     c, addr = u.recvfrom(1024)
     print("Message [{}] from {}".format(c, addr))
     u.sendto(b'Hello UDP Client', addr)

