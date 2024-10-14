import socket
s = socket.socket()
host = socket.gethostname()
port=2222
s.bind((host, port))
s.listen(5)
print('Start socket server')
while True:
     conn, addr = s.accept()
     print('Got connection from', addr)
     conn.send(b'Thank you for connecting')
     conn.close()
s.close()

