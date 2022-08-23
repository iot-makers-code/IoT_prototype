# pip3 install websocket-client
# pip 3 install json

from websocket import create_connection
import json
ws = create_connection("ws://192.168.200.127/ws")
while True:
    r = json.loads(ws.recv())
    message="{:.2f}/{:.2f}".format(r["current"]["temperature"],r["current"]["humidity"])
    with open('eth.txt', 'w') as f:  
          f.write(message)
    with open('eth.txt', 'r') as f:  
          msg = f.read()
          print("READ", msg)
ws.close()
