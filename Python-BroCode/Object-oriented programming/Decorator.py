# Decorator = A function that extends the behavior of another function
#            w/o modifying the base function
#            Pass the base function as an argument to the decorator

def add_cream(func):
    def warpper(*args, **kwargs):
        print("With extra cream")
        func(*args, **kwargs)
    return warpper

def add_chocolate(func):
    def warpper(*args, **kwargs):
        print("With more chocolate")
        func(*args, **kwargs)
    return warpper


@add_cream
@add_chocolate
def get_ice_cream(flavor):
    print(f"You got a {flavor} ice-cream")


@add_cream
def get_bar(brand, size):
    print(f"You got a {size} {brand} chocolate bar")

get_ice_cream('vanilla')

print()

get_bar(size='big', brand='Pran')