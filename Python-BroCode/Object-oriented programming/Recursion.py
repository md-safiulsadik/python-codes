
# recursion = a function that calls itself from within
#             helps to visualize a complex problem into basic steps
#             problems can be solved more easily iteratively or recursively
#             iterative = faster, complex
#             recursive = slower, simpler

# ------------- Ireative ---------------

# def walk(steps):
#     for step in range(1, steps + 1):
#         print(f"You take step#{step}")

# walk(100)

# def factorial(x):
#     result = 1
#     if x > 0:
#         for y in range(1, x + 1):
#             result *= y
#         return result

# print(factorial(7))

#--------------- Recursion ----------------

# def walk(step):
#     if step == 0:
#         return 
#     walk(step - 1)
#     print(f"You take step#{step}")

# walk(100)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))