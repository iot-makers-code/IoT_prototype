import RPi.GPIO as GPIO
import time
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
while True:
    time.sleep(0.1)
    inx = GPIO.input(24)
    url = "http://192.168.200.11:8000/"+\
           ("ON" if inx else "OFF")
    requests.get(url)
GPIO.clenaup()
