
import cx_Oracle
import cv2
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
from tkinter import ttk
import pyqrcode
################################# Data - base [ oracle ] connection ########################

# create a connection
connection = cx_Oracle.connect('database2/password@127.0.0.1:1521/xe')

# crate cursor object for executon of querries
cur = connection.cursor()


########################## Scanner Code #####################################

# this func return scanned data from the qr code
def qr_code_data():
  cap = cv2.VideoCapture(0)
  detector = cv2.QRCodeDetector()
  while True:
    _,img=cap.read()
    data,one,_=detector.detectAndDecode(img)
    if data:
        cap.release()
        print(data)
        return data
    cv2.imshow('qr_code',img)
    if cv2.waitKey(1)==ord('q'):
         break

############################### FRONT-END ############################
def Sucess():
    messagebox.showwarning("Registered SucessFully")
def Company():
        def Close():
            window.destroy()

        window = Tk(className='Python Examples - Window Color')
        window.title('Company_Reg')
        window.geometry('800x600')
        window.maxsize(800, 600)
        window['background'] = '#856ff8'

        Cname = Label(window, text="Company-Name ").place(relx=0.1, rely=0.1)
        Name = Entry(window, width=25, font=('Arial 12'))  # .place(relx=0.3, rely=0.2)
        Name.place(relx=0.1, rely=0.16)
        E_mail = Label(window, text="Email").place(relx=0.1, rely=0.22)
        Email = Entry(window, width=25, font=('Arial 12'))  # .place(relx=0.3, rely=0.3)
        Email.place(relx=0.1, rely=0.28)
        P_hone = Label(window, text="Phone").place(relx=0.6, rely=0.22)
        Phone = Entry(window, width=25, font=('Arial 12'))  # .place(relx=0.3, rely=0.4)
        Phone.place(relx=0.6, rely=0.28)
        Address = Entry(window, width=25, font=('Arial 12'))#.place(relx=0.1, rely=0.40)
        Address.place(relx=0.1,rely=0.40)
        a_ddress = Label(window, text="Address").place(relx=0.1, rely=0.34)
        C_ity = Label(window, text="City").place(relx=0.1, rely=0.46)
        City = Entry(window, width=25, font=('Arial 12'))  # .place(relx=0.3, rely=0.5)
        City.place(relx=0.1, rely=0.52)
        z_ip = Label(window, text="Zip").place(relx=0.6, rely=0.46)
        Zip = Entry(window, width=25, font=('Arial 12'))  # .place(relx=0.3, rely=0.6)
        Zip.place(relx=0.6, rely=0.52)

        u_name = Label(window, text="User-Name").place(relx=0.1, rely=0.58)
        Username = Entry(window, width=25, font=('Arial 12'))  # .place(relx=0.3, rely=0.6)
        Username.place(relx=0.1, rely=0.64)

        passw = Label(window, text="Password").place(relx=0.1, rely=0.70)
        Password = Entry(window, show='*', width=25, font=('Arial 12'))  # .place(relx=0.3, rely=0.6)
        Password.place(relx=0.1, rely=0.76)
    ##############################################################################
        def get_name():
            global name
            name = Name.get()


        def get_email():
            global email
            email = Email.get() #1.0, "end-1c"

        def get_phone():
            global phone_no
            phone_no = Phone.get()

        def get_address():
            global address
            address = Address.get()

        def get_city():
            global city
            city=City.get()

        def get_zip():
            global zip
            zip=Zip.get()

        def get_username():
            global user_name
            user_name = Username.get()

        def get_password():
            global password
            password = Password.get()

        def comp_reg():
            print("inserting in company database")
            querry1="insert into comp_login(name,email,phone_no,username,password,address,city,zip,id) values(" +"'"+str(name)+"',"+"'"+ email+ "',"+str(phone_no)+"," + "'"+str(user_name)+"',"+"'"+str(password)+"','"+str(address)+"',"+"'"+str(city)+"',"+str(zip)+",seq_id.nextval)"
            cur.execute(querry1)
            cur.execute("commit")
            print("committed")
            messagebox.showinfo("success","Sucessfully registered !!")
            Close()

        def get_val():
            get_name()
            get_email()
            get_phone()
            get_username()
            get_password()
            get_zip()
            get_address()
            get_city()
            comp_reg()




        b1 = customtkinter.CTkButton(window, text="Register", fg_color='blue', hover_color="#87CEFA",text_color='white',
                                text_font="lucida 12 italic bold",
                                     corner_radius=12,command=get_val)
        b1.place(relx=0.2, rely=0.88)
        b = customtkinter.CTkButton(window, text="exit",fg_color='blue',hover_color="#87CEFA",text_color='white',
                                text_font="lucida 12 italic bold",
                                     corner_radius=12, command=Close)
        b.place(relx=0.6, rely=0.88)

