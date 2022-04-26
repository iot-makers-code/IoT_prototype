import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def run(t, r):
    totime =0;
    i=0.001
    d = r>0
    r = r if r>0 else -r
    while totime < t:
       GPIO.output(23, d)
       GPIO.output(24, not d)
       time.sleep( i * r/100 )
       GPIO.output(23, False)
       GPIO.output(24, False)
       time.sleep( i * (100 - r)/100 )
       totime += i

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(23, False)
GPIO.output(24, False)

run(2,100)
run(1,30)
run(2,-100)
run(1,-30)
run(1,0)

GPIO.cleanup()
