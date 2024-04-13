import turtle

def regular_polygon(turt: turtle.Turtle, n):
    angle = 360/n
    for i in range(n):
        turt.forward(100)
        turt.left(angle)

t = turtle.Turtle()
t.speed(0)
n =8
for i in range(n):
    regular_polygon(t,n)
    t.setheading(0)
    t.left((360/n)*(i+1))

turtle.mainloop()