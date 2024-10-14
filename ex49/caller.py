# UDP Broadcast Client. caller.py
import socket
import time
host = '<broadcast>'
port=37021
u = socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM,
                   socket.IPPROTO_UDP)
u.setsockopt(socket.SOL_SOCKET,
              socket.SO_BROADCAST, 1)
u.settimeout(3)
print("UDP, Device checker, caller")
while(True):
     u.sendto(b"broadcast message", (host, port))
     print("Broadcast message")
     try:
         while True:
             c, addr = u.recvfrom(1024)
             print("Message from callee {}".format(addr))
     except: #timeout
         pass
     time.sleep(1)

