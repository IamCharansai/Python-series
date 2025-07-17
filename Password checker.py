import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (min 8 characters)": length_error,
        "Missing digit": digit_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing special character": symbol_error,
    }

    if not any(errors.values()):
        strength = "Strong "
    elif sum(errors.values()) <= 2:
        strength = "Moderate "
    else:
        strength = "Weak "

    return strength, [err for err, present in errors.items() if present]

# --- Main Program ---
print(" Password Strength Checker")
password = input("Enter your password: ")
strength, problems = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if problems:
    print("Issues:")
    for problem in problems:
        print(f" - {problem}")
