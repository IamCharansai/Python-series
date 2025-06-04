import random
words = ["python", "developer", "program", "keyboard", "learning", "function", "variable"]

def scramble(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def play_game():
    word = random.choice(words)
    scrambled = scramble(word)

    print("\n Welcome to the Word Scramble Game!")
    print(f" Unscramble this word: {scrambled}")

    guess = input("Your guess: ")

    if guess.lower() == word:
        print(" Correct! Great job.")
    else:
        print(f" Oops! The correct word was: {word}")

while True:
    play_game()
    again = input("\n Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(" Thanks for playing!")
        break
