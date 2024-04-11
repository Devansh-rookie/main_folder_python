import turtle
import random

def regular_polygon(turt: turtle.Turtle , n, size, color_line= "black", color_fill= "yellow"):
    turt.pendown()
    turt.color(color_line, color_fill)
    turt.begin_fill()
    for i in range(n):
        turt.forward(size)
        turt.left(360/n)
    turt.end_fill()
    turt.penup()

how_many = int(input("How many shapes to draw: "))

turt = turtle.Turtle()

turt.screen.screensize(500,500)
colors = ["black", "white", "yellow", "blue", "red", "teal", "green"]
turt.speed(0)
for i in range(how_many):
    rand1 = random.randrange(len(colors))
    rand2 = random.randrange(len(colors))
    n = random.randrange(3,8)
    size = random.randrange(100)
    regular_polygon(turt, n, size, colors[rand1], colors[rand2])
    turt.penup()
    rand_x = random.randrange((-300), 300)
    rand_y = random.randrange(-300, 300)
    turt.setpos((rand_x, rand_y))
# turtle.Screen().exitonclick()
turtle.mainloop()
