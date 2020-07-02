import socket
import callback_handler
import callback_lib
import msg_parser

CLOSE_MSG = b"['close']"

ip = "127.0.0.1"
port = 42069
server_address = (ip, port)

callbacks = callback_handler.Simple_Callback_Handler()
callbacks.register("callback",      callback_lib.test_callback)
callbacks.register("test_function", callback_lib.test_callback_args)
callbacks.register("add",           callback_lib.add_numbers)

parser = msg_parser.Json_Msg_Parser()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.bind(server_address)
  listen = True

  while listen:
    data, addr = s.recvfrom(256)

    if data == CLOSE_MSG:
      print("Closing Server")
      listen = False

    else:
      msg = data.decode()
      func, args = parser.unpack(msg)
      if func is not None:
        print(callbacks.get(func, args))
      else:
        print(msg)
