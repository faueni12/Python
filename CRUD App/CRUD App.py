from Usuarios import Usuarios
from tkinter import *

class app():
    def __init__(self, toplevel):

        self.fontetitulo = ('Cambrias', '20', 'bold')
        self.fontenormal = ('Cambrias', '15')
        self.fonte_ex = ('Cambrias', '10')

        self.retangulo = Frame(toplevel)
        self.retangulo['bg'] = 'lightblue'
        self.retangulo.place(x=60, y=60, width = 500, height = 400)
        self.retangulo2 = Frame(self.retangulo)
        self.retangulo2['bg'] = 'moccasin'
        self.retangulo2.place(x=10, y=10, width=480, height=380)

        x, y = 40, 90
        self.titulo = Label(toplevel, text='Registration', font=self.fontetitulo, bg='moccasin')
        self.titulo.place(x=240 - x, y=y-10)
        
        self.lblID = Label(self.retangulo2, font=self.fontenormal, text='ID:', bg='moccasin')
        self.lblID.place(x=x+260, y=y)
        self.ID = Entry(self.retangulo2, width=6)
        self.ID.focus()
        self.ID.place(x=x+290, y=y+6)
        self.btn_buscar = Button(self.retangulo2, relief="groove", text='Search', bg="#F4A460", padx=15, pady=2)
        
        self.btn_buscar.bind('<Button-1>', self.buscarUser)
        self.btn_buscar.bind('<Return>', self.buscarUser)
        self.btn_buscar.bind('<Enter>', self.alterarbg_btn_buscar)
        self.btn_buscar.bind('<Leave>', self.voltarbg_btn_buscar)
        self.btn_buscar.bind('<FocusIn>', self.focusinbg_btn_buscar)
        self.btn_buscar.bind('<FocusOut>', self.voltarbg_btn_buscar)

        self.btn_buscar.place(x=x+340, y=y)
        
        self.nomelab = Label(self.retangulo2, font=self.fontenormal, text='Name:', bg='moccasin')
        self.nomelab.place(x=x, y=y)
        self.nome = Entry(self.retangulo2)
        self.nome.place(x=x+70, y=y+6)

        self.loginlab = Label(self.retangulo2, font=self.fontenormal, text='Login:', bg='moccasin')
        self.loginlab.place(x=x, y=y+35)
        self.login = Entry(self.retangulo2)
        self.login.place(x=x+70, y=y+41)


        self.senhalab = Label(self.retangulo2, font=self.fontenormal, text='Passw:', bg='moccasin')
        self.senhalab.place(x=x, y=y+70)
        self.senha = Entry(self.retangulo2, show='*')
        self.senha.place(x=x+70, y=y+76)


        self.emaillab = Label(self.retangulo2, font=self.fontenormal, text='Email:', bg='moccasin')
        self.emaillab.place(x=x, y=y+105)

        email_deu = janela.register(self.stringemail)
        self.email = Entry(self.retangulo2, validate='key', validatecommand=(email_deu, '%P'))
        self.email.place(x=x+70, y=y+111)
        self.emailex = Label(self.retangulo2, font=self.fonte_ex, text='ex: yourmail@gmail.com', bg='moccasin', fg='gray')
        self.emailex.place(x=x+200, y=y+108)

        
        self.tellab = Label(self.retangulo2, font=self.fontenormal, text='Phone:', bg='moccasin')
        self.tellab.place(x=x, y=y+140)
        tel_deu = janela.register(self.stringtel)
        self.tel = Entry(self.retangulo2, validate='key', validatecommand=(tel_deu, '%P'))
        self.tel.place(x=x+70, y=y+146)
        self.telex = Label(self.retangulo2, font=self.fonte_ex, text='ex: 84987654321', bg='moccasin', fg='gray')
        self.telex.place(x=x+200, y=y+143)

        
        self.btn_inserir = Button(self.retangulo2, relief="groove", text='Insert', bg="#F4A460", padx=35, pady=3)
        
        self.btn_inserir.bind('<Button-1>', self.InsertUser)
        self.btn_inserir.bind('<Return>', self.InsertUser)
        self.btn_inserir.bind('<Enter>', self.alterarbg_btn_inserir)
        self.btn_inserir.bind('<Leave>', self.voltarbg_btn_inserir)
        self.btn_inserir.bind('<FocusIn>', self.focusinbg_btn_inserir)
        self.btn_inserir.bind('<FocusOut>', self.voltarbg_btn_inserir)
        
        self.btn_inserir.place(x=x, y=y+190)
        
        self.btn_atualizar = Button(self.retangulo2, relief="groove", text='Update', bg="#F4A460", padx=35, pady=3)
        
        self.btn_atualizar.bind('<Button-1>', self.UpdateUser)
        self.btn_atualizar.bind('<Return>', self.UpdateUser)
        self.btn_atualizar.bind('<Enter>', self.alterarbg_btn_atualizar)
        self.btn_atualizar.bind('<Leave>', self.voltarbg_btn_atualizar)
        self.btn_atualizar.bind('<FocusIn>', self.focusinbg_btn_atualizar)
        self.btn_atualizar.bind('<FocusOut>', self.voltarbg_btn_atualizar)


        self.btn_atualizar.place(x=x+116, y=y+190)

        self.btn_excluir = Button(self.retangulo2, relief="groove", text='Delete', bg="#F4A460", padx=35, pady=3)
        self.btn_excluir.bind('<Button-1>', self.deletUser)
        self.btn_excluir.bind('<Return>', self.deletUser)
        self.btn_excluir.bind('<Enter>', self.alterarbg_btn_excluir)
        self.btn_excluir.bind('<Leave>', self.voltarbg_btn_excluir)
        self.btn_excluir.bind('<FocusIn>', self.focusinbg_btn_excluir)
        self.btn_excluir.bind('<FocusOut>', self.voltarbg_btn_excluir)


        self.btn_excluir.place(x=x+246, y=y+190)

        self.mensagem = Label(self.retangulo2, text='', bg='moccasin', font=self.fonte_ex, fg='red')
        self.mensagem.place(x=x, y=y+250)
       
    #verificar espaços no email
    def stringemail(self, email):
        if ' ' in email:
            return False
        else:
            return True

    #verificar espaços no telefone
    def stringtel(self, tel):
        if ' ' in tel:
            return False
        else:
            if tel.isdigit():
                if len(tel) < 12:
                    return True
                else:
                    return False
            else:
                if len(tel) == 0: #se quiser apagar o primeiro digito.
                    return True
                else:
                    return False

    #mudar cores background dos botoes
    def alterarbg_btn_buscar(self, event):
        self.btn_buscar['bg']='limegreen'
    def voltarbg_btn_buscar(self, event):
        self.btn_buscar['bg'] = '#F4A460'
    def focusinbg_btn_buscar(self, event):
        self.btn_buscar['bg'] = '#008000'

    def alterarbg_btn_inserir(self, event):
        self.btn_inserir['bg']='limegreen'
    def voltarbg_btn_inserir(self, event):
        self.btn_inserir['bg'] = '#F4A460'
    def focusinbg_btn_inserir(self, event):
        self.btn_inserir['bg'] = '#008000'

    def alterarbg_btn_atualizar(self, event):
        self.btn_atualizar['bg']='limegreen'
    def voltarbg_btn_atualizar(self, event):
        self.btn_atualizar['bg'] = '#F4A460'
    def focusinbg_btn_atualizar(self, event):
        self.btn_atualizar['bg'] = '#008000'

    def alterarbg_btn_excluir(self, event):
        self.btn_excluir['bg']='red'
    def voltarbg_btn_excluir(self, event):
        self.btn_excluir['bg'] = '#F4A460'
    def focusinbg_btn_excluir(self, event):
        self.btn_excluir['bg'] = 'darkred'

    #------Definir funcionalidade botão: Inserir-----
    def InsertUser(self, event):
        user = Usuarios()

        user.nome = self.nome.get()
        user.login = self.login.get()
        user.senha = self.senha.get()
        user.email = self.email.get()
        user.tel = self.tel.get()

        #mostrar mensagem
        condicoes = [user.nome != '', user.login != '', user.senha != '',
                     user.email != '', user.tel != '']
        if all(condicoes):
            self.mensagem['text'] = user.insertUser()
        else:
            self.mensagem['text'] = 'Error registering user'
        self.ID.delete(0, END)
        self.nome.delete(0, END)
        self.login.delete(0, END)
        self.senha.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)
    #------Definir funcionalidade botão: Alterar-----
    def UpdateUser(self, event):
        user = Usuarios()
    
        user.ID = self.ID.get()
        user.nome = self.nome.get()
        user.login = self.login.get()
        user.senha = self.senha.get()
        user.email = self.email.get()
        user.tel = self.tel.get()

        #mostrar mensagem
        self.mensagem['text'] = user.updateUser()

        self.ID.delete(0, END)
        self.nome.delete(0, END)
        self.login.delete(0, END)
        self.senha.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)
        
    #------Definir funcionalidade botão: Excluir-----
    def deletUser(self, event):
        user = Usuarios()

        user.ID = self.ID.get()

        #mostrar mensagem
        self.mensagem['text'] = user.deletarUser()

        self.ID.delete(0, END)
        self.nome.delete(0, END)
        self.login.delete(0, END)
        self.senha.delete(0, END)
        self.email.delete(0, END)
        self.tel.delete(0, END)
    #------Definir funcionalidade botão: Inserir-----
    def buscarUser(self, event):
        user = Usuarios()

        Id = self.ID.get()
        #mostrar mensagem
        self.mensagem['text'] = user.pesquisarUser(Id)

        self.ID.delete(0, END)
        self.ID.insert(INSERT, user.ID)
        
        self.nome.delete(0, END)
        self.nome.insert(INSERT, user.nome)

        self.login.delete(0, END)
        self.login.insert(INSERT, user.login)
        
        self.senha.delete(0, END)
        self.senha.insert(INSERT, user.senha)
        
        self.email.delete(0, END)
        self.email.insert(INSERT, user.email)
        
        self.tel.delete(0, END)
        self.tel.insert(INSERT, user.tel)
        
janela = Tk()
janela.geometry('620x500+100+100')
janela.title('CRUD')
janela.maxsize(width=620, height=500)
janela.minsize(width=620, height=500)
app(janela)
janela.mainloop()
