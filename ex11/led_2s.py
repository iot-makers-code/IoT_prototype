import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
cnt = 1000
for i in range(0,cnt,1):
   GPIO.output(18, True)
   GPIO.output(24, False)
   time.sleep(1)
   GPIO.output(18, False)
   GPIO.output(24, True)
   time.sleep(1)
   print(i)
GPIO.cleanup()
