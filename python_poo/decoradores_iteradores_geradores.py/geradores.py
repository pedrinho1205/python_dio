# geradores são tipos de iteradores que ajudam a economizar memória do pc
# ele acessa cada valor de uma vez e não todos de uma vez
# uma vez que o item gerado é consumido, ele não pode ser acessado novamente
# de maniera geral, quando é um código simples

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)
