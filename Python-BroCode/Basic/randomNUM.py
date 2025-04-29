
# import random
# low = 0
# high = 2

# rand = random.randint(low , high)
# options = (('rock 1', 'paper11', 'scissors 1'),
#            ('rock 2', 'paper 2', 'scissors 2'),
#            ('rock 3', 'paper 3', 'scissors 3'),)

# num = random.choice(options[rand])

# options = ('rock', 'paper', 'scissors')
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "A", "K", "Q", "J", "10"]

# num = random.randint(low , high)
# num = random.random()
# num = random.choice(options)

# random.shuffle(cards)
# for card in cards:
#     print(card , end=" ")

# print(num)


import random

low = 1
high = 100
top_score = 10
guesses = 0

number = random.randint(low, high)
print("""
                                             _______________________________________
                                            |          Number Guessing Game         |
                                            |_______________________________________|
      """)
while guesses < top_score:
    guess = input(f"Guess a number between ({low} - {high})  ")

    if guess.isdigit():
        guess = int(guess)
        if guess < low or guess > high:
            print(f"Opss...!!\nNumer Should be Between ({low} - {high})")
        else:
            guesses += 1
            if guess > number:
                print("The numer is smaller ↓ \nTry again !")
            elif guess < number:
                print("The number is bigger ↑ \nTry again !")
            else:
                print(f"\nCurrect !\nThe number was {number}")
                print(f"Top Score {top_score}")
                print(f"Your Score {top_score - guesses}")
                break
    else:
        print(f"Opss...!!\nNumer Should be Between ({low} - {high})")

if guesses == top_score and guess != number:
    print(f"\nYou Lose!\nThe number was {number}")


from msvcrt import getch
getch()