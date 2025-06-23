import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# GUI Setup
root = tk.Tk()
root.title(" Simple Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        action = calculate if char == "=" else lambda c=char: button_click(c)
        tk.Button(frame, text=char, font=("Arial", 16), command=action if char != "=" else calculate).pack(side="left", expand=True, fill="both")

tk.Button(root, text="Clear", font=("Arial", 16), command=clear).pack(expand=True, fill="both")

root.mainloop()
