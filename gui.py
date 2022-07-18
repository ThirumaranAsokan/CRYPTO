from tkinter import *
from tkinter import messagebox
import label as label
import pandas as pd

file = pd.read_csv("C:/Users/aruni/PycharmProjects/script/Bitcoin.csv")
file = file.set_index(pd.DatetimeIndex(file['Date'].values))
root = Tk()
root.geometry("700x350")
a = Entry(root,width=80,borderwidth=5)
a.pack()
a.insert(0, "Enter amount:" )
try:
    def profit_cal():
        Amount = a.get()
        if (int(Amount) ):
            but1 = Label(root,text="$"+Amount,cursor="Circle",fg="Purple",bg="Yellow")
            but1.pack()
    but = Button(root,text="Enter the Amount$:",command=profit_cal,cursor="Circle",highlightcolor="Black",width=20,bg="Pink",state ="normal")
    but.pack()
except ValueError:
    print("Enter the number in integer")
b = Entry(root, width=80, borderwidth=5)
b.pack()
b.insert(0, "Enter date:")
try:
    def profit_cal1():
        Date = b.get()
        if(str(Date)):
            but2 = Label(root, text=Date, cursor="Circle", fg="Purple",bg="Yellow", )
            but2.pack()
    but0 = Button(root,text="Enter the Date:YYYY-MM-DD",command=profit_cal1,cursor="Circle",highlightcolor="Black",width=25,bg="Pink",state="normal")
    but0.pack()
except ValueError:
    print("Enter the date format(YYYY-MM-DD)")

def but_add():
    return
but_profit=Button(root,text="profit",command=but_add,cursor="Circle",highlightcolor="Black",padx=40)
but_profit.pack()
root.mainloop()





