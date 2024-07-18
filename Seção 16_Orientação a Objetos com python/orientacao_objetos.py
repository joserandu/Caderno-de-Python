"""
ORIETAÇÃO A OBJETOS

Temos paradigmas de orientação, que são formas de desenvolver um software.
    - Paradigmas:
        - Estrutural
        - Orientado a Objetos
        - Funcional
            - A depender da linguagem, não dá para usar OO, como a linguagem C.

Classe é um elemento da linguagem OO.

O python é uma linguagem multiparadigma.

O objetivo desse paradigma é mapear objetos do mundo real.
CLASSE - Criar uma classe é criar um modelo de um objeto do mundo real sendo representado computacionalmente,
por exemplo, Produto.
ATRIBUTOS - Além disso, temos os atributos, como por exemplo, na classe Produto, tem os atributos, nome,
preço e desconto.
MÉTODOS - Também temos os métodos de como o objeto pode funcionar, métodos são funções, mas que ficam dentro da classe.
CONSTRUTOR - É um método especial para criar novos objetos da classe.
OBJETO - Elementos que a gente cria baseado nas classes.
"""

numero = 10

print(numero)
print(type(numero))

nome = "Geek"

print(nome)
print(type(nome))


class Produto:
    pass  # Serve para indicar que é para passar


# Criando um produto:
ps4 = Produto()

print(ps4)
print(type(ps4))  # Mostra o local de alocação.
