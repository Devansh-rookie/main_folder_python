import turtle
import random
def regular_polygon(turt: turtle.Turtle, n, size):
    angle = 360/n
    for i in range(n):
        turt.forward(size)
        turt.left(angle)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.colormode(255)
n=8
m=8
for i in range(n):
    t.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
    regular_polygon(t,m, 150)
    t.left(360/n)
turtle.mainloop()