import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

rw = [23,24]
lw = [7,8]

def run2(t, w1, r1, w2, r2):
    print ("{}, {}, {}, {}, {}".format(t, w1, r1, w2, r2))
    totime =0;
    i=0.001
    d1 = r1>=0
    d2 = r2>0
    r1 = r1 if r1>=0 else -r1
    r2 = r2 if r2>0 else -r2
    while totime < t:
       GPIO.output(w1[0], d1)
       GPIO.output(w1[1], not d1)
       GPIO.output(w2[0], d2)
       GPIO.output(w2[1], not d2)
       time.sleep( i * r1/100 )
       GPIO.output(w1[0], False)
       GPIO.output(w1[1], False)
       GPIO.output(w2[0], False)
       GPIO.output(w2[1], False)
       time.sleep( i * (100 - r1)/100 )
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

vspeed = 30.0; # 100% 
vratio = 100.0
def fd(x):
  # x : cm, t : second, v : cm /sec
  t = x / vspeed
  run2(t, rw, vratio, lw, vratio)

def bk(x):
  # x : cm, t : second, v : cm /sec
  t = x / vspeed
  run2(t, rw, -vratio, lw, -vratio)

rspeed = 90.0
def rt(x):
  # x : 0 ~ 360, t : second, r : (0~360) /sec
  t = x / rspeed
  run2(t, rw, vratio, lw, -vratio)

def lt(x):
  # x : 0 ~ 360, t : second, r : (0~360) /sec
  t = x / rspeed
  run2(t, rw, -vratio, lw, vratio)

def speed(x):
  global vratio
  vratio = x * 1.0
  
def stop(x):
  t = x
  run2(t, rw, 0, lw, 0)


fd(30);bk(30);rt(90);lt(90);
stop(2)
speed(20);fd(30);bk(30);rt(90);lt(90);

GPIO.cleanup()
