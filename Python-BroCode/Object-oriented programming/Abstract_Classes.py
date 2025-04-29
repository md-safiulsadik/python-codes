
# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
# They can contain abstract methods, which are declared but have no implementation.
#               Abstract classes benefits:
#               1. Prevents instantiation of the class itself
#               2. Requires children to use inherited abstract methods


from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    
    @abstractclassmethod
    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

    @abstractclassmethod
    def buy(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You are driving the car")

    def stop(self):
        print("You stop the car")

    def buy(self):
        print("You bought it !")



class Bike(Vehicle):
    def go(self):
        print("You are ride the bike")

    def stop(self):
        print("You stop the bike")

    def buy(self):
        print("You bought it !")



class Boat(Vehicle):
    def go(self):
        print("You are sail the boat")

    def stop(self):
        print("You stop the boat")

    def buy(self):
        print("You bought it !")


car = Car()
bike = Bike()
boat = Boat()

boat.go()
boat.stop()
boat.buy()