# os decoradors servem para colocar uma personalização de comportamento em uma funcionalidade

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
    # envelope irá substituir a função original ola_mundo, ele é a função decorada
    return envelope


@meu_decorador  # açucar sintax, para ficar mais facil, funciona com a mesma lógica
def ola_mundo():
    print("Olá mundo!")


# ola_mundo = meu_decorador(ola_mundo)  # a função ola_mundo está sendo alterada
ola_mundo()
