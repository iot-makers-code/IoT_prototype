import RPi.GPIO as GPIO
import time
import threading
from queue import Queue
 
GPIO.setmode(GPIO.BCM)
pins=[12,21,25,23,18,16,20,24]
coms=[ 26,19,13,6]
#coms=[ 13,6,19,26]
nums=[[ 1, 1, 1, 1, 1, 1, 0, 0], #0
       [ 0, 1, 1, 0, 0, 0, 0, 0], #1
       [ 1, 1, 0, 1, 1, 0, 1, 0], #2
       [ 1, 1, 1, 1, 0, 0, 1, 0], #3
       [ 0, 1, 1, 0, 0, 1, 1, 0], #4
       [ 1, 0, 1, 1, 0, 1, 1, 0], #5
       [ 1, 0, 1, 1, 1, 1, 1, 0], #6
       [ 1, 1, 1, 0, 0, 0, 0, 0], #7
       [ 1, 1, 1, 1, 1, 1, 1, 0], #8
       [ 1, 1, 1, 1, 0, 1, 1, 0]] #9
 
que = Queue()
for p in pins: GPIO.setup(p, GPIO.OUT);GPIO.output(p, 1)
for c in coms: GPIO.setup(c, GPIO.OUT);GPIO.output(c, 0)
que. put(8888)
 
def display():
     num=0
     while True:
         ifque.empty()==False:
            num = que.get()
 
         n=num
         for com in coms:
            r = %10
            n = int(n/10)
            GPIO.output(com, 1)
            digit(r)
            time.sleep(.001)
            GPIO.output(com, 0)
 
def digit(d) :
         for d in range(len(pins)):
            GPIO.output(pins[i], nums[d][i]==0)
 
try:
    thread = threading.Thread(target=display)
    thread.start()
    while True:
       value =int(input("Enter number (0 to 9999):"))
       query.put(value)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    thread.join()

