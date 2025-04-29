
# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#                        Benefit: Add additional logic when you read, write, or delete attributes
#                        Gives you a getter, setter, and deleter method

class Rectangle:

    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width

    @property
    def height(self):
        return f"{self._height:.2f}cm"


    @property
    def width(self):
        return f"{self._width:.2f}cm"


    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height 
        else:
            print("Must be gretter than zero")          

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Must be gretter than zero")

    @height.deleter
    def height(self):
        print("Height deteled !")

    @width.deleter
    def width(self):
        print("Width deteled !")


rectangle = Rectangle(height=4, width=6)

rectangle.height = 29
rectangle.width = 23        

print(rectangle.height)
print(rectangle.width)

del rectangle.height
del rectangle.width
