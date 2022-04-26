from BaseHTTPServer \
    import BaseHTTPRequestHandler,HTTPServer
from gpiozero import PWMOutputDevice
import time

pin1 = 23
pin2 = 24
pin3 =  8
pin4 = 25

forwardRight=PWMOutputDevice(pin1,True,0,1000)
reverseRight=PWMOutputDevice(pin2,True,0,1000)
forwardLeft=PWMOutputDevice(pin3,True,0,1000)
reverseLeft=PWMOutputDevice(pin4,True,0,1000)

def moveto(move):
    fr,rr,fl,rl,ti = move
    forwardRight.value = fr
    reverseRight.value = rr
    forwardLeft.value = fl
    reverseLeft.value = rl
    time.sleep(ti)
    STOP()

def STOP():
    forwardRight.value=0
    reverseRight.value=0
    forwardLeft.value=0
    reverseLeft.value=0
    
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path =='/favicon.ico': return
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        led=True if self.path=='/ON' else False
        
        message= '<a href=/FW>Forward</a><br>'\
                 '<a href=/BW>Backward</a><br>'\
                 '<a href=/LT>LeftTurn</a><br>'\
                 '<a href=/RT>RightTurn</a><br>'\
                 '<a href=/ST>STOP</a>'

        self.wfile.write(bytes(message))
        print(self.path)

        if self.path=='/FW':
            moveto([1, 0.0, 1, 0.0, 1.0])
        elif self.path=='/BW':
            moveto([0.0, 1, 0.0, 1, 1.0])
        elif self.path=='/LT':
            moveto([0.0, 0.0, 0.6, 0.0, 1.0])
        elif self.path=='/RT':
            moveto([0.6, 0.0, 0.0, 0.0, 1.0])
        elif self.path=='/ST':
            STOP()
        else:
            pass
        return

def run():
    server_addr=('0.0.0.0', 8000)
    httpd=HTTPServer(server_addr, MyHandler)
    print('starting web server...')
    httpd.serve_forever()
    
run()