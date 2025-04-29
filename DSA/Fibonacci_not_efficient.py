
def FibRec(n):
    if n <= 1:
        return n
    
    return FibRec(n - 1) + (n - 2)

n = int(input("n: "))
print(FibRec(n))

