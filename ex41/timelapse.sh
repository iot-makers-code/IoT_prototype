#!/bin/bash
/usr/bin/python /home/pi/strobe.py &

sleep 10
cd /home/pi/camera
/usr/bin/python -m http.server 8000 &

CD
sleep 10
/bin/bash /home/pi/fehshow.sh &

