import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
pins=[12,16,20,23,18,25,24,21]
for p in pins:
     GPIO.setup(p, GPIO.OUT);
     GPIO.output(p, 1)
 
while True:
     for p in range(len(pins)):
         p = pins[i]
         print(p)
         GPIO.output(p, 0)
         time.sleep(.5)
         GPIO.output(p, 1)
         time.sleep(.5)

