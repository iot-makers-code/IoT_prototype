import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
status=False
GPIO.output(18, status)
for i in range(30):
   print("ON" if ~status else "OFF"),
   raw_input(", Press enter key !")
   status = ~status
   GPIO.output(18, status)
GPIO.cleanup()