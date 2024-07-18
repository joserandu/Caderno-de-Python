"""
MRO - METHOD RESOLUTION ORDER

O MRO é a ordem de execução dos métodos, ou seja, quem será executado primeiro.

Em python a gente pode conferir a ordem de execução dos métodos de três formas:
    - Via propriedade da classe
    - Via método
    - Via help
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar!"


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"


class Pinguim(Aquatico, Terrestre):  # O primeiro é mais significativo.

    def __init__(self, nome):
        super(Terrestre, self).__init__(nome)


tux = Pinguim("Tux")
print(tux.cumprimentar())

"""
Esse é o fenômeno do MRO:

Pinguim(Aquatico, Terrestre)
Eu sou Tux do mar!
Pinguim(Terrestre, Aquatico)
Eu sou Tux da terra!
"""
