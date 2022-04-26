#!/usr/bin/python
import Adafruit_DHT
import time
import requests
import socket

sensor = Adafruit_DHT.DHT11

# GPIO16 (pin no: #36)
pin = 16
id = socket.gethostname()

while True :
    humidity,temperature=\
          Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print "Temp={0:0.1f}*C Humidity={1:0.1f}%"\
                  .format(temperature, humidity)

        url="http://localhost/iot/check.php?"+\
             "id={}&h={}&t={}".\
             format(id, temperature, humidity)
        requests.get(url)

    else:
        print "Failed to get reading."
    time.sleep(3)