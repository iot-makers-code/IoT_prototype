import RPi.GPIO as GPIO
import time
pins = [18, 24, 21, 12, 16, 11, 17, 14]
GPIO.setmode(GPIO.BCM)
for p in pins:
   GPIO.setup(p, GPIO.OUT);GPIO.output(p, False)

cnt = 1000
for i in range(0, cnt, 1):
    for c in range(0,len(pins),1):
        for p in pins:
            if c == pins.index(p):
                GPIO.output(p, True)
            else:
                GPIO.output(p, False)
        time.sleep(0.2)
    print(i)
GPIO.cleanup()

 