import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexão estabelecida com sucesso!")
        except mysql.connector.Error as err:
            print("Erro ao conectar:", err)

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

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Estoque")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.db = MySQLDatabase(host='localhost', user='root', password='root', database='estoque_db')
        self.db.connect()

        self.create_main_screen()
    
    #autenticando usuário
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Estoque")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.db = MySQLDatabase(host='localhost', user='root', password='root', database='estoque_db')
        self.db.connect()

        self.create_login_screen()
        
    def create_login_screen(self):
        self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.login_frame.pack(fill=tk.BOTH, expand=True)
                
        self.login_label = tk.Label(self.login_frame, text="Login de usuário:", font=("Helvetica", 16), bg="#f0f0f0")
        self.login_label.pack(pady=20)

        self.username_label = tk.Label(self.login_frame, text="Usuário:", bg="#f0f0f0")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Senha:", bg="#f0f0f0")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.check_login, bg="#4CAF50", fg="white")
        self.login_button.pack(pady=20)
        
    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.login_frame.destroy()
            self.create_main_screen()
        else:
            messagebox.showerror("Erro de login", "Credenciais inválidas.")   

    def create_main_screen(self):
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.main_frame, text="Controle de Estoque", font=("Helvetica", 18), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.add_button = tk.Button(self.main_frame, text="Adicionar Produto", command=self.open_add_product_screen, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.main_frame, text="Visualizar Estoque", command=self.open_view_stock_screen, bg="#007BFF", fg="white")
        self.view_button.pack(pady=10)
        
        self.logout_button = tk.Button(self.main_frame, text="Sair", command=self.logout, bg="#FF5733", fg="white")
        self.logout_button.pack(pady=10)
        
    def logout(self):
        self.main_frame.destroy()
        self.create_login_screen()

    def open_add_product_screen(self):
        self.main_frame.destroy()

        self.add_product_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.add_product_frame.pack(fill=tk.BOTH, expand=True)

        self.add_title_label = tk.Label(self.add_product_frame, text="Adicionar Produto", font=("Helvetica", 18), bg="#f0f0f0")
        self.add_title_label.pack(pady=20)

        self.product_name_label = tk.Label(self.add_product_frame, text="Nome do Produto:", bg="#f0f0f0")
        self.product_name_label.pack()

        self.product_name_entry = tk.Entry(self.add_product_frame)
        self.product_name_entry.pack()

        self.product_quantity_label = tk.Label(self.add_product_frame, text="Quantidade:", bg="#f0f0f0")
        self.product_quantity_label.pack()

        self.product_quantity_entry = tk.Entry(self.add_product_frame)
        self.product_quantity_entry.pack()

        self.add_button = tk.Button(self.add_product_frame, text="Adicionar", command=self.add_product, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=10)

        self.back_button = tk.Button(self.add_product_frame, text="Voltar", command=self.back_to_main, bg="#007BFF", fg="white")
        self.back_button.pack(pady=10)

    def add_product(self):
        product_name = self.product_name_entry.get()
        product_quantity = int(self.product_quantity_entry.get())

        if product_name and product_quantity > 0:
            query = f"INSERT INTO produtos (nome, quantidade) VALUES ('{product_name}', {product_quantity})"
            self.db.execute_query(query)
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            self.product_name_entry.delete(0, tk.END)
            self.product_quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, insira informações válidas.")

    def open_view_stock_screen(self):
        self.main_frame.destroy()

        self.view_stock_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.view_stock_frame.pack(fill=tk.BOTH, expand=True)

        self.view_title_label = tk.Label(self.view_stock_frame, text="Visualizar Estoque", font=("Helvetica", 18), bg="#f0f0f0")
        self.view_title_label.pack(pady=20)

        self.tree = ttk.Treeview(self.view_stock_frame, columns=("Nome", "Quantidade"))
        self.tree.heading("#1", text="Nome")
        self.tree.heading("#2", text="Quantidade")
        self.tree.pack()

        self.populate_stock_tree()

        self.back_button = tk.Button(self.view_stock_frame, text="Voltar", command=self.back_to_main, bg="#007BFF", fg="white")
        self.back_button.pack(pady=10)

    def populate_stock_tree(self):
        query = "SELECT nome, quantidade FROM produtos"
        cursor = self.db.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert("", "end", values=row)

        cursor.close()

    def back_to_main(self):
        if hasattr(self, 'add_product_frame'):
            self.add_product_frame.destroy()
        
        if hasattr(self, 'view_stock_frame'):
            self.view_stock_frame.destroy()
        self.create_main_screen()

    def __del__(self):
        if self.db:
            self.db.disconnect()

if __name__ == "__main__":
    root = tk.Tk()
    app = StockApp(root)
    root.mainloop()
