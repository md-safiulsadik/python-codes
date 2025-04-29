
# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

#    Instance methods = Best for operations on instances of the class (objects)
#    Static methods = Best for utility functions that do not need access to class data
#    Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0   

    def __init__(self, name, gpa) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def __str__(self):
        return f"{self.name} : {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of student {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        return f"Average GPA : {(cls.total_gpa / cls.count):.02f}" 
    

student1 = Student(gpa=3.52, name="Sandy")
student2 = Student(name="Rocky", gpa=2.92)
student3 = Student(name="Timiy", gpa=3.67)

print(student1)
print(student2)
print(student3)

print(Student.get_avg_gpa())
print(Student.get_count())