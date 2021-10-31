import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
for i in range(50):
   GPIO.output(18, GPIO.input(24))
   time.sleep(1)
