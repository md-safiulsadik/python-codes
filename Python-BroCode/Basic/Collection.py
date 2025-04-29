# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(frutes[0])  # Output: "apple"



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(frutes[1:3])  # Output: ["banana", "cherry"]



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(frutes[-1])  # Output: "mango"



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
frutes.append("pineapple")
print(frutes)  # Output: ["apple", "banana", "cherry", "orange", "kiwi", "mango", "pineapple"]



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
frutes.insert(2, "grape")
print(frutes)  # Output: ["apple", "banana", "grape", "cherry", "orange", "kiwi", "mango"]



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
frutes.remove("banana")
print(frutes)  # Output: ["apple", "cherry", "orange", "kiwi", "mango"]



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
frutes.sort()
print(frutes)  # Output: ["apple", "banana", "cherry", "kiwi", "mango", "orange"]



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
for fruit in frutes:
    print(fruit)
# Output:
# apple
# banana
# cherry
# orange
# kiwi
# mango



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
uppercase_fruits = [_.upper() for _ in frutes]
print(uppercase_fruits)  # Output: ["APPLE", "BANANA", "CHERRY", "ORANGE", "KIWI", "MANGO"]



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("apple" in frutes)  # Output: True



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("pear" not in frutes)  # Output: True



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(len(frutes))  # Output: 6



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(frutes.index("cherry"))  # Output: 2



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
frutes_tuple = tuple(frutes)
print(frutes_tuple)  # Output: ("apple", "banana", "cherry", "orange", "kiwi", "mango")



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
frutes_set = set(frutes)
print(frutes_set)  # Output: {"apple", "banana", "cherry", "kiwi", "mango", "orange"}



frutes = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
frutes_dict = dict(enumerate(frutes))
print(frutes_dict)  # Output: {0: "apple", 1: "banana", 2: "cherry", 3: "orange", 4: "kiwi", 5: "mango"}



numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]


numbers = [1, 2, 3, 4, 5]
even_and_greater_than_3 = [x for x in numbers if x % 2 == 0 and x > 3]
print(even_and_greater_than_3)  # Output: [4]


add_five = lambda x: x + 5
print(add_five(3))  # Output: 8


add_and_multiply = lambda x, y: x + y * 2
print(add_and_multiply(3, 4))  # Output: 11



numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]



numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]





import functools
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = functools.reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15





def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2






def even_numbers():
    num = 0
    while True:
        if num % 2 == 0:
            yield num
        num += 1

gen = even_numbers()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 2
print(next(gen))  # Output: 4




def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.






def repeat(num_times):
    def my_decorator(func):
        def wrapper():
            for i in range(num_times):
                func()
        return wrapper
    return my_decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello!
# Hello!




# R = u^2(sin(20)) / g    distance
# H = u^2(sin(0)^2) / 2g   hight 


