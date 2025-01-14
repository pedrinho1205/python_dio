# interfaces definem o que uma classe deve fazer e não como
# é como se fosse um padrão
# o conceito de interface é definir um contrato onde são declarados os métodos e suas respectivas assinaturas
# para criar os contratos, usamos classes abstratas, as quais nao podem ser instanciadas
# método abstrato é um metodo que todas as classes filhas vão ser obrigadas a implementá-lo, a partir do momento que se cria um metodo abstrato a classe se torna abstrata tambem e nao pode mais ser instanciada diretamente
# se existe uma classe abstrata, isso obriga que todas as classes filhas tenham os métodos que existem na classe abstrata, pois a classe abstrata é um padrão


# deve-se importar o módulo ABC
from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):  # controle remoto é uma extensão de ABC
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property  # cria obrigatoriedade de criar esse métodos nas classes filhas
    @abstractproperty
    def marca(self):
        pass


class ControleTv(ControleRemoto):
    def ligar(self):  # como ControleTv é filha de Controle remoto que é uma classe abstrata ela é obrigada a implementar os 2 métodos abstratos
        print("Ligando a Tv...")
        print("Ligada")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar condicionado...")
        print("Ligado")

    def desligar(self):
        print("Desligando o ar condicionado...")
        print("Desligado")

    @property
    def marca(self):
        return "LG"


controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
