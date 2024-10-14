import sys
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
StepPins =[17,18,27,23]
print("Setup pins")
 
for pins in StepPins:
   GPIO.setup(pin,GPIO.OUT)
   GPIO.output(pin, False)
 
   Seq =[[1,0,0,1],
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1]]
StepCount =len(Seq)
StepDir =1
WaitTime =1/float(1000)
StepCounter =0
 
while True:
     for pin in range(0,4):
         xpin =StepPins[pin]
         ifSeq[StepCounter][pin] !=0:
             print(" Enable GPIO %i"%(xpin))
             GPIO.output(xpin,True)
         else:
             GPIO.output(xpin, False)
           
     StepCounter += StepDir
   
     if(StepCounter >=StepCount):
         StepCounter =0
     if(StepCounter <0):
         StepCounter =StepCount+StepDir
       
     time.sleep(WaitTime)

