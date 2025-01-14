class Foo:
    def __init__(self, x=None):
        self._x = x

    @property  # o property permite usar o método como um atributo, ele é uma forma de acessar o self._x que é privado, ele é o get
    def x(self):
        return self._x or 0

    @x.setter  # permite alterar o atributo self._x que é privado, uma modificação, é o set
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1
        # del self._x


foo = Foo(10)
print(foo.x)
foo.x = 10  # é o valor que é informado no setter, é o value
print(foo.x)  # chama o property, ou seja, exibe o valor
del foo.x
print(foo.x)
