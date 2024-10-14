# UDP IPv6 client
import socket
import time
host = "::1" # localhost
port=5005
s = socket.socket(socket.AF_INET6, # IPv6
socket.SOCK_DGRAM) # UDP
i = 0
print ("Start, UPD IPv6 Client")
while True:
     s.sendto("{}".format(i).encode("UTF-8"),
                (host, port))
     print(i)
     i += 1
     time.sleep(1)

