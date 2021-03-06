from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import backend
from datetime import date
import os
from PIL import ImageTk
from tkcalendar import *
import sqlite3
from unicodedata import name

def main():
    root = Tk()

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("__Login__")
        self.root.geometry("1350x700+0+0")

        def login():
            global name1
            username1 = username.get()
            password1 = password.get()
            txtuser.delete(0, END)
            txtpass.delete(0, END)

            list_of_files = os.listdir()
            if username1 in list_of_files:
                file1 = open(username1, "r")
                verify = file1.read().splitlines()
                if password1 in verify:
                    con = sqlite3.connect('lib.db')
                    cur = con.cursor()
                    cur.execute('SELECT NAME FROM LIBRARIAN WHERE USERNAME = ?',(username1,))
                    name1 = cur.fetchall()
                    con.commit()
                    con.close()
                    tkinter.messagebox.showinfo('Success','Login Successful')
                    self.newWindow = Toplevel(self.root)
                    self.app = Lib_system(self.newWindow)

                else:
                    tkinter.messagebox.showerror('Failed','Wrong Password')

            else:
                tkinter.messagebox.showerror('Failed','User not found, please reegister!')




        def register():

            global register_screen
            register_screen = Toplevel()
            register_screen.title("Register")
            register_screen.geometry("1350x750+0+0")

            global username
            global password
            global name
            global mob_no
            global email
            global mem
            username = StringVar()
            password = StringVar()
            name = StringVar()
            mob_no = IntVar()
            email = StringVar()

            Label(register_screen, text="Please enter details below",font=('Constantia',35,'bold','italic'),fg='black').pack()
            Label(register_screen, text="").pack()

            username_lable = Label(register_screen, text="Username * ",font=('Constantia',18,'bold','italic'))
            username_lable.pack()
            username_entry = Entry(register_screen, textvariable=username,font=('Constantia',18,'bold','italic'))
            username_entry.pack()

            password_lable = Label(register_screen, text="Password * ",font=('Constantia',18,'bold','italic'))
            password_lable.pack()
            password_entry = Entry(register_screen, textvariable=password, show='*',font=('Constantia',18,'bold','italic'))
            password_entry.pack()

            name_lable = Label(register_screen,text='Name',font=('Constantia',18,'bold','italic'))
            name_lable.pack()
            name_entry = Entry(register_screen,textvariable = name,font=('Constantia',18,'bold','italic'))
            name_entry.pack()

            mobile_lable = Label(register_screen,text='Mobile Number',font=('Constantia',18,'bold','italic'))
            mobile_lable.pack()
            mobile_entry = Entry(register_screen,textvariable=mob_no,font=('Constantia',18,'bold','italic'))
            mobile_entry.pack()

            mail_lable = Label(register_screen,text='E-Mail',font=('Constantia',18,'bold','italic'))
            mail_lable.pack()
            mail_entry = Entry(register_screen,textvariable=email,font=('Constantia',18,'bold','italic'))
            mail_entry.pack()

            mobile_entry.delete(0,END)

            Label(register_screen, text="").pack()
            Button(register_screen, text="Register", width=10, height=1, bg="black",fg='white', command = register_user).pack()



        def register_user():
            username_info = username.get()
            password_info = password.get()
            if len(username_info) > 0 and len(password_info)>0 and len(name.get())>0 and len(str(mob_no.get()))>0 and len(email.get())>0:
                file = open(username_info, "w")
                file.write(username_info + "\n")
                file.write(password_info)
                file.close()
                txtuser.delete(0, END)
                txtpass.delete(0, END)

                backend.insert(name.get(),mob_no.get(),email.get(),username.get(),password.get())

                tkinter.messagebox.showinfo('Succcess','Registration Successful!!')
                register_screen.destroy()


        def disp(s,m):
                list1=Text(s,font=("arial 15"))
                list1.place(relx=0.14,rely=0.34,relheight=0.6,relwidth=0.6)
                con=sqlite3.connect('lib.db')
                list1.insert(END,"=====================================================\n")
                list1.insert(END,"   BOOK NAME\t\tBOOK ID\t\tISSUE DATE\t\tFINE    \n")
                list1.insert(END,"-------------------------------------------------------------------------------------------\n")

                cur=con.cursor()
                cur.execute('''PRAGMA foreign_keys = ON''')
                cur.execute("SELECT BK_NAME,ISSSUE,FINE FROM LIBRARY WHERE MEM_NAME=(SELECT NAME FROM MEMBER WHERE MEM_ID = ?)",(m,))
                val = cur.fetchone()

                cur.execute("SELECT ISSUE_BK_ID FROM ISSUE WHERE ISSUE_MEM_ID=?",(m,))
                val2 = cur.fetchone()
                list1.insert(END,f"""   {val[0]}\t\t{val2[0]}\t\t{val[1]}\t\t{val[2]}""")


                con.commit()
                con.close()




        def std_login():
                s = Toplevel()
                s.title('Member Info')
                s.geometry('1080x500')
                mem_id = Label(s,text="Enter your member id:",font=('Constantia',18,'bold','italic'),padx=5,pady=5)
                mem_id.grid(row=0,column=0,padx=25,pady=25)
                txt_mem_id = Entry(s,textvariable=mem,font=('Constantia',18,'bold','italic'))
                txt_mem_id.grid(row=0,column=2)
                btn_srch = Button(s,text='Search',font=('Constantia',18,'bold','italic'),command=lambda:disp(s,mem.get()))
                btn_srch.grid(row=2,column=2)
                txt_mem_id.delete(0,END)



        def iExit():
            self.iExit = tkinter.messagebox.askyesno('Login Systems','Confirm if you want to exit')
            if self.iExit > 0:
                self.root.destroy()
            else :
                return

