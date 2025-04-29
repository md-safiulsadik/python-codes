# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math

while True:
    try:
        radius = float(input("Radius of the Circle?  "))
        break
    except ValueError:
        pass

area = math.pi * math.pow(radius , 2)

print(f"Area of the Circle is  {round(area , 3)}")