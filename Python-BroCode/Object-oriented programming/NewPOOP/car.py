
class Car:
    def __init__(self, driver, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        self.driver = driver

    def drive(self):
        print(f"{self.driver} is driving the {self.model}")
        
    def stop(self):
       print(f"{self.driver} stop the {self.model} !")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