def User():
    def Close():
        win.destroy()

    win = Tk()
    win.title('User_Reg')

    win.geometry('548x400')
    win.maxsize(548, 400)
    win['background'] = '#856ff8'

    # l3 = Label(win, text="USER details", font="lucida 13", fg="White", bg="Black", padx=2, pady=3,
    #            justify='center')
    # l3.place(relx=0.2, rely=0.1)
    Cname = Label(win, text="Name ").place(relx=0.1, rely=0.2)
    Name = Entry(win,width=20, font=('Arial 12'))
    Name.place(relx=0.3, rely=0.2)
    E_mail = Label(win, text="Email").place(relx=0.1, rely=0.3)
    Email = Entry(win, width=20, font=('Arial 12'))
    Email.place(relx=0.3, rely=0.3)
    P_hone = Label(win, text="Phone").place(relx=0.1, rely=0.4)
    Phone = Entry(win, width=20, font=('Arial 12'))
    Phone.place(relx=0.3, rely=0.4)
    u_name = Label(win, text="UserName").place(relx=0.1, rely=0.5)
    Username = Entry(win,width=20, font=('Arial 12'))
    Username.place(relx=0.3, rely=0.5)
    passw = Label(win, text="Password").place(relx=0.1, rely=0.6)
    Password = Entry(win,show='*', width=20, font=('Arial 12'))
    Password.place(relx=0.3, rely=0.6)

    #########################################################################
    def get_name():
        global name
        name = Name.get()

    def get_email():
        global email
        email = Email.get()

    def get_phone():
        global phone_no
        phone_no = Phone.get()

    def get_username():
        global user_name
        user_name = Username.get()

    def get_password():
        global password
        password = Password.get()

    def user_reg():
        print("inserting in user database")
        querry1 = "insert into user_login(name,email,phone_no,username,password) values(" + "'" + str(
            name) + "'," + "'" + email + "'," + str(phone_no) + "," + "'" + str(user_name) + "'," + "'" + str(
            password) + "')"
        cur.execute(querry1)
        cur.execute("commit")
        messagebox.showinfo("success", "Sucessfully registered !!")
        close()


    def get_val():
        get_name()
        get_email()
        get_phone()
        get_username()
        get_password()
        user_reg()


    b1 = customtkinter.CTkButton(win, text="Register", fg_color='blue', hover_color="#87CEFA",text_color='white',
                                text_font="lucida 12 italic bold",
                                 corner_radius=12,command=get_val)
    b1.place(relx=0.2, rely=0.7)
    b = customtkinter.CTkButton(win, text="exit", fg_color='blue', hover_color="#87CEFA",text_color='white',
                                text_font="lucida 12 italic bold",
                                corner_radius=12, command=Close)
    b.place(relx=0.55, rely=0.7)

def Scanner():
    win = Tk()
    win.title('User_Login')
    def close():
        win.destroy()

    win.geometry('550x100')
    win.maxsize(500, 100)
    win['background'] = '#F4ABAA'
    btn = customtkinter.CTkButton(win, text="SCAN", fg_color='blue', hover_color="#87CEFA", text_color='white',
                                text_font="lucida 12 italic bold", corner_radius=12,command=main_)
    btn.place(relx=0.1, rely=0.3)
    btn = customtkinter.CTkButton(win, text="Exit", fg_color='blue', hover_color="#87CEFA", text_color='white',
                                  text_font="lucida 12 italic bold", corner_radius=12,command=close)
    btn.place(relx=0.5, rely=0.3)

