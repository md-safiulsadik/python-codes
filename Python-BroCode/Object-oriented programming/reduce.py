# reduce(function, collection) = Reduces elements in a collection to a single value
#        For loop is better in most cases
#        Reduce is better for a functional approach + readability


from functools import reduce

prices = [43.53, 53.53, 35.353, 5353.53, 39.344, 453.430]

total = reduce(lambda x, y: x + y, prices)

print(total) 