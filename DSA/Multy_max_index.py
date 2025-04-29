def multy_of_maxindex(numbers):
    n = len(numbers)
    if n < 2:
        raise ValueError("Must input 2 or more integers!")

    max_index1, max_index2 = (0, 1) if numbers[0] > numbers[1] else (0, 1)
    
    for i in range(2, n):
        if numbers[i] > numbers[max_index1]:
            max_index2 = max_index1
            max_index1 = i
        elif numbers[i] > numbers[max_index2]:
            max_index2 = i 

    return f"Multipication of the max numbers: {numbers[max_index2] * numbers[max_index1]}"

if __name__ == "__main__":
    try:
        numbers = list(map(int, input("Enter the numbers: ").split()))
        print(multy_of_maxindex(numbers))
    except ValueError as e:
        print(f"Error {e}")
    except Exception as e:
        print(f"Unknown Error {e}")