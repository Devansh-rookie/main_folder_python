import turtle

t = turtle.Turtle()
# turtle.screensize(800,800)
n=8
t.speed(0)
for j in range(n):
    for i in range(n):
        t.forward(100)
        t.left(360/n)
    t.left(360/n)

turtle.mainloop()