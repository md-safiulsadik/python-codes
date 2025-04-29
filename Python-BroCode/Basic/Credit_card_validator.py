
# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
# (If result is a two-digit number,
# add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

# Step 1

sum_odd_num = 0
sum_even_num = 0
total = 0
card_number = input("Enter you credit card number #: ")

card_number = card_number.replace("-" , "")
card_number = card_number.replace(" " , "")
card_number = card_number[::-1]

# Step 2

for odd_num in card_number[::2]:
    sum_odd_num += int(odd_num) 

# Step 3 

for even_num in card_number[1::2]:
    even_num = int(even_num) * 2
    if even_num >= 10:
        sum_even_num += (1 + (even_num % 10))
    else:
        sum_even_num += even_num

# Step 4

total = sum_even_num + sum_odd_num
if total % 10 == 0:
    print("Valid !")
else:
    print("Invalid !")

# exe  = 4124189741024891  this number I typed just randomly and it truns out valid