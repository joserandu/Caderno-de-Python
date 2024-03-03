"""
MODULO RANDOM

- Os módulos nada mais são do que outros arquivos em Python.

O modulo random já é uma função integrada.

O modulo random possúi varias funções para a geração de números pseudoaleatórios.
    São gerados não tão aleatóriamente, pode haver repetições.

OBS: Existem duas formas de se utilizar um módulo ou função desse
"""

# Forma 1

# import random

"""
Ao realizar o import, importando todo o módulo. Ao realizar o import de todo o módulo, (ou seja só o , 
todas as funções, atributos, classes e propriedades que estiverem dentro do módulo ficaram disponíveis, 
em outras palavras, ficaram em memória. Então não é recomendado.
Caso você saiba quais funções você precisa utilizar desse módulo, então esta não seria a fórma ideal de utilização.
Se quiser saber quais são os módulos, no terminal escreva: dir(random), e para saber o que ele faz, utilize a função 
help().

Nós veremos uma forma melhor na forma 2.
"""

# Forma 2

from random import random

"""
Gera um número pseudoaleatório entre 0 e 1.
Veja que para utilizar a função random() no pacote random() nos colocamos o nome do pacote e o nome da função 
separados por ponto.
Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random é apenas uma função 
dentro do módulo random.
Para ver o código fonte do random = ctrl + clique no código fonte do random.
Se você fazer do primeiro jeito, você vai importar quase 800 linhas de código, deixando sua função mais lenta. Por 
isso, importe somente a função que você quer
"""

for i in range(0, 10):
    print(random())

"""
Repare que nessa forma recomendada não precisamos chamar novamente a coleção random().
Esse código é bastante usado em IA. Em redes neurais a gente usa bastante esse módulo random() para gerar pequenos 
valores.
"""

print('FUnção uniforme() ------------------------------------------------')

"""
Gerar um número real pseudoaleatório entre os valores estabelecidos.
"""

from random import uniform

for i in range(1, 7):
    print(uniform(3, 7))  # O número 7 não é incluido.


"""
Vai gerar numeros pseudo-aleatórios entre 3 e numeros menores que 7.
"""

print('Fazendo valores inteiros -------------------------------')

from random import randint

for n in range(1, 6):
    print(randint(1, 61), end=', ')

"""
Infelizmente, acaba dando números repetidos.
"""

print('Choice() --------------------')

"""
Mostra um valor aleatório entre um iterável.
"""

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(choice('Geek University'))  # Imprime as letras.

print('Shuffle() ---------------------')

from random import shuffle

"""
Tem a função de embaralhar dados.
A semântica é diferente das funções normais, se colocar no print, da errado, ela muda a ordem normal.
"""

cartas = ['K', 'Q', 'J', 'A', '1', '2', '3', '4', '5', '6', '7']

print(cartas)
shuffle(cartas)
print(cartas)
# Para entregar a primeira:
print(cartas[0])
