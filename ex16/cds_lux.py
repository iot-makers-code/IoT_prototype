import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
t = [ [100, 100000],
       [500, 20000],
       [700, 10000],
       [1000, 5000],
       [3000, 1000],
       [11000, 200],
       [83500, 1]]
 
def lux(x):
   if x <= t[0][0]: return t[0][1]
   if x >= t[len(t)-1][0]: return t[len(t)-1][1]
 
   i=0;
   for i in range(len(t)):
      if t[i][0] <x: continue
      break
 
   d = (x -t[i-1][0]) *\
       (t[i][1] -t[i-1][1]) /(t[i][0] -t[i-1][0])
   u = t[i-1][1] +d
   return u
 
def cdstime():
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24,0)
    time.sleep(0.1)
 
    GPIO.setup(24, GPIO.IN)
    count=0
    while GPIO.input(24) ==False:
       count += 1
    return count
try:
    while True:
       c=cdstime()
       l = lux(c)
       print("Count: {}, Lux: {}".format(c,l));
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