#=====================================all images======================================
        #add image path instead of the path i have used
        self.bg_icon=ImageTk.PhotoImage(file="C:/Users/Darshan/OneDrive/Desktop/login/login1.jpg")
        self.user_icon=ImageTk.PhotoImage(file="C:/Users/Darshan/OneDrive/Desktop/lib1.jpg")
        self.username_icon=ImageTk.PhotoImage(file="C:/Users/Darshan/OneDrive/Desktop/login/username_icon.jpg")
        self.password_icon=ImageTk.PhotoImage(file="C:/Users/Darshan/OneDrive/Desktop/login/password_icon.jpg")
#===============Variables=====================
        global username
        global password

        username=StringVar()
        password=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon)
        bg_lbl.pack()
        title=Label(self.root,text="LIBRARY LOGIN",font=('Constantia',35,'bold','italic'),fg="white",bd=10,relief=GROOVE,bg='black')
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="black")
        Login_Frame.place(x=400,y=100)

        Btn_Frame=Frame(self.root,bg='black')
        Btn_Frame.place(x=500,y=570)

        userlbl=Label(Login_Frame,image=self.user_icon,compound=CENTER,bg='Black')
        userlbl.grid(row=0,columnspan=2)

        lbluser=Label(Login_Frame,text="Username*",image=self.username_icon,compound=LEFT,font=('Constantia',12,'bold','italic'),bg='black',fg='white')
        lbluser.grid(row=1,padx=10,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=username,relief=GROOVE,font=('Constantia',12,'bold','italic'))
        txtuser.grid(row=1,column=1,padx=10)

        lblpass=Label(Login_Frame,text="Password*",image=self.password_icon,compound=LEFT,font=('Constantia',12,'bold','italic'),bg='black',fg='white')
        lblpass.grid(row=2,padx=10,pady=10)
        txtpass=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=password,show='*',font=('Constantia',12,'bold','italic'))
        txtpass.grid(row=2,column=1,padx=10)

        btn_log=Button(Btn_Frame,text="LOGIN",font=('Constantia',12,'bold','italic'),fg="black",command=login)
        btn_log.grid(row=0,column=0,padx=5)

        btn_register=Button(Btn_Frame,text='REGISTER',font=('Constantia',12,'bold','italic'),command=register)
        btn_register.grid(row=0,column=1,padx=5)

        btn_stdlogin=Button(Btn_Frame,text='MEMBER LOGIN',font=('Constantia',12,'bold','italic'),command=std_login)
        btn_stdlogin.grid(row=0,column=2,padx=5)

        btn_exit=Button(Btn_Frame,text='EXIT',font=('Constantia',12,'bold','italic'),command=iExit)
        btn_exit.grid(row=0,column=3,padx=5)

        txtuser.focus()


