"""Callback handler that extends dictionaries to support callback specific operations
   Should probably be extended to support function arguments, but that will require more
   robust message validation
   
   TODO: add in some sort of validation for the number of arguments and possibly keyword arguments"""

class Simple_Callback_Handler():

  def __init__(self):
    self._callback_table = {}

  def _validate_msg(self, msg):
    """Validate that the message is a string for use with sockets"""
    assert(isinstance(msg, str))

  def register(self, msg, func):
    """Add a unique callback to the callback table"""
    if msg in self._callback_table: #double check this is actuall optimized and not a linear scan
      raise Exception("Registered duplicate callback for " + str(msg))
    else:
      self._callback_table[msg] = func

  def get(self, func, args=None):
    if func in self._callback_table: #double check this is actuall optimized and not a linear scan
      return self._callback_table[func](*args)
    else:
      return None

  def unregister(self, msg):
    """Todo: implement removal function"""

