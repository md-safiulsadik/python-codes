# dictionary =  a collection of {key:value} pairs
#    ordered and changeable. No duplicates

# capitals = {"USA"   : "Washington D.C.",
#             "India" : "New Delhi",
#             "China" : "Beijing",
#             "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Jnapa"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()

# for key, value in capitals.items():
#     print(f"{key}: {value}")



menu = {"pizza": 3.99,
        "nachos": 4.55,
        "popcorn": 6.45,
        "fries": 2.99,
        "chips": 1.99,
        "pretzel": 3.50,
        "soda": 3.99,
        "lemonade": 4.25}

cart = []
total = 0

print("------- MENU -------")
for index ,(key, value) in enumerate(menu.items()):
    print(f"{index + 1}.{key:10}: ${value:.02f}")
print("--------------------")

while True:
    food = input("Food Name (Q/q) to Quit : ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Not in the Menu")
print("------- Your Oder -------")
for i, food in enumerate(cart):
    total += menu.get(food)
    food = food.upper()
    print(f"{i + 1}.{food}", end=" - " if i < len(cart) - 1 else "\n")
print(f"\nTotol ${total:.02f}")

from msvcrt import getch
getch()





# cart = []
# total = 0

# print("--------- MENU ---------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print("------ YOUR ORDER ------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is: ${total:.2f}")
