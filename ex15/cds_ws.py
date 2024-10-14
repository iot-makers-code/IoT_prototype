from http.server import BaseHTTPRequestHandler, HTTPServer
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
class MyHandler(BaseHTTPRequestHandler):
     def do_GET(self):
        if self.path !="/cds": return
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        light ="ON" if GPIO.input(24) else 'OFF'
        self.wfile.write(bytes(light,"utf-8"))
        return
def run():
     server_addr =('0.0.0.0', 8000)
     httpd =HTTPServer(server_addr, MyHandler)
     print("starting web server ...")
     httpd.serve_forever()
run()

