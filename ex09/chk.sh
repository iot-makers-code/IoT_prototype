#!/bin/bash

count=100
while (( count > 0 ))
do
   echo $$ $count $(date)
   (( --count ))
   sleep 1
done

