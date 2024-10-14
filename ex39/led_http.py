from http.server\
     import BaseHTTPRequestHandler,HTTPServer
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
class MyHandler(BaseHTTPRequestHandler):
     def do_GET(self):
         if self.path == '/favicon.ico': return
         self.send_response(200)
         self.send_header('Content-type','text/html')
         self.end_headers()
         Relay =True if self.path =='/ON' else False
         GPIO.output(23, Relay==True)
         message = '<a href=/ON>SWITCH ON</a><br>'\
                     '<a href=/OFF>SWITCH OFF</a>'
         self.wfile.write(bytes(message,"utf-8"))
         return
def run():
     server_addr =('0.0.0.0', 8000)
     httpd = HTTPServer(server_addr, MyHandler)
     print('starting web server...')
     httpd.serve_forever()
run()

