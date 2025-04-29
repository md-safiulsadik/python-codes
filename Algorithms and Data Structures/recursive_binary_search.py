
import time

def recursive_binary_search(list, targrt):
    
    start_time = time.time()
    
    if len(list) == 0:
        return False
    
    mid_index = len(list) // 2

    if list[mid_index] == targrt:
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time} sec")
        return True
    
    elif list[mid_index] < targrt:
        return recursive_binary_search(list[mid_index + 1:], targrt)
    else:
        return recursive_binary_search(list[:mid_index], targrt)

def verify(result):
    print("Target found: ", result)


numbers = list(range(1, 100000000))

result = recursive_binary_search(numbers, 99999999)
verify(result)
