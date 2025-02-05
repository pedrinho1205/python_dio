import sqlite3
from pathlib import Path 

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite") #criando um banco de dados e realizando conexao
print(conexao)

cursor = conexao.cursor() #o cursor permite executar comandos sql, ele fica dentro da variavel conexao
cursor.row_factory = sqlite3.Row #altera a forma como os resultados das consultas são retornados, faz com que cada linha retornada pela consulta seja acessível como um dicionário.

def criar_tabela(cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))") #criando uma tabela
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (data)) #para se inserir dados em uma tabela é interessante usar querys preparadas (?), para evitar maiores problemas
    conexao.commit() #o commit deve ser usado para confirmar as mudanças e gravá-las definitivamente no banco de dados, se nao usar as informações serão perdidas

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data) #atualiza dado da tabela
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?;", data) #exclui registro da tabela
    conexao.commit()

def inserir_varios_usuarios(conexao, cursor, dados): #inserir vários usuarios
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?);", dados)
    conexao.commit()

# dados = [
#     ("Guilherme", "guilherme@gmail.com"),
#     ("Pedro", "pedro@gmail.com"),
#     ("Maria", "maria@gmail.com"),
#     ("João", "joão@gmail.com"),
# ]
# inserir_varios_usuarios(conexao, cursor, dados)

def recuperar_cliente(cursor, id): #realizar consulta única 
    cursor.execute("SELECT * FROM clientes WHERE id = ?;", (id,))
    resultado = cursor.fetchone() #retorna apenas uma linha do resultado de um SELECT. Se não houver mais linhas, retorna None.
    return resultado

print(recuperar_cliente(cursor, 2))

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente)) #convertendo ara dicionario para melhor visualização

#gerenciando transações
try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Paulo", "paulo@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ocorreu um erro {exc}")
    conexao.rollback() # essa função desfaz qualquer alteração feita dentro de uma transação que ainda não foi confirmada (commit)
