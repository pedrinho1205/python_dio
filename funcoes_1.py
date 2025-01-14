def exibir_mensagem(nome):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem(nome="Pedro")


def calcular_total(numeros):
    return sum(numeros)


def sucessor_antecessor(numero):
    sucessor = numero + 1
    antecessor = numero - 1

    return sucessor, antecessor


print(calcular_total([10, 20, 34]))
print(sucessor_antecessor(10))


def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso {marca}/{modelo}/{ano}/{placa}")


print(salvar_carro(marca="fiat", modelo="palio", ano="1999", placa="ABC-1234"))

# *args recebe uma tupla e **kargs recebe um dicionário (chave e valor)
# existem parâmetros nomeados e parâmetros por posição ao chamar a função
# os parâmetros por posição são passados diretamente, sem chave(nome de variável)
# ex: salvar_carro("fiat", "palio", "1999")
# estrutura: def salvar_carro(marca, modelo, ano, /, placa, motor, combustivel):
# antes da barra, obrigatoriamente os parametros devem ser passados por posição
# depois da barra, podem ser passados por posição ou nomeados
# caso queira que todos os parametros sejam passados por nome, deve-se inserir um * na função
# ex: def salvar_carro(*, modelo, ano, placa, marca, motor):
# em virtude do *, todos os parametros devem ser exibidos por nome


def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# os 3 primeiros antes da barra devem ser por posicao, os 3 depois do * devem ser por nome
criar_carro("palio", 1999, "ABC-1234", marca="fiat",
            motor="1.0", combustivel="Gasolina")
