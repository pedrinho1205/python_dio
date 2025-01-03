def somar(a, b):
    return a + b


def exibir_resultado(a, b, somar):
    resultado = somar(a, b)
    print(f"A soma de {a} + {b} é {resultado}")


exibir_resultado(10, 10, somar)
