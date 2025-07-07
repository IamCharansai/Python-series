import time
import random

flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"question": "What keyword is used to define a function in Python?", "answer": "def"},
    {"question": "What data type is used to store True/False?", "answer": "Boolean"},
    {"question": "Who developed Python?", "answer": "Guido van Rossum"}
]

random.shuffle(flashcards)

print(" Flashcard Quiz - Type ENTER to reveal the answer")
print("--------------------------------------------------")

score = 0

for card in flashcards:
    print("\n", card["question"])
    input("Press Enter to reveal the answer...")
    print("", card["answer"])
    response = input("Did you know the answer? (y/n): ").lower()
    if response == "y":
        score += 1

print(f"\n Quiz Complete! Your score: {score}/{len(flashcards)}")
