# introspecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução

import functools


def meu_decorador(funcao):
    # usando esse decorador, a função que vem por argumento tem seu nome mantido
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)  # armazena o retorno de ola_mundo
        print("faz algo depois de executar")
        return resultado  # retorna o retorno de ola_mundo que é nome.upper()
    return envelope


@meu_decorador  # ola_mundo foi modificado pelo meu_decorador, onde ele se passa pela funcao envelope
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo("João")
print(resultado)
print(ola_mundo.__name__)
