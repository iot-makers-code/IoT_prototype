import RPi.GPIO as GPIO
import time
import requests
ips=['192.168.200.11:8000','192.168.200.12:8000']
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
while True:
    for ip in ips:
       url = "http://"+ip+"/cds"
       try:
          r = requests.get(url)
          if r.status_code == 200:
             print(ip+" :"+r.text)
          else:
             print(ip+"("+r.status_code+") error")
       except :
          print(ip+": fail to connect")

       GPIO.output(18, True)
       time.sleep(0.1)
       GPIO.output(18, False)
       time.sleep(1)
    time.sleep(5)
GPIO.clenaup()
