import turtle

t = turtle.Turtle()

def shape_to_make(size ,n):
    for i in range(n):
        t.forward(size)
        t.right(360/n)
