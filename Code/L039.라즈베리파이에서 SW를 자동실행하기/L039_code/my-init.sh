#!/bin/bash
cd ~pi
while [ 1 ]
do
   echo "Date & time >> $(date)" > date-init.txt
   sleep 10
done