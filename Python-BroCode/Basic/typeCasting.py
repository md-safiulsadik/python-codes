#Typecasting  = The process of converting from one to other 
#    srt()
#    int()
#    float()
#    bool()

name = "Sadik"
age = 21
gpa = 4.67
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#typecast float to int
gpa = int(gpa)
# new data type
print(type(gpa))

age = float(age)
print(age)

# typecast srt to bool
name = bool(name)
print(f"{name} {type(name)}")

input()

