
# Polymorphism = Greek word that means to "have many forms or faces"
#           Poly = Many
#           Morphe = Form

# TWO WAYS TO ACHIEVE POLYMORPHISM
#          1. Inheritance = An object could be treated of the same type as a parent class
#          2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractclassmethod

class Shape():

    @abstractclassmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, height, widht):
        self.height = height
        self.widht = widht

    def area(self):
        return self.height * self.widht 
    
class Square(Shape):
    def __init__(self, base):
        self.base = base

    def area(self):
        return self.base ** 2


class Pizza(Circle):
    def __init__(self, toppings, redius):
        super().__init__(redius)
        self.toppings = toppings
      
        
shapes = [Circle(5), Triangle(4, 6), Square(7), Pizza("Perparoni", 7)]

for shape in shapes:
    print(f"Area : {shape.area()}cm^2")