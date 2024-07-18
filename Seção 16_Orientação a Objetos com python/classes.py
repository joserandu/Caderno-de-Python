"""
CLASSES

Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para altomatizar o controle das lampadas da sua casa.
Para isso, você cria uma classe chamada lâmpada.
"""

idade = 32

preco = 7643.03

nome = "Fred Mercury"

print(type(idade))
print(type(preco))
print(type(nome))

"""
Ok, mas não existe um tipo para lampada.

Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos representar 
    computacionalmente os estados de um objeto. No caso da lampada, possivelmente iriamos querer saber se a lampada é 
    110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela etc.
    
    - Métodos -> função, de ligar e desligar essa lampada.
    
Em pYthon para definir uma classe utilizamos a palavra reservada class.

OBS: Quando nomeamos uma classe em Python, utilizamos por convenção o nome com a primeira letra maiuscula, 
se o nome for composto utilizamos as iniciais de todas as palavras em maiúscula de todas as palavras.

Dica: Em computação não utilizamos acentuação, caracteres especiais, espaços ou similares para nomes de classes, 
atributos, métodos, arquivos, diretorios, e etc.
"""


class Lampada:  # Sem parêntesis.
    pass  # Essa paravra é utilizada quando temos um bloco de código que ainda não está implementado.


class ContaCorrente:
    pass


lamp = Lampada()
lamp2 = Lampada

print(type(lamp))

"""
Podemos criar quantas classes a gente quiser em um documento python.
"""

# Quando fazemos cast estamos usando uma classe:
valor = int('42')  # cast
# print(help(int))  # Eu tirei porque é muito grande, mas mostra a classe.

"""
Perceba que a letra não é maiúscula porque é para as NOSSAS CLASSES, mas nas nossas deve ser maiúscula, 
para que possa ser diferenciado o que é uma classe python e o que é uma classe nossa.
list(), set(), 

Quando estamos planejando um software definimos quais classes teremos no sistema, chamamos estes objetos que serão 
mapeados para classes de ENTIDADE.
"""
