import RPi.GPIO as GPIO
import os
import traceback
import threading

import time
GPIO.setmode(GPIO.BCM)
print("Setup LED pins as output")
GPIO.setup(17,GPIO.OUT)

def spk():
    GPIO.output(17,True)
    print("music on")
    cmd = "mpg123 http://ice1.somafm.com/u80s-128-mp3"
    os.system(cmd);

threading.Thread(target=spk, args=())

while True:
    time.sleep(3)

GPIO.cleanup()
