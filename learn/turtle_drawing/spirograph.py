import turtle
import random
t= turtle.Turtle()
t.speed(0)
n=100
t.pensize(2)
t.screen.bgcolor("black")
# colors= ['brown', 'white', 'red', 'blue', 'orange', 'teal', 'purple', 'yellow', 'pink']
turtle.colormode(255)  # Set color mode to use 0-255 RGB values
# turtle.pencolor(255, 0, 0)
# len_col = len(colors)
for i in range(n):
    # t.color(colors[i%len_col])
    t.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
    t.circle(100)
    t.left((360/(n)))

turtle.mainloop()