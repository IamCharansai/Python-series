def split_bill():
    print(" Bill Splitter")

    try:
        total_amount = float(input("Enter total bill amount: ₹ "))
        num_people = int(input("Enter number of people: "))
        tip_percent = float(input("Enter tip percentage (e.g., 10 for 10%): "))

        tip_amount = total_amount * (tip_percent / 100)
        grand_total = total_amount + tip_amount
        per_person = grand_total / num_people

        print("\n Bill Summary:")
        print(f"Total Bill: ₹{total_amount:.2f}")
        print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
        print(f"Grand Total: ₹{grand_total:.2f}")
        print(f"Each Person Pays: ₹{per_person:.2f}")

    except ValueError:
        print(" Please enter valid numbers.")

# Run it
split_bill()
