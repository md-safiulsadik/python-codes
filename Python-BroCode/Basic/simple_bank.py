
import os , msvcrt , time

def withdraw(main_balance):
    os.system('cls')
    while True:
        try:
            amount = float(input("How much you want to withraw ?\nAmount : $"))
            break
        except ValueError:
            print("Invalid Input\nTry again !")
    print("Processing transaction......")
    time.sleep(2)
    if amount <= 0:
        print("Amount must be greatter than Zero !")
        time.sleep(1)
        return 0
    elif amount > main_balance:
        print("Innsufficient balance !")
        time.sleep(1)
        return 0
    else:
        print("withraw Successfull !")
        time.sleep(1)
        return amount
    
def deposit():
    os.system('cls')
    while True:
        try:
            amount = float(input("How much you want to diposit ?\nAmount : $"))
            break
        except ValueError:
            print("Invalid Input\nTry again !")
    if amount <= 0:
        print("Amount must be greatter than Zero !")
        time.sleep(1)
        return 0
    else:
        print("Processing transaction......")
        time.sleep(2)
        print("Diposit Successful !")
        time.sleep(1)
        return amount

def display_balance(balance):
    os.system("cls")
    print(f"""
                                    _______________________________
                                   |                               |
                                   |           AB Bank LTD         |
                                   |_______________________________|
                              
          """)
    print(f"\t\t\t\nYour main balance is ${balance:2f}")
    msvcrt.getch()
    

def display():
    print("""
                                    _______________________________
                                   |                               |
                                   |           AB Bank LTD         |
                                   |_______________________________|

                                         Welcome to AB Bank
                                       How can we help you today !
                                    
                                1. Withdraw
                                2. Deposit
                                3. Check Balance
                                4. Exit
              """)

def main():
    main_balance = 20
    is_running = True

    while is_running:
        display()
        choice = input("Enter you choice  ")
        if choice == '1':
            main_balance -= withdraw(main_balance)
        elif choice == '2':
            main_balance += deposit()
        elif choice == '3':
            display_balance(main_balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")
            
if __name__ == '__main__':
    main()
