from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Status Message","Insert all the needed fields please!!!")
    else:
        conn = mysql.connect(host="localhost",user="root",password="",database="niit")
        cursor = conn.cursor()
        cursor.execute("insert into student values ('"+ id +"','" + name + "', +'" + phone + "')")
        cursor.execute("commit");

        e_id.delete(0,'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()

        MessageBox.showinfo("Insert status","Student Record inserted successfully")
        conn.close()

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete status","ID is compustory to delete")
    else:
        conn = mysql.connect(host="localhost",user="root",password="",database="niit")
        cursor = conn.cursor()
        cursor.execute("delete from student where id = '" + e_id.get() + "'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()

        MessageBox.showinfo("Delete Status","The data has been deleted successfully")
        conn.close()
def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Update status","All fields required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="niit")
        cursor = con.cursor()
        cursor.execute("update student set name='" + name + "',phone='" + phone + "' where id ='"
                                                                                + id + "'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()


        MessageBox.showinfo("Update status", "Updated Successfully")
        con.close()
def fetch():
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch Status","ID is neccessary to fetch items")
    else:
        conn = mysql.connect(host="localhost",user="root",password="",database="niit")
        cursor = conn.cursor()
        cursor.execute("select  * from student where id = '" + e_id.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
        conn.close()
def show():
    conn = mysql.connect(host="localhost",user="root",password="",database="niit")
    cursor = conn.cursor()
    cursor.execute("select *from student")
    rows = cursor.fetchall()
    list.delete(0,list.size())

    for row in rows:
        insertData = str(row[0])+ '          ' + row[1] + '    ' +  row[2]
        list.insert(list.size()+1, insertData)
    conn.close()
root = Tk()
root.title("STUDENT DATA")
root.geometry("600x300")

id = Label(root,text="Enter ID",font=('bold',10))
id.place(x=20,y=30)

name = Label(root,text="Enter name",font=('bold',10))
name.place(x=20,y=60)

phone = Label(root,text="Enter phone number",font=('bold',10))
phone.place(x=20,y=90)

e_id = Entry()
e_id.place(x=150,y=30)

e_name = Entry()
e_name.place(x=150,y=60)

e_phone = Entry()
e_phone.place(x=150,y=90)

insert = Button(root,text="insert", font=("italic",10),bg="white", command=insert)
insert.place(x=20,y=140)

delete = Button(root,text="delete", font=("italic",10),bg="white", command=delete)
delete.place(x=70,y=140)

update = Button(root,text="update", font=("italic",10),bg="white", command=update)
update.place(x=130,y=140)

fetch = Button(root,text="fetch", font=("italic",10),bg="white", command=fetch)
fetch.place(x=190,y=140)

list = Listbox(root,bg="#eee")
list.place(x=350,y=30)
show()

root.mainloop()