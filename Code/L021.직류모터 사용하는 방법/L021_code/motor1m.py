import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(25, True)

print("F,T")
GPIO.output(23, False);GPIO.output(24, True);
time.sleep(1)
print("T,T")
GPIO.output(23, True);GPIO.output(24, True);
time.sleep(1)
print("T,F")
GPIO.output(23, True);GPIO.output(24, False);
time.sleep(1)
print("F,F")
GPIO.output(23, False);GPIO.output(24, False);
time.sleep(1)
print("_,_")

GPIO.cleanup()