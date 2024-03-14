# import ColabTurtle.Turtle as turtle
import turtle

t = turtle.Turtle()

# t.circle(100)
# height = t.window
height = turtle.window_height()
width = turtle.window_width()
# print(height)
for i in range(1,6):
    t.circle(i*25)
    t.penup()
    t.goto(0,-i*25)# that means the center(0,0)
    t.pendown()
