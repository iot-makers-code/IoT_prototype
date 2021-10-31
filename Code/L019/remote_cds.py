import RPi.GPIO as GPIO
import time
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
while True:
    url = "http://192.168.200.11:8000/cds"
    response = requests.get(url)
    print(response.text)
    GPIO.output(18, True \
        if response.text=="ON" else False)
    time.sleep(2)
    
GPIO.clenaup()
