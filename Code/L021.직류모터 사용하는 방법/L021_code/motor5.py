import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

rw = [23,24]
lw = [7,8]

def run2(t, w1, r1, w2, r2):
    totime =0;
    i=0.001
    d1 = r1>0
    d2 = r2>0
    r1 = r1 if r1>0 else -r1
    r2 = r2 if r2>0 else -r2
    while totime < t:
       GPIO.output(w1[0], d1)
       GPIO.output(w1[1], not d1)
       GPIO.output(w2[0], d2)
       GPIO.output(w2[1], not d2)
       time.sleep( i * r1/100 )
       GPIO.output(w1[0], False)
       GPIO.output(w2[1], False)
       GPIO.output(w1[0], False)
       GPIO.output(w2[1], False)
       time.sleep( i * (100 - r2)/100 )
       totime += i

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
"""
for w in [rw, lw]:
   run(w, 2,100)
   run(w, 1,30)
   run(w, 2,-100)
   run(w, 1,-30)
   run(w, 1,0)
"""
run2(2, rw, 100, lw, 100)
run2(2, rw, -100, lw, 100)
run2(2, rw, 100, lw, -100)
run2(2, rw, -100, lw, -100)

GPIO.cleanup()
