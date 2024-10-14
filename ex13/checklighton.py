import RPi.GPIO as GPIO
import time
import requests
print("Get file remote:")
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
for i in range(50):
     url="http://localhost:8000/DATA"
     r =requests.get(url)
     diff =time.time() - float(r.text)
     print(r.text, diff)
     signal =True if diff <5.0 else False
     GPIO.output(18, signal)
     time.sleep(2)
GPIO.cleanup()

