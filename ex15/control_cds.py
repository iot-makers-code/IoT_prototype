import RPi.GPIO as GPIO
import time
import requests
print("Check remote cds status.")
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
try:
      while True:
           url="http://localhost:8000/cds"
           response = requests.get(url)
           print(response.text)
           GPIO.output(18, True\
                if response.text=="ON" else False)
           time.sleep(2)
except KeyboardInterrupt:
      pass
finally:
      GPIO.cleanup()

