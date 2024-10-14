import requests
import json
import sys

def viewcsv(csvfile) :
     url="http://localhost/iot/sht.php"
     data= {'func':'viewcsv', 'csvfile':csvfile}
     rt = requests.post(url, data= data)
     log = json.loads(rt.text)
     lines = log.split("\n")
     for line in lines:
        print(line)

viewcsv(sys.argv[1])

