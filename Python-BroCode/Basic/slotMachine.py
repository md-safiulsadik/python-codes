# Slot Machine Game

import time
import random

def add_money() -> float:
    money = input("How you want to add\nAmount : ")
    return(float(money))

def spin_row():
    symbols = ['⭐', '🍌' , '🔥' , '❤️' , '🧁' ]
    return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("Spining...\n")
    time.sleep(1)
    print(" | ".join(row), '\n')

def get_payout(row , bet) -> float:

    if row[0] == row[2] == row[1]:
        print("Boom ! you got strick !")
        if row[0] == '⭐':
            print(f"You get in return {bet * 5}")
            return bet * 5
        elif row[0] == '🍌':
            print(f"You get in return {bet * 3}")
            return bet * 3
        elif row[0] == '❤️':
            return bet * 2
        elif row[0] == '🧁':
            return bet * 1.5
        elif row[0] == '🔥':
            print(f"You get in return {bet * 10}")
            return bet * 10
    else:
        print("You get nothing !\n Try again !")
        return 0

def main():
    
    # balance = 100
    while True:    
        try:
            balance = float(input("Deposit money to start 🔥\nAmonut : $"))
            break
        except ValueError:
            print("Invalid input")
  
    print("""
                              Welcome to Python Slot
                            ------------------------------
                              | ⭐ | 🍌 | ❤️ | 🧁 | 🔥 |           
        """)

    while True:
        print(f"Current Balance {balance:.02f}")
        bet = input("Enter you bet ammout : $")
        if not bet.isdigit():
            print("Not vaid !\n")
            continue
        if bet == '0':
            print("Bet must be gretter than Zero\n")
            continue
        
        bet = float(bet)
        
        if balance < bet:
            print()
            choice = input("Insufficent token !\nAdd token to continue (Y/N)  ").lower()
            if choice == 'y':
                balance += add_money()
            else:
                break
        
        balance -= bet
        row = spin_row()
        print_row(row)
        balance += get_payout(row , bet)   

        choice = input("(Q/q) to quit or any key to continue...  ").lower()
        print()
        if choice == 'q':
            print(f"Your current balanace {balance:.02f}")
            break
        else:
            continue
if __name__ == '__main__':
    main()