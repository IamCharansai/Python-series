import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all
    all_chars = lowercase + uppercase + digits + symbols

    # Make sure the password has at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest with random choices
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# Run
print("🔐 Random Password Generator")
try:
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
except ValueError:
    print("❗ Please enter a valid number.")
