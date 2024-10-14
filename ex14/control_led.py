import RPi.GPIO as GPIO
import time
import requests
GPIO.setmode(GPIO.BCM)
print("Remote On/Off led:")
GPIO.setup(24,GPIO.IN)
try:
      while True:
           time.sleep(1)
           inx=GPIO.input(24)
           url='http://localhost:8000/'+('ON'if inx else 'OFF')
           print(url)
           requests.get(url)
           print("finish!")
except KeyboardInterrupt:
      pass
finally:
      GPIO.cleanup()

