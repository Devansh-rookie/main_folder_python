import turtle

t = turtle.Turtle()
def print_points(a,b):
    t.goto(a[0],a[1])
    t.write(f"({a[0]}, {a[1]})", font=("Arial", 20))
    t.goto(b[0],b[1])
    t.write(f"({b[0]},{b[1]})",font=("Arial", 20))
    t.goto((a[0]+b[0])/2,(a[1]+b[1])/2)
    t.write(f"({(a[0]+b[0])/2},{(a[1]+b[1])/2})",font=("Arial", 20))
# while(True):
print_points((10,10),(100,100))
turtle.mainloop()