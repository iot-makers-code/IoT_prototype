import requests
import json
    
url="http://localhost/iot/name.php"
data= {'func':'list'}
rt = requests.post(url, data= data)
list = json.loads(rt.text)
for key in list.keys():
     print(key, "::", list[key])

