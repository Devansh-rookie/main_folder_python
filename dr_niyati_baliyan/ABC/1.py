import tkinter as tk
from tkinter import messagebox

i = 1
discount = 0
bill = None
billnet = None
discount_label = None



def enable_order():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
        entry.config(state=tk.NORMAL)

def disable_order():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
        entry.config(state=tk.DISABLED)

def clear_entries():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
        entry.delete(0, tk.END)

def clear_bill_labels():
    global bill, billnet, discount_label
    if bill:
        bill.destroy()
    if discount_label:
        discount_label.destroy()
    if billnet:
        billnet.destroy()

def calculate():
    global discount, bill, discount_label, billnet
    
    dic = {
        'Aloo Paratha': [entry1, 30],
        'Samosa': [entry2, 15],
        'Pizza': [entry3, 150],
        'Gulab Jamun': [entry4, 35],
        'Chowmein': [entry5, 70],
        'Churma': [entry6, 200]
    }
    total = 0
    net = 0
    for key, val in dic.items():
        if val[0].get() != "":
            total = total + int(val[0].get()) * val[1]
    if total >= 500:
        discount = 5
    elif total >= 1000:
        discount = 10
    else:
        discount = 1
    
    
    clear_bill_labels()
    
    bill = tk.Label(root, text="Total Bill: Rs. " + str(total), font=('arial', 14))
    bill.pack(pady=5)
    
    
    discount_label = tk.Label(root, text="Discount: " + str(discount) + "%", font=('arial', 14))
    discount_label.pack(pady=5)
   

    net = total - (total * discount) / 100
    
    
    billnet = tk.Label(root, text="Net Amount: Rs. " + str(net), font=('arial', 16), fg="blue")
    billnet.pack(pady=10)
def leave_table():
    global i
    if(i>2):
      i=i-1
      showtable.config(text="Table no. " + str(i-1) + " is available", bg="lightgreen", fg="black")
      enable_order()
      clear_entries()
      
    else:
        messagebox.showinfo(title="Already empty", message="All tables are already empty")
        

def checktable():
    global i, showtable
    if i <= 20:
        showtable.config(text="Table no. " + str(i) + " is available", bg="lightgreen", fg="black")
        enable_order() 
        clear_entries()  
        i += 1
    else:
        showtable.config(text="No Tables Available!", bg="red", fg="white")
        disable_order() 


root = tk.Tk()
root.configure(background="lightgrey")
root.geometry('800x800')
root.title("Naveen Restaurant")


def change_color(button):
    if button.cget('bg') == "green":
        button.config(bg="red")
    else:
        button.config(bg="green")

k = 1
for i in range(4):
    for j in range(5):
        button = tk.Button(root, text=f"{k}", width=2, height=2, bg="green")
        button.config(command=lambda b=button: change_color(b))
        k += 1
        button.place(x=5+55*j, y=10+50*i)


tablecheck = tk.Button(root, text="Check for available tables", font=("arial", 16), command=checktable)
tablecheck.pack(pady=8, padx=20)


showtable = tk.Label(root, bg="lightgrey", fg="purple", font=("arial", 18), text="")
showtable.pack(pady=8, padx=10)


label1 = tk.Label(root, text="Menu", bg="lightgreen", font=("arial", 24))
label1.pack(padx=10, pady=8)


menu_items = [
    ("Aloo Paratha", 30),
    ("Samosa", 15),
    ("Pizza", 150),
    ("Gulab Jamun", 35),
    ("Chowmein", 70),
    ("Churma", 200)
]

for item, price in menu_items:
    label = tk.Label(root, bg="lightgreen", text=f"{item} - Rs. {price}", font=("arial", 16))
    label.pack()


asking = tk.Label(root, text="Select your order", font=("arial", 18))
asking.pack(pady=10)


entry1 = tk.Entry(root, state=tk.DISABLED)
entry1.pack(pady=5)
entry2 = tk.Entry(root, state=tk.DISABLED)
entry2.pack(pady=5)
entry3 = tk.Entry(root, state=tk.DISABLED)
entry3.pack(pady=5)
entry4 = tk.Entry(root, state=tk.DISABLED)
entry4.pack(pady=5)
entry5 = tk.Entry(root, state=tk.DISABLED)
entry5.pack(pady=5)
entry6 = tk.Entry(root, state=tk.DISABLED)
entry6.pack(pady=5)


generate_bill_btn = tk.Button(root, text="Generate Bill", font=("arial", 18), command=calculate)
generate_bill_btn.pack(pady=10)
leave_table_btn = tk.Button(root, text="Leave the Table", font=("arial", 16), command=leave_table)
leave_table_btn.pack(pady=8)
root.mainloop()