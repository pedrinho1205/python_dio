# iterador é um objeto que contém um número contável de valores que podem ser iterados, uma sequencia de valores
# bastante usado para ler arquivos grandes
# para transformar uma classe em um objeto iterável é necessário que se definam 2 métodos, o __iter__ e o __next__

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self  # retorna o objeto

    # retorna o próximo elemento da sequência. Quando não há mais elementos, ele levanta a exceção StopIteration para indicar que a iteração terminou.
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            # encerra o loop de iteração quando der erro, ou seja, quando não houver mais números na lista
            raise StopIteration


for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)