def InvalidDetails():
    messagebox.showwarning("invalid details","invalid details")
    #### ended

def pro_win(comp_id):
    print(type(comp_id))
    wid = Tk()
    wid.title("Company-details")
    wid.geometry("1600x1600")
    # wid.attributes('-fullscreen',true)
    wid['background'] = '#856ff8'
    ###########################
    connection = cx_Oracle.connect('database2/password@127.0.0.1:1521/xe')
    cur = connection.cursor()
    # cur.execute("SELECT * FROM comp_login")
    cur.execute("SELECT * FROM PRODUCT_TABLE WHERE COMP_ID=%s" %comp_id )
    records = cur.fetchall()
    print(records)
    #############################3
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7

    def Add():
        product_name = e1.get()
        product_type=e2.get()
        brand = e3.get()
        catagory = e4.get()
        mfd = e5.get()
        exp_d=e6.get()
        price=e7.get()
        querry="insert into product_table(PRODUCT_ID,PRODUCT_NAME,PRODUCT_TYPE,BRAND,COMP_ID,CATAGORY,MFD,EXP_D,PRICE)VALUES(seq_pro.nextval,'%s','%s','%s','%s','%s','%s','%s',%s)"
        values=(product_name,product_type,brand,comp_id,catagory,mfd,exp_d,price)
        print(values)
        cur.execute(querry % values)
        cur.execute("commit")
        print("sucess")

    def generate_QR():
        if len(e1.get()) != 0:
            global qr, img
            qr = pyqrcode.create(user_input.get() + e3.get())
            #img = BitmapImage(data=qr.xbm(scale=5))
            qr.png('qrcodes_img/%s'%str(e1.get())+'.png',scale=6)
            print("here it is ",e1.get())
            #image = Image.open(img)
            img = ImageTk.PhotoImage(Image.open(r'C:\Users\Diwakar\Desktop\mca\Project\qrcodes_img\%s.png'%e1.get()))
            img_lbl.config(image=img)
            output.config(text="QR code of " + e1.get())
        # else:
        #     messagebox.showwarning('warning', 'All Fields are Required!')

    l1 = Label(wid, text="Product Name", width=15)
    l1.place(x=10, y=10)
    l2 = Label(wid, text="Product Type", width=15)
    l2.place(x=10, y=40)
    l3 = Label(wid, text="Brand Name", width=15)
    l3.place(x=10, y=70)
    l4 = Label(wid, text="Category", width=15)
    l4.place(x=10, y=100)
    l5 = Label(wid, text="Mfd", width=15)
    l5.place(x=10, y=130)
    l6 = Label(wid, text="Exp Date", width=15)
    l6.place(x=10, y=160)
    l7 = Label(wid, text="Price", width=15)
    l7.place(x=10, y=190)
    img_lbl = Label(wid, bg='red')
    img_lbl.pack()
    img_lbl.place(x=380, y=50)
    output = Label(wid, text="", bg='red')
    output.pack()
    output.place(x=430, y=230)
    user_input = StringVar()
    e1 = Entry(wid, textvariable=user_input)
    e1.place(x=140, y=10)

    e2 = Entry(wid)
    e2.place(x=140, y=40)

    e3 = Entry(wid)
    e3.place(x=140, y=70)

    e4 = Entry(wid)
    e4.place(x=140, y=100)

    e5 = Entry(wid)
    e5.place(x=140, y=130)

    e6 = Entry(wid)
    e6.place(x=140, y=160)

    e7 = Entry(wid)
    e7.place(x=140, y=190)
    # user_input = StringVar()
    # entry = Entry(root,textvariable=user_input)
    # entry.pack(padx=10,pady=10)
    def add_print():
        # Add()
        generate_QR()

    Button(wid, text="Add", height=2, width=13, command=add_print).place(x=30, y=250)
    # c =Canvas(root,width=200,height=150)
    # c.configure(bg="teal")
    # c.place(relx=0.48,rely=0.1)

    cols = ('PID','ProductName','Brand','Catagory', 'mfd','Price','Customer')
    listBox = ttk.Treeview(wid, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)
        # listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=350)

    # listBox.bind('<Double-Button-1>', GetValue)
    #############################
    for i, (comp_id, product_id, product_name, product_type, Brand, catagory, MFD, EXP_D, Price, is_valid,customer) in enumerate(
            records, start=1):
        listBox.insert("", "end", values=(product_id, product_name,Brand,catagory, MFD, Price,customer))

    wid.mainloop()

