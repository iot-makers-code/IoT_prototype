import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
print("Fan on")
GPIO.setup(18,GPIO.OUT)
GPIO.output(18, True)

