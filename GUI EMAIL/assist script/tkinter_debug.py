from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry("400x500")
## Text box untuk pesannya 
# text_msg = Text(root,height = 10 , width= 30)
# text_msg.place(x=1,y=10)
## Ini labelnya
# label_username = Label(root,text="Username")
# label_password = Label(root,text="Password")
# label_from = Label(root,)
## input nya
# entry_username = Entry(root,bd=5,width=40)
# entry_password =Entry(root,bd=5,width=40,show="*")
## ini posisinya
# label_username.place(x=1,y=10)
# label_password.place(x=1,y=60)
# entry_username.place(x=100,y=10)
# entry_password.place(x=100,y=60)
## ini button enter atau kirimnya
# def enter():
#     print(text_msg.get("1.0","end-1c"))
# button_enter = Button(root,text="ENTER",command=enter)
# button_enter.place(x=200,y=200)
entry_open = Entry(root,bd=5,width=30)
def Open():
    root.filename = filedialog.askopenfilename(initialdir="\Documents",title="Pilih File.",filetypes=(("png files","*.png"),("all files","*.*")))
    entry_open.insert(END,root.filename)
open_button = Button(root,text="Open Files",command=Open)
label_file = Label(root,text="File Location ")
label_file.place(x=1,y=10)
entry_open.place(x=80,y=10)
open_button.place(x=280,y=10)

root.mainloop()
