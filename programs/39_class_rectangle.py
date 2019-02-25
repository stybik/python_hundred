# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

class Rectangle(object):
   def __init__(self, l, b):
      self.length = l
      self.breadth = b

   def area (self):
      return self.length*self.breadth

obj = Rectangle(2,10)
print obj.area()