class Lib_system:

    def __init__(self,root):
        self.root = root
        self.root.title('Library Database Management System')
        self.root.geometry("1350x750")#+0+0 for the coordinate

        #variavles
        member_id = StringVar()
        member_name = StringVar()
        member_mobile = IntVar()
        member_email = StringVar()
        member_address = StringVar()
        member_dept = StringVar()
        book_id = StringVar()
        book_name = StringVar()
        book_author = StringVar()
        book_publication = StringVar()
        book_price = DoubleVar()
        book_dept = StringVar()
        issue_id = StringVar()
        issue_date = StringVar()
        issue_return = StringVar()
        daysoverdue = IntVar()
        fine = DoubleVar()
        i_d = IntVar()

         #===========================================Function Declaration=====================================================


        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Database Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return


        def ClearData():
            self.txtmember_id.delete(0,END)
            self.txtmember_name.delete(0,END)
            self.txtmember_mobile.delete(0,END)
            self.txtmember_email.delete(0,END)
            self.txtmember_address.delete(0,END)
            self.txtmember_dept.delete(0,END)
            self.txtbook_id.delete(0,END)
            self.txtbook_name.delete(0,END)
            self.txtbook_author.delete(0,END)
            self.txtbook_publication.delete(0,END)
            self.txtbook_price.delete(0,END)
            self.txtbook_dept.delete(0,END)
            self.txtissue_id.delete(0,END)
            self.txtissue_date.delete(0,END)
            self.txtreturn_date.delete(0,END)
            self.txtdaysoverdue.delete(0,END)
            self.txtfine.delete(0,END)
            self.txtid.delete(0,END)
            booklist.delete(0, END)
            member_mobile.set(0)
            daysoverdue.set(0)
            book_price.set(0.0)
            fine.set(0.0)
            i_d.set(0)


        def addDataRec():
                global f
                if(member_id.get()!='' and member_name.get()!='' and member_mobile.get()!=0 and member_email.get()!='' and member_address.get()!='' and member_dept.get()!='' and book_id.get()!='' and book_name.get()!='' and book_author.get()!='' and book_publication.get()!='' and book_price.get()!=0.0 and book_dept.get()!='' and issue_id.get()!=''):
                        if(len(str(member_mobile.get()))!=10):
                                tkinter.messagebox.showerror('Phone Number','Invalid Phone Number!!')
                        else:
                                #try:
                                dl = daysoverdue.get()
                                f = 0
                                if dl < 7 :
                                        f = dl * 1.5
                                elif dl < 15 :
                                        f = (dl - 7) * 2 + 1.5 * 7
                                elif dl < 30 :
                                        f = (dl - 15) * 3.5 + 1.5 * 7 + 2 * 8
                                else :
                                        f = (dl - 30) * 5 + (1.5 * 7) + (8 * 2) + (15 *3.5)
                                backend.InsertData(member_id.get(),member_name.get(),member_mobile.get(),member_email.get(),member_address.get(),member_dept.get(),book_id.get(),book_name.get(),book_author.get(),book_publication.get(),book_price.get(),book_dept.get(),issue_id.get(),issue_date.get(),issue_return.get(),daysoverdue.get(),f,name1[0][0])
                                booklist.delete(0, END)
                                booklist.insert(END,(member_id.get(),member_name.get(),member_mobile.get(),member_email.get(),member_address.get(),member_dept.get(),book_id.get(),book_name.get(),book_author.get(),book_publication.get(),book_price.get(),book_dept.get(),issue_id.get(),issue_date.get(),issue_return.get(),daysoverdue.get(),f))
                                #except:
                                        #tkinter.messagebox.showerror('Inappropriate Data','Enter appropriate data')
                else:
                        tkinter.messagebox.showerror('Error!','Opps!!! \n Not all entries are filled')


        def DisplayData():
            booklist.delete(0,END)
            #row = backend.viewData()
            for row in backend.viewData():
                   booklist.insert(END,row)

        def SelectedBook(event):
                global sb
                searchbk = booklist.curselection()[0]
                sb = booklist.get(searchbk)
                try:
                        self.txtmember_id.delete(0,END)
                        self.txtmember_id.insert(END,sb[1])
                        self.txtmember_name.delete(0,END)
                        self.txtmember_name.insert(END,sb[2])
                        self.txtmember_mobile.delete(0,END)
                        self.txtmember_mobile.insert(END,sb[3])
                        self.txtmember_email.delete(0,END)
                        self.txtmember_email.insert(END,sb[4])
                        self.txtmember_address.delete(0,END)
                        self.txtmember_address.insert(END,sb[5])
                        self.txtmember_dept.delete(0,END)
                        self.txtmember_dept.insert(END,sb[6])
                        self.txtbook_id.delete(0,END)
                        self.txtbook_id.insert(END,sb[7])
                        self.txtbook_name.delete(0,END)
                        self.txtbook_name.insert(END,sb[8])
                        self.txtbook_author.delete(0,END)
                        self.txtbook_author.insert(END,sb[9])
                        self.txtbook_publication.delete(0,END)
                        self.txtbook_publication.insert(END,sb[10])
                        self.txtbook_price.delete(0,END)
                        self.txtbook_price.insert(END,sb[11])
                        self.txtbook_dept.delete(0,END)
                        self.txtbook_dept.insert(END,sb[12])
                        self.txtissue_id.delete(0,END)
                        self.txtissue_id.insert(END,sb[13])
                        self.txtissue_date.delete(0,END)
                        self.txtissue_date.insert(END,sb[14])
                        self.txtreturn_date.delete(0,END)
                        self.txtreturn_date.insert(END,sb[15])
                        self.txtdaysoverdue.delete(0,END)
                        self.txtdaysoverdue.insert(END,sb[19])
                        self.txtfine.delete(0,END)
                        self.txtfine.insert(END,sb[20])
                        self.txtid.delete(0,END)
                        self.txtid.insert(END,sb[0])
                except:
                        print()

        def DeleteData():
                if(len(member_id.get())!=0 or len(book_id.get())!=0 or len(issue_id.get())!=0):
                        if(len(member_id.get())!=0 and len(book_id.get())!=0 and len(issue_id.get())!=0):
                                id = member_id.get()
                                backend.del_member(id)
                                id = book_id.get()
                                backend.del_book(id)
                                id = issue_id.get()
                                backend.del_issue(id)
                                ClearData()
                                DisplayData()
                        elif(len(member_id.get())!=0 and len(book_id.get())!=0):
                                id = member_id.get()
                                backend.del_member(id)
                                id = book_id.get()
                                backend.del_book(id)
                                ClearData()
                                DisplayData()
                        elif(len(book_id.get())!=0 and len(issue_id.get())!=0):
                                id = book_id.get()
                                backend.del_book(id)
                                id = issue_id.get()
                                backend.del_issue(id)
                                ClearData()
                                DisplayData()
                        elif(len(member_id.get())!=0 and len(issue_id.get())!=0):
                                id = member_id.get()
                                backend.del_member(id)
                                id = issue_id.get()
                                backend.del_issue(id)
                                ClearData()
                                DisplayData()
                        elif(len(member_id.get())>0):
                                id = member_id.get()
                                backend.del_member(id)
                                ClearData()
                                DisplayData()
                        elif(len(book_id.get())>0):
                                id = book_id.get()
                                backend.del_book(id)
                                ClearData()
                                DisplayData()
                        elif(len(str(issue_id.get()) > 0)):
                                id = issue_id.get()
                                backend.del_issue(id)
                                ClearData()
                                DisplayData()

                else:
                        tkinter.messagebox.showinfo('No Data Entered!','Please Enter:\nMember ID to delete Member\nBook ID to delete a book\nIssue ID to delete a Issue')

        def SearchData():
                data = backend.searchdata(member_id.get(),member_name.get(),member_mobile.get(),member_email.get(),member_address.get(),member_dept.get(),book_id.get(),book_name.get(),book_author.get(),book_publication.get(),book_price.get(),book_dept.get(),issue_id.get(),issue_date.get(),issue_return.get(),daysoverdue.get(),f)
                con=sqlite3.connect('lib.db')
                cur=con.cursor()
                if(len(member_id.get())>1 or len(member_address.get())>1 or len(member_dept.get())>1 or len(member_email.get())>1 or len(str(member_mobile.get()))>1 or len(member_name.get())>1):
                        cur.execute("SELECT * FROM MEMBER WHERE MEM_ID = ? OR NAME = ? OR MOBILE_NO = ? OR EMAIL = ? OR ADDRESS = ? OR DEPT = ?",(member_id.get(),member_name.get(),member_mobile.get(),member_email.get(),member_address.get(),member_dept.get(),))
                        s = cur.fetchone()
                        member_id.set(s[0])
                        member_name.set(s[1])
                        member_mobile.set(s[2])
                        member_email.set(s[3])
                        member_address.set(s[4])
                        member_dept.set(s[5])
                elif(len(book_id.get())>1 or len(book_name.get())>1 or len(book_author.get())>1 or len(book_publication.get())>1 or  len(book_dept.get())>1):
                        cur.execute("SELECT * FROM BOOK WHERE BK_ID = ? OR NAME = ? OR AUTHOR = ? OR PUBLICATION = ? OR PRICE = ? OR DEPT = ?",(book_id.get(),book_name.get(),book_author.get(),book_publication.get(),book_price.get(),book_dept.get(),))
                        s = cur.fetchone()
                        book_id.set(s[0])
                        book_name.set(s[1])
                        book_author.set(s[2])
                        book_publication.set(s[3])
                        book_price.set(s[4])
                        book_dept.set(s[5])
                elif(len(issue_id.get())>1 or len(issue_date.get())>1 or len(issue_return.get())>1):
                        cur.execute("SELECT * FROM ISSUE WHERE ID = ? OR ISSUE_DATE = ? OR RETURN = ? ",(issue_id.get(),issue_date.get(),issue_return.get(),))
                        s = cur.fetchone()
                        issue_id.set(s[0])
                        issue_date.set(s[1])
                        issue_return.set(s[2])
                        book_id.set(s[3])
                        member_id.set(s[4])
                        try:
                                cur.execute("SELECT * FROM MEMBER WHERE MEM_ID = ?",(s[4],))
                                s1 = cur.fetchone()
                                member_name.set(s1[1])
                                member_mobile.set(s1[2])
                                member_email.set(s1[3])
                                member_address.set(s1[4])
                                member_dept.set(s1[5])
                        except:
                                booklist.insert(END,'Member Doesn\'t exist')
                        try:
                                cur.execute("SELECT * FROM BOOK WHERE BK_ID = ?",(s[3],))
                                s2 = cur.fetchone()
                                book_name.set(s2[1])
                                book_author.set(s2[2])
                                book_publication.set(s2[3])
                                book_price.set(s2[4])
                                book_dept.set(s2[5])
                        except:
                                booklist.insert(END,'Book No More Avaliable in Library!')
                elif(len(str(daysoverdue.get()))!=0 or len(str(fine.get()))!=0):
                        i = 0
                        cur.execute("SELECT * FROM LIBRARY WHERE OVERDUE = ? OR FINE = ?",(daysoverdue.get(),fine.get(),))
                        s = cur.fetchone()
                        member_name.set(s[1])
                        book_name.set(s[2])
                        issue_date.set(s[3])
                        issue_return.set(s[4])
                        daysoverdue.set(s[5])
                        fine.set(s[6])
                        try:
                                cur.execute("SELECT * FROM MEMBER WHERE NAME = ?",(s[1],))
                                s1 = cur.fetchone()
                                member_id.set(s1[0])
                                member_mobile.set(s1[2])
                                member_email.set(s1[3])
                                member_address.set(s1[4])
                                member_dept.set(s1[5])
                        except:
                                booklist.insert(END,'Member Doesn\'t Exist')
                        try:
                                cur.execute("SELECT * FROM BOOK WHERE NAME = ?",(s[2],))
                                s2 = cur.fetchone()
                                book_id.set(s2[0])
                                book_author.set(s2[2])
                                book_publication.set(s2[3])
                                book_price.set(s2[4])
                                book_dept.set(s2[5])
                        except:
                                booklist.insert(END,'Book no more in library!')
                        try:
                                cur.execute("SELECT * FROM ISSUE WHERE ISSUE_DATE =  ?",(s[3],))
                                s3 = cur.fetchone()
                                issue_id.set(s3[0])
                        except:
                                booklist.insert(END,'No such Issue!')
                con.close()
                for row in data:
                        booklist.insert(END,row)
        def updatedata():
                if((i_d.get()!=0 or i_d.get()!='') and member_id.get()!='' and member_name.get()!='' and member_mobile.get()!=0 and member_email.get()!='' and member_address.get()!='' and member_dept.get()!='' and book_id.get()!='' and book_name.get()!='' and book_author.get()!='' and book_publication.get()!='' and book_price.get()!=0.0 and book_dept.get()!='' and issue_id.get()!=''):
                        dl = daysoverdue.get()
                        new_fine = 0
                        if dl < 7 :
                                new_fine = dl * 1.5
                        elif dl < 15 :
                                new_fine = (dl - 7) * 2 + 1.5 * 7
                        elif dl < 30 :
                                new_fine = (dl - 15) * 3.5 + 1.5 * 7 + 2 * 8
                        else :
                                new_fine = (dl - 30) * 5 + (1.5 * 7) + (8 * 2) + (15 *3.5)
                        backend.update(member_id.get(),member_name.get(),member_mobile.get(),member_email.get(),member_address.get(),member_dept.get(),book_id.get(),book_name.get(),book_author.get(),book_publication.get(),book_price.get(),book_dept.get(),issue_id.get(),issue_date.get(),issue_return.get(),daysoverdue.get(),new_fine,i_d.get())
                        tkinter.messagebox.showinfo('Sucessful','Data updated sucesshully')
                        ClearData()
                        DisplayData()
                else:
                        if(i_d.get()==0):
                                tkinter.messagebox.showerror('opps!','ID is not valid')
                        else:
                                tkinter.messagebox.showinfo('Warning!','Opps!, not all entries are filled.')


