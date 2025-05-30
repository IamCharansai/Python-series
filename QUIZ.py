print("Welcome to the Python Quiz!\n")

# Define the quiz questions and answers
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["A. J.R.R. Tolkien", "B. J.K. Rowling", "C. George R.R. Martin", "D. Agatha Christie"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B"
    }
]

# Initialize the score
score = 0

# Quiz loop
for q in quiz:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}\n")

# Final score display
print(f"Quiz Completed! Your Score: {score}/{len(quiz)}")
