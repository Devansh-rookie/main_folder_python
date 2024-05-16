from tkinter import *

window = Tk()

def commandPlus():
    ans = f"The answer is: {number1.get() +number2.get()}"
    outputStr.set(ans)

def commandMul():
    ans = f"The answer is: {number1.get() *number2.get()}"
    outputStr.set(ans)

def commandDiv():
    ans = f"The answer is: {number1.get() /number2.get()}"
    outputStr.set(ans)

outputStr = StringVar()
number1Frame = Frame(master=window)
number1Label = Label(master= number1Frame, text="Number 1: ", font="Arial 14 bold")
number1 = IntVar()
number1Entry = Entry(master= number1Frame, textvariable= number1)
number1Label.pack()
number1Entry.pack()

number1Frame.pack()

number2Frame = Frame(master=window)
number2Label = Label(master= number1Frame, text="Number 1: ", font="Arial 14 bold")
number2 = IntVar()
number2Entry = Entry(master= number1Frame, textvariable= number2)
number2Label.pack()
number2Entry.pack()

number2Frame.pack()

plus = Button(text= "+", font="Arial 14 bold", command=commandPlus)
mul = Button(text= "*", font="Arial 14 bold", command=commandMul)
div = Button(text= "/", font="Arial 14 bold", command=commandDiv)
plus.pack()
mul.pack()
div.pack()

Label(textvariable= outputStr, font="Arial 14 bold").pack()

window.mainloop()