print("""
# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23'] # values.split()
# Tuple : ('3', ' 5', ' 7', ' 23') # tuple()
      """) #########

# value = input("Enter some number using comma : ")
value = "1231-2342432-34243-243-242-4-234234234-234-324-2"

list = value.split("-") 
tuple = tuple(value.split("-"))

print(f"List : {list}")
print(f"Tuple : {tuple}")

print("""
# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java
      """) ##########

# file = input("Enter File Name : ") 
file = "abc.java"

filetype = file.split(".")
print(f"File Type : {repr(filetype[-1])}")

print("""
# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
      """) #########

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])


print("""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
      """) #########
# num = input("Enter Number to (n+nn+nnn) ")
num = 5
sum = 0

for i in range(1 , 4):
    sum += int(str(num) * i)

print(sum,"\n Done\n\n\n")


n = -4324
m = "Sadik3242"
# print(abs(n))
# print(len(m))
# print(sorted(m))


import calendar

# yaer = int(input("Year "))
# month = int(input("Month "))
yaer = 2024
month = 9
print(calendar.month(yaer , month))


# day calculate 
import datetime
from w3rPra1 import time

birth_date = datetime.date(2003,5,15)
today_date = datetime.date(2024,9,8)

lived = today_date - birth_date

print(f"You are {lived.days} days old")