lista = []

for i in range(10):
    lista.append(i)


print(lista)
copia_lista = lista.copy()  # copia da lista

print(copia_lista)

print(lista.clear())  # limpar a lista

cores = ["verde", "vermelho", "azul", "azul"]

print(cores.count("azul"))  # conta quantas vezes aparece

# insere diversos objetos na lista diretamente
print(cores.extend(["amarelo", "marrom"]))

# mostra a posição da primeira ocorrência do objeto informado
print(cores.index("vermelho"))

cores.pop()  # remove o último elemento da lista se não foi informado indice
print(cores)

cores.remove("amarelo")  # remove o elemento passando o valor
print(cores)

cores.reverse()  # inverse os elementos da lista, espelhando-os
print(cores)

cores.sort()  # ordena os elementos da lista em ordem alfabética
print(cores)

cores.sort(reverse=True)  # deixa ao contrário da ordem alfabética
print(cores)

cores.sort(key=lambda x: len(x))  # ordena pelo tamanho da string
print(cores)
