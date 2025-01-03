print(set([1, 2, 3, 1, 3, 4]))  # elimina todos os elementos repetidos da lista

print(set("abacaxi"))  # elimina todas as letras repetidas da string

linguagens = {"python", "java", "python"}  # declarando conjuntos
print(linguagens)

numeros = {1, 2, 3, 2}
numeros = list(numeros)  # convertendo conjunto para lista

for numero in numeros:  # os conjuntos tambem sao objetos iteraveis
    print(numero)

for indice, numero in enumerate(numeros):
    print(f"{indice}: {numero}")
