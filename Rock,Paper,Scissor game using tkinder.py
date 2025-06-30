import tkinter as tk
import random

# Choices and results logic
choices = ['Rock', 'Paper', 'Scissors']

def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=f"Result: {result}")

def determine_winner(user, comp):
    if user == comp:
        return "It's a tie!"
    elif (user == 'Rock' and comp == 'Scissors') or \
         (user == 'Paper' and comp == 'Rock') or \
         (user == 'Scissors' and comp == 'Paper'):
        return " You win!"
    else:
        return " Computer wins!"

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x350")
root.resizable(False, False)

title = tk.Label(root, text="Rock, Paper, Scissors", font=('Arial', 16))
title.pack(pady=10)

# Result labels
user_label = tk.Label(root, text="", font=('Arial', 12))
user_label.pack()

comp_label = tk.Label(root, text="", font=('Arial', 12))
comp_label.pack()

result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'))
result_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

for choice in choices:
    btn = tk.Button(button_frame, text=choice, width=10, height=2,
                    font=('Arial', 12),
                    command=lambda ch=choice: play(ch))
    btn.pack(side=tk.LEFT, padx=5)

# Quit button
quit_btn = tk.Button(root, text="Quit", command=root.quit, font=('Arial', 12))
quit_btn.pack(pady=10)

root.mainloop()
