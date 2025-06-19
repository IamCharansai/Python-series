import random

# Word list (you can expand this)
words = ["python", "hangman", "programming", "challenge", "developer"]

# Choose a word
word = random.choice(words).lower()
guessed = ["_"] * len(word)
used_letters = set()
attempts = 6

print(" Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord: " + " ".join(guessed))
    print("Used letters:", ", ".join(sorted(used_letters)))
    print(f" Remaining attempts: {attempts}")

    guess = input(" Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Enter a single alphabet.")
        continue

    if guess in used_letters:
        print(" Already guessed that letter.")
        continue

    used_letters.add(guess)

    if guess in word:
        print(" Correct!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        print(" Wrong guess.")
        attempts -= 1

# End of game
print("\n The word was:", word)
if "_" not in guessed:
    print(" Congrats! You saved the hangman!")
else:
    print(" You lost! Better luck next time.")
