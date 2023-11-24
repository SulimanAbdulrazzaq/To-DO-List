from tkinter import *
from tkinter import messagebox,ttk
import customtkinter
import sqlite3
import tkinter
import bcrypt
import customtkinter
from tkinter import messagebox,ttk,Listbox,END
import sqlite3
app = customtkinter.CTk()
app.geometry("400x360")
app.title("Family Mangement")
app.config(bg="#001220")

font = ("Helvetica",20,"bold")


conn = sqlite3.connect("users.db")

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(ID TEXT NOT NULL,Password TEXT NOT NULL)")

fra1 = customtkinter.CTkFrame(app,bg_color="#001220",fg_color="#001220",width=470,height=360)
fra1.place(x=0,y=0)
def loginb():
    id = logid.get()
    pas= logpass.get()
    if id != "" and pas !="":
        cur.execute("SELECT Password FROM users WHERE ID = ?",[id])
        result = cur.fetchone()
        if result:
            if bcrypt.checkpw(pas.encode("utf8"),result[0]):
                messagebox.showinfo("Success","Login Successfully.")
                app.destroy()


                app2 = customtkinter.CTk()
                app2.geometry("350x450")
                app2.config(bg="#09112e")

                def loadt():
                    try:
                        with open("Tasks.txt","r") as f:
                            tasks = f.readlines()
                            for task in tasks:
                                listb.insert(END,task.strip())
                    except FileNotFoundError:
                        messagebox.showerror("Error","Cannot Load Tasks")
                            


                def savet():
                    with open("Tasks.txt","w") as f:
                        tasks = listb.get(0,END)
                        for task in tasks:
                            f.write(task+"\n")
                def delete():
                    select = listb.curselection()
                    if select:
                        listb.delete(select[0])
                        savet()
                    else:
                        messagebox.showerror("Error","Choose A Task to delete")


                def add():
                    list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
                    task = taske.get()
                    if task:
                        listb.insert(END,task)
                        taske.delete(0,END)
                        savet()
                    else:
                        messagebox.showerror("Error","Enter A Task")
                        




                font1 = ("Arial",30,"bold")
                font2 = ("Arial",18,"bold")
                font3 = ("Arial",10,"bold")

                title = customtkinter.CTkLabel(app2,font=font1,text="To-DO List",text_color="#fff",bg_color="#09112e")
                title.place(x=100,y=20)


                addb = customtkinter.CTkButton(app2,font=font2,command=add,text_color="#fff",hover_color="#06911f",text="Add Task",fg_color="#06911f",bg_color="#09112e",corner_radius=5,cursor = "hand2",width=120)
                addb.place(x=40,y=80)

                removeb = customtkinter.CTkButton(app2,command=delete,font=font2,text_color="#fff",hover_color="#96061c",text="Remove Task",fg_color="#96061c",bg_color="#09112e",corner_radius=5,cursor = "hand2")
                removeb.place(x=180,y=80)


                taske = customtkinter.CTkEntry(app2,font=font2,placeholder_text="Add Task",text_color="#000",fg_color="#fff",border_color="#fff",width=280,bg_color="#09112e")
                taske.place(x=40,y=120)

                listb = Listbox(app2,font=font3,width=39,height=16)
                listb.place(x=40,y=160)


                loadt()


                app2.mainloop()
         
            else:
                messagebox.showerror("Error","Invalid Password.")
    else:
        messagebox.showerror("Error","Enter All Fields.")
def login():
    fra1.destroy()
    fra2 = customtkinter.CTkFrame(app,bg_color="#001220",fg_color="#001220",width=470,height=360)
    fra2.place(x=0,y=0)
    loginl = customtkinter.CTkLabel(fra2,text="Login",font=font,text_color="#fff",bg_color="#001220")
    loginl.place(x=150,y=30)
    global logid
    global logpass
    logid = customtkinter.CTkEntry(fra2,text_color="#fff",fg_color="#001a2e",bg_color="#121111",font=font,border_color="#004780",placeholder_text="ID:",border_width=3,placeholder_text_color="#a3a3a3",width=200,height=50)
    logid.place(x=10,y=100)
    logpass = customtkinter.CTkEntry(fra2,text_color="#fff",fg_color="#001a2e",bg_color="#121111",font=font,border_color="#004780",placeholder_text="Password:",show = "*",border_width=3,placeholder_text_color="#a3a3a3",width=200,height=50)
    logpass.place(x=10,y=170)
    
    loginbb = customtkinter.CTkButton(fra2,command=loginb,width=180,height=35,text="Login",text_color="#fff",corner_radius=12,bg_color="#121111",fg_color="#004780",font=font,)
    loginbb.place(x=20,y=270)
    

        


    

def signup():
    id = ide.get()
    password= passw.get()
    if id !="" and password !="":
        cur.execute("SELECT ID FROM users WHERE ID =?",[id])
        if cur.fetchone() is not None:
            messagebox.showerror("Error","ID is Already Exists")
        else:
            enpass = password.encode("utf-8")
            hashp = bcrypt.hashpw(enpass,bcrypt.gensalt())
            cur.execute("INSERT INTO users VALUES(?,?)",[id,hashp])
            conn.commit()
            messagebox.showinfo("Success","Sign Up Successfully")
                           
                        
    else:
        messagebox.showerror("Error","Enter All Fields")
signupl = customtkinter.CTkLabel(fra1,text="Sign up",text_color="#fff",font=font,fg_color="#001220",bg_color="#001220",)
signupl.place(x=150,y=30)


ide =  customtkinter.CTkEntry(fra1,text_color="#fff",fg_color="#001a2e",bg_color="#121111",font=font,border_color="#004780",placeholder_text="ID:",border_width=3,placeholder_text_color="#a3a3a3",width=200,height=50)
ide.place(x=10,y=100)

passw =  customtkinter.CTkEntry(fra1,text_color="#fff",show="*",fg_color="#001a2e",bg_color="#121111",font=font,border_color="#004780",placeholder_text="Password:",border_width=3,placeholder_text_color="#a3a3a3",width=200,height=50)
passw.place(x=10,y=170)

font3 = ("Arial",13,"bold")

signupl = customtkinter.CTkLabel(fra1,font=font3,text="Already have an account ?",fg_color="#001220",bg_color="#121111",text_color="#fff")
signupl.place(x=10,y=220)
font4 = ("Arial",13,"bold","underline")

loginbu = customtkinter.CTkButton(fra1,font=font4,command=login,text="Login",text_color="#00bf77",fg_color="#001220",bg_color="#001220",hover_color="#001220",cursor="hand2",width=40)
loginbu.place(x=180,y=220)


signupb = customtkinter.CTkButton(fra1,command=signup,width=180,height=35,text="Sign Up",text_color="#fff",corner_radius=12,bg_color="#121111",fg_color="#004780",font=font,)
signupb.place(x=20,y=290)






app.mainloop()