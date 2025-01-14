contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": "28"},
    "giovanna@gmail.com": {"nome": "Giovana", "idade": "18"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": "35"},
}

print(contatos.clear())  # limpa o dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": "28"},
    "giovanna@gmail.com": {"nome": "Giovana", "idade": "18"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": "35"},
}

copia = contatos.copy()  # cria copia do dicionario
print(copia)

dict.fromkeys(["nome", "telefone"])  # cria dicionario com valores padrões

# se ele nao encontrar a chave ele retorna none e nao da erro
contatos.get("chave")

print(contatos.items())  # retorna uma lista de tuplas com as chaves e valores

print(contatos.keys())  # retorna as chaves do dicionario

# remove uma chave do dicionario, se ela nao existir retorna o valor vazio
print(contatos.pop("chappie@gmail.com", "não encontrado"))
print(contatos.popitem())  # remove na ordem

contato = {"nome": "Guilherme", "telefone": "3333-2221"}
# se a chave existir, não altera o valor, se nao existir ele cria com o valor
print(contato.setdefault("nome", "Giovana"))


# altera a chave
print(contatos.update({"guilherme@gmail.com": {"nome": "Gui"}}))
for chave in contatos:
    print(chave, contatos[chave])

print(contatos.values())  # retorna os valores das chaves do dicionario

# retorna se uma chave esta no dicionario
resultado = "guilherme@gmail.com" in contatos
print(resultado)

resultado = "nome" in contatos["guilherme@gmail.com"]
print(resultado)

del contatos["guilherme@gmail.com"]["nome"]
for chave in contatos:
    print(chave, contatos[chave])

print(contatos.update(
    {"guilherme@gmail.com": {"nome": "Guilherme", "idade": 28}}))

for chave in contatos:
    print(chave, contatos[chave])
