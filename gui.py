"""
from tkinter import *
from tkinter import messagebox
def show():
    text=inp.get()
    print(text)
root=Tk()
root.title("input to user")
root.geometry("250x200")
inp=Entry(root)
inp.pack()
but=Button(root,text="show" ,command=show)
but.pack()
root.mainloop()

"""
from tkinter import *
#from tkinter import messagebox
def show():
    text=inp.get()
    print(text)
root=Tk()
root.title("input to user")
root.geometry("250x200")
inp=Entry(root,bd=8,show="*",font=("Arial",15,"bold"))
inp.pack()
but=Button(root,text="show" ,command=show)
but.pack()
root.mainloop()










