import time
import requests
print("Get file remote:")
for i in range(50):
     url="http://localhost:8000/DATA"
     r =requests.get(url)
     print(r.text)
     time.sleep(2)

