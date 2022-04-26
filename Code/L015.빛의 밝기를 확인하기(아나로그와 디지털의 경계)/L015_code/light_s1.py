import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
print("Test photo regitster")
GPIO.setup(24, GPIO.IN)
cnt=60*50
for i in range(0,cnt,1):
   light = GPIO.input(24)
   sys.stdout.write("#" if light else "_")
   if i % 60 == 59 :
      sys.stdout.write("\n")
   sys.stdout.flush()
   time.sleep(0.01)
GPIO.cleanup()
