# UDP Broadcast announce Clients
import socket
import time
host = '<broadcast>'
port=37020
u = socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM,
                   socket.IPPROTO_UDP)
u.setsockopt(socket.SOL_SOCKET,
                 socket.SO_BROADCAST, 1)
u.settimeout(0.2)
print("UDP Broadcaster up and announce message")
while(True):
     u.sendto(b"broadcast message", (host, port))
     print("Broadcast message")
     time.sleep(1)

