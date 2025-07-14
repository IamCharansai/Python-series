import random

def generate_question(level):
    if level == "easy":
        a, b = random.randint(1, 20), random.randint(1, 20)
        op = random.choice(["+", "-"])
    elif level == "medium":
        a, b = random.randint(2, 12), random.randint(2, 12)
        op = "*"
    elif level == "hard":
        a, b = random.randint(10, 99), random.randint(1, 9)
        op = random.choice(["+", "-", "*", "/"])
    else:
        return None, None, None

    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, round(answer, 2), op

# Game setup
print(" Math Quiz Game")
level = input("Choose difficulty (easy/medium/hard): ").lower()
score = 0

for i in range(5):
    question, correct_answer, op = generate_question(level)
    if not question:
        print(" Invalid level. Exiting.")
        break

    print(f"\nQ{i+1}: What is {question}?")
    try:
        user_answer = float(input("Your answer: "))
        if abs(user_answer - correct_answer) < 0.01:
            print(" Correct!")
            score += 1
        else:
            print(f" Incorrect. Correct answer is {correct_answer}")
    except:
        print(" Invalid input.")

print(f"\n Quiz Complete! Your Score: {score}/5")
