from tkinter import *
from book_backend import Database
database=Database("books.db")
def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    title=e1.get()
    author=e2.get()
    year=e3.get()
    isbn=e4.get()
    for row in database.search(title,author,year,isbn):
        list1.insert(END,row)


def insert_command():
    title=e1.get()
    author=e2.get()
    year=e3.get()
    isbn=e4.get()
    database.insert(title,author,year,isbn)
    list1.delete(0,END)
    list1.insert(END,(title,author,year,isbn))



def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def delete_command():

    database.delete(selected_tuple[0])

def update_command():
    title=e1.get()
    author=e2.get()
    year=e3.get()
    isbn=e4.get()
    database.update(selected_tuple[0],title,author,year,isbn)


def close_command():
    root.destroy()

root=Tk()
l1=Label(root,text="Title")
l1.grid(row=0,column=0)
l2=Label(root,text="Author")
l2.grid(row=0,column=2)
l3=Label(root,text="Year")
l3.grid(row=1,column=0)
l4=Label(root,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(root,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(root,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(root,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(root,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(root,height=5,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

sb1=Scrollbar(root)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(root,text="view all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(root,text="search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(root,text="add entry",width=12,command=insert_command)
b3.grid(row=4,column=3)

b4=Button(root,text="update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(root,text="delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(root,text="Close",width=12,command=close_command)
b6.grid(row=7,column=3)

root.mainloop()
