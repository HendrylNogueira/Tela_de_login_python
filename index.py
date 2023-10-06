from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

#  criando a janela
janela = Tk()
janela.title('Nog System')
janela.geometry('1000x600')
janela.configure(background='white')
janela.resizable(width=False, height=False)

#  Carregando a imagem
logo = PhotoImage(file='icons/logo.png')
icone = PhotoImage(file='icons/icone.png')

#  criando direita e esquerda da tela

LeftFrame = Frame(janela, width=400, height=600, bg='BLACK', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=595, height=600, bg='BLACK', relief='raise')
RightFrame.pack(side=RIGHT)

#  Posicionando a imagem

LogoLabel = Label(LeftFrame, image=logo, bg='GREEN')
LogoLabel.place(x=20, y=80)

#  Posicionando login

# Nome login
UserLabel = Label(RightFrame, text='Username:', font=('Arial', 20), bg='BLACK', fg='GREEN')
UserLabel.place(x=5, y=100)

# Entrada de dados
UserEntry = Entry(RightFrame, width=30)
UserEntry.place(x=145, y=111)

# Nome senha
PassLabel = Label(RightFrame, text='Password:', font=('Arial', 20), bg='BLACK', fg='GREEN')
PassLabel.place(x=5, y=150)

# Entrada de dados
PassEntry = Entry(RightFrame, width=30, show='•')
PassEntry.place(x=145, y=161)

#  Criando os botões


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    database.cursor.execute('''
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    ''', (User, Pass))
    print('Selecionou')

    VerifyLogin = database.cursor.fetchone()
    try:
        if User in VerifyLogin and Pass in VerifyLogin:
            messagebox.showinfo(title='Login Info', message='Acesso confirmado. Bem vindo!')

    except:
        messagebox.showerror(title='Login info', message='Acesso negado. Verifique seu cadastro e tente novamente.')


# Botão de Login
LoginButton = ttk.Button(RightFrame, text='Login', width=20, command=Login)
LoginButton.place(x=146, y=200)


def Register():
    # Retira os botões
    LoginButton.place(x=8888)
    RegisterButton.place(x=888)

    # Criando o nome
    NameLabel = Label(RightFrame, text='Nome:', font=('Arial', 20), bg='BLACK', fg='GREEN')
    NameLabel.place(x=5, y=5)

    NameEntry = ttk.Entry(RightFrame, width=39)
    NameEntry.place(x=94, y=16)

    # Criando o email
    EmailLabel = Label(RightFrame, text='Email:', font=('Arial', 20), bg='BLACK', fg='GREEN')
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=90, y=61)

    # Função que retira as informações da tela e volta para a tela inicial
    def BackToLogin():
        NameLabel.place(x=8888)
        NameEntry.place(x=8888)
        EmailLabel.place(x=8888)
        EmailEntry.place(x=8888)
        Back.place(x=8888)
        NewRegister.place(x=8888)

        LoginButton.place(x=146, y=200)
        RegisterButton.place(x=146, y=235)

    # Criando Botão Voltar
    Back = ttk.Button(RightFrame, text='Back', width=20, command=BackToLogin)
    Back.place(x=146, y=200)

    # Função que pega os valores que o usuário digitou e manda para o banco de dados
    def RegisterToDatabase():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        UserName = UserEntry.get()
        Password = PassEntry.get()

        if Name == '' or Email == '' or UserName == '' or Password == '':
            messagebox.showerror(title='Redister error', message='Há campos vazios. Preencha todos os campos. ')

        else:
            database.cursor.execute('''
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            ''', (Name, Email, UserName, Password))
            database.conn.commit()
            messagebox.showinfo(title='Register info', message='Register Successful')

    # Criando o botão de novo cadastro
    NewRegister = ttk.Button(RightFrame, text='New NewRegister', width=20, command=RegisterToDatabase)
    NewRegister.place(x=146, y=235)


# Botão de Registrar
RegisterButton = ttk.Button(RightFrame, text='Register', width=20, command=Register)
RegisterButton.place(x=146, y=235)

janela.mainloop()

# Enviado para o GitHub
