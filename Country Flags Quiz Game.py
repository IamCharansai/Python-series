import random

# Flag options
flags = {
    "India": "🇮🇳",
    "United States": "🇺🇸",
    "Japan": "🇯🇵",
    "Germany": "🇩🇪",
    "Brazil": "🇧🇷",
    "France": "🇫🇷",
    "Italy": "🇮🇹",
    "Canada": "🇨🇦",
    "China": "🇨🇳",
    "South Korea": "🇰🇷"
}

def flag_quiz():
    score = 0
    questions = random.sample(list(flags.items()), 5)  # 5 random questions

    for country, correct_flag in questions:
        # Get all other flags and choose 3 incorrect ones
        all_flags = list(flags.values())
        all_flags.remove(correct_flag)
        incorrect_flags = random.sample(all_flags, 3)

        # Combine correct flag with incorrect options and shuffle
        choices = incorrect_flags + [correct_flag]
        random.shuffle(choices)

        print(f"\nWhat is the flag of {country}?")
        for i, opt in enumerate(choices):
            print(f"{chr(65 + i)}. {opt}")

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if len(answer) != 1 or answer not in "ABCD":
            print("Invalid option. Skipping question.")
            continue

        index = ord(answer) - 65
        selected_flag = choices[index]

        if selected_flag == correct_flag:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_flag}")

    print(f"\nYour Final Score: {score}/5")

# Run the quiz
flag_quiz()

