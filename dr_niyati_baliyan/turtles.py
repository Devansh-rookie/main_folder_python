import turtle
import math
import random
t = turtle.Turtle()
a = 100
turtle.colormode(255)
b = a*math.sin(0.942478)/math.sin(1.25664)
for i in range(5):
    # t.forward(a*math.sin(0.942478))
    t.begin_fill()
    t.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
    t.forward(b)
    t.left(180-54)
    t.forward(a)
    t.left(180-54)
    # t.forward(a*math.sin(0.942478))
    t.forward(b)
    # t.goto((0,0))
    t.left(180)
    t.end_fill()
turtle.mainloop()