
import time

def linear_search(list, target):
    # find the index item in a given list
    start_time = time.time()
    for i in range(0, len(list)):
        if list[i] == target:
            end_time = time.time()
            print(f"Time: {end_time - start_time} sec")
            return i
    return None

def verify(index):
    if index is not None:
        print(f"target found at index {index}")
    else:
        print("target not found")


# numbers = [1,4,56,343,34,434,65,564,43,867,454,65,45,8,354,36,35,3636,7,677,74,34,3]

numbers = list(range(1, 100000000))

result = linear_search(numbers, 99999999)

verify(result)