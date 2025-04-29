
# Nested class = A class defined within another class
#       class Outer:
#          class Inner:

# Benefits: Allows you to logically group classes that are closely related
#       Encapsulates private details that aren't relevant outside of the outer class
#       Keeps the namespace clean; reduces the possibility of naming conflicts


class Company:

    class Employee:
        def __init__(self, name, position) -> None:
            self.name = name
            self.position = position
        
        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_emlpoyee(self):
        return [emlpoyee.get_details() for emlpoyee in self.employees]


company1 = Company("Walton")

company1.add_employee(name="Dr. Kabir", position="Manager")
company1.add_employee(name="Mula Alu", position="Cook")
company1.add_employee(name="Zohir Khan", position="Production")

company2 = Company("Nokia")

company2.add_employee(name="Dr. Nadir", position="Manager")
company2.add_employee(name="Kola Mola", position="Tecnician")
company2.add_employee(name="J. Holand", position="Loader")


for employee in company2.list_emlpoyee():
    print(employee)