import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor()[1]  # Returns (RGB, HEX)
    if color:
        color_label.config(text=f"Selected Color: {color}", bg=color)

# Setup main window
window = tk.Tk()
window.title(" Color Picker")
window.geometry("300x150")

# Button to pick color
pick_button = tk.Button(window, text="Pick a Color", command=pick_color, font=("Arial", 14))
pick_button.pack(pady=20)

# Label to show selected color
color_label = tk.Label(window, text="No color selected", font=("Arial", 12))
color_label.pack(pady=10)

# Run app
window.mainloop()