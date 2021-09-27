import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT);GPIO.output(25, False)
GPIO.setup(8, GPIO.OUT);GPIO.output(8, False)
time.sleep(0.1)
cnt=10
for i in range(0,cnt,1):
   GPIO.output(25, False)
   time.sleep(0.2)
   GPIO.output(25, True)
   time.sleep(0.2)
   print(i)
GPIO.cleanup()