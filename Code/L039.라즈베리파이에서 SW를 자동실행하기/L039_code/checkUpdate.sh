#!/bin/bash

cd ~pi/bin 
RPi=downloads.raspberrypi.org
OSinfo=operating-systems-categories.json
releaseDate=$(
    wget --server-response --spider \
        https://${RPi}/${OSinfo} 2>&1 | \
         | grep -i Last-Modified)
echo $relaseDate | tee raspberryOS.date