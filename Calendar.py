import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

def show_calendar():
    try:
        month = months.index(month_var.get()) + 1
        year = int(year_var.get())
        cal_output = calendar.month(year, month)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, cal_output)
    except Exception as e:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Error: " + str(e))

# GUI Window
root = tk.Tk()
root.title(" Calendar Generator")
root.geometry("400x400")
root.resizable(False, False)

# Month and Year Options
months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
years = [str(y) for y in range(1980, 2101)]

month_var = tk.StringVar(value=months[datetime.now().month - 1])
year_var = tk.StringVar(value=str(datetime.now().year))

# Layout
tk.Label(root, text="Select Month:", font=("Arial", 12)).pack(pady=5)
month_menu = ttk.Combobox(root, textvariable=month_var, values=months, state="readonly")
month_menu.pack()

tk.Label(root, text="Select Year:", font=("Arial", 12)).pack(pady=5)
year_menu = ttk.Combobox(root, textvariable=year_var, values=years, state="readonly")
year_menu.pack()

tk.Button(root, text="Generate Calendar", command=show_calendar).pack(pady=10)

text_area = tk.Text(root, height=10, width=40, font=("Courier", 12))
text_area.pack(pady=5)

# Run
root.mainloop()
