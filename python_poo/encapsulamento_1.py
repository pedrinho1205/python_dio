class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo  # o _ indica que o atributo é privado

    def sacar(self, valor):
        self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo


conta = Conta(100)
print(conta.depositar(100))
