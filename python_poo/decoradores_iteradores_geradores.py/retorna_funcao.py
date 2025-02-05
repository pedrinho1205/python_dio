def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        return a / b

    # mesma coisa do switch case
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return multiplicacao
        case "/":
            return divisao


# deve ser passado os argumentos das funções internas junto, pois a funcao calculadora chama outras funções
print(calculadora("+")(2, 2))
op = calculadora("-")
print(op(2, 2))
