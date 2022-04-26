import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

rw = [23,24]
lw = [7,8]

def run(w, t, r):
    totime =0;
    i=0.001
    d = r>0
    r = r if r>0 else -r
    while totime < t:
       GPIO.output(w[0], d)
       GPIO.output(w[1], not d)
       time.sleep( i * r/100 )
       GPIO.output(w[0], False)
       GPIO.output(w[1], False)
       time.sleep( i * (100 - r)/100 )
       totime += i

for w in [rw, lw]:
   for p in w:
      GPIO.setup(p, GPIO.OUT)
      GPIO.output(p, False)

for w in [rw, lw]:
   run(w, 2,100)
   run(w, 1,30)
   run(w, 2,-100)
   run(w, 1,-30)
   run(w, 1,0)

GPIO.cleanup()
