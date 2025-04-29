
import time 
import random

values = [random.randint(100, 10000) for _ in range(10000)]

def merge_sort(values):
    if len(values) <= 1:
        return values
    
    mid_index = len(values) // 2
    left_half = merge_sort(values[:mid_index])
    right_half = merge_sort(values[mid_index:])

    sorted_values = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_values.append(left_half[left_index])
            left_index += 1
        else:
            sorted_values.append(right_half[right_index])
            right_index += 1
    sorted_values += left_half[left_index:]
    sorted_values += right_half[right_index:]
    
    return sorted_values

def verify(values):
    for value in range(len(values) - 1):
        if values[value] > values[value + 1]:
            return f"Values are not sorted !"
    return f"Values are SORTED !"

start_time = time.time()
sorted_values = merge_sort(values)
end_time = time.time()

# print(sorted_values)

print(verify(sorted_values))
print(f"Execution time: {end_time - start_time:.04f} sec")
