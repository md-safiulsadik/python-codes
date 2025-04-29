def FiboLoop(n):
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    total_sum = prev + curr

    for _ in range(2, n + 1):
        prev, curr = curr , curr + prev
        total_sum += curr

    return total_sum


print(FiboLoop(100))