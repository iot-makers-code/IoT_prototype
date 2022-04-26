import RPi.GPIO as GPIO
import time
import requests
print("Check remote cds status")
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
while True:
   url = "http://192.168.200.11:8000/cds"
   r = requests.get(url)
   print(r.text)
   GPIO.output(18, True \
        if r.text == "ON" else False)
   time.sleep(.1)
GPIO.cleanup()
