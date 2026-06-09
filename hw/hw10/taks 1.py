class Polygon(): 
     def __init__(self,sides=0): 
      self.sides = sides 
class Rectangle(Polygon): 
     def __init__(self,a,b):

         self.a = a
         self.b = b

         Polygon.__init__(self,4)  
    
     def findArea(self):
         return self.a * self.b

rectangles = Rectangle (15,5)

print(rectangles.findArea())

#75