import tkinter as tk
import mysql.connector

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    username = entry_username.get()
    password = entry_password.get()

    # Substitua os valores abaixo com as configurações do seu banco de dados
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'projeto_teste'
    }

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()

        label_status.config(text="Usuário cadastrado com sucesso!", fg="green")

        connection.close()
    except mysql.connector.Error as err:
        label_status.config(text=f"Erro: {err}", fg="red")

# Configuração da janela
root = tk.Tk()
root.title("Cadastro Simulado")

# Campos de entrada
label_username = tk.Label(root, text="Novo Usuário:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Senha:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Botão de cadastro
btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_usuario)
btn_cadastrar.pack()

# Status do cadastro
label_status = tk.Label(root, text="", fg="black")
label_status.pack()

root.mainloop()
