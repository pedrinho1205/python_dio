pessoa = {"nome": "Guilherme", "idade": 28}  # chave: nome, valor: guilherme
print(pessoa["nome"])

pessoa = dict(nome="Guiherme", idade=28)  # criando dicionario com classe dict

pessoa["telefone"] = "3333-1234"  # adicionando nova chave

# dicionario aninhado

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": "28"},
    "giovanna@gmail.com": {"nome": "Giovana", "idade": "18"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": "35"},
}

print(contatos["guilherme@gmail.com"]["nome"])

for chave in contatos:
    print(chave, contatos[chave])
