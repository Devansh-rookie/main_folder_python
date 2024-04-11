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
t.speed(0)

# n= 100
# m=8
# for i in range(n):
#     t.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
#     # t.forward(i+1)
#     regular_polygon(t, m, i)
#     t.left(360/m)

# n= 1000
# m=6
# angle = 360/m
# for i in range(n):
#     t.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
#     t.forward(i+1)
#     t.left((angle+i)%360)

n= 300
m=5
angle = 360/m
for i in range(n):
    t.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
    t.forward(i+1)
    t.left(angle+1) # -1 for opposite spiral direction

turtle.mainloop()