import time
import os
for i in range(50):
     print("Update data.")
     with open("DATA","wt") as d:
           d.write("DATA,")
           d.write(str(time.time()))
     time.sleep(2)

