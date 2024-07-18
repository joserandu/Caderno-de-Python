"""
O MÉTODO SUPER()

O método super se refere a super-classe.
"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def som(self, som):
        print(f"O {self.__nome} faz {som}")


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # Podemos escrever dessa forma
        super().__init__(nome, especie)         # e dessa daqui, que é o recomendado.
        super().som("auauauauau")  # Acessando o método da classe pai.
        self.__raca = raca


felix = Gato("Felix", "Felino", "Angorá")

felix.som("miau")

"""
Com o método super podemos fazer qualquer acesso à classe pai, como pegando os métodos e atributos.
"""
