# funções são objetos primários e por isso possuem várias peculiaridades
# elas podem ser passadas por parâmetro, podem ser criadas funções dentro de outras funções

def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"


def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)


# a função deve ser passada por referência, sem os ()
print(executar(mensagem, "João"))
