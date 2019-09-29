import sqlite3
class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('Banco.db')
        self.createTables()
    def createTables(self):
        cursor = self.conexao.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS clientes2 (ID integer PRIMARY KEY, nome text NOT NULL, login text NOT NULL, senha text NOT NULL, email text NOT NULL, tel text)""")
        self.conexao.commit()
        cursor.close()
