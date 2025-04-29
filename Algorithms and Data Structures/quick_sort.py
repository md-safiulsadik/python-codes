
import random, time

values = [random.randint(100, 10000) for _ in range(100000)]


def quick_sort(values):

    if len(values) <= 1:
        return values
    
    less_then = []
    grater_then = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_then.append(value)
        else:
            grater_then.append(value)

    return quick_sort(less_then) + [pivot] + quick_sort(grater_then)

start_time = time.time()
sorted_values = quick_sort(values)
end_time = time.time()


# print(sorted_values)
print(f"Execution time: {end_time - start_time} sec")