import sqlite3
import tkinter

def ConnectData():
    con=sqlite3.connect("lib.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS MEMBER(MEM_ID VARCHAR2(10) PRIMARY KEY, NAME VARCHAR2(20), MOBILE_NO INTEGER, EMAIL VARCHAR2(30), ADDRESS VARCHAR2(50), DEPT VARCHAR2(20))")
    cur.execute("CREATE TABLE IF NOT EXISTS BOOK(BK_ID  VARCHAR2(20) PRIMARY KEY, NAME VARCHAR2(20), AUTHOR VARCHAR2(20), PUBLICATION VARCHAR2(20), PRICE FLOAT,DEPT VARCHAR2(20))")
    cur.execute('CREATE TABLE IF NOT EXISTS LIBRARIAN(ID INTEGER PRIMARY KEY, NAME VARCHAR2(20), MOBILE INTEGER, EMAIL VARCAHR2(30),USERNAME VARCHAR2(20),PASSWORD VARCHAR2(20))')
    cur.execute("CREATE TABLE IF NOT EXISTS ISSUE(ID VARCHAR2(20) PRIMARY KEY, ISSUE_DATE DATE, RETURN DATE, ISSUE_BK_ID VARCHAR2(20) REFERENCES BOOK(BK_ID), ISSUE_MEM_ID VARCHAR2(20) REFERENCES MEMBER(MEM_ID), ISSUE_LIB_NAME VARCHAR2(20) REFERENCES LIBRARIAN(NAME))")
    cur.execute("CREATE TABLE IF NOT EXISTS LIBRARY(ID INTEGER PRIMARY KEY, MEM_NAME VARCHAR2(20) REFERENCES MEMBER(NAME), BK_NAME VARHAR2(20) REFERENCES BOOK(NAME), ISSSUE DATE REFERENCES ISSUE(ISSUE_DATE), RETURN DATE REFERENCES ISSUE(RETURN), OVERDUE INTEGER, FINE FLOAT)")
    con.commit()
    con.close()

def insert(librarian_name,librarian_mobile,librarian_email,username,password):
    con = sqlite3.connect('lib.db')
    cur = con.cursor()
    cur.execute("INSERT INTO LIBRARIAN VALUES(NULL,?,?,?,?,?)",(librarian_name,librarian_mobile,librarian_email,username,password))
    con.commit()
    con.close()


def InsertData(member_id,member_name,member_mobile,member_email,member_address,member_dept,book_id,book_name,book_author,book_publication,book_price,book_dept,issue_id,issue_date,issue_return,daysoverdue,fine,librarian_name):
    con=sqlite3.connect('lib.db')
    cur=con.cursor()
    try:
        cur.execute("INSERT INTO MEMBER VALUES(?,?,?,?,?,?)",(member_id,member_name,member_mobile,member_email,member_address,member_dept))
        cur.execute("INSERT INTO BOOK VALUES(?,?,?,?,?,?)",(book_id,book_name,book_author,book_publication,book_price,book_dept))
        cur.execute("INSERT INTO ISSUE VALUES(?,?,?,?,?,?)",(issue_id,issue_date,issue_return,book_id,member_id,librarian_name))
        cur.execute("INSERT INTO LIBRARY VALUES(NULL,?,?,?,?,?,?)",(member_name,book_name,issue_date,issue_return,daysoverdue,fine))
    except sqlite3.IntegrityError:
        tkinter.messagebox.showerror('Error!','Key violation')

    con.commit()
    con.close()



def viewData():
    con=sqlite3.connect("lib.db")
    cur=con.cursor()
    cur.execute("SELECT LIBRARY.ID,MEMBER.MEM_ID,MEMBER.NAME,MEMBER.MOBILE_NO,MEMBER.EMAIL,MEMBER.ADDRESS,MEMBER.DEPT,BOOK.BK_ID,BOOK.NAME,BOOK.AUTHOR,BOOK.PUBLICATION,BOOK.PRICE,BOOK.DEPT,ISSUE.ID,ISSUE.ISSUE_DATE,ISSUE.RETURN,LIBRARIAN.NAME,LIBRARIAN.MOBILE,LIBRARIAN.EMAIL,LIBRARY.OVERDUE,LIBRARY.FINE FROM MEMBER,BOOK,ISSUE,LIBRARIAN,LIBRARY WHERE MEMBER.MEM_ID = ISSUE.ISSUE_MEM_ID AND MEMBER.NAME = LIBRARY.MEM_NAME AND BOOK.BK_ID = ISSUE.ISSUE_BK_ID AND BOOK.NAME = LIBRARY.BK_NAME AND ISSUE.ISSUE_DATE = LIBRARY.ISSSUE AND ISSUE.RETURN = LIBRARY.RETURN AND ISSUE_LIB_NAME = LIBRARIAN.NAME")
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows


