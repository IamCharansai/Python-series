import time
import random

sentences = [
    "Python is a great programming language.",
    "Artificial intelligence is the future.",
    "Typing speed is important for productivity.",
    "Always test your code before deploying.",
    "Practice makes a person perfect."
]

def typing_test():
    print(" Welcome to the Typing Speed Test")
    sentence = random.choice(sentences)
    print("\nType the following sentence:\n")
    print(f" {sentence}\n")

    input("Press Enter when you're ready to start...")

    start_time = time.time()
    typed = input("\nStart Typing:\n")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)
    words = len(sentence.split())
    wpm = round((len(typed.split()) / time_taken) * 60, 2)

    correct_chars = sum(1 for i, c in enumerate(typed) if i < len(sentence) and c == sentence[i])
    accuracy = round((correct_chars / len(sentence)) * 100, 2)

    print("\n Time Taken:", time_taken, "seconds")
    print(" Words Per Minute (WPM):", wpm)
    print(" Accuracy:", accuracy, "%")

# Run the test
typing_test()
