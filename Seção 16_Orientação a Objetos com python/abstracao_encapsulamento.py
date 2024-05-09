"""
ABSTRAÇÃO E ENCAPSULAMENTO

O grande objetivo da POO é encapsular o nosso código dentro de um grupo lógico e hierarquico utilizando classes.

Class________________________________________
|                                           |
|           Atributos e métodos             |
|___________________________________________|

Relembrando Atributos
    - Imagine que temos uma classe chamada pessoa contendo um atributo privado chamado __nome e um método privado
    chamado __falar()
        - Esses elementos privados só poderiam ser acessados dentro da classe, mas o python não bloqueia esse acesso
        fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que fas uma alteração na forma de se
        acessar os elementos privados, conforme:
            - _Classe__elemento
            - Exemplo - Acessando elementos privados fora da classe:
                instancia._Pessoa__nome
                instancia._Pessoa__falar()

Abstração, em POO é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de
usuário.


"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador  # deixei para o exemplo
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Titular: {self.__titular} | Saldo: {self.__saldo} | Limite: {self.__limite}")

    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
        else:
            print(f"Você digitou {valor}, o valor não pode ser 0 ou negativo.")

    def sacar(self, valor):
        if valor >= 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print(f"Saldo insuficiente!\nSaldo: {self.__saldo}\nSaque pedido: {valor}")
        else:
            print(f"Você digitou {valor}, o valor não pode ser 0 ou negativo.")

    def transferir(self, valor, conta_destino):
        # 1ª - Remover valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de cobrança transferência.

        # 2ª - Adicionar o valor na conta destino
        conta_destino.__saldo += valor


# Testando

conta1 = Conta("Geek", 150, 1500)

print(conta1.numero)
conta1.extrato()

# Como o atributo saldo está público conseguimos acessá-lo dessa forma, mas acaba não ficando seguro, pois podemos
# mudar o numero assim:

conta1.saldo = 99999999999999999999999999
print(f"Novo numero: {conta1.numero}")


"""
Com os atributos privados, a única forma de fazer acesso é com o name manglin.
"""

print("--------------------------------------------------------")

conta1.extrato()
conta1.depositar(-35)
conta1.extrato()
conta1.sacar(-56)
conta1.extrato()

print("--------------------------------------------------------")

conta1 = Conta("Angelina", 150.00, 1500)
conta1.extrato()

conta2 = Conta("Felicity", 200.00, 2000)
conta2.extrato()

valor = 100

conta2.sacar(valor)
conta1.depositar(valor)

conta1.extrato()
conta2.extrato()

print("---------------------------------------------------------------")

"""
Isso é bacana, mas precisamos de um método que faça isso automáticamente, para isso, vamos fazer um método chamado 
transferir.
"""

conta1 = Conta("Angelina", 150.00, 1500)
conta1.extrato()

conta2 = Conta("Felicity", 200.00, 2000)
conta2.extrato()

print("Após a transferência: ")

conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()
