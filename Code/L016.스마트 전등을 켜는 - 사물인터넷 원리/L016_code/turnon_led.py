import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
print("Turn on led")
GPIO.setup(18,GPIO.OUT)
GPIO.output(18, False)

while True:
    inx = os.path.exists("BRIGHT")
    GPIO.output(18, True if inx else False)
    time.sleep(0.1)
GPIO.cleanup()