#==============================================================FRAMES===================================================================

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=10,padx=40,pady=8,bg="Cadet blue", relief=RIDGE)
        TitFrame.pack(side=TOP)

        lblTit = Label(TitFrame, font=('Constantia',46,'italic','bold','underline'), text = '  Library Database Management System  ', bg = 'Cadet blue')
        lblTit.grid(sticky = W)

        ButtonFrame = Frame(MainFrame, bd=6, width=1350, height=70, padx = 20, pady=10, relief=RIDGE,bg='Cadet blue')
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = LabelFrame(MainFrame, bd=2, width=1350, height=150, padx=20, relief=RIDGE, font =('Consolas',12,'bold','italic'),bg="Cadet Blue" , text = 'Book Details:')
        FrameDetail.pack(side=BOTTOM,pady=10)

        DataFrame = Frame(MainFrame,  bd=10, width=1700, height=300, padx=20, pady=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM,pady=5)

        DataFrameLEFT = LabelFrame(DataFrame, bd=2, width=1600, height=350, padx=10,relief=RIDGE, font=('Consolas',12,'bold','italic'),text = 'Library Membership Info:', bg = 'Cadet Blue')
        DataFrameLEFT.pack(side=LEFT)



#========================================================LABEL and ENTRY=====================================================

        self.lblmember_id = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Member ID',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblmember_id.grid(row = 0, column = 0, sticky = W)
        self.txtmember_id = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = member_id, width = 25)
        self.txtmember_id.grid(row = 0, column = 1)

        self.lblmember_name = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Member Name',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblmember_name.grid(row = 0, column = 2, sticky = W)
        self.txtmember_name = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = member_name, width = 25)
        self.txtmember_name.grid(row = 0, column = 3)

        self.lblmember_mobile = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Moble No.',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblmember_mobile.grid(row = 0, column = 4, sticky = W)
        self.txtmember_mobile = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = member_mobile, width = 25)
        self.txtmember_mobile.grid(row = 0, column = 5)

        self.lblmember_email = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Member Email-ID',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblmember_email.grid(row = 1, column = 0, sticky = W)
        self.txtmember_email = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = member_email, width = 25)
        self.txtmember_email.grid(row = 1, column = 1)

        self.lblmember_address = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Member Address',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblmember_address.grid(row = 1, column = 2, sticky = W)
        self.txtmember_address = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = member_address, width = 25)
        self.txtmember_address.grid(row = 1, column = 3)

        self.lblmember_dept = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Member Department',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblmember_dept.grid(row = 1, column = 4, sticky = W)
        self.txtmember_dept = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = member_dept, width = 25)
        self.txtmember_dept.grid(row = 1, column = 5)

        self.lblbook_id = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Book ID',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblbook_id.grid(row = 2, column = 0, sticky = W)
        self.txtbook_id = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = book_id, width = 25)
        self.txtbook_id.grid(row = 2, column = 1)

        self.lblbook_name = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Book Name',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblbook_name.grid(row = 2, column = 2, sticky = W)
        self.txtbook_name = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = book_name, width = 25)
        self.txtbook_name.grid(row = 2, column = 3)

        self.lblbook_author = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Book Author',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblbook_author.grid(row = 2, column = 4, sticky = W)
        self.txtbook_author = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = book_author, width = 25)
        self.txtbook_author.grid(row = 2, column = 5)

        self.lblbook_publication = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Book Publication',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblbook_publication.grid(row = 3, column = 0, sticky = W)
        self.txtbook_publication = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = book_publication, width = 25)
        self.txtbook_publication.grid(row = 3, column = 1)

        self.lblbook_price = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Book Price',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblbook_price.grid(row = 3, column = 2, sticky = W)
        self.txtbook_price = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = book_price, width = 25)
        self.txtbook_price.grid(row = 3, column = 3)

        self.lblbook_dept = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Book Department',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblbook_dept.grid(row = 3, column = 4, sticky = W)
        self.txtbook_dept = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = book_dept, width = 25)
        self.txtbook_dept.grid(row = 3, column = 5)

        self.lblissue_id = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Issue ID',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblissue_id.grid(row = 4, column = 0, sticky = W)
        self.txtissue_id = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = issue_id, width = 25)
        self.txtissue_id.grid(row = 4, column = 1)

        self.lblissue_date = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Issue Date',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblissue_date.grid(row = 4, column = 2, sticky = W)
        self.txtissue_date = DateEntry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = issue_date, width = 23)
        self.txtissue_date.grid(row = 4, column = 3)

        self.lblreturn_date = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Return Date',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblreturn_date.grid(row = 4, column = 4, sticky = W)
        self.txtreturn_date = DateEntry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = issue_return, width = 23)
        self.txtreturn_date.grid(row = 4, column = 5)

        self.lbldaysoverdue = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Days Over Due',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lbldaysoverdue.grid(row = 5, column = 0, sticky = W)
        self.txtdaysoverdue = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = daysoverdue, width = 25)
        self.txtdaysoverdue.grid(row = 5, column = 1)

        self.lblfine = Label(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), text= 'Fine',padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblfine.grid(row = 5, column = 2, sticky = W)
        self.txtfine = Entry(DataFrameLEFT, font = ('Constantia',12,'bold','italic'), textvariable = fine, width = 25)
        self.txtfine.grid(row = 5, column = 3)

        self.lblid = Label(DataFrameLEFT,font = ('Constantia',12,'bold','italic'), text = "ID",padx = 2, pady = 2, bg = 'Cadet blue')
        self.lblid.grid(row=5, column=4, sticky=W)
        self.txtid = Entry(DataFrameLEFT,font = ('Constantia',12,'bold','italic'), textvariable = i_d, width = 25)
        self.txtid.grid(row = 5, column = 5)


