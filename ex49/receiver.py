# UDP broadcast receive Server
import socket
host=""
port=37020
u = socket.socket(family=socket.AF_INET,
                   type=socket.SOCK_DGRAM,
                   proto=socket.IPPROTO_UDP)
u.setsockopt(socket.SOL_SOCKET,
                 socket.SO_BROADCAST, 1)
u.bind((host, port))
print("Broadcast receiver start")
while True:
     c, addr = u.recvfrom(1024)
     print("Message from Server {}".format(addr))

