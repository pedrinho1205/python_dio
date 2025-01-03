frutas = ["maça", "pera", "laranja", "banana"]
print(frutas)

print(frutas[-1])

numeros = list(range(10))
print(numeros)

letras = list("aeiou")
print(letras)

print(letras[:2])
print(letras[2:])

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][1])
print(matriz[-1][-1])

carros = ["gol", "saveiro", "golf", "jetta"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
