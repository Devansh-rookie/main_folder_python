import turtle

def regularOctagon(t):
    t.forward(100)
    t.left(360/8)

t = turtle.Turtle()

t.right(45)
for i in range(8):
    regularOctagon(t)
    t.left(360/8)
turtle.mainloop()