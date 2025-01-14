# polimorfismo: um método de mesmo nome pode ter vários comportamentos, funciona na herança
class Passaro:  # classe pai
    def voar(self):  # esse método será sobrescrito nas outras classes
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        # super().voar()  # chamando o método voar da classe pai
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


def plano_voo(obj):  # esse método demonstra o polimorfismo. Ele recebe o objeto e executa o método conforme o objeto recebido
    obj.voar()


# esta vazio pois nao possui contrutor, não possui atributos
# passaros = [Pardal(), Avestruz()]

# for passaro in passaros:
#    plano_voo(passaro)
p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
