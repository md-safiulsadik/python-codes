
# map(function, collection) = Applies a given function to all items in a collection

# def cal_to_fahr(temp):
#     return f"{(temp * 9/5) + 32:.2f}"

celsius_temp = [54.5, 69.1 ,65.34, 87.75, 54.43]

fahrenheit_temp = list(map(lambda temp: f"{(temp * 9/5) + 32:.2f}" , celsius_temp))

print(fahrenheit_temp)