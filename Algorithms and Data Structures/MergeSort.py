
import random
import time

def merge_sort(list):

    if len(list) <= 1:
        return list
    
    mid = len(list) // 2

    left_half = merge_sort(list[:mid])
    right_half = merge_sort(list[mid:])

    return merged(left_half ,right_half)

def merged(left_half, right_half):

    sorted_list = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):

        if left_half[i] < right_half[j]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1

    sorted_list.extend(left_half[i:])
    sorted_list.extend(right_half[j:])
    
    return sorted_list


def verify(list):

    if len(list) <= 1:
        return True
    else:
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                return False
        return True
    

unsorted_list = [random.randint(134, 823789) for _ in range(1000000)]

start_time = time.time() 
sorted_list = merge_sort(unsorted_list)
end_time = time.time()

if verify(sorted_list):
    print("The list sorted successfuly !")
else:
    print("Something went worng !")

print(f"Execution time: {(end_time - start_time):.02f} sec")






# **************************************************************************

# start_time = time.time()
# unsorted_list = [random.randint(134, 823789) for _ in range(10000000)]

# sorted_list = sorted(unsorted_list)
# end_time = time.time()

# print(f"Execution time: {end_time - start_time}sec")

# print(sorted_list)





# How the Code Runs
# Splitting Phase:
# [8, 3, 5, 4] → [8, 3], [5, 4] → [8], [3], [5], [4].

# Merging Phase:

# Merge [8] and [3] → [3, 8].
# Merge [5] and [4] → [4, 5].
# Merge [3, 8] and [4, 5] → [3, 4, 5, 8].


# merge_sort([8, 3, 5, 4])
#   |
#   |-- split([8, 3, 5, 4]) → [8, 3], [5, 4]
#   |-- merge_sort([8, 3]) ----------------------- merge_sort([5, 4])
#        |                                         |
#        |-- split([8, 3]) → [8], [3]             |-- split([5, 4]) → [5], [4]
#        |-- merge_sort([8]) → [8]                |-- merge_sort([5]) → [5]
#        |-- merge_sort([3]) → [3]                |-- merge_sort([4]) → [4]
#        |-- merge([8], [3]) → [3, 8]             |-- merge([5], [4]) → [4, 5]
#   |
#   |-- merge([3, 8], [4, 5]) → [3, 4, 5, 8]

# ***********************************************************************************