from tkinter import *

window = Tk()

def convert():
    miles = (entryInt.get())
    kms = miles * 1.61
    output_variable.set(f"Output: {kms} Kilometers")
window.title("Learning GUIs")
window.geometry("400x200")
title_label = Label(master= window, text="Miles to Kilometers: ", font = "Algerian 24 bold")
# in font, its font = "font fontsize bold"
title_label.pack()

# input fields

entryInt = IntVar()

input_frame = Frame(master=window)# from to put widgets into
#master is input frame for the entry and button widgets
entry = Entry(master=input_frame, textvariable= entryInt)# for entry of things
button = Button(master=input_frame,  text="Convert", command= convert)

entry.pack(side = "left", padx=10) # padding in x direction is 10 pixels 
button.pack(side="left") # not necessary to kepp it left as we have already done it with the entry field
input_frame.pack(pady= 20)


# Output
# textvariable can be used to update label dynamically
output_variable = StringVar()
output_label = Label(master= window, text= "Output: ", font="Calibri 20", textvariable= output_variable)
# if we add textvariable there then the text i.e. Output: won't be visible as textvariable would overwrite it and it can be used to dynamically change the output
output_label.pack()

window.mainloop()