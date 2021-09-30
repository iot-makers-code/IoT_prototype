import RPi.GPIO as GPIO
import time
pins = [18, 24, 21]
GPIO.setmode(GPIO.BCM)
for p in pins:
   GPIO.setup(p, GPIO.OUT);GPIO.output(False)

cnt = 1000
for i in range(0, cnt, 1):
    for c in range(0,length(pins),1):
        for p in pins:
            if c == pins.index(p):
                GPIO.output(18, True)
            else:
                GPIO.output(18, False)
   time.sleep(0.2)
   print(i)
GPIO.cleanup()

 