nome = "Pedro"
idade = 18
profissao = "estudante"
curso = "Python"
valor = 45.89684

dados = {"nome": "Pedro", "idade": 18}

print(f"Olá, me chamo {nome} e tenho {idade} anos. Sou {
      profissao} e estou matriculado no curso de {curso}.")

print("Nome: %s" % (nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Valor {valor:10.2f}")
