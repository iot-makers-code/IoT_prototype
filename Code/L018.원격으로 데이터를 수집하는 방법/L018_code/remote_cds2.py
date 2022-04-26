import RPi.GPIO as GPIO
import time
import requests
print("Check remote cds status")
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
ips=['192.168.200.11:8000', '192.168.200.10:8000', '192.168.200.12:8000' ]

while True:
   for ip in ips:
      url = "http://"+ip+"/cds"
      try:
         r = requests.get(url, verify=False, timeout=1)
         print(ip+": "+ r.text)
      except:
         print(ip+": fail to connect")
      GPIO.output(18, True)
      time.sleep(0.1)
      GPIO.output(18, False)
   time.sleep(1)
GPIO.cleanup()
