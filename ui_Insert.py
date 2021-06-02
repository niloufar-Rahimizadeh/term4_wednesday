from tkinter import *
import pymysql


con = pymysql.connect(host="localhost", user="poulstar", password="poulstar", database="my_db_n")

def add():
    sql = "INSERT INTO users1(name, family, age) VALUES(%s,%s,%s)"
    data =(var1.get(), var2.get(), var3.get())
    try:
        with con.cursor() as cr:
            cr.execute(sql, data)
            con.commit()
    except:
        print("Access denied!")

def update():
    sql = "UPDATE users1 SET `family`= 'Rahimizadeh' WHERE `name`='Amir'"
    try:
        with con.cursor() as cr:
            cr.execute(sql)
            con.commit()
    except:
        print("Access denied!")    

def delete():
    pass

def select():
    pass

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

b2 = Button(root, text="Update", command=update)
b2.grid(row=4, column=0, columnspan=2, sticky='we')

b3 = Button(root, text="Delete", command=delete)
b3.grid(row=5, column=0, columnspan=2, sticky='we')

b4 = Button(root, text="Select", command=select)
b4.grid(row=6, column=0, columnspan=2, sticky='we')

root.mainloop()