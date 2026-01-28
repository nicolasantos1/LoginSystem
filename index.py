#IMPORTAR BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#CRIAÇÃO DA JANELA PRINCIPAL
jan = Tk()
jan.title("DP Systems = Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=FALSE, height=FALSE)
jan.attributes("-alpha", 0.9)

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

passEntry = ttk.Entry(RightFrame, width=30)
passEntry.place(x=150, y=150)

#Botão de login
LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

registerButton = ttk.Button(RightFrame, text="Register", width=20)
registerButton.place(x=125, y=260)

jan.mainloop()