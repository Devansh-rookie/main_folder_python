from tkinter import *
def change_font():
    myLabel.config(font=("Arial", 25, "bold"))

window = Tk()

window.geometry("400x400")

myLabel = Label(window, text="This is a Normal Label.")
myLabel.grid(row=0, column=0)

# myLabel2= Label(window, text="This is a formatted label.")

button = Button(window, text="Click to change", command=change_font)

button.grid(row=1, column=0)

window.mainloop()