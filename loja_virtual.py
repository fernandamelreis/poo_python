import tkinter as tk
import mysql.connector

# Função para cadastrar um novo usuário
def cadastrar_produto():
    nome_produto = entry_nome_produto.get()
    desc_produto = entry_desc_produto.get()
    preco_produto = entry_preco_produto.get()
    codigo_de_barras = entry_codigo_de_barras.get()
    

    #configurando banco de dados
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'loja_virtual'
    }

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "INSERT INTO produtos (nome_produto, desc_produto, preco_produto, codigo_de_barras) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nome_produto, desc_produto, preco_produto, codigo_de_barras))
        connection.commit()

        label_status.config(text="Produto cadastrado com sucesso!", fg="green")

        connection.close()
    except mysql.connector.Error as err:
        label_status.config(text=f"Erro: {err}", fg="red")

# Configuração da janela
root = tk.Tk()
root.title("Cadastro de Produtos")

# Campos de entrada
label_nome_produto = tk.Label(root, text="Novo Produto:")
label_nome_produto.pack()
entry_nome_produto = tk.Entry(root)
entry_nome_produto.pack()

label_desc_produto = tk.Label(root, text="Descrição do Produto:")
label_desc_produto.pack()
entry_desc_produto = tk.Entry(root)
entry_desc_produto.pack()

label_preco_produto = tk.Label(root, text="Preço:")
label_preco_produto.pack()
entry_preco_produto = tk.Entry(root)
entry_preco_produto.pack()

label_codigo_de_barras = tk.Label(root, text="Código de barras:")
label_codigo_de_barras.pack()
entry_codigo_de_barras = tk.Entry(root)
entry_codigo_de_barras.pack()

# Botão de cadastro
btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_produto)
btn_cadastrar.pack()

# Status do cadastro
label_status = tk.Label(root, text="", fg="black")
label_status.pack()

root.mainloop()
