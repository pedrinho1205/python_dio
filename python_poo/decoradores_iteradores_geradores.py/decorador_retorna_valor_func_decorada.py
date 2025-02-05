def meu_decorador(funcao):
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
