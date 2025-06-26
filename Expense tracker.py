import datetime

def add_expense():
    amount = input("Enter amount: ₹")
    category = input("Enter category (food, travel, bills, etc.): ")
    note = input("Add a note (optional): ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("expenses.csv", "a") as file:
        file.write(f"{date},{amount},{category},{note}\n")
    
    print(" Expense added!")

def view_expenses():
    print("\n Your Expenses:")
    try:
        with open("expenses.csv", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No expense records found yet.")

def main():
    while True:
        print("\n<<<--Expense Tracker-->>>")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print(" Exiting Expense Tracker.")
            break
        else:
            print(" Invalid choice. Please try again.")

main()
