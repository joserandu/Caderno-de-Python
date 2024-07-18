"""
HERANÇA MULTIPLA

Herança multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes, fazendo com que a
classe filha herde todos os atributos e métodos de todas as classes herdadas.
    - A herança multipla pode ser feita de duas maneiras:
        - MULTIDERIVAÇÃO DIRETA:
            -
        - MULTIDERIVAÇÃO INDIRETA:

"""


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


# Multiderivação direta
class MultiDerivada(Base1, Base2, Base3):
    pass


class Super1:
    pass


class Super2(Super1):
    pass


# Multiderivação indireta
class Super3(Super2):
    pass


"""
Não importa se a derivação é direta ou indireta, a classe que realizar a herança herdará todos os atributos e métodos 
da super classe.
    - O resultado é o mesmo.
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


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super(Terrestre, self).__init__(nome)


# Testes

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim("Tux")
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Ele executou o método mais próximo dele, o cumprimentar do Terrestre.

"""
Para resolver isso a gente muda a ordem de herança da classe:
    - class Pinguim(Aquatico, Terrestre): -> class Pinguim(Terrestre, Aquatico):

Method Resolution Order - MRO -> tema da nossa próxima aula.
"""

print(f"Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}")
print(f"Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}")
print(f"Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}")
print(f"Tux é instancia de object? {isinstance(tux, object)}")

"""
Nessa aula tivemos que fazer o name manglin porque o nome do atributo recebido foi o mesmo do que estava no atributo 
da classe.
"""
