import time
import os
for i in range(50):
     print("Update time, ", end="")
     if os.path.exists("DATA"):
        os.utime("DATA")
     else:
        open("DATA","w").close()
     print( os.stat("DATA").st_mtime)
     time.sleep(2)

