import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
cnt = 1000
for i in range(0,cnt,1):
   GPIO.output(18, True)
   GPIO.output(24, False)
   GPIO.output(21, False)
   time.sleep(0.2)
   GPIO.output(18, False)
   GPIO.output(24, True)
   GPIO.output(21, False)
   time.sleep(0.2)
   GPIO.output(18, False)
   GPIO.output(24, False)
   GPIO.output(21, True)
   time.sleep(0.2)
   print(i)
GPIO.cleanup()