def CmpLog():
    win = Tk()
    win.title('Cmp_Login')

    win.geometry('548x400')
    win.maxsize(548, 400)
    win['background'] = '#FFFFC1'
    c = Canvas(win, width=420, height=280)
    c.configure(bg="teal")
    c.place(relx=0.1, rely=0.1)
    name = Label(win, text="User - Name ").place(relx=0.16, rely=0.2)
    Username = Entry(win, width=20, font=('Arial 12'))
    Username.place(relx=0.16, rely=0.3)
    passw = Label(win, text="Password").place(relx=0.16, rely=0.4)
    Password = Entry(win, show='*', font=('Arial 12'))
    Password.place(relx=0.16, rely=0.5)
    # b = customtkinter.CTkButton(win, text="LOGIN", fg_color='salmon', hover_color="#87CEFA", text_color='white',
    #                             text_font="lucida 12 italic bold", command=Scanner)
    # b.place(relx=0.16, rely=0.6)
#############################################################################
    def get_username():
        global user_name
        user_name = Username.get()

    def get_password():
        global password
        password = Password.get()

    def comp_validation():
        cur.execute("select * from comp_login where username="+"'" + str(user_name) +"'" +" and password=" +"'"+ str(password)+"'")
        if cur.fetchall():
            return True
        return False

    def get_comp_id():
        global comp_id
        cur.execute("select id from comp_login where username="+"'" + str(user_name) +"'" +" and password=" +"'"+ str(password)+"'")
        comp_id=cur.fetchall()[0][0]

    def check_cred():
        get_username()
        get_password()
        if comp_validation():
            print("Sucessfully loged in")
            win.destroy()
            get_comp_id()
            pro_win(comp_id)
        else:
            print("wrong_cred")
            win.destroy()
            InvalidDetails()



    b = customtkinter.CTkButton(win, text="LOGIN", fg_color='salmon', hover_color="#87CEFA",text_color='white',
                                text_font="lucida 12 italic bold",command=check_cred)
    b.place(relx=0.16, rely=0.6)


def UserLog():
    win = Tk()
    win.title('User_Login')

    win.geometry('548x400')
    win.maxsize(548, 400)
    win['background'] = '#FFFFC1'
    c = Canvas(win, width=420, height=280)
    c.configure(bg="teal")
    c.place(relx=0.1, rely=0.1)
    name = Label(win, text="User - Name ").place(relx=0.16, rely=0.2)
    Username = Entry(win, width=20, font=('Arial 12'))
    Username.place(relx=0.16, rely=0.3)
    passw = Label(win, text="Password").place(relx=0.16, rely=0.4)
    Password = Entry(win, show='*', font=('Arial 12'))
    Password.place(relx=0.16, rely=0.5)
    # b = customtkinter.CTkButton(win, text="LOGIN", fg_color='salmon', hover_color="#87CEFA", text_color='white',
    #                             text_font="lucida 12 italic bold", command=Scanner)
    # b.place(relx=0.16, rely=0.6)
