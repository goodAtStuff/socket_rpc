"""Parser to map messages to callbacks and arguments"""

import json

class Json_Msg_Parser():
  """Easy to implement parser using JSON.  Having this as the impelementation is a little overkill
     and resource indensive for many applications though.
     
     Takes in JSON and returns the name of the function to be called and the arguments to call it with"""
  def __init__(self):
    """No initialization as the parser does not have any internal variables or state"""
    pass

  def unpack(self, msg):
    msg_dict = json.loads(msg)

    func = self._unpack_function(msg_dict)
    args = self._unpack_args(msg_dict)
    
    clean_func = self._sanitize_function(func)
    clean_args = self._sanitize_args(args)
    
    return clean_func, clean_args
    
  def _unpack_function(self, msg_dict):
    if "__function__" in msg_dict:
      function = msg_dict["__function__"]
    else:
      function = None
    return function

  def _unpack_args(self, msg_dict):
    if "__args__" in msg_dict:
      args = msg_dict["__args__"]
    else:
      args = None
    return args
    
  def _sanitize_function(self, func_msg):
    """Ensure the func_msg is a string
       TODO: think through potentail security implications"""
    if func_msg is not None:
      func = str(func_msg)
    else:
      func = None
    return func

  def _sanitize_args(self, args_msg):
    """Ensure that args are a list at the top level.  Return None otherwise
       TODO: think through potential security implications"""
    if isinstance(args_msg, (list, tuple)):
      args = args_msg
    else:
      args = None
    return args

# this needs to be tested and re-implemented as a class.  Use "_" to mark as private for now
def _parse_msg(msg):
  """parse and sanitize message.  extract callback name and message
     expects messages and arguments in the form: "<message>:<arg_1>,<arg_2>,...,<arg_n>" """
  split_args_regex = "(.*?)\:(.*)"
  args_split_regex = "\,"
  match = re.match(split_args_regex, msg)
  if match is not None:
    message = match.group(1)
    arg_str = match.group(2)
    arg_iter = re.finditer(args_split_regex, args)
    args = []
    for arg in arg_iter:
      args.append(arg)  
  return None


# Run some unit tests when this file is called on its own
if __name__ == "__main__":

  def Test_nominal_unpack():
    parser = Json_Msg_Parser() 
    json_msg = json.dumps({"__function__": "test_function", "__args__": ["a", "b"]})
    
    func, args = parser.unpack(json_msg)
    
    assert(func == "test_function")
    assert(args == ["a", "b"])
    
    return "Test_nominal_unpack: pass"

  print("Running tests")
  print(Test_nominal_unpack())
