class Estudante:
    escola = "DIO"  # objeto de classe: é compartilhado entre as instancias, é unica para todos os objetos

    def __init__(self, nome, numero):
        self.nome = nome  # objeto de instancia: pertence a cada instância
        self.numero = numero  # o self é a instância do objeto

    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovana", 2)
