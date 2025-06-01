users = {
    "admin": "admin123",
    "user1": "python123",
    "guest": "guestpass",
    "testuser": "testpass",
    "johndoe": "doepass",
    "alice": "alicepass"
}

print(" Welcome to the Simple Login System")

attempts = 3

while attempts > 0:
    username = input(" Enter username: ")
    password = input(" Enter password: ")

    if username in users and users[username] == password:
        print(f" Login successful. Welcome, {username}!")
        break
    else:
        attempts -= 1
        print(f" Invalid credentials. Attempts left: {attempts}\n")

if attempts == 0:
    print(" Too many failed attempts. Access locked.")
