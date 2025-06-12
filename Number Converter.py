def show_menu():
    print("\n Number Converter")
    print("1. Decimal to Binary")
    print("2. Decimal to Hexadecimal")
    print("3. Binary to Decimal")
    print("4. Hexadecimal to Decimal")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        num = int(input("Enter decimal number: "))
        print(f"Binary: {bin(num)[2:]}")

    elif choice == '2':
        num = int(input("Enter decimal number: "))
        print(f"Hexadecimal: {hex(num)[2:].upper()}")

    elif choice == '3':
        binary = input("Enter binary number: ")
        try:
            decimal = int(binary, 2)
            print(f"Decimal: {decimal}")
        except ValueError:
            print(" Invalid binary number.")

    elif choice == '4':
        hexa = input("Enter hexadecimal number: ")
        try:
            decimal = int(hexa, 16)
            print(f"Decimal: {decimal}")
        except ValueError:
            print(" Invalid hexadecimal number.")

    elif choice == '5':
        print(" Exiting Number Converter. Goodbye!")
        break

    else:
        print(" Invalid choice. Please select 1 to 5.")
