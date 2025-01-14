class Carro:  # metodo construtor, sempre é o primeiro a ser executado quando um objeto é instanciado, ou seja, no inicio do processo de instanciação do objeto
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def __del__(self):  # executado ao final do processo de instanciacao do objeto
        print("Destruindo a classe...")

    def buzinar(self):
        print("bibi")

    def __str__(self):
        print(f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}")


c1 = Carro("Saveiro", "Volkswagem", 2003)
c1.__str__()
c1.buzinar()
