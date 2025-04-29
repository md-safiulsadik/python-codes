# input() = A fanction that prompts the user to enter data
#  Return the data as a String


# name = input("What is Your name? ")
# while True:
#     try:
#         age = int(input("What's your age? "))
#         break
#     except ValueError:
#         print("Please Enter Integar Vaule")

# while True:
#     try:
#         gpa = float(input("What's Your gpa ? "))
#         break
#     except ValueError:
#         print("Enter a Float Value")

# print(f"Your Name {name}\nYou are {age} Years Old\nYour GPA is {gpa}")


# Area of a Circle

# radious = float(input("Radious = "))
# area = (radious * radious) * 3.1416
# print(f"Area of Circle {area}")


# area of a Rectangle
while True:
    try:
        lenght = float(input("Lenght "))
        break
    except ValueError:
        pass

while True:
    try:
        hight = float(input("Higth "))
        break
    except ValueError:
        pass

area = lenght * hight
print(f"Area = {area}cm²")