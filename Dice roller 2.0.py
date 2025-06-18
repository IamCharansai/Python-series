import random

dice_faces = {
    1: ("┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"),
    2: ("┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"),
    3: ("┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"),
    4: ("┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"),
    5: ("┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"),
    6: ("┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"),
}

def roll_dice():
    roll = random.randint(1, 6)
    for line in dice_faces[roll]:
        print(line)
    print(f" You rolled a {roll}!\n")

print(" Welcome to the Dice Rolling Simulator!")
while True:
    input("Press Enter to roll the dice... (or type 'q' to quit) ")
    roll_dice()
    again = input("Roll again? (y/n): ").strip().lower()
    if again != 'y':
        print(" Thanks for playing!")
        break
