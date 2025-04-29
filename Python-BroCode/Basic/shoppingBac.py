# Simple Sopping in pyhton 

# item = input("What You Would Like To Buy? ")
# while True:
#     try:
#         price = float(input("What is the Price? "))
#         break
#     except ValueError:
#         pass
# while True:
#     try:  
#         quantity = int(input("How many you would like to buy?" ))
#         break
#     except ValueError:
#         pass

# total = price * float(quantity)

# print(f"You bought {item} Quantity of {quantity}\nTotal Price ${total}")


# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER



# foods = []
# prices = []
# total = 0

# while True:
#     food =  input("Iteam name : ")
#     if(food.upper() == 'Q'):
#         break
#     else:
#         price = float(input("Price of the iteam : "))
#         foods.append(food)
#         prices.append(price)

# for price in prices:
#     total += price

# for i, food, price in foods and prices:
#     print(f"{i + 1}.{food} , ")

# print(f"\nTotal : {total}")


import msvcrt
foods = {}

while True:
    food = input("Item Name (or Q/q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Price : $"))
        foods[food] = price
print("\nReceipt:")
for index, (food, price) in enumerate(foods.items()):
    print(f"{index + 1}. {food}: ${price}")

total = sum(foods.values())    
print(f"\nTotal : ${total:.02f}")

print("\nThanks for shopping!")
msvcrt.getch()