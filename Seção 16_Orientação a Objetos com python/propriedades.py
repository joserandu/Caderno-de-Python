"""
PROPRIEDADES - PROPERTIES

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property  # Isso, por definição é um getter
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # Setter
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    # Métodos get e set
    def get_numero(self):  # Não faz sentido ter um método set para essa função
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta("Felicity", 3000, 2000)
conta2 = Conta("Angelina", 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

"""
Jeito errado que o professor insiste mais uma vez em ensinar para a gente:
soma = conta1._Conta__saldo + conta2._Conta__saldo

print(soma)

O melhor jeito de ter acesso aos nossos dados é com os métodos getters e setters, o qual fizemos acima.
O ideal é ter métodos set para todos os métodos get, a menos em alguns casos como na nossa classe acima.

Em linguagens de programação como java ao declararmos atributos privados nas classes, costumamos criar métodos 
públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e setters, onde os getters 
retornam o valor do atributo e os setters alteram o valor do mesmo.
    - Por convenção, colocamos os nomes dessa maneira get_<nome do atributo>.
    - Cuidado com os Setters, porque eles alteram o valor dos atributos.
"""

print(conta1.__dict__)
conta1.set_limite(999999)  # Alterando o valor com o método set.
print(conta1.__dict__)

"""
Esse tipo de nomenclatura é bem do tipo do java, mas veremos o método do python, que são as PROPRIEDADES.
"""

print("PROPRIEDADES---------------------------------------------------------------------------------------")

"""
Para não apagar as anotações acima eu vou deixar e a partir daqui trabalhar com os propertys.
"""

soma = conta1.saldo + conta2.saldo
print(f"A soma do saldo das contas é {soma}")

"""
A partir do momento que você criou uma property, é só usar o método sem precisar de um __saldo e pode acessar fora da 
classe.
"""

# Utilizando o Setter
print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)

# Utilizando o getter
print(conta1.limite)

print("------------------------------------------------------------")

"""
Podemos fazer métodos a partir das propertys. 
"""

print(conta1.valor_total)
print(conta2.valor_total)

"""
Perceba que não colocamos valor_total(), pois não estamos tratando de uma função, estamos fazendo uma property.
"""