#========================================================Listbox and Scrollbar============================================

        scrollbar = Scrollbar(FrameDetail)
        scrollbar.grid(row=0, column=1, sticky ='ns')
        scrollbar1 = Scrollbar(FrameDetail,orient='horizontal')
        scrollbar1.grid(row=1, column=0, sticky ='ns')

        booklist = Listbox(FrameDetail, width = 130, height=8, font=('Constantia',12,'bold','italic'), yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)#what is clicked is to be put into the entry box
        booklist.grid(row=0, column=0, padx=8, pady = 8)
        scrollbar.config(command=booklist.yview)
        scrollbar1.config(command=booklist.xview)

        ClearData()


#==========================================================Buttons widget======================================================

        self.btnAddData=Button(ButtonFrame, text='Add Data', font=('Constantia',14,'bold','italic'), height=1, width=13, bd=4, command = addDataRec)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData=Button(ButtonFrame, text='Display Data', font=('Constantia',14,'bold','italic'), height=1, width=13, bd=4, command = DisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnClearData=Button(ButtonFrame, text='Clear Data', font=('Constantia',14,'bold','italic'), height=1, width=13, bd=4, command = ClearData)
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData=Button(ButtonFrame, text='Delete Data', font=('Constantia',14,'bold','italic'), height=1, width=13, bd=4,command = DeleteData)
        self.btnDeleteData.grid(row=0,column=3)

        self.btnUpdateData=Button(ButtonFrame, text='Update Data', font=('Constantia',14,'bold','italic'), height=1, width=13, bd=4, command=updatedata)
        self.btnUpdateData.grid(row=0,column=4)

        self.btnSearchData=Button(ButtonFrame, text='Search Data', font=('Constantia',14,'bold','italic'), height=1, width=13, bd=4,command = SearchData)
        self.btnSearchData.grid(row=0,column=5)

        self.btnExit=Button(ButtonFrame, text='Exit', font=('Constantia',14,'bold','italic'), height=1, width=13, bd=4, command=iExit )
        self.btnExit.grid(row=0,column=6)




root=Tk()
name1=None
register_screen=None
username=None
password=None
mob_no=None
email=None
sb=None
f=None
mem=StringVar()
obj=Register(root)
root.mainloop()

