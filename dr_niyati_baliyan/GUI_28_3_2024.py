from tkinter import *

window = Tk() # Tk is a class constructor for the window

window.title("tkinter demo")
window.geometry("400x400") # for size and Grid is for position
myLabel = Label(window, text="Name: ")
# grid size is to be given 
myLabel.grid(row =0, column=0)# row 1 would be below row 0 and column 1 is on the right of column 0

myEntry = Entry(window)
myEntry.grid(row=0, column=1) # if we put column=0 here then the entry field would overlap the Label that is the previously put there

def clicked():
    display = "Hello "+ myEntry.get()
    myLabel.configure(text = display)

# quit can also be used in command to exit
button = Button(window, text="Click Me", command=clicked, bg="cyan", fg = "red", width= 10)
button.grid(row=1, column=1)
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
Checkbutton(window, text='Python',variable=var_1).grid(row=2,column=1)
Checkbutton(window, text='C',variable=var_2, onvalue=1).grid(row=3,column=1)
Checkbutton(window, text='C++',variable=var_3).grid(row=4,column=1)
Checkbutton(window, text='Rust',variable=var_4).grid(row=5,column=1)
# Radio Buttons one time only one should be selected, check again
var_5 = IntVar()
var_6 = IntVar()
Radiobutton(window, text="OK", variable=var_5, value= "ok").grid(row=6,column=1)
Radiobutton(window, text="Cancel", variable=var_5, value="cancel").grid(row=7,column=1)

# print(var_2.get())
window.mainloop()