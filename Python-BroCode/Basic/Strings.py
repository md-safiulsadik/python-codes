# -------------------------------

# STRING METHODS

# -------------------------------
name = "MD Safiul Kafi Sadik"



# length = len(name)

# index = name.find(" ")

# name = name.capitalize()

# name = name.upper()

# name = name.lower()

# result = name.isdigit()

# result = name.isalpha()

# result = name.count(" ")

# result = name.replace("-", "")

# print(result)


# -------------------------------
#        EXERCISE
# -------------------------------

# username = input("Enter a username: ")

# if len(username) > 12:

#    print("Your name can't be more than 12 characters")

# elif not username.find(" ") == -1:

#    print("Your username can't contain spaces")

# elif not username.isalpha():

#    print("Your username can't contain digits")

# else:

#    print(f"Welcome {username}!")

#indexing = accessing elements of a sequence using[] (indexing operator)
#  [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:8])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])


#EXERCISE 1
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#EXERCISE 2
credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)

# mail = input("Enter You Mail Address ")

# index = mail.index("@")

# username = mail[:index]
# domain = mail[index + 1:]

# print(f"Your UserName {username} Domaain {domain}")

num = "017174929069"
for x in range(11):
    print(num[x], end="")   

print("\n")
# blocks = int(input("How Many Block?  "))
blocks = 3
for x in range(blocks , 0, -1):
    for y in range(blocks):       
        print("#", end="")
    print()
    blocks -= 1

