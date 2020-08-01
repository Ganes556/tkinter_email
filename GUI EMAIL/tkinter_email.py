import os
import re
import smtplib
import imghdr
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from email.message import EmailMessage
from tkinter import messagebox
from tkinter import ttk
class Command(Widget):
    
    def Open(self):

        type_name = (("PNG files","*.png"),("JPG files","*.jpg"),("PDF files","*.pdf"),("All files","*.*"))
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Pilih File.",filetypes=type_name)

        if "." in self.entry_file.get(): 
            
            self.entry_file.insert(END,","+filename)
        else:
            self.entry_file.insert(END,filename)
    def open_penerima(self):
        type_name = (("TXT files","*.txt"),("All files","*.*"))
        files = filedialog.askopenfilename(initialdir=os.getcwd(),title="Pilih File.",filetypes=type_name)
        try:
            if files == "":
                return
            with open(files,'r') as f:
                file = f.readlines()
                if ".txt" in f.name:
                    self.entry_penerima.delete(0,END)
                    self.entry_penerima.insert(0,",".join(file))
        except Exception:
            messagebox.showwarning("File type","File invalid !")
    def show(self):
    
        if  self.entry_password["show"] == "*":
            self.entry_password["show"] = ""
            self.button_show["text"] = "Hide"
        else:
            self.entry_password["show"]= "*"
            self.button_show["text"] = "Show"

    
    ############################### BUAT POP UP BARUNYA ##################################
    def file_show(self): 
        global pop_up,lists_file
        files = self.entry_file.get().split(",")
        pop_up = tk.Tk()
        pop_up.title("File list")
        pop_up.geometry("300x220")
        pop_up.configure(bg="red")
        pop_up.iconbitmap(r'C:\Users\62831\Documents\GitHub\GUI EMAIL\png_icon\list.ico')
        my_frame = Frame(pop_up)
        y_scrollbar = Scrollbar(my_frame,orient=VERTICAL)
        lists_file = Listbox(my_frame,height="10",width="50",yscrollcommand=y_scrollbar.set,selectmode=EXTENDED,font=("arial",10,"bold"))
        y_scrollbar.config(command=lists_file.yview)
        y_scrollbar.pack(side=RIGHT,fill=Y)
        my_frame.pack()
        lists_file.pack(pady=5)

        if len(files) >= 1:
            for index,file in enumerate(files,start=1):
                if file:
                    hapus = re.match(r".*/",file)
                    file = file.replace(hapus.group(),"")
                    lists_file.insert(END,f"{index}. {file}")

        butt_delete = tk.Button(pop_up,text="Delete",command=self.show_delete,activebackground="skyblue",bg="deepskyblue")
        butt_delete.pack(pady=5)
        pop_up.mainloop()
    def show_delete(self):
        files = self.entry_file.get().split(",")
        # files barunya
        files_baru = files
        index_file = lists_file.index(ANCHOR) # single index
        index_multi = lists_file.curselection() # multi index
        if len(index_multi) > 1: # multi delete
            for index in reversed(index_multi):
                lists_file.delete(index)
                # hanya mengisikan file yg tdk di hapus
                files_baru.pop(index)
            
        else: # single delete
            lists_file.delete(index_file)
            # hanya mengisikan file yg tdk di hapus
            files_baru.pop(index_file)
        
        # hapus semua entry    
        self.entry_file.delete(0,END)
        # menambahkan string entry dengan file sisa tadi
        self.entry_file.insert(0,"".join(files_baru))
        
    #########################################################################

    def kirim(self):
        entry_list = [self.entry_username,self.entry_password,self.entry_penerima]
        label_list = [self.label_username,self.label_password,self.label_penerima]
        for entry in range(len(entry_list)):
            if entry_list[entry].get() == "":
                label_list[entry]["foreground"]="red"
            else: 
                label_list[entry]["foreground"]="black"

        if "<html>" in self.text_msg.get("1.0",END):
            msg= self.msg_html()
        if self.entry_file.get() != "":
            msg= self.msg_file()
        if  "<html>" not in self.text_msg.get("1.0",END) and self.entry_file.get() == "":
            msg= self.msg_program()
        try:
            self.main_program(msg)
        except Exception as er:
            messagebox.showerror("Error","Check your input !")
            return
        question = messagebox.askquestion("Delete/Not","Delete your lasted message ?")
        if question == "yes":
            self.entry_subjek.delete(0,END)
            self.entry_penerima.delete(0,END)
            self.entry_file.delete(0,END)
            self.text_msg.delete("1.0",END)
        
        
    def main_program(self,msg):
        
        EMAIL_ADDRESS = self.entry_username.get()
        EMAIL_PASSWORD = self.entry_password.get()
        EMAIL_PENERIMA =  self.entry_penerima.get()
    
        terkirim = True
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            try:
                smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp.send_message(msg)
            except Exception:
                messagebox.showerror("Error","Check akun/connection !")
                terkirim = False
        if terkirim:
            messagebox.showinfo("Sukses","Terkirim !")

    def msg_program(self):
        msg = EmailMessage()
        msg['Subject'] = self.entry_subjek.get()
        msg['From'] = self.entry_username.get()
        msg['To'] = self.entry_penerima.get()
        msg.set_content(self.text_msg.get("1.0",END))
        return msg
    def msg_file(self):
        msg = EmailMessage()
        msg['Subject'] = self.entry_subjek.get()
        msg['From'] = self.entry_username.get()
        msg['To'] = self.entry_penerima.get()
        msg.set_content(self.text_msg.get("1.0",END))
        sperate_coma = self.entry_file.get().split(",")

        for file in sperate_coma:
            with open(file,'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype= "octet-stream", filename= file_name)
        return msg

    def msg_html(self):
        msg = EmailMessage()
        msg['Subject'] = self.entry_subjek.get()
        msg['From'] = self.entry_username.get()
        msg['To'] = self.entry_penerima.get()
        msg.add_alternative(self.text_msg.get("1.0",END), subtype='html')
        return msg
    def up_down(self,event):
        list_call = [self.entry_username,self.entry_password,self.entry_subjek,
                    self.entry_penerima,self.entry_file]
        list_output = [".!entry",".!entry2",".!entry3",".!entry4",".!entry5"]
        current_focus = event.widget

        if event.keysym == "Down":
            for index,string in enumerate(list_output):
                if str(current_focus) == ".!entry5": # jika di index terakhir dan menekan Down maka ke balik ke awal
                    list_call[0].focus_set()
                elif str(current_focus) == string: 
                    if index+1 < len(list_output): # agar tidak out range 
                        list_call[index+1].focus_set() # pindah focus ke bawah 

        elif event.keysym == "Up":
            for index,string in enumerate(list_output):
                if str(current_focus) == ".!entry":
                    list_call[4].focus_set()
                elif str(current_focus) == string:
                    if index-1 >= 0 : # agar tidak out range 
                        list_call[index-1].focus_set() # pindah focus ke atas
        

class Widged(Command):

    def label(self):
        ## label syntax
        
        self.label_username = tk.Label(root,text="Email Username",relief="sunken", width=12,bg="deepskyblue")
        self.label_password = tk.Label(root,text="Email Password",relief="sunken", width=12,bg="deepskyblue")
        label_subjek = tk.Label(root,text="Subjek",relief="sunken",width=12,bg="deepskyblue")
        self.label_penerima = tk.Label(root,text="Penerima",relief="sunken", width=12,bg="deepskyblue")
        label_file = tk.Label(root,text="Lokasi File",relief="sunken", width=12,bg="deepskyblue")
        label_pesan = tk.Label(root,text="Pesan",relief="sunken", width=12,bg="deepskyblue")

        ## posisi label
        self.label_username.place(x=1,y=11)
        self.label_password.place(x=1,y=51)
        label_subjek.place(x=1,y=91)
        self.label_penerima.place(x=1,y=131)
        label_file.place(x=1,y=171)
        label_pesan.place(x=1,y=221)

    def entry(self):
        ## entry syntax
        
        self.entry_username = tk.Entry(root,bd=5,width=26,font=("arial",10,"bold"))
        self.entry_password =tk.Entry(root,bd=5,width=26,font=("arial",10,"bold"),show="*")
        self.entry_subjek = tk.Entry(root,bd=5,width=26,font=("arial",10,"bold"))
        self.entry_penerima = tk.Entry(root,bd=5,width=26,font=("arial",10,"bold"))
        self.entry_file = tk.Entry(root,bd=5,width=26,font=("arial",10,"bold"))
        self.text_msg = tk.Text(root,height = 10 , width= 26,bd=5,font=("arial",10,"bold"))
  
        ## posisi entry
        self.entry_username.place(x=100,y=10)
        self.entry_password.place(x=100,y=50)
        self.entry_subjek.place(x=100,y=90)
        self.entry_penerima.place(x=100,y=130)
        self.entry_file.place(x=100,y=170)
        self.text_msg.place(x=100,y=220)


    def button(self):
      
        ## button syntax
        
        self.button_show = tk.Button(root,text="Show",command=self.show, width=4,bg="deepskyblue",activebackground="skyblue") # belum lese
        button_open = tk.Button(root,image=photo_open,command=self.Open,bd=0,bg="red",activebackground="skyblue",relief="raised") # belum
        button_kirim = tk.Button(root,text="Send",command=self.kirim,bg="deepskyblue",activebackground="skyblue")
        button_file_show = tk.Button(root,text="Show",command=self.file_show, width=4,bg="deepskyblue",activebackground="skyblue")
        button_open_penerima = tk.Button(root,image=photo_penerima,command=self.open_penerima,bd=0,bg="red",activebackground="skyblue")

        ## posisi button 
        self.button_show.place(x=305,y=49)
        button_open.place(x=305,y=170)
        button_kirim.place(x=180,y=400)
        button_file_show.place(x=330,y=169)
        button_open_penerima.place(x=305,y=130)

   

class Running_program(Widged,Command):
    def __init__(self):
        root.bind("<Down>",self.up_down)
        root.bind("<Up>",self.up_down)
        # root.bind("<Return>",self.kirim)
        Widged.label(self)
        Widged.entry(self)
        Widged.button(self)
    

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("380x450")
    root.title("EMAIL APP")
    root.iconbitmap(r'C:\Users\62831\Documents\GitHub\GUI EMAIL\png_icon\email_ico.ico')
    root.resizable(False,False)
    root.configure(background="red")
    photo_open = PhotoImage(file=r"C:\Users\62831\Documents\GitHub\GUI EMAIL\png_icon\open.png")
    photo_penerima = PhotoImage(file=r"C:\Users\62831\Documents\GitHub\GUI EMAIL\png_icon\penerima.png")
    Running_program()
    root.mainloop()