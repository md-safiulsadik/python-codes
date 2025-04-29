import time

def binary_search(list, target):

    start_time = time.time() 

    first = 0
    last = len(list) - 1

    while first <= last:

        midpoint  = (first + last) // 2

        if list[midpoint] == target:
            end_time = time.time()  
            print(f"Execution time: {end_time - start_time} seconds")
            return midpoint

        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found")


numbers = list(range(1, 100000000))

result = binary_search(numbers, 99999999)

verify(result)
