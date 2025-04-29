
# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:

    class_year = "Passing year 2023"
    num_std = 0
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Student.num_std += 1


std_1 = Student("Spongebob", 32)
std_2 = Student("Patrick", 43)
std_3 = Student("Sadik", 21)

# print(std_2.name,",", std_1.name,"&" , std_3.name)
# print(std_2.age, std_1.age, std_3.age)
# print(Student.class_year)
# print(Student.num_std)

print(f"There were {Student.num_std} student in {Student.class_year}")
print()
print(f"Student Info\n"
      f"-------------\n"
      f"Name : {std_1.name} \nage : {std_1.age} \n"
      f"Name : {std_2.name} \nage : {std_2.age} \n"
      f"Name : {std_3.name} \nage : {std_3.age}" )

