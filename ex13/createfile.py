import time
import os
for i in range(50):
    print("Create ..., ", \
            end="", flush=True)
    open("DATA","w").close()
    time.sleep(2)
    print("Delete data")
    if os.path.exists("DATA"):
       os.remove("DATA")
    time.sleep(2)
