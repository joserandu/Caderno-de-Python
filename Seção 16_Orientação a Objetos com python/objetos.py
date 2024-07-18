"""
OBJETOS

Objetos são instancias da classe. Ou seja, após o mapeamento de um objeto real para a sua representação
computacional, devemos poder criar quantos objetos forem necessarios. Podemos pensar nos objetos/instancias de uma
classe como variáveis do tipo definido na classe.
"""

import datetime  # Exercício 3


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False  # Repare aqui influenciando no resultado da função.

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f"O cliente {self.__nome} diz oi")


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f"O cliente é {self.__cliente._Cliente__nome}")  # Colocamos uma classe dentro de outra.


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


print("Instanciando Objetos ----------------------------------------------------------------Lampada('Branca', 110, 60)")

lamp1 = Lampada("Branca", 110, 60)

print(f"Lampada ligada: {lamp1.checa_lampada()}")

user1 = Usuario("Felicity", "Jones", "felicity@gmail.com", "123456")

nome1 = "Angelina"
sobrenome1 = "Jolie"
email1 = "angelina@hotmail.com"
senha1 = "123456"

"""
Coloquei o 1 ao final das variáveis por conta de não ser pythonico colocar o nome das variáveis sendo os mesmos dos 
paramentos das funções dentro da classe.
"""

user2 = Usuario(nome1, sobrenome1, email1, senha1)

print("Colocando uma classe dentro de outra --------------------------------------ContaCorrente(5000, 10000, cliente2)")

cliente2 = Cliente("Angelina Jolie", "123.456.789-00")

cc = ContaCorrente(5000, 10000, cliente2)

cc.mostra_cliente()

print("Exercício 1 -----------------------------------------------------------------------------")

"""
Criar uma Classe Televisão:
Crie uma classe chamada Televisao com os seguintes atributos:
- marca: Uma string representando a marca da televisão.
- tamanho: Um número inteiro representando o tamanho da tela em polegadas.
- ligada: Um booleano indicando se a televisão está ligada ou desligada (inicialmente desligada).
Implemente um método ligar_desligar que alterna o estado da televisão entre ligada e desligada.
"""


class Televisao:

    def __init__(self, marca, tamanho):
        self.__marca = marca
        self.__tamanho = tamanho
        self.__ligada = False

    def ligar_desligar(self):
        self.__ligada = not self.__ligada


tv = Televisao("Sansung", "32 polegadas")
print(f"TV ligada: {tv.ligar_desligar()}")

print("Exercício 2 ------------------------------------------------------")

"""
Criar uma Classe Produto:
Crie uma classe chamada Produto com os seguintes atributos:
nome: Uma string representando o nome do produto.
preco: Um número decimal representando o preço do produto.
Implemente um método desconto que receba um valor percentual de desconto e retorne o preço do produto com o desconto 
aplicado.
"""


class Produto:

    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def desconto(self, percentual):
        print(f"Preço atual: {self.__preco}")
        if 100 > percentual >= 0:
            self.__preco = self.__preco - percentual / 100 * self.__preco
        print(f"Novo Preço: {self.__preco}")


produto1 = Produto("Sansung Galaxy", float("1999.90"))
produto1.desconto(10)

print("Exercício 3 ---------------------------------------------------")

"""
Criar uma Classe Carro:
Crie uma classe chamada Carro com os seguintes atributos:
- marca: Uma string representando a marca do carro.
- modelo: Uma string representando o modelo do carro.
- ano: Um número inteiro representando o ano de fabricação do carro.
Implemente um método idade que retorne a idade do carro em anos com base no ano atual.
"""


class Carro:

    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def idade(self):
        return f"O modelo {self.__modelo} da marca {self.__marca} é de {self.__ano} e possui" \
               f" {datetime.datetime.now().year - self.__ano} anos de idade"


brand = input("Marca: ")
model = input("Modelo: ")
year = input("Ano: ")

carro1 = Carro(brand, model, int(year))
print(carro1.idade())

"""
Para colocar qual ano estamos em formato inteiro:

import datetime

datetime.datetime.now().year
"""
