import tkinter as tk
from tkinter import messagebox

def is_palindrome():
    text = entry.get().lower().replace(" ", "")
    if text == text[::-1]:
        result = f" '{entry.get()}' is a Palindrome!"
    else:
        result = f" '{entry.get()}' is NOT a Palindrome."
    messagebox.showinfo("Result", result)

# GUI Setup
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, text="Enter a word or number:", font=('Arial', 12))
label.pack(pady=10)

entry = tk.Entry(root, font=('Arial', 14), justify='center')
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check", command=is_palindrome, font=('Arial', 12), bg='lightblue')
check_btn.pack(pady=20)

root.mainloop()
