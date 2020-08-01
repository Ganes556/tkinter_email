from tkinter import *

#command 
def delete():
    if len(my_listbox.curselection()) > 1:
    
        for index in reversed(my_listbox.curselection()):
            my_listbox.delete(index)
            
            
    else:
        my_listbox.delete(ANCHOR)
    my_label["text"] = ""

def select():
    if my_listbox.curselection() != ():
        result = ""
        indexs = my_listbox.curselection()
        for index in indexs:
            result += my_listbox.get(index) + "\n"
        my_label.config(text=result)    
    else:
        my_label.config(text=my_listbox.get(ANCHOR))
def delete_all():
    my_listbox.delete(0,END)
    

root = Tk()
root.geometry("400x400")

# create frame
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame,orient=VERTICAL)

# lISTBOX!
# SELECTMODE = SINGLE="default",BROWSE= "only down and up with left mouse clicked",MULTIPLE="select multi just only click left mouse",
# EXTENDED = "select multi with click ctrl or shift+left mouse in same time"

my_listbox = Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set,selectmode=EXTENDED)
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_frame.pack()
my_listbox.pack(pady=5) 


# Add Item to listbox
my_listbox.insert(END,"item number 1")
for x in range(2,70):
    my_listbox.insert(END,"item number "+str(x))
select_button = Button(root,text="Select",command=select)

delete_button = Button(root,text="Delete",command=delete)
delete_all = Button(root,text="Delete all", command=delete_all)
my_label = Label(root,text="")


select_button.pack(pady=5)
delete_button.pack()
my_label.pack(pady=5)
delete_all.pack(side=BOTTOM)

root.mainloop()