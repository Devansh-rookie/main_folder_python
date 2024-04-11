import turtle
import random
tim = turtle. Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange','black']
# set colors for turtle
tim.color ('black', 'red') # first color is the pen color/outline color which writes and the second color is the fill-up color which fills the shape

# set pen width
tim.width (5)
# Fill in shape with color
tim.begin_fill()
tim.circle (50)
tim. end_fill()

tim.penup()
tim.forward(100) # to the right basically
tim.pendown()

tim.color("navy", "teal")

tim.begin_fill()
for i in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()
turtle.Screen().exitonclick()