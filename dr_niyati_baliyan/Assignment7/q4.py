from tkinter import *

window = Tk()

# window.minsize(400,400)# this sets the minimum size of the window size can't be reduced from it but can be increased

# OR
a= 400
b = 300
window.geometry(f"{a}x{b}")

window.mainloop()