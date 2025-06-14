import tkinter as tk

# Function to draw on canvas
def draw(event):
    x, y = event.x, event.y
    radius = 3
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='black')

# Window setup
root = tk.Tk()
root.title(" Python Paint")
root.geometry("500x400")

# Canvas setup
canvas = tk.Canvas(root, bg='white', width=480, height=360)
canvas.pack(pady=20)

# Bind mouse movement
canvas.bind("<B1-Motion>", draw)

# Run the app
root.mainloop()
