import turtle

# turt = turtle.Turtle()
# turt.speed(0)
# turt.hideturtle()
# for i in range(0,400,2):
#     turt.forward(i)
#     turt.left(90)

t = turtle.Turtle()
t.color("black", "black")
# for i in range(9):
#     t.forward(200)
#     t.right(140)# 144 was working , 720/n
# t.begin_fill()
# t.fillcolor("yellow")
for i in range(5):
    t.begin_fill()
    t.forward(200)
    t.left(144)
    t.end_fill()

turtle.mainloop()