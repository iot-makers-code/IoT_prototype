import time
import os
print("Read status")
while True:
     print("Read data", \
            end="", flush=True)
     if os.path.exists("DATA"):
         print(" YES")
     else:
         print(" NO")
     time.sleep(1)
