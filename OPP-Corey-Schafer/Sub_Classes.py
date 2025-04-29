from Classes_and_Instances import Employee

class Developer(Employee):
    raise_salary = 1.10
    
    def __init__(self, first, last, salary, prg_lang):
        super().__init__(first, last, salary)
        self.prg_lang = prg_lang


class Manager(Employee):

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employee = []
        else:
            self.employee = employees

    def add_employee(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_employee(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_employee(self):
        for emp in self.employee:
            print("-->", emp.fullname())


dev_1 = Developer("Sheikh", "Sadik", 7000, 'Java')
dev_2 = Developer("Mushaikh", "Kafi", 9000, 'C++')

mgr_1 = Manager('Toa', 'Kueta', 1200)
mgr_1 = Manager('Toa', 'Kueta', 1200, [dev_1, dev_2])

mgr_1.add_employee(dev_1)
mgr_1.add_employee(dev_2)

mgr_1.remove_employee(dev_1)

print(mgr_1.email)
mgr_1.print_employee()



# print(dev_1.email)
# print(dev_1.prg_lang)

# print(dev_1.salary)
# dev_1.apply_raise()
# print(dev_1.salary)