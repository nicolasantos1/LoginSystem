#IMPORTAR BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#CRIAÇÃO DA JANELA PRINCIPAL
jan = Tk()
jan.title("DP Systems = Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=FALSE, height=FALSE)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

#Adicionar logo
logo = PhotoImage(file="icons/logo.png")

LeftFramame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFramame.pack(side=LEFT) 

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

logoLabel = Label(LeftFramame, image=logo, bg="MIDNIGHTBLUE")
logoLabel.place(x=0, y=50)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

passLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
passLabel.place(x=5, y=140)

passEntry = ttk.Entry(RightFrame, width=30, show="•")
passEntry.place(x=150, y=150)

def Login():
    User = UserEntry.get()
    Pass = passEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE User = ? AND Password = ?
    """, (User, Pass))
    print("Selecionou")
    verifyLogin = DataBaser.cursor.fetchone()
    try:
        if(User in verifyLogin and Pass in verifyLogin):
            messagebox.showinfo(title="Login Info", message="Login realizado com sucesso!")
    except:
        messagebox.showinfo(title="Login Error", message="Login ou senha incorretos!")
#Botão de login
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #removendo widgets de login
    LoginButton.place(x=5000)
    registerButton.place(x=5000)
    #Inserindo widgets de cadastro
    nomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    nomeLabel.place(x=5, y=5)

    nomeEntry = ttk.Entry(RightFrame, width=39)
    nomeEntry.place(x=100, y=16)    

    emailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    emailLabel.place(x=5, y=55)

    emailEntry = ttk.Entry(RightFrame, width=39)
    emailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = nomeEntry.get()
        Email = emailEntry.get()
        User = UserEntry.get()
        Pass = passEntry.get()

        if (Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Todos os campos devem ser preenchidos!")
            return
        
        DataBaser.cursor.execute("""
        INSERT INTO Users (Name, Email, User, Password) VALUES (?, ?, ?, ?)
        """, (Name, Email, User, Pass))
        DataBaser.conn.commit()
        messagebox.showinfo(title="Register Info", message="Conta criada com sucesso!")
    
    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        #removendo widgets de cadastro
        nomeLabel.place(x=5000)
        nomeEntry.place(x=5000)
        emailLabel.place(x=5000)
        emailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Inserindo widgets de login
        LoginButton.place(x=100, y=225)
        registerButton.place(x=125, y=260)


    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

registerButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
registerButton.place(x=125, y=260)


jan.mainloop()