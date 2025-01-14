class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1 or 0

    @property
    def num2(self):
        return self._num2 or 0

    def operacao(self, op):
        self._op = op

        if op == 1:
            soma = self._num1 + self._num2
            return soma
        elif op == 2:
            sub = self._num1 - self._num2
            return sub
        elif op == 3:
            mult = self._num1 * self._num2
            return mult
        elif op == 4:
            if self._num2 == 0:
                return "Erro: não é possível dividir por 0"
            else:
                div = self._num1 / self._num2
                return div
        else:
            return "Operação inválida!"


while True:
    print("""===Menu===
    1: soma
    2: subtração
    3: mutiplicação
    4: divisão
    5: sair
    """)

    op = int(input("Informe a operação: "))

    if op == 5:
        print("Saindo...")
        break
    else:
        num1 = float(input("Informe o número 1: "))
        num2 = float(input("Informe o número 2: "))

        c1 = Calculadora(num1, num2)
        print(f"Resultado: {c1.operacao(op)}")
