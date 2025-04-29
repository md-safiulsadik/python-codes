
# SORTING IN PYTHON .sort() or sorted()
#                   Lists[], Tuples(), Dictionaries{"":""}, Objects



# --------- list [ ] ---------

# fruits = ["banana", "orange", "apple", "coconut"]
# num = [5, 4, 3, 3, 5, 6, 7, 8, 6, 4, 3, 56, 543 ,2]

# fruits.sort()
# fruits.sort(reverse=True)
# num.sort(reverse=False)

# print(fruits)




# ------- tuples ( ) -------

# fruits = ("banana", "orange", "apple", "coconut")
# num = (5, 4, 3, 3, 5, 6, 7, 8, 6, 4, 3, 56, 543 ,2)

# fruits = tuple(sorted(fruits))
# fruits = tuple(sorted(fruits, reverse=True))

# num = tuple(sorted(num, reverse=True))

# print(num)





# ------------ dict { } --------------

# fruits = {
#     "banana" : 105,
#     "orange" : 72,
#     "apple" : 43,
#     "coconut" : 604
#     }

# fruits = dict(sorted(fruits.items()))

# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))

# fruits = dict(sorted(fruits.items(), key= lambda item: item[1], reverse=False))

# print(fruits)





# ------------- OBJECTS ---------------

class Fruits:

    def __init__(self, name, calories) -> None:
        self.name = name
        self.calories = calories

    def __str__(self) -> str:
        return f"{self.name} : {self.calories}"

    def __repr__(self) -> str:
        return self.__str__()

fruits = [
    Fruits("banana", 105),
    Fruits("orange", 72),
    Fruits("apple", 43),
    Fruits("coconut", 604)
         ]

fruits = (sorted(fruits, key=lambda x: x.calories, reverse=True))

print(fruits)

