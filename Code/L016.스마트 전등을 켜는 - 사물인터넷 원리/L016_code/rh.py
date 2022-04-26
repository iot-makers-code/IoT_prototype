import time
import requests
print("Get file remote:")

url="http://localhost:8000/DATA"
while True:
   r = requests.get(url)
   print(r.text)
   time.sleep(2)
