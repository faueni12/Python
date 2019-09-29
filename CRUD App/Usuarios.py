from Banco import Banco
import sqlite3

class Usuarios(object):
    def __init__(self, ID='', nome='', login='', senha='', email='', tel=''):
        self.info={}
        self.ID = ID
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        self.tel = tel

    def insertUser(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute("""INSERT INTO clientes2 (nome, login, senha, email, tel) VALUES (?, ?, ?, ?, ?)""", (self.nome, self.login, self.senha, self.email, self.tel))
            banco.conexao.commit()
            cursor.close()
            return "Registered successfully!"
        except:
            return "Registration error"

    def updateUser(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute("""update clientes2 set nome = ?, login = ?, senha = ?, email = ?, tel = ? where ID = ?""", (self.nome, self.login, self.senha, self.email, self.tel, self.ID))
            banco.conexao.commit()
            cursor.close()
            return "Updated"
        except:
            return "Update error"

    def pesquisarUser(self, Id):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute("""SELECT * FROM clientes2 WHERE ID = ?""", (Id,))
            for linha in cursor.fetchall():
                self.ID = linha[0]
                self.nome = linha[1]
                self.login = linha[2]
                self.senha = linha[3]
                self.email = linha[4]
                self.tel = linha[5]
                condicoes = [self.ID == '', self.nome == '', self.login == '',
                             self.senha == '', self.email == '', self.tel == '']

            cursor.close()
            if all(condicoes):
                return "Search error"
            else:
                return "Successfully seeked!"
        except:
            return "Search error"

    def deletarUser(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute("""DELETE FROM clientes2 WHERE ID = ?""", (self.ID))
            banco.conexao.commit()
            cursor.close()
            return "Sucessfully deleted!"
        except:
            return "Error deleting user"
