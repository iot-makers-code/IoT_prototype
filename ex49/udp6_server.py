# UDP IPv6 server
import socket
host = "::" # = 0.0.0.0 u IPv4
port=5005
s = socket.socket(socket.AF_INET6, # IPv6
socket.SOCK_DGRAM) # UDP
s.bind((host, port))
print ("Start, UPD IPv6 Server")
while True:
c, addr = s.recvfrom(1024)
print("received [{}] from {} :".
            format(c.decode(), addr))

