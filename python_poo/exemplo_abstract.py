from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def se_locomover(self):
        pass


class Dev(Pessoa):
    def falar(self):
        print("Dá pra descarregar")
        print("Vai toma no cu")

    def se_locomover(self):
        print("Dev se locomove de bicicleta")


class Pedrao(Pessoa):
    def falar(self):
        print("Sp vota muito mal")

    def se_locomover(self):
        print("Pedrao se locomove de Renault Fluence")


class Stumble(Pessoa):
    def falar(self):
        print("Stuuuuummmmblee")
        print("Faz o L ai")
        print("Where is dev?")
        print("Como pode?")

    def andar(self):
        print("Stumble anda a pé")
