# mclient.py
import socket
host="127.0.0.1"
port=8080
s = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(bytes("HELLO",'UTF-8'))
while True:
   in_data = s.recv(1024)
   print("From Server :" ,in_data.decode())
   out_data = input()
   s.sendall(bytes(out_data,'UTF-8'))
   if out_data=='bye':
      break
s.close()

