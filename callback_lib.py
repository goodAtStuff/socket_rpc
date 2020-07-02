""" Library of callback functions to run on the udp/tcp server"""
from functools import reduce

def test_callback ():
  return "test resposne"
  
def test_callback_args(str1, str2):
  return "hey {}, you're {}!".format(str1, str2)
  
def add_numbers(*args):
  add = lambda x, y: x + y
  float_args = map(float, args)
  sum = reduce(add, float_args)
  return sum
  