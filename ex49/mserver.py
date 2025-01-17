# mserver.py
import socket, threading
class ClientThread(threading.Thread):
     def __init__(self,addr,c):
         threading.Thread.__init__(self)
         self.conn = c
         print("New connection added: ", addr)
     def run(self):
         print("Connection from: ", addr)
         msg = ''
         while True:
             data = self.conn.recv(2048)
             msg = data.decode()
             if msg=='bye':
               break
             print ("\"{}\" from client [{}]"
                  .format(msg,addr))
             self.conn.send(bytes(msg,'UTF-8'))
         self.conn.close()
         print("Client at ", addr,
                  "disconnected...")
        
host="127.0.0.1"
port=8080
s = socket.socket(socket.AF_INET,
                   socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,
              socket.SO_REUSEADDR, 1)
s.bind((host, port))
print("Server started")
print("Waiting for client request..")
while True:
     s.listen(1)
     conn, addr = s.accept()
     n = ClientThread(addr, conn)
     n.start()

