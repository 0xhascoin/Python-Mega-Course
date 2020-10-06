from tkinter import *

window = Tk()

def convert_kg():
    kg = float(e1_val.get())

    to_grams = kg * 1000
    to_pounds = kg * 2.205
    to_ounces = kg * 35.274

    grams.delete("1.0", END)
    grams.insert(END, str(to_grams) + ' grams')

    pounds.delete("1.0", END)
    pounds.insert(END, str(to_pounds) + ' pounds')

    ounces.delete("1.0", END)
    ounces.insert(END, str(to_ounces) + ' ounces')

e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

b1 = Button(window, text='Convert', command=convert_kg)
b1.grid(row=0, column=2)

e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0 , column=1)


grams = Text(window, height=1, width=20)
grams.grid(row=1, column=0)

pounds = Text(window, height=1, width=20)
pounds.grid(row=1, column=1)

ounces = Text(window, height=1, width=20)
ounces.grid(row=1, column=2)


window.mainloop()

