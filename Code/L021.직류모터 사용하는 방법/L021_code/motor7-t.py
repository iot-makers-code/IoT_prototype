import time
import RPi.GPIO as GPIO
import threading

lw = [23,24]
rw = [7,8]

class Wheel () :
   t=0
   r=0
   d=True

   def __init__(self, w):
      GPIO.setmode(GPIO.BCM)
      self.w = w
      for p in self.w:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, False)
      self._stop = threading.Event()
      self.__thread = threading.Thread(\
          target=self.__move)
      self.__thread.start()

   def mov(self, t, r):
      self.r = r if r>0 else -r
      self.d = True if r>0 else False
      self.t = t

   def busy(self):
      print(self.t)
      return self.t < 0

   def __motor(self, f, r):
      if self._stop.is_set(): return
      GPIO.output(self.w[0], f)
      GPIO.output(self.w[1], r)

   def __move(self):
      i=0.01
      while True:
        while self.t > 0:
           self.__motor(self.d, not self.d)
           time.sleep( i * self.r/100 )
           self.__motor(False, False)
           time.sleep( i * (100 - self.r)/100 )
           self.t -= i
        time.sleep(0.1)
        print("--move {} {}".format(self.t, self.r))

   def reset(self):
      self._stop.set()
      #self.__thread.join()
      GPIO.cleanup(self.w)

lft = Wheel(lw)
rft = Wheel(rw)
try:
   lft.mov(3,100)
   rft.mov(2,100)

   while i < 20:
     if not lft.busy(): 
        lft.mov(2,10*i)
        i += 1

     if not rft.busy(): 
        rft.mov(2,10*i)
        i += 1

     time.sleep(0.2)
     print(i)
  
except KeyboardInterrupt:
   pass
finally:
   lft.reset()
   lft.reset()