##################################################################################
    def get_username():
        global user_name
        user_name = Username.get()

    def get_password():
        global password
        password = Password.get()

    def user_validation():
        cur.execute("select * from user_login where username="+"'" + str(user_name) +"'" +" and password=" +"'"+ str(password)+"'")
        print(user_name, password)
        if cur.fetchall():
            global U_id
            cur.execute(
                "select username from user_login where username=" + "'" + str(user_name) + "'" + " and password=" + "'" + str(
                    password) + "'")
            U_id=cur.fetchall()[0][0]
            #print(U_id)
            return True
        return False


    def check_cred():
        get_username()
        get_password()
        if user_validation():
            print("logged in sucessFully")
            win.destroy()
            Scanner()
        else:
            print("wrong_cred")
            win.destroy()
            InvalidDetails()

    b = customtkinter.CTkButton(win, text="LOGIN", fg_color='salmon', hover_color="#87CEFA",text_color='white',
                               text_font="lucida 12 italic bold",command=check_cred)
    b.place(relx=0.16, rely=0.6)


def start():
    root = Tk()

    root.title('Real/FakeProductIdentifier')
    img = Image.open('digi.jpg')
    bg = ImageTk.PhotoImage(img)
    root.geometry('800x600')
    root.maxsize(800, 800)
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    #add image
    label = Label(root, image=bg)
    label.place(x=0, y=0)

    # b1 = Button(root,text="Login As a User",font="lucida 10")
    # b1.place(relx=0.15,rely=0.4)
    b1 = customtkinter.CTkButton(root,text="Company-Registration ",fg_color='purple',hover_color="#87CEFA",text_font="lucida 18 italic bold",text_color='white',command=Company)
    b1.place(relx=0.02,rely=0.2)
    b2 = customtkinter.CTkButton(root,text=" User-Registration ",fg_color='purple',hover_color="#87CEFA",text_color='white',text_font="lucida 18 italic bold",command=User)
    b2.place(relx=0.02,rely=0.34)
    b3 = customtkinter.CTkButton(root,text="  Company-Login  ",fg_color='purple',text_color='white',hover_color="#87CEFA",text_font="lucida 18 italic bold",command=CmpLog)
    b3.place(relx=0.02,rely=0.46)
    b3 = customtkinter.CTkButton(root,text="     User-Login       ",fg_color='purple',hover_color="#87CEFA",text_font="cursive 18 italic bold",text_color='White',command=UserLog)
    b3.place(relx=0.02,rely=0.58)
    root.mainloop()

def is_in_database(data):
    querry="select * from product_table where product_id=%s and (is_valid=0 or (is_valid=1 and customer='%s'))"
    cur.execute(querry % (data,U_id))
    if cur.fetchall():
        #cur.execute("select * from product_table where product_id=%s and is_valid=0")
        # if cur.fetchall():
        #     return T1
        # else:
        #     return T2
        return True
    else:
        return False


###############################################
def main_() :
    # using try catch block because some time qr_code_data return string value which can not be converted to int
    try:
        Data=qr_code_data()
        lst=Data.split()
        pid=int(lst[2])
    except:
        messagebox.showwarning("UNKNOWN", "THIS PRODUCT IS UNKNOWN !!")

    check=is_in_database(pid)
    if check:
        messagebox.showinfo("Real","THIS PRODUCT IS REAL")
        cur.execute("UPDATE PRODUCT_TABLE SET IS_VALID=1 WHERE PRODUCT_ID=%s" % pid)
        cur.execute("UPDATE PRODUCT_TABLE SET CUSTOMER='%s' WHERE PRODUCT_ID=%s" % (U_id,pid))
        cur.execute("COMMIT")
        ##############################
    # elif check=='T2':
    #     messagebox.showinfo("Real", "!!Beaware if u  are rescannnig this product its REAL /n if scanning for first time its FAKE")
    #     messagebox.showinfo("ON progress","Work on progress")
    else:
        messagebox.showwarning("FAKE","THIS PRODUCT IS FAKE !!!")
        messagebox.showinfo("ON progress", "Work on progress")

################### Execution ###################

# start()
#Scanner()
#print(U_id)
pro_win(21)