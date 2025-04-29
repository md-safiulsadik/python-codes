# Here are the Unicode characters I use for drawing the dice.
# Youtube has strange spacing, so the ASCII art looks warped in the description. 
# It should still work if you copy and paste it into PyCharm.

# ● ┌ ─ ┐ │ └ ┘

import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
num_of_dice = int(input("Number of dice?  "))

for _ in range(num_of_dice):
    dice.append(random.randint(1 , 6))

# for die in range(num_of_dice):
#     for art in dice_art.get(dice[die]):
#         print(art)

for line in range(5):
    for die in dice:
        from time import sleep
        sleep(0.5)
        print(dice_art.get(die)[line] , end="")
    print()

total = sum(dice)
print(f"Total : {total}")






# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # PRINT VERTICALLY
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# # PRINT HORIZONTALLY
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total: {total}")