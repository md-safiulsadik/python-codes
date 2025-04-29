
# exception = An event that interrupts the flow of a program
#             ( ZeroDivisionError, TypeError, ValueError )
#             1.try, 2.except, 3.finally

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
        
    except ZeroDivisionError as e:
        print(e)
        print("denominator can't be 0")
        
    except ValueError as e:
        print(e)  
        print("Numerator and denominator must be numbers")
        
    except Exception as e:
        print(e)
        print("something went wrong...")    

    else:
        print(result)
        break

    finally:
        print("Thanks for using this program")