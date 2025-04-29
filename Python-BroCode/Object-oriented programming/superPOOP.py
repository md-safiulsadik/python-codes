
# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled) -> None:
        self.color = color 
        self.is_filled = is_filled

    def discribe(self):
        print(f"The color is {self.color}\n"
              f"{'The shape is filled' if self.is_filled else 'The shape is not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius) -> None:
        super().__init__(color, is_filled)
        self.radius = radius

    def discribe(self):
        super().discribe()
        print(f"The area is {3.1416 * self.radius * self.radius}")
        

class Square(Shape):
    def __init__(self, color, is_filled, base) -> None:
        super().__init__(color, is_filled)
        self.base = base
    
    def discribe(self):
        print(f"The area is {self.base * self.base}")
        super().discribe()


class Triangle(Shape):
    def __init__(self, color, is_filled, height, width) -> None:
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

    def discribe(self):
        print(f"The area is {self.height * self.width}")
        super().discribe()


circle = Circle(color="Red", is_filled=True, radius=5)
square= Square(color="Blue", is_filled=False, base=8)
triangle = Triangle(color="Yellow", is_filled=True, height=4, width=5)

# print(triangle.color)
# print(triangle.is_filled)
# print(f"{circle.radius}cm")
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")

# print(f"Radius : {circle.radius}")
# print(f"Height : {triangle.height}")
# print(f"Width : {triangle.width}")
print(f"Base : {square.base}")
square.discribe()