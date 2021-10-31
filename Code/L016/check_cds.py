import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
print("Read light signal")
GPIO.setup(24,GPIO.IN)
while True:
    time.sleep(0.1)
    inx = GPIO.input(24)
    if inx:
       open("BRIGHT","w").close()
    else:
       if os.path.exists("BRIGHT"):
          os.remove("BRIGHT")
GPIO.cleanup()

