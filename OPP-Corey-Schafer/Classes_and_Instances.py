
class Employee:

    raise_salary = 1.02      # Class variable
    num_of_emp = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last              # These are instance/constructor
        self.salary = salary
        self.email = self.first.lower() + self.last.lower() + "@company.com"

        Employee.num_of_emp += 1


    def fullname(self):       # Methods 
        return self.first + " " + self.last


    def apply_raise(self):
        self.salary = int(self.salary * self.raise_salary)# There is difference
    

    @classmethod
    def set_raise_amt(cls, amount):  # As it named it's a class method
        cls.raise_salary = amount
        

    @classmethod                  
    def from_string(cls, emp_str):         # Construct object form classmethod
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)
    

    @staticmethod
    def is_workday(day):         # This not work by using ant instance or class 
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):     # Magic methods
        return f"Employee('{self.first}', '{self.last}', {self.salary})"

    def __str__(self):
        return f'{self.fullname()} -> {self.email} -> {self.salary}'

    def __add__(self, other):
        return self.salary + other.salary
    
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Safiul', 'Sadik', 4000)
emp_2 = Employee("MD", "Kafi", 2000)

emp_str_1 = 'John-Doe-8000'
emp_str_2 = 'John-Smith-3000'                # Constructing from classmethod  
emp_str_3 = 'Calory-Hoe-5000'
new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)


print(f"Total: {emp_1 + emp_2}")
print(len(emp_1))

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())