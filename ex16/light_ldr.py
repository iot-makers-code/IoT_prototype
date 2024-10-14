import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
def cdstime():
    GPIO.setup(24,GPIO.OUT)
    GPIO.output(24, False)
    time.sleep(0.1)
   
    GPIO.setup(24,GPIO.IN)
    Light=0
    while(GPIO.input(24) == False):
       Light += 1
    return Light
 
try:
   while True:
     print("Light:", cdstime())
except KeyboardInterrupt:
   pass
finally:
   GPIO.cleanup()

