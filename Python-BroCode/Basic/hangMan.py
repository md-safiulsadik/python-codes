
import random

words = {
    "FROST": "A weather condition that occurs when the temperature drops below a certain point",
    "SPACE": "The vastness that contains stars, planets, and galaxies",
    "PULSE": "A rhythmic beating of the heart",
    "RULER": "A tool used to measure length or width",
    "LEMON": "A sour citrus fruit often used in cooking",
    "TIGER": "A large, carnivorous mammal with orange and black stripes",
    "BLOOM": "To produce flowers or to come into flower",
    "GRAPE": "A small, round fruit often used to make wine",
    "OCEAN": "A vast body of saltwater that covers most of the Earth",
    "PIANO": "A musical instrument played by pressing keys"
}

#art
hangman_art =  {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}


def display_art(wrong_guesses):
    for art in hangman_art[wrong_guesses]:
        print(art)


def display_hint(hint, hint_line):
    print()
    print(' '.join(hint))
    print("Hint :", hint_line)


def display_answer(answer, wrong_guesses):
    display_art(wrong_guesses)
    print(f"The word was '{answer}'")


def display_win(answer, score, wrong_guesses):
    print()
    print(f"The word was '{answer}'")
    print()
    
    if score == 6:
        print("YOU WIN !")
        print(f"You score {score}")
        print("Congratutations you got the highest score !")
    else:
        print("YOU WIN !")
        print(f"You score {score}")
        print(f"Your wrong guesses {wrong_guesses}")

def main():
    is_running = True
    answer = random.choice(list(words.keys()))
    hint_line = words[answer]
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    score = 6

    print("""
                                Welcome to Python HangMan Game ! 
    """)
    
   
    while is_running:
        if '_' not in hint:
            display_win(answer, score, wrong_guesses)
            is_running = False
    
        elif wrong_guesses == 6:
            print()
            print("You Lose !")
            display_answer(answer, wrong_guesses)
            is_running = False
            
        else:
            display_art(wrong_guesses)
            display_hint(hint, hint_line)
            print()
            guess = input("Enter a latter : ").upper()
        
            if not guess.isalpha() or len(guess) != 1:
                print("\nWrong input !\nTry again..")
                continue
            
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1
                score -= 1
        
if __name__ == '__main__':
    main()