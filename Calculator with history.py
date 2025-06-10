def calculate(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return " Cannot divide by zero"

history = []

print(" Advanced Calculator with History\n")

while True:
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        result = calculate(a, b, op)
        history.append(f"{a} {op} {b} = {result}")
        print(f" Result: {result}")
    except ValueError:
        print(" Please enter valid numbers.")
        continue

    choice = input("\nDo you want to continue? (y/n/history): ").lower()
    if choice == 'history':
        print("\n Calculation History:")
        for record in history:
            print(record)
    elif choice != 'y':
        print(" Exiting Calculator. Goodbye!")
        break
