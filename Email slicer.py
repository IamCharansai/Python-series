print(" Email Slicer \n")

# Ask user for email input
email = input("Enter your email address: ").strip()

# Check for basic format
if "@" in email and "." in email:
    # Split email
    username = email.split('@')[0]
    domain = email.split('@')[1]

    print("\n Sliced Email Details:")
    print(f" Username: {username}")
    print(f" Domain: {domain}")
else:
    print(" Invalid email format. Please try again.")
