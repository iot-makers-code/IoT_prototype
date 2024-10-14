# notifier.py
import socket
name = socket.gethostname()
host="127.0.0.1"
port=20001
u = socket.socket(family=socket.AF_INET,
                   type=socket.SOCK_DGRAM)
u.settimeout(5.0)
u.sendto("Hello UDP Listener".encode('UTF-8'),
            (host, port))
c, addr = u.recvfrom(1024)
print("Message from listener {}".format(addr))

