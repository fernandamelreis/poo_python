import mysql.connector
import tkinter as tk
from tkinter import messagebox

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexão estabelecida com sucesso!")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão fechada.")

    def execute_query(self, query):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Integração do MySQL + Tkinter")

        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'users'
        }

        self.db = MySQLDatabase(**self.db_config)
        self.db.connect()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Nome:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        
        self.label = tk.Label(self.root, text="Senha:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Inserir", command=self.insert_data)
        self.button.pack()

    def insert_data(self):
        nome = self.entry.get()
        senha = self.entry.get()
        query = f"INSERT INTO users (username, password) VALUES ('{nome}', '{senha}')"
        self.db.execute_query(query)
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
        
    def __del__(self):
        if self.db:
            self.db.disconnect()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
