import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pyqrcode

import cx_Oracle

# connection = cx_Oracle.connect('experiment/experiment@127.0.0.1:1521/xe')
# cur = connection.cursor()

root = Tk()
root.title("Company-details")
root.geometry("800x500")
root['background'] = '#856ff8'
connection = cx_Oracle.connect('database2/password@127.0.0.1:1521/xe')
cur = connection.cursor()
cur.execute("SELECT * FROM PRODUCT_TABLE")
records = cur.fetchall()
print(records)

global e1
global e2
global e3
global e4
global e5
global e6
global e7
global P_i_d
global i_d
def Add():
        product_name = e1.get()
        product_type= e2.get()
        brand = e3.get()
        catagory = e4.get()
        mfd = e5.get()
        exp_d = e6.get()
        price = e7.get()
        product_id=int(P_i_d.get())
        comp_id=int(i_d.get())
        querry="insert into product_table(PRODUCT_ID,PRODUCT_NAME,PRODUCT_TYPE,BRAND,COMP_ID,CATAGORY,MFD,EXP_D,PRICE)VALUES(%s,'%s','%s','%s',%s,'%s','%s','%s',%s)"
        values=(product_id,product_name,product_type,brand,comp_id,catagory,mfd,exp_d,price)
        print(querry % values)
        cur.execute(querry % values)
        cur.execute("commit")
        print("sucess")

def generate_QR():
    if len(user_input.get()) != 0:
        global qr, img
        qr = pyqrcode.create(user_input.get()+e1.get()+" "+i_d.get()+" "+P_i_d.get())
        img = BitmapImage(data=qr.xbm(scale=5))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
        Add()
    except:
        pass


def display_code():
    img_lbl.config(image=img)
    #output.config(text="QR code of " + user_input.get()+e1.get()+e2.get()+e3.get()+e4.get()+e5.get()+e6.get()+e7.get())

def update():
    print("update")
def delete():
    print("delete")

tk.Label(root, text="Product Name",width=15).place(x=10, y=10)
Label(root, text="Product Type",width=15).place(x=10, y=40)
Label(root, text="Brand Name",width=15).place(x=10, y=70)
Label(root,text="Category",width=15).place(x=10,y=100)
Label(root, text="Mfd",width=15).place(x=10, y=130)
Label(root,text="Exp Date",width=15).place(x=10,y=160)
Label(root,text="Price",width=15).place(x=10,y=190)
Label(root,text="Product_id",width=15).place(x=10,y=220)
Label(root,text="Company_id",width=15).place(x=10,y=250)

img_lbl = Label(root,bg='white')
# img_lbl.pack()
img_lbl.place(x=380,y=50)
output = Label(root,text="",bg='white')
output.place(x=400,y=230)
user_input = StringVar()
e1 = Entry(root,textvariable=user_input)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)

e6 = Entry(root)
e6.place(x=140, y=160)

e7 = Entry(root)
e7.place(x=140, y=190)

P_i_d= Entry(root)
P_i_d.place(x=140,y=220)

i_d= Entry(root)
i_d.place(x=140,y=250)

Button(root, text="Add", height=2, width=13,command=generate_QR).place(x=30, y=290)

cols = ('PID','ProductName','Brand','Catagory', 'mfd', 'Price','customer')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
        listBox.heading(col, text=col)
        # listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=350)

    # listBox.bind('<Double-Button-1>', GetValue)
    #############################
for i, (comp_id, product_id, product_name, product_type, Brand, catagory, MFD, EXP_D, Price, is_valid,customer) in enumerate(
            records, start=1):
        listBox.insert("", "end", values=(product_id, product_name, Brand,catagory, MFD, Price,customer))

root.mainloop()