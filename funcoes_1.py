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
