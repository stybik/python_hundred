#couldn't figure out how to make it more efficient


class input_output_string(object):
   def __init__(self):
      self.s = ""

   def getString(self):
      self.s = raw_input()

   def printString(self):
      print self.s.upper()

str_obj = input_output_string()
str_obj.getString()
str_obj.printString()