from datetime import datetime

def log_mood():
    mood = input("How are you feeling today? 😊😔😡😴🤔: ")
    note = input("Would you like to add a short note? (optional): ")

    entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Mood: {mood} | Note: {note}\n"

    with open("mood_log.txt", "a") as file:
        file.write(entry)

    print("\n Your mood has been logged.")

def view_log():
    print("\n Mood Log:")
    try:
        with open("mood_log.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No mood entries found yet.")

# Menu
while True:
    print("\n--- Daily Mood Tracker ---")
    print("1. Log today's mood")
    print("2. View mood history")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        log_mood()
    elif choice == "2":
        view_log()
    elif choice == "3":
        break
    else:
        print(" Invalid option. Please try again.")
