import turtle
import colorsys

# Setup screen
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pensize(2)

# Colors
h = 0
for i in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.circle(100)
    t.right(10)
    h += 0.01

turtle.done()
