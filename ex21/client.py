import requests
import json

while True:
     name = input("What's your name?")
     age = input("What's your age?")

     url="http://localhost/iot/control.php"
     data= {'name':name, 'age':age }
     x = requests.post(url, data= data)
     tj = json.loads(x.text)
     print("Name:", tj['name'])
     print("Age:", tj['age'])

