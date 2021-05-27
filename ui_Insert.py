from tkinter import *


def add():
    print("Hello")

root = Tk()

l1 = Label(root, text="Name: ")
l1.grid(row=0, column=0)

var1 = StringVar()
e1 = Entry(root, textvariable=var1)
e1.grid(row=0, column=1)

l2 = Label(root, text="Family: ")
l2.grid(row=1, column=0)

var2 = StringVar()
e2 = Entry(root, textvariable=var2)
e2.grid(row=1, column=1)

l3 = Label(root, text="Age: ")
l3.grid(row=2, column=0)

var3 = StringVar()
e3 = Entry(root, textvariable=var3)
e3.grid(row=2, column=1)

b1 = Button(root, text="Register", command=add)
b1.grid(row=3, column=0, columnspan=2, sticky='we')
root.mainloop()