
import random, time

values = [random.randint(1, 1000) for _ in range(1000)]

def selection_sort(values):
    sorted_values = []

    for i in range(len(values)):
        min_index = find_min_index(values)
        sorted_values.append(values.pop(min_index))

    return sorted_values

def find_min_index(values):
    min_index = 0

    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i

    return min_index

print(values)

print("\n\n\n")
start_time = time.time()
sorted_values = selection_sort(values)
end_time = time.time()


# print(sorted_values)
print(f"Execution time: {end_time - start_time} sec")
