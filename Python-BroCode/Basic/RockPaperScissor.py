import random , msvcrt

options = ('rock', 'paper', 'scissor')

def print_result(choice, computer, result):
    print(f"Choice: {choice}")
    print(f"Computer: {computer}")
    print(result)

def main():
    user_score = 0
    computer_score = 0

    while True:
        

        choice = input("Enter your choice (Q/q) to Quit ").lower()
        if choice == 'q':
            print(f"Your Score: {user_score}\nComputer Score: {computer_score}")
            print("Thanks for playing !")
            print("Press any key to exit ...")
            msvcrt.getch()
            break
        elif choice not in options:
            print("Wrong Input !\nYour Input must be (rock, paper or scissor)")
        else:
            computer = random.choice(options)
            if (computer == 'rock' and choice == 'paper' or 
                computer == 'paper' and choice == 'scissor' or 
                computer == 'scissor' and choice == 'rock'):
                print_result(choice, computer , "You Win !")
                user_score += 1

            elif computer == choice:
                print_result(choice, computer , "Tie !")
            else:
                print_result(choice, computer , "You Lose !")
                computer_score += 1    


if __name__ == '__main__':
    main()