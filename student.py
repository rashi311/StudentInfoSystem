from tkinter import *
import tkinter as tk
import psycopg2
root=Tk()
def get_data(name,age,address):
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    curr = conn.cursor()
    query=(''' INSERT INTO STUDENTS (NAME,AGE,ADDRESS) VALUES (%s,%s,%s)''')
    curr.execute(query,(name,age,address))
    conn.commit()
    conn.close()
    print("DATA INSERTED successfully") 

def search(id):
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    curr = conn.cursor()
    query=(''' select * from students where id=%s''')
    curr.execute(query,(id,))
    row=curr.fetchone()
    display_search(row)
    conn.commit()
    conn.close()
    print("DATA FETCHED successfully") 

def display_search(row):
    list_box=Listbox(frame,width=20,height=2)
    list_box.grid(row=9,column=1)
    list_box.insert(END,row) 

def display_all():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    curr = conn.cursor()
    query=(''' select * from students''')
    curr.execute(query)  
    row=curr.fetchall()   
    list_box=Listbox(frame,width=20,height=5)
    list_box.grid(row=10,column=1)
    for i in row:
        list_box.insert(END,i) 
 



canvas=Canvas(root,height=480,width=800)
canvas.pack()

frame=Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label=Label(frame,text="add data")
label.grid(row=0,column=1)

label=Label(frame,text="Name")
label.grid(row=1,column=0)

entry_name=Entry(frame)
entry_name.grid(row=1,column=1)

label=Label(frame,text="Age")
label.grid(row=2,column=0)

entry_age=Entry(frame)
entry_age.grid(row=2,column=1)

label=Label(frame,text="address")
label.grid(row=3,column=0)

entry_address=Entry(frame)
entry_address.grid(row=3,column=1)


button=Button(frame,text="add",command=lambda : get_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4,column=1)

label=Label(frame,text="search data")
label.grid(row=5,column=1)

label=Label(frame,text="search by id")
label.grid(row=6,column=0)

id_search=Entry(frame)
id_search.grid(row=6,column=1)

button=Button(frame,text="search",command=lambda : search(id_search.get()))
button.grid(row=7,column=1)
display_all()
root.mainloop()