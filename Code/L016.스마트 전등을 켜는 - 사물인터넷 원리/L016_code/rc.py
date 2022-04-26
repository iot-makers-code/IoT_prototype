import time
import os

while True:
   print("Read data:", \
         end="", flush=True)
   if os.path.exists("DATA"):
      with open("DATA", "rt") as f:
         data = f.readline()
      print(data)
   else:
      print(" NO")
   time.sleep(1)
