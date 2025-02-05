# um método de classe aponta pra classe e pode acessar e modificar a classe, ele recebe um parametro que aponta pra classe
# um método estatico nao recebe parametro nenhum, mas tambem aponta pra classe e nao para o objeto, entao ele nao pode acessar nem modificar o estado da classe
# usamos os metodos de classe para criar métodos de fábrica (retorna instancia da classe) e metodos estaticos para funcoes utilitarias
# para transformar um método em um método de classe se usa o decorador @classmethod passando como parametro cls, que se referencia a propria classe

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # decorador que transforma o método em um método de classe
    def criar_a_partir_ano_nascimento(cls, nome, ano_nascimento):
        idade = 2025 - ano_nascimento  # retorna uma nova instancia da classe
        return cls(nome, idade)

    @staticmethod  # método estático
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_a_partir_ano_nascimento("Guilherme", 2005)  # método de classe
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))  # método estático
print(Pessoa.e_maior_idade(8))
