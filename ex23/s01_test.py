#!/bin/python3
import time
import requests
 
while True:
     try:
         url="http://localhost/iot/s01.php";
         postdata ={'func': 'test'};
         res =requests.post(url, data=postdata);
         dres =res.json()
         print("data : {}".format(dres['data']));
         print("status : {}".format(dres['status']));
     except:
         print("Failed to requests.")
     time.sleep(3)

