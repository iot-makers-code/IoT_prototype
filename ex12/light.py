import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Test photo regitster")
GPIO.setup(24, GPIO.IN)
cnt=500
for i in range(0,cnt,1):
   light = GPIO.input(24)
   print("input :", light)
   time.sleep(0.1)
GPIO.cleanup()
