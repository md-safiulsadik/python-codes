
questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
           "What is the most abundant gas in Earth's atmosphere?: ",
           "How many bones are in the human body?: ",
           "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
question_num = 0
score = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter answer (A ,B, C or D) : ").upper()
    guesses.append(guess)
    if guesses[question_num] == answers[question_num]:
        print("Correct !")
        score += 1
    else:
        print("Incorrect !")
        print(f"Correct Answer is {answers[question_num]}")
    question_num += 1
    
print("------------------")
print("       Result     ")
print("------------------")
# print(f"Your Answers {guesses}")
print("\nCorrect Answer", end="\t")
for answer in answers:
    print(answer , end=" ")
print("\nYour Answer", end="\t")
for guess in guesses:
    print(guess, end=" ")
# print(f"Currect Answers {answers}")
print(f"\nYour Sorce {score}")

from msvcrt import getch
getch()



# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("----------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1

# print("----------------------")
# print("       RESULTS        ")
# print("----------------------")

# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")




# num_pad_list_of_lists = [
#     [1, 2, 3],       # Row 1
#     [4, 5, 6],       # Row 2
#     [7, 8, 9],       # Row 3
#     ["*", 0, "#"]    # Row 4
# ]

# num_pad_list_of_tuples = [
#     (1, 2, 3),       # Row 1
#     (4, 5, 6),       # Row 2
#     (7, 8, 9),       # Row 3
#     ("*", 0, "#")    # Row 4
# ]

# num_pad_list_of_sets = [
#     {1, 2, 3},       # Row 1
#     {4, 5, 6},       # Row 2
#     {7, 8, 9},       # Row 3
#     {"*", 0, "#"}    # Row 4
# ]

# num_pad_tuple_of_lists = (
#     [1, 2, 3],       # Row 1
#     [4, 5, 6],       # Row 2
#     [7, 8, 9],       # Row 3
#     ["*", 0, "#"]    # Row 4
# )

# num_pad_tuple_of_tuples = (
#     (1, 2, 3),       # Row 1
#     (4, 5, 6),       # Row 2
#     (7, 8, 9),       # Row 3
#     ("*", 0, "#")    # Row 4
# )

# num_pad_tuple_of_sets = (
#     {1, 2, 3},       # Row 1
#     {4, 5, 6},       # Row 2
#     {7, 8, 9},       # Row 3
#     {"*", 0, "#"}    # Row 4
# )

# def print_number_pad(num_pad):
#     for row in num_pad:
#         for num in row:
#             print(num, end=" ")
#         print()

# # Example usage:
# print_number_pad(num_pad_list_of_lists)

# # 2D set of lists (NOT VALID)
# # num_pad = {[1, 2, 3],
# #            [4, 5, 6],
# #            [7, 8, 9],
# #            ["*", 0, "#"]}

# # 2D set of sets (NOT VALID)
# # num_pad = {{1, 2, 3},
# #            {4, 5, 6},
# #            7, 8, 9},
# #          {"*", 0, "#"}}