import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def run(t, r):
    totime =0;
    i=0.01
    while totime < t:
       GPIO.output(23, True)
       GPIO.output(24, False)
       time.sleep( i * r/100 )
       GPIO.output(23, False)
       GPIO.output(24, False)
       time.sleep( i * (100 - r)/100 )
       totime += i

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(23, False)
GPIO.output(24, False)

run(3,100)
run(3,50)

GPIO.cleanup()
