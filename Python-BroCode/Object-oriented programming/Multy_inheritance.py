
# multiple inheritance = inherit from more than one parent class

#                                        C(A, B)
# multilevel inheritance = inherit from a parent which inherits from another parent

#                                       C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eatting")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Pray(Animal):
    def flee(self):
        print(f"{self.name} is fleeing !")


class Preditor(Animal):
    def hunt(self):
        print(f"{self.name} is huntting !")


class Rabbit(Pray):
    def live(self):
        print(f"{self.name} lives in mounten")


class Hawk(Preditor):
    def live(self):
        print(f"{self.name} lives in tree")
    


class Fish(Preditor, Pray):
    def live(self):
        print(f"{self.name} lives in water")



fish = Fish("Nemo the Fish")
rabbit = Rabbit("Luke the Rabbit")
hawk = Hawk("Bob the Hawk")



hawk.live()
hawk.eat()
hawk.sleep()
# hawk.flee()
hawk.hunt()
print(hawk.name)
