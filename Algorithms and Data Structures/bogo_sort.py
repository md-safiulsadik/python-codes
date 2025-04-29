
import random, time

numbers = [random.randint(1, 1000) for _ in range(8)]

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0

    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    return values, attempts

start_time = time.time()
sorted_values, attempts = bogo_sort(numbers)
end_time = time.time()

print(sorted_values)
print(f"Attempts: {attempts}")
print(f"Execution time: {end_time - start_time} sce")