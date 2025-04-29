
# Aggregation = A relationship where one object contains references to other INDEPENDENT objects
#        "has-a" relationship

# Composition = The composed object directly owns its components, which cannot exist independently
#       "owns-a" relationship

class Engine:
    def __init__(self, horse_power) -> None:
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size) -> None:
        self.size = size


class Car:
    def __init__(self, menu, model, horse_power, wheel_size) -> None:
        self.menu = menu
        self.model = model
        self.engine = Engine(horse_power)
        self.wheel = [Wheel(wheel_size) for _ in range(4)]

    def display_car(self):
        return (
            f"Menufectrature : {self.menu} \nModel : {self.model}"
            f"\nHorse power : {self.engine.horse_power} \nWheel size : {self.wheel[0].size}" 
            )


car1 = Car(menu="Toyota", model="SY-43", horse_power=320, wheel_size=16)
car2 = Car(menu="Audi", model="S-8", horse_power=880, wheel_size=19)
car3 = Car(menu="Velvo", model="LenVo", horse_power=450, wheel_size=21)


print(car1.display_car())

print()

print(car2.display_car())

print()

print(car3.display_car())