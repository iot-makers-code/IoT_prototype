import time
import os
while True:
      print("Read time", end="")
      if os.path.exists("DATA"):
          s =os.stat("DATA")
          print(s.st_mtime)
      else:
          print("NO")
      time.sleep(0.5)

