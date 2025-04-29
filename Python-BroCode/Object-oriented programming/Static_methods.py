
# Static methods = A method that belong to a class rather than any object from that class (instance)
#           Usually used for general utility functions

# Instance methods - Best for operations on instances of the class (objects)
# Static methods - Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} : {self.position}"
    
    @staticmethod
    def is_valid(position):
        vaild_positon = ["Cook", "Cashier", "Manager"]
        return position in vaild_positon    


employee1 = Employee(name="Spongbob", position="Cook")
employee2 = Employee(name="Ching Chong", position="Ping Pong")
employee3 = Employee(name="Mojnu", position="Manager")
employee4 = Employee(name="T. K. Tom", position="Cashier")


if Employee.is_valid(employee2.position):
    print(employee2.get_info())  
else:
    print("There no position for the persion")