
def test_duplicate(data):
    if len(data) == len(set(data)):
        return "NO Duplicates"
    else:
        return "Has Duplicates"

def main():
    data = [1, 2, 3, 4, 5]
    data2 = [1, 2, 3, 4, 5, 1]
    print(test_duplicate(data2))
    
if __name__ == "__main__":
    main()

# sets don't allow duplicates so if the length of the set is equal to the length of the data then there are no duplicates