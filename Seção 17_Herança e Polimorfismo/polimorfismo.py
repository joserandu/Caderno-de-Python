"""
POLIMORFISMO

Poli -> Muitas
Morfos -> Formas

O overriding (sobrescrita de método) é a melhor representação do polimorfismo.
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplemented("A classe filha precisa implementar este método")

    def comer(self):
        print(f"{self.__nome} está comendo...")


"""
Com o raise a gente lança uma exeção, e estamos lançando uma mensagem para essa exeção. Nesse caso se alguma classe 
filha implementar esse método vai ser lançado uma exessão. 
"""


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala au au")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala au au")


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


# Testes
felix = Gato("Felix")
felix.comer()
felix.falar()

pluto = Cachorro("Pluto")
pluto.comer()
pluto.falar()

Mickey = Rato("Mickey")
Mickey.comer()
Mickey.falar()
