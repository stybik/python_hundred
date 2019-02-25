# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

class Circle(object):
   def __init__(self, r):
      self.radius = r

   def area(self):
      return self.radius**2*3.14

obj = Circle(3)
print obj.area()
