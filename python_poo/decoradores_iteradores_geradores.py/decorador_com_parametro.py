# essa função faz a função de um decorador, ou seja, de adicionar funcionalidades a uma funcao retornando ela com essas novas funcionalidades
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")


ola_mundo("João")
