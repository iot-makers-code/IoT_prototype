import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
with open("DATA","wt") as d:
      d.write(str(time.time()))
for i in range(50):
     print("Update data.")
     if GPIO.input(24):
          with open("DATA","wt") as d:
               d.write(str(time.time()))
     time.sleep(2)
GPIO.cleanup()

