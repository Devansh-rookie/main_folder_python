from tkinter import *
from tkinter import messagebox

window = Tk()

def change_color(button):
    if button.cget('bg') == "green":
        button.config(bg="red")
    else:
        button.config(bg="green")

k = 1
for i in range(4):
    for j in range(5):
        button = Button(window, text=f"{k}", width=7, height=2, bg="green")
        button.config(command=lambda b=button: change_color(b))
        k += 1
        button.grid(row=i, column=j, padx=10, pady=4)
l=1
label1=Label(window,text="Menu",font=("Arial", 20))
label1.grid(row=i+l,column=j+1)
l+=1

text_frame = Frame(window, bg="white", width=200, height=100)
text_frame.grid(row=i+l,column=j+1)
l+=1

label1 = Label(text_frame,text="Kadhai Paneer: 150 Rupees", bg="white", height=1, width=30)
label1.grid(row=i+l,column=j+1)
l+=1

label2 = Label(text_frame,text="Palak Paneer: 300 Rupees", bg="white", height=1, width=30)
label2.grid(row=i+l,column=j+1)
l+=1

label3 = Label(text_frame,text="Butter Naan: 50 Rupees", bg="white", height=1, width=30)
label3.grid(row=i+l,column=j+1)
l+=1

label4 = Label(text_frame,text="Tawa Roti: 15 Rupees", bg="white", height=1, width=30)
label4.grid(row=i+l,column=j+1)
l+=1

label5 = Label(text_frame,text="Malai Kofta: 250 Rupees", bg="white", height=1, width=30)
label5.grid(row=i+l,column=j+1)
l+=1

label6 = Label(text_frame,text="Paneer Korma: 270 Rupees", bg="white", height=1, width=30)
label6.grid(row=i+l,column=j+1)
l+=1

label7 = Label(text_frame,text="Dal Makhni: 120 Rupees", bg="white", height=1, width=30)
label7.grid(row=i+l,column=j+1)
l+=1

label8 = Label(text_frame,text="Mix Veg: 200 Rupees", bg="white", height=1, width=30)
label8.grid(row=i+l,column=j+1)
l+=1

label9 = Label(text_frame,text="Veg Pulao: 250 Rupees", bg="white", height=1, width=30)
label9.grid(row=i+l,column=j+1)
l+=1

label10 = Label(text_frame,text="Fried rice: 300 Rupees", bg="white", height=1, width=30)
label10.grid(row=i+l,column=j+1)
l+=1

text_frame2= Frame(text_frame, width=200, height=10)
text_frame2.grid(row=i+l,column=j+1)
l+=1

label11=Label(text_frame2,text="Customer Name:",height=2, width=30,font=("Arial", 10))
label11.grid(row=i+l,column=j+1)
l+=1

text_entry=Text(text_frame2,height=1,width=50)
text_entry.grid(row=i+l,column=j+1)
l+=1

label12=Label(window,text="Enter your order:",height=2, width=30,font=("Arial", 10))
label12.grid(row=i+l,column=j+1)
l+=1

text_entry2=Text(window,height=5,width=100)
text_entry2.grid(row=i+l,column=j+1)
l+=1

button1 = Button(window, text='Reserve Table', 
                   bg='gray',width=20)
button1.grid(row=i+l,column=j+1,pady=5)
l+=1

button2 = Button(window, text='Cancel Booking', 
                   bg='gray',width=20)
button2.grid(row=i+l,column=j+1,pady=5)
l+=1

bill=Label(window,text="Total bill:",height=2, width=30,font=("Arial", 10))
bill.grid(row=i+l,column=j+1)
l+=1

text_frame3= Frame(text_frame, width=50, height=5)
text_frame3.grid(row=i+l,column=j+1)
l+=1

final=Label(window,text="520",font=("Arial", 10))
final.grid(row=i+l,column=j+1)
l+=1

window.mainloop()