# 📌 Tarefa:
# Copiar e rodar o código no VS Code.
# 
# Testar cada função do menu com pelo menos 2 clientes.
# 
# Tentar apagar um cliente que não existe e ver o que acontece.
# 
# (Desafio) Adicionar um campo “Data de nascimento” à tabela e adaptar todas as funções.

import sqlite3

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# Criar a tabela de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    data_nascimento TEXT DEFAULT NULL
)
""")

conexao.commit()
conexao.close()

def menu():
    print("\nAGENDA DE CLIENTES")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Deletar cliente")
    print("5 - Sair")

def adicionar_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")

    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO clientes (nome, telefone, email, data_nascimento) VALUES (?, ?, ?, ?)",
                   (nome, telefone, email, data_nascimento))

    conexao.commit()
    conexao.close()

    print("Cliente adicionado com sucesso!")


def listar_clientes():
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente encontrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Telefone: {cliente[2]} | E-mail: {cliente[3]}")

    conexao.close()


def atualizar_cliente():
    id_cliente = input("ID do cliente a ser atualizado: ")

    novo_nome = input("Novo nome: ")
    novo_telefone = input("Novo telefone: ")
    novo_email = input("Novo e-mail: ")

    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("UPDATE clientes SET nome = ?, telefone = ?, email = ? WHERE id = ?",
                   (novo_nome, novo_telefone, novo_email, id_cliente))

    conexao.commit()
    conexao.close()

    print("Cliente atualizado com sucesso!")


def deletar_cliente():
    id_cliente = input("ID do cliente a ser deletado: ")

    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))

    conexao.commit()
    conexao.close()

    print("Cliente deletado com sucesso!")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        atualizar_cliente()
    elif opcao == "4":
        deletar_cliente()
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

