"""
CONHECENDO O PICKLE

É como se fosse um banco de dados mais rudimentar, visando segurança.
É salvo em hexadecimal os dados

A função do pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Esse processo é chamado de serialização para deserialização.

OBS: O módulo Pickle não é seguro contra dados maliciosos e dessa forma, não é recomendado trabalhar com arquivos
pickle vindos de outras pessoas que você não conheça ou de fontes desconhecidas.
"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @staticmethod
    def comer():
        print("Esse animal tem penas.")


class Galinha(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def cisca(self):
        print(f"{self.nome} está ciscando.")


class Cao(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self.nome} está latindo.")


sacola = Galinha("Sacola")
mosquito = Cao("Mosquito")

# Binarizando o arquivo
with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((sacola, mosquito), arquivo)  # Perceba que é uma tupla.

# Ler o arquivo pickle
with open('animais.pickle', 'rb') as arquivo:
    galinha, cao = pickle.load(arquivo)
    print(f"A galinha se chama {galinha.nome}")  # PROPERTY
    galinha.cisca()
    print(f"O Cão se chama {cao.nome}")
    cao.late()

"""
Esse código escreveu, codificou e depois descodificou os animais instanciados no código. Perceba que não usamos no 
segundo caso as variaveis dos objetos das classes e nem as funções.
"""
