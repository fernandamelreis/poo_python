import tkinter as tk
import mysql.connector

# Função para verificar o login
def verificar_login():
    username = entry_username.get()
    password = entry_password.get()

    # Substitua os valores abaixo com as configurações do seu banco de dados
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'projeto'
    }

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        user = cursor.fetchone()

        if user:
            label_status.config(text="Login bem-sucedido!", fg="green")
        else:
            label_status.config(text="Usuário ou senha incorretos.", fg="red")

        connection.close()
    except mysql.connector.Error as err:
        label_status.config(text=f"Erro: {err}", fg="red")

# Configuração da janela
root = tk.Tk()
root.title("Login")

# Campos de entrada
label_username = tk.Label(root, text="Usuário:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Senha:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Botão de login
btn_login = tk.Button(root, text="Login", command=verificar_login)
btn_login.pack()

# Status do login
label_status = tk.Label(root, text="", fg="black")
label_status.pack()

root.mainloop()
