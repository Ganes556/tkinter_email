# import keyring

# MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

# # the service is just a namespace for your app
# service_id = '1'  

# username = 'dustin'

# # save password
# keyring.set_password(service_id, username, "password")

# # optionally, abuse `set_password` to save username onto keyring
# # we're just using some known magic string in the username field
# keyring.set_password(service_id, MAGIC_USERNAME_KEY, username)
# username1 = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
# password1 = keyring.get_password(service_id, username)  
# print(username1)
# print(password1)

from tkinter import *
from tkinter.messagebox import _show
from tkinter import messagebox
import re

# text = ""
# def down(event):
#     global text
#     if event.keysym != "":
#         text += event.keysym
#     else:
#         text += event.char
#     label = Label(root,text=text)
#     label.place(x=10,y=200)
number = 0
def down(event):
    yes = messagebox.askquestion("Delete/Not","hapus ?")


    # print("focus is:", root.focus_get())

    list_entry = [entry1,entry2,entry3,text1]
    output_entry = [".!entry",".!entry2",".!entry3",".!text"]

    tes= event.widget
    if event.keysym == "Down":
        for index,string in enumerate(output_entry):
            if str(tes) == string:
                if index+1 < len(list_entry):
                    list_entry[index+1].focus_set()
    elif event.keysym == "Up":
        for index,string in enumerate(output_entry):
            if str(tes) == string:
                if index-1 >= 0 :
                    list_entry[index-1].focus_set()

    # file = re.findall(r"[0-9]",str(tes))
    # if estr(tes):


    # if file == [] and event.keysym == "Down":
    #     list_entry[1].focus_set()
    # elif file == [] and event.keysym == "Up":
    #     list_entry[2].focus_set()
        
    # if file == ["2"] and event.keysym == "Down":
    #     list_entry[2].focus_set()
    # elif file == ["2"] and event.keysym == "Up":
    #     list_entry[0].focus_set()

    # if file == ["3"] and event.keysym == "Down":
    #     list_entry[3].focus_set()

    # elif file == ["3"] and event.keysym == "Up":
    #     list_entry[1].focus_set()

    # if file == ["3"] and event.keysym == "Down":
    #     list_entry[0].focus_set()
    # elif file == ["3"] and event.keysym == "Up":
    #     list_entry[2].focus_set()




    # print(file)
    
    # elif file == ["2"] and event.keysym == "Up":
    #     list_entry[1].focus_set()

    # elif file == ["2"] and event.keysym == "Up":
    #     list_entry[index-1].focus_set()

    
    # for index,entry in enumerate(list_entry):
        
    #     list_entry[number].focus_set()
    #     number +=1
    # elif event.keysym == "Up":
    #     number -=1
    #     list_entry[number].focus_set()


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300")
    entry1 = Entry(root,bd=5)
    entry2 = Entry(root,bd=5)
    entry3 = Entry(root,bd=5)
    text1 = Text(root,bd=5)
    entry1.pack(pady=5)
    entry2.pack(pady=5)
    entry3.pack(pady=5)
    text1.pack(pady=5)
    # root.after(5000, lambda:_show("Title","Time Over"))
    root.bind("<Down>",down)
    root.bind("<Up>",down)

    root.mainloop()


