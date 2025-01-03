conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))  # faz a união dos conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.intersection(conjunto_b))  # intersecção
# diferença, numero que em a e nao esta em b
print(conjunto_a.difference(conjunto_b))

# elementos que nao estao na intersecção
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
# verifica se conjunto a esta contido no conjunto b
print(conjunto_a.issubset(conjunto_b))

sorteio = {1, 23}
sorteio.add(25)  # adiciona elementos
sorteio.add(42)
print(sorteio)

sorteio.copy()  # cria uma cópia do set
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1)  # descarta o numero passado
print(numeros)

numeros.pop()  # elimina o primeiro valor do set
print(numeros)

numeros.remove(2)
