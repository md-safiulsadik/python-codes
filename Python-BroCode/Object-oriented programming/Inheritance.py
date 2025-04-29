
# Inheritance = Inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eatting !")

    def sleep(self):
        print(f"{self.name} is sleeping !")
    

class Dog(Animal):
    def speak(self):
        print("Woof !")


class Cat(Animal):
    def speak(self):
        print("Meow !")


class Mouse(Animal):
    def speak(self):
        print("Squck !")

dog = Dog("Scooby")
cat = Cat("Garfild")
mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
