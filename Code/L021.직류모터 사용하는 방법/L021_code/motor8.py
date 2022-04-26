import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

lw = [23,24]
rw = [7,8]
def setwheel(w):
   for p in w:
      GPIO.setup(p, GPIO.OUT)
      GPIO.output(p, False)
def motor(w,f,r):
    GPIO.output(w[0], f)
    GPIO.output(w[1], r)

def wheel2a(t, lw, lr, rw, rr):  #+/-r, [23, 24]
    totime =0;
    i=0.01
    ld = True if lr>0 else False
    rd = True if rr>0 else False
    lr = lr if lr>0 else -lr
    rr = rr if rr>0 else -rr
    while totime < t:
       motor(lw, ld == True, ld == False)
       motor(rw, ld == True, ld == False)
       time.sleep( i * lr/100 )
       motor(lw, ld == False, ld == False)
       motor(rw, ld == False, ld == False)
       time.sleep( i * (100 - lr)/100 )
       totime += i

def wheel(w, t, r):  #+/-r, [23, 24]
    totime =0;
    i=0.01
    d = True if r>0 else False
    r = r if r>0 else -r
    while totime < t:
       motor(w, d == True, d == False)
       time.sleep( i * r/100 )
       motor(w, d == Fasle, d == False)
       time.sleep( i * (100 - r)/100 )
       totime += i

setwheel(lw)
setwheel(rw)

wspeed = 30;
wtime  = 0;
def fd(x):
   wtime = x/5
   wheel2a(wtime,lw,wspeed,rw,wspeed)

def bk(x):
   wtime = x/5
   wheel2a(wtime,lw,-wspeed,rw,-wspeed)

def rt(x):
   wtime = x/90
   wheel2a(wtime,lw,wspeed,rw,-wspeed)

def lt(x):
   wtime = x/90
   wheel2a(wtime,lw,-wspeed,rw,wspeed)

def speed(x):
   wspeed = x

fd(10);lt(90);bk(30);rt(90);speed(100);

GPIO.cleanup()
