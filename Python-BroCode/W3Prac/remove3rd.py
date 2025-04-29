def remove_and_print_every_third(numbers):
    index = 2
    while numbers:
        print(numbers.pop(index))
        index = 2 if len(numbers) > 2 else 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_and_print_every_third(numbers)
