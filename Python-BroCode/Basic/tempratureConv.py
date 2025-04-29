#          Formula
# C/5 = (F - 32)/9 = (K - 273)/5

import  msvcrt

print("Temprature Convertion Program \n\n")
print("1.Convert form Celsius To Fahrenhei")
print("2.Convert form Fahrenheit To Celsius")
print("3.Convert form Celsius To Kalvin")
print("4.Convert form Kalvin To Celsius ")
print("5.Convert form Fahrenheit To Kalvin ")
print("6.Convert form Kalvin To Fahrenheit\n\n")


while True:
    try:
        choise = int(input("What's Your Oparation? "))
        break
    except ValueError:
        pass
print()
if choise == 1:
    c = float(input("Enter Temprature in Celsius : "))
    result = (c * (9/5)) + 32
    print(f"Temprature in Fahrenheit : {round(result, 2)}")

elif choise == 2:
    f = float(input("Enter Temprature in Fahrenheit : "))
    result = (f - 32) * (5/9)
    print(f"Temprature in Celsius : {round(result, 2)}")

elif choise == 3:
    C = float(input("Enter Temprature in Celsius : "))
    result = C + 273
    print(f"Temprature in Kalvin : {round(result, 2)}")

elif choise == 4:
    k = float(input("Enter Temprature in Kalvin : "))
    result = k - 273
    print(f"Temprature in Celsius : {round(result, 2)}")

elif choise == 5:
    F = float(input("Enter Temprature in Fahrenheit : "))
    result = ((F - 32) * (5/9)) + 273
    print(f"Temprature in Kalvin : {round(result, 2)}")

elif choise == 6:
    K = float(input("Enter Temprature in Kalvin : "))
    result = ((K - 273) * (9/5)) + 32
    print(f"Temprature in Fahrenheit : {round(result, 2)}")
else:
    print("Wrong Input\nType (1 or 2 or 3 or 4 or 5 or 6)")

msvcrt.getch()

# Allhamdulillah




# def convert_temp():
#     print("Temperature Conversion Program")
#     print("1. Celsius to Fahrenheit")
#     print("2. Fahrenheit to Celsius")
#     print("3. Celsius to Kelvin")
#     print("4. Kelvin to Celsius")
#     print("5. Fahrenheit to Kelvin")
#     print("6. Kelvin to Fahrenheit")

#     choice = int(input("What's your operation? "))

#     if choice == 1:
#         celsius = float(input("Enter temperature in Celsius: "))
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"Temperature in Fahrenheit: {round(fahrenheit, 2)}")

#     elif choice == 2:
#         fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#         celsius = (fahrenheit - 32) * 5/9
#         print(f"Temperature in Celsius: {round(celsius, 2)}")

#     elif choice == 3:
#         celsius = float(input("Enter temperature in Celsius: "))
#         kelvin = celsius + 273
#         print(f"Temperature in Kelvin: {round(kelvin, 2)}")

#     elif choice == 4:
#         kelvin = float(input("Enter temperature in Kelvin: "))
#         celsius = kelvin - 273
#         print(f"Temperature in Celsius: {round(celsius, 2)}")

#     elif choice == 5:
#         fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#         kelvin = (fahrenheit - 32) * 5/9 + 273
#         print(f"Temperature in Kelvin: {round(kelvin, 2)}")

#     elif choice == 6:
#         kelvin = float(input("Enter temperature in Kelvin: "))
#         fahrenheit = (kelvin - 273) * 9/5 + 32
#         print(f"Temperature in Fahrenheit: {round(fahrenheit, 2)}")

# convert_temp()