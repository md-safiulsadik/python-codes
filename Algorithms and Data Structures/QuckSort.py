import random, time

def quick_sort(values):
    if len(values) <= 1: 
        return values

    pivot = values[len(values) // 2]
    left = [value for value in values if value < pivot]
    middle = [value for value in values if value == pivot]
    right = [value for value in values if value > pivot]

    return quick_sort(left) + middle + quick_sort(right)

values = [random.randint(100, 10000) for _ in range(10)]
start_time = time.time()
sorted_values = quick_sort(values)
end_time = time.time()


print(sorted_values)
print(f"Execution time: {end_time - start_time} sec")