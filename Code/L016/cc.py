import time
import os

for i in range(50):
   print("Update data.")
   with open("DATA", "wt") as f:
      f.write("DATA, ")
      f.write( str(time.time()) )
   time.sleep(2)