def del_member(id):
    print(id)
    con=sqlite3.connect('lib.db')
    cur=con.cursor()
    cur.execute("DELETE FROM MEMBER WHERE MEM_ID = ?",(id,))
    rows1=cur.fetchall()
    con.commit()
    con.close()
    return rows1

def del_book(id):
    con=sqlite3.connect('lib.db')
    cur=con.cursor()
    cur.execute("DELETE FROM BOOK WHERE BK_ID = ?",(id,))
    rows2=cur.fetchall()
    con.commit()
    con.close()
    return rows2

def del_issue(id):
    con=sqlite3.connect('lib.db')
    cur=con.cursor()
    cur.execute("DELETE FROM ISSUE WHERE ID = ?",(id,))
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows

def searchdata(member_id,member_name,member_mobile,member_email,member_address,member_dept,book_id,book_name,book_author,book_publication,book_price,book_dept,issue_id,issue_date,issue_return,daysoverdue,fine):

    print(type(member_id))
    print(member_id)
    con=sqlite3.connect('lib.db')
    cur=con.cursor()
    if(len(member_id)>1 or len(member_address)>1 or len(member_dept)>1 or len(member_email)>1 or len(str(member_mobile))>1 or len(member_name)>1):
        cur.execute('''SELECT * FROM LIBRARY WHERE MEM_NAME = (SELECT NAME FROM MEMBER WHERE NAME = ? OR MEM_ID= ? OR MOBILE_NO = ? OR EMAIL = ? OR ADDRESS = ? OR DEPT = ?)''',(member_name,member_id,member_mobile,member_email,member_address,member_dept,))
    elif(len(book_id)>1 or len(book_name)>1 or len(book_author)>1 or len(book_publication)>1 or len(str(book_price))>3 or len(book_dept)>1):
        cur.execute('''SELECT * FROM LIBRARY WHERE BK_NAME = (SELECT NAME FROM BOOK WHERE BK_ID = ? OR NAME = ? OR AUTHOR = ? OR PUBLICATION = ? OR PRICE = ? OR DEPT = ?)''',(book_id,book_name,book_author,book_publication,book_price,book_dept,))
    elif(len(issue_id)>1 or len(issue_date)>1 or len(issue_return)>1):
        cur.execute('''SELECT * FROM LIBRARY WHERE ISSSUE = (SELECT ISSUE_DATE FROM ISSUE WHERE ID = ? OR ISSUE_DATE = ? OR RETURN = ?) OR RETURN =(SELECT RETURN FROM ISSUE WHERE ID = ? OR ISSUE_DATE = ? OR RETURN = ?)''',(issue_id,issue_date,issue_return,issue_id,issue_date,issue_return,))
    elif(len(str(daysoverdue))!=0 or len(str(fine))!=0):
        cur.execute('''SELECT * FROM LIBRARY WHERE OVERDUE = ? OR FINE = ?''',(daysoverdue,fine,))
    a = cur.fetchall()
    print(a)
    con.commit()
    con.close()
    return a

def update(member_id,member_name,member_mobile,member_email,member_address,member_dept,book_id,book_name,book_author,book_publication,book_price,book_dept,issue_id,issue_date,issue_return,daysoverdue,fine,i_d):
    con=sqlite3.connect('lib.db')
    cur=con.cursor()
    cur.execute("UPDATE MEMBER SET NAME = ?, MOBILE_NO = ?, EMAIL = ?,ADDRESS = ? ,DEPT = ? WHERE MEM_ID=?",(member_name,member_mobile,member_email,member_address,member_dept,member_id))
    cur.execute("UPDATE BOOK SET NAME=?,AUTHOR=?,PUBLICATION=?,PRICE=?,DEPT=? WHERE BK_ID=?",(book_name,book_author,book_publication,book_price,book_dept,book_id))
    cur.execute("UPDATE ISSUE SET ISSUE_DATE=?,RETURN=?,ISSUE_BK_ID=?,ISSUE_MEM_ID=? WHERE ID=?",(issue_date,issue_return,book_id,member_id,issue_id))
    cur.execute("UPDATE LIBRARY SET MEM_NAME=?,BK_NAME=?,ISSSUE=?,RETURN=?,OVERDUE=?,FINE=? WHERE ID = ?",(member_name,book_name,issue_date,issue_return,daysoverdue,fine,i_d,))
    con.commit()
    con.close()


ConnectData()
