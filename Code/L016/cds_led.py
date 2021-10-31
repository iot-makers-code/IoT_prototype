import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Link cds and led")
GPIO.setup(24,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
cnt=500
for i in range(cnt):
    time.sleep(0.1)
    inx = GPIO.input(24)
    GPIO.output(18, inx)
GPIO.cleanup()

