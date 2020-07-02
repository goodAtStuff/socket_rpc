import socket
import json
import time

CLOSE_MSG = b"['close']"

ip = "127.0.0.1"
server_port = 42069
client_port = 42068
server_address = (ip, server_port)
client_address = (ip, client_port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.connect(server_address)
  send = True
  while send:
    try:
      s.send(json.dumps("test message").encode())
      s.send(json.dumps("callback").encode())
      s.send(json.dumps({"__function__": "test_function", "__args__": ["Audrey", "cute"]}).encode())
      s.send(json.dumps({"__function__": "add", "__args__": [5, 9, 12]}).encode())
      time.sleep(0.1)
    except KeyboardInterrupt:
      s.send(CLOSE_MSG)
      send = False