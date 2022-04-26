from turtle import *
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
print("Test photo regitster")
GPIO.setup(24, GPIO.IN)

colors=['white', 'red', 'green', 'yellow']
pre=0; page=0; x=0;

while x<1200:
   if x % 600 == 0:
       page = 0 if page==1 else 1
       clearscreen();bgcolor('black')
       pencolor('white');speed(0)
       up();rt(-90);fd(90);
       rt(-90);fd(300);rt(180);down();

   light = GPIO.input(24)

   pencolor(colors[page*2+light])
   if light == pre : fd(10)
   if pre == 0 and light == 1:
       rt(-90);fd(10);rt(90);fd(10);
   if pre == 1 and light == 0:
       rt(90);fd(10);rt(-90);fd(10);
   pre = light

   if x % 30 == 29:
      up();rt(90);fd(30);
      rt(90);fd(30*10);rt(180);down();

   time.sleep(0.01)
   x = x + 1

exitonclick()
GPIO.cleanup()